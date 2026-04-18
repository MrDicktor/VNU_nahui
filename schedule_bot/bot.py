import asyncio
import logging
import os
from datetime import date, timedelta
from typing import Dict

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ConversationHandler, filters, ContextTypes

from exceptions import GroupNotFoundException
from schedule_bot.services import Services
from schedule_bot.constants import TelegramBotConstants
from schemas import WeekSchedule

load_dotenv()

"""схема така якшо новий юзер його просить ввести групу зберігає її і зразу парсить для цієї групи, 
зберігається в дікті schedule schemas[group: WeekSchedule] і потім вже з цього дікта берем схему для вивода. Якщо користувач збередений але в дікті нема знов парсим(наприклпд  бот перезапущено то з дікта все пропадає) 
але проблема того шо зараз його треба кожен день перезапускати шоб оновленні данні отримувати, потім вже як json буде як ти казав то наперед напарсити можна буде"""

user_ids: Dict[str, str] = {}
schedule_schemas: Dict[str, WeekSchedule] = {}




class TelegramBot:

    def __init__(self, session):
        self.services = Services(session)



    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """старт тут, якщо ідішка не записана просим ввести групу"""
        user_id: str = str(update.effective_user.id)
        logging.debug(user_id)
        session_factory = context.bot_data["db_factory"]
        async  with session_factory() as session:
            service = Services(session)
            if not await service.user_exists(user_id):
                await update.message.reply_text("Введіть назву групи")
                return TelegramBotConstants.ENTER_GROUP_HANDLER_CODE
            else:
                await update.message.reply_text("Ваша група вже збережена")
                return ConversationHandler.END

    async def special_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """тут будуть всякі додаткові кнопки, зараз не працюють """
        keyboard = ["2 тижні", "змінити групу", "знайти викладача"]
        reply_markup = ReplyKeyboardMarkup(keyboard,
                                           resize_keyboard=True,
                                           one_time_keyboard=True,)
        await update.message.reply_text(text="Оберіть опцію", reply_markup=reply_markup)
        return TelegramBotConstants.MENU_HANDLER_CODE



    async def enter_group(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """коли користувач вводить групу тут оброблюється"""
        session_factory = context.bot_data["db_factory"]
        async  with session_factory() as session:
            services = Services(session)
            try:
                group = update.message.text
                user = update.effective_user
                await services.new_user(user, group)
            except GroupNotFoundException:
                await update.message.reply_text("Групу не знайдено або розкладу немає 😕\n\nСпробуйте ще раз. Введіть назву групи:")
                return TelegramBotConstants.ENTER_GROUP_HANDLER_CODE

            await update.message.reply_text("Групу збережено")
            keyboard = [["Сьогодні", "Завтра", "Тиждень"],
                        ["Меню"]]
            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               resize_keyboard=True,
                                               is_persistent=True,
                                               one_time_keyboard=False
                                               )
            await update.message.reply_text(text="Оберіть опцію", reply_markup=reply_markup)
            return ConversationHandler.END



    #вирубає все якщо команда кенсел
    @staticmethod
    async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        return ConversationHandler.END

    @staticmethod
    async def show_today(update: Update, context: ContextTypes.DEFAULT_TYPE) ->None:
        """тут виводим розклад на сьогодні і завтра"""
        session_factory = context.bot_data["db_factory"]
        async  with session_factory() as session:
            services = Services(session)
            text: str = update.message.text
            day_command: date = date.today()
            if text == "Завтра":
                day_command = day_command + timedelta(days=1)
            if day_command.weekday() in [5,6]:
                message = "Вихідний"
            else:
                message = await services.get_schedule("КНІТ-24",day_command)
            await update.message.reply_text(message)

    @staticmethod
    async def show_week(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """те саме що попередня тільки для тижня"""
        session_factory = context.bot_data["db_factory"]
        target_date = date.today()
        sent_messages = 0
        message_limit = 6
        if date.today().weekday() in [5,6]:
            message_limit = 5
        async  with session_factory() as session:
            services = Services(session)
            while sent_messages < message_limit:
                if target_date.weekday() in [5,6]:
                    target_date = target_date + timedelta(days=1)
                    continue
                message = await services.get_schedule("КНІТ-24",target_date)
                await update.message.reply_text(message)
                sent_messages += 1
                target_date = target_date + timedelta(days=1)
                await asyncio.sleep(0.3)


    @staticmethod
    def main() -> None:
        engine = create_async_engine(TelegramBotConstants.DATABASE_URL, echo=True)
        async_session_factory = async_sessionmaker(engine, expire_on_commit=False)

        application: Application = Application.builder().token(TelegramBotConstants.TOKEN).build()

        application.bot_data["db_factory"] = async_session_factory
        #конв хандлер тут обробляється діалог
        # в майбутньому в конв хендлері будуть ше стейтс

        bot_instance = TelegramBot(async_session_factory)
        conversation: ConversationHandler = ConversationHandler(
            # на команду старт він запускається і викликає старт
            entry_points=[CommandHandler(TelegramBotConstants.START_HANDLER_COMMAND, TelegramBot.start)],
            states={
                # старт вертає ентер груп, ентер груп оброблює повідомлення користувача фільтрує шоб це був текст і не команда і визиває шоу дата
                TelegramBotConstants.ENTER_GROUP_HANDLER_CODE: [MessageHandler(filters.TEXT & ~filters.COMMAND, bot_instance.enter_group)],
            },
            # фолбек  це причини чо конв хедлер зупиняєтсья, і фунція туд просто якісь текст пихнути
            fallbacks=[CommandHandler("cancel", TelegramBot.cancel)],
            # reentry це під час робти конв хендлера можна нажати старт комнду і він заново запкуститься
            allow_reentry=True,
        )

        application.add_handler(conversation)
        #обробники для кнопок
        application.add_handler(MessageHandler(filters.Text(["Сьогодні", "Завтра"]), TelegramBot.show_today))
        application.add_handler(MessageHandler(filters.Text(["Тиждень"]), TelegramBot.show_week))

        application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    TelegramBot.main()
