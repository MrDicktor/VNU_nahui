import asyncio
import logging
import os
from datetime import date, timedelta
from typing import Dict

from dotenv import load_dotenv
from redis import Redis
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters,
    ContextTypes,
)

from exceptions import GroupNotFoundException
from schedule_bot.schedule_services import ScheduleService
from schedule_bot.user_service import UserService
from schedule_bot.constants import TelegramBotConstants
from schemas import WeekSchedule
import redis.asyncio as redis

load_dotenv()


user_ids: Dict[str, str] = {}
schedule_schemas: Dict[str, WeekSchedule] = {}


class TelegramBot:

    def __init__(self, session, redis: Redis) -> None:

        self.schedule_services = ScheduleService(session, redis)
        self.user_service = UserService(session, redis)

    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """старт тут, якщо ідішка не записана просим ввести групу"""
        user_id: str = str(update.effective_user.id)
        logging.debug(user_id)
        session_factory = context.bot_data["db_factory"]
        redis: Redis = context.bot_data["redis"]
        async with session_factory() as session:
            user_service = UserService(session, redis)
            if not await user_service.get_user(user_id):
                await update.message.reply_text("Введіть назву групи")
                return TelegramBotConstants.ENTER_GROUP_HANDLER_CODE
            else:
                await update.message.reply_text("Ваша група вже збережена")
                return ConversationHandler.END

    @staticmethod
    async def special_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """тут будуть всякі додаткові кнопки, зараз не працюють"""
        keyboard = ["2 тижні", "змінити групу", "знайти викладача"]
        reply_markup = ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True,
            one_time_keyboard=True,
        )
        await update.message.reply_text(text="Оберіть опцію", reply_markup=reply_markup)
        return TelegramBotConstants.MENU_HANDLER_CODE

    @staticmethod
    async def enter_group(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """коли користувач вводить групу тут оброблюється"""
        session_factory = context.bot_data["db_factory"]
        redis: Redis = context.bot_data["redis"]

        async with session_factory() as session:
            user_services = UserService(session, redis)
            try:
                group = update.message.text
                user = update.effective_user
                telegram_id = str(update.effective_user.id)
                user_fullname = update.effective_user.full_name
                username = update.effective_user.username
                await user_services.create_user(
                    telegram_id, user_fullname, username, group
                )
            except GroupNotFoundException:
                await update.message.reply_text(
                    "Групу не знайдено або розкладу немає 😕\n\nСпробуйте ще раз. Введіть назву групи:"
                )
                return TelegramBotConstants.ENTER_GROUP_HANDLER_CODE

            await update.message.reply_text("Групу збережено")
            keyboard = [["Сьогодні", "Завтра", "Тиждень"], ["Меню"]]
            reply_markup = ReplyKeyboardMarkup(
                keyboard,
                resize_keyboard=True,
                is_persistent=True,
                one_time_keyboard=False,
            )
            await update.message.reply_text(
                text="Оберіть опцію", reply_markup=reply_markup
            )
            return ConversationHandler.END

    # вирубає все якщо команда кенсел
    @staticmethod
    async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        return ConversationHandler.END

    @staticmethod
    async def beautiful_message(
        group: str, day_command: date, context: ContextTypes.DEFAULT_TYPE
    ) -> str:
        session_factory = context.bot_data["db_factory"]
        redis: Redis = context.bot_data["redis"]
        async with session_factory() as session:
            schedule_services = ScheduleService(session, redis)
            day_schedule = await schedule_services.get_schedule(group, day_command)
        if not day_schedule:
            return "Вихідний"
        else:
            message: str = ""
            message += f"{day_schedule[0].date.strftime("%d.%m.%Y")} {TelegramBotConstants.DB_TO_UKR.get(day_schedule[0].week_day)}\n\n"
            for lesson in day_schedule:
                message += f"{lesson.lesson_number}\ufe0f\u20e3 {lesson.start_time.strftime('%H:%M')}—{lesson.end_time.strftime('%H:%M')}\n"
                message += f"📚{lesson.subject}{lesson.subject_type}\n"
                message += f"👨‍🏫{lesson.teacher_name}\n"
                message += f"🏫{lesson.room_name}\n"
                if lesson.sub_group:
                    message += f"{lesson.sub_group}\n"
                if lesson.group_name:
                    message += f"🥷{lesson.group_name}\n"
                # if lesson.elimination:
                #     message += f"{lesson.elimination}\n"
                message += "\n"
            return message

    @staticmethod
    async def show_today(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """тут виводим розклад на сьогодні і завтра"""
        session_factory = context.bot_data["db_factory"]
        redis: Redis = context.bot_data["redis"]
        async with session_factory() as session:
            user_services = UserService(session, redis)
            text: str = update.message.text
            telegram_id = str(update.effective_user.id)
            user = await user_services.get_user(telegram_id)
            group = user.user_group
            day_command: date = date.today()
            if text == "Завтра":
                day_command = day_command + timedelta(days=1)
            if day_command.weekday() == 6:
                message = "Вихідний"
            else:
                message = await TelegramBot.beautiful_message(
                    group, day_command, context
                )
            if not message:
                message = "Вихідний"
            await update.message.reply_text(message)

    @staticmethod
    async def show_week(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """те саме що попередня тільки для тижня"""
        session_factory = context.bot_data["db_factory"]
        redis: Redis = context.bot_data["redis"]
        target_date = date.today()
        sent_messages = 0
        message_limit = 7
        if date.today().weekday() == 6:
            message_limit = 5
        async with session_factory() as session:
            user_services = UserService(session, redis)
            telegram_id = str(update.effective_user.id)
            user = await user_services.get_user(telegram_id)
            group = user.user_group
            while sent_messages < message_limit:
                if target_date.weekday() == 6:
                    target_date = target_date + timedelta(days=1)
                    continue
                message = await TelegramBot.beautiful_message(
                    group, target_date, context
                )
                if not message:
                    message = "Вихідний"
                await update.message.reply_text(message)
                sent_messages += 1
                target_date = target_date + timedelta(days=1)
                await asyncio.sleep(0.3)

    @staticmethod
    def main() -> None:
        engine = create_async_engine(TelegramBotConstants.DATABASE_URL, echo=True)
        async_session_factory = async_sessionmaker(engine, expire_on_commit=False)
        redis_client = redis.from_url("redis://localhost:6379/0", decode_responses=True)

        application: Application = (
            Application.builder().token(TelegramBotConstants.TOKEN).build()
        )

        application.bot_data["db_factory"] = async_session_factory
        application.bot_data["redis"] = redis_client
        # конв хандлер тут обробляється діалог
        # в майбутньому в конв хендлері будуть ше стейтс

        bot_instance = TelegramBot(async_session_factory, redis_client)
        conversation: ConversationHandler = ConversationHandler(
            # на команду старт він запускається і викликає старт
            entry_points=[
                CommandHandler(
                    TelegramBotConstants.START_HANDLER_COMMAND, TelegramBot.start
                )
            ],
            states={
                # старт вертає ентер груп, ентер груп оброблює повідомлення користувача фільтрує шоб це був текст і не команда і визиває шоу дата
                TelegramBotConstants.ENTER_GROUP_HANDLER_CODE: [
                    MessageHandler(
                        filters.TEXT & ~filters.COMMAND, bot_instance.enter_group
                    )
                ],
            },
            # фолбек  це причини чо конв хедлер зупиняєтсья, і фунція туд просто якісь текст пихнути
            fallbacks=[CommandHandler("cancel", TelegramBot.cancel)],
            # reentry це під час робти конв хендлера можна нажати старт комнду і він заново запкуститься
            allow_reentry=True,
        )

        application.add_handler(conversation)
        # обробники для кнопок
        application.add_handler(
            MessageHandler(filters.Text(["Сьогодні", "Завтра"]), TelegramBot.show_today)
        )
        application.add_handler(
            MessageHandler(filters.Text(["Тиждень"]), TelegramBot.show_week)
        )

        application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    TelegramBot.main()
