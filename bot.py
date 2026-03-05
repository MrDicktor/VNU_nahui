import logging
from typing import Dict
from dotenv import load_dotenv
import os

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ConversationHandler, CallbackQueryHandler, \
    filters, ContextTypes, Updater

import pars
from exceptions import GroupNotFoundException
from pars import Parser
from schemas import WeekSchedule

load_dotenv()

"""схема така якшо новий юзер його просить ввсти групу зберігає її і зразу парсить для цієї групи, 
зберігається в дікті schedule schemas[group: WeekSchedule] і потім вже з цього дікта берем схему для вивода. Якщо користувач збередений але в дікті нема знов парсим(наприклпд  бот перезапущено то з дікта все пропадає) 
але проблема того шо зараз його треба кожен день перезапускати шоб оновленні данні отримувати, потім вже як json буде як ти казав то наперед напарсити можна буде"""

user_ids: Dict[str, str] = {}
schedule_schemas: Dict[str, WeekSchedule] = {}

class TelegramBotConstants:
    TOKEN: str = os.getenv("TOKEN")
    ENTER_GROUP_HANDLER_CODE: int = 2
    MENU_HANDLER_CODE: int = 3
    CANCEL_HANDLER_COMMAND: int = 4
    START_HANDLER_COMMAND: str = 'start'
    MAX_MESSAGE_LENGTH: int = 4000

class TelegramBot:

    user_ids: list[int]

    @staticmethod
    def load_ids() -> None:
        """загружаєм ід з файла"""
        user_ids.clear()
        try:
            with open("user_ids.txt", "r", encoding="utf-8") as f:
                ids = f.read().split("\n")
            for user in ids:
                if not user: continue
                user_id, group = user.split(";")
                user_ids[str(user_id)] = group
            logging.info(user_ids)
        except FileNotFoundError:
            logging.error()
            pass


    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """старт тут, якщо ідішка не записана просим ввести групу"""
        TelegramBot.load_ids()
        user_id: str = str(update.effective_user.id)
        logging.debug(user_id)
        if user_id not in user_ids:
            await update.message.reply_text("Введіть назву групи")
            return TelegramBotConstants.ENTER_GROUP_HANDLER_CODE
        #якщо записана то показуєм кнопки
        else:
            keyboard = [["Сьогодні", "Завтра", "Тиждень"],
                        ["Меню"]]
            reply_markup = ReplyKeyboardMarkup(keyboard,
                                               resize_keyboard=True,
                                               is_persistent=True,
                                               one_time_keyboard=False
                                                )
            context.user_data["group"] = user_ids[user_id]
            await update.message.reply_text(text="bebebe", reply_markup= reply_markup)
            return ConversationHandler.END

    async def special_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """тут будуть всякі додаткові кнопки, зараз не працюють """
        keyboard = ["2 тижні", "змінити групу", "знайти викладача"]
        reply_markup = ReplyKeyboardMarkup(keyboard,
                                           resize_keyboard=True,
                                           one_time_keyboard=True,)
        await update.message.reply_text(text="bebebe", reply_markup=reply_markup)
        return TelegramBotConstants.MENU_HANDLER_CODE


    @staticmethod
    async def show_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """коли користувач вводить групу тут оброблюється"""
        try:
            group = update.message.text
            week_schedule = await Parser.main(update, group)
        except GroupNotFoundException:
            await update.message.reply_text("Групу не знайдено або розкладу немає 😕\n\nСпробуйте ще раз. Введіть назву групи:")
            return TelegramBotConstants.ENTER_GROUP_HANDLER_CODE
        user_id: str = str(update.effective_user.id)
        with open("user_ids.txt", "a", encoding="utf-8") as f:
            f.write(f"{user_id};{group}\n")
        user_ids[user_id] = group
        schedule_schemas[group] = week_schedule
        await update.message.reply_text("Групу збережено")
        return ConversationHandler.END


    #вирубає все якщо команда кенсел
    @staticmethod
    async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        return ConversationHandler.END

    @staticmethod
    async def show_today(update: Update, context: ContextTypes.DEFAULT_TYPE) ->None:
        """тут виводим розклад на сьогодні і завтра"""
        global schedule_schemas
        text: str = update.message.text
        user_id: str = str(update.effective_user.id)
        group = user_ids[user_id]
        #якщо все добре просто виводим
        if group in schedule_schemas.keys():
            week_schema = schedule_schemas[group]
        #якщо немає схеми то парсим і тоді вивід
        else:
            schedule_schemas[group] = await Parser.main(update, group)
            week_schema = schedule_schemas[group]
        if text == "Сьогодні":
            today = week_schema.day_1
        elif text == "Завтра":
            today = week_schema.day_2
        #формування повідомлення
        message = ""
        message += f"{today.date}\n\n"
        for lesson in today.schedule:
            message += f"{lesson.lesson_number}\ufe0f\u20e3 {lesson.start_time.strftime('%H:%M')}—{lesson.end_time.strftime('%H:%M')}\n"
            message += f"📚{lesson.subject.subject}{lesson.subject.subject_type}\n"
            message += f"👨‍🏫{lesson.teacher}\n"
            message += f"🏫{lesson.room}\n"
            if lesson.sub_group:
                message += f"{lesson.sub_group}\n"
            if lesson.groups:
                message += f"🥷{lesson.groups}\n"
            if lesson.elimination:
                message += f"{lesson.elimination}\n"
            message += "\n"
        await update.message.reply_text(message)

    @staticmethod
    async def show_week(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """те саме що попередня тільки для тижня"""
        user_id: str = str(update.effective_user.id)
        group = user_ids[user_id]
        if group in schedule_schemas.keys():
            week_schema = schedule_schemas[group]
        else:
            schedule_schemas[group] = await Parser.main(update, group)
            week_schema = schedule_schemas[group]
        days = [week_schema.day_1, week_schema.day_2, week_schema.day_3, week_schema.day_4, week_schema.day_5, week_schema.day_6]
        for today in days:
            message: str = ""
            message += f"{today.date}\n\n"
            for lesson in today.schedule:
                message += f"{lesson.lesson_number}\ufe0f\u20e3 {lesson.start_time.strftime('%H:%M')}—{lesson.end_time.strftime('%H:%M')}\n"
                message += f"📚{lesson.subject.subject}{lesson.subject.subject_type}\n"
                message += f"👨‍🏫{lesson.teacher}\n"
                message += f"🏫{lesson.room}\n"
                if lesson.sub_group:
                    message += f"{lesson.sub_group}\n"
                if lesson.groups:
                    message += f"🥷{lesson.groups}\n"
                if lesson.elimination:
                    message += f"{lesson.elimination}\n"
                message += "\n"
            await update.message.reply_text(message)


    @staticmethod
    def main() -> None:

        application: Application = Application.builder().token(TelegramBotConstants.TOKEN).build()
        #конв хандлер тут обробляється діалог
        # в майбутньому в конв хендлері будуть ше стейтс
        TelegramBot.load_ids()

        conversation: ConversationHandler = ConversationHandler(
            # на команду старт він запускається і викликає старт
            entry_points=[CommandHandler(TelegramBotConstants.START_HANDLER_COMMAND, TelegramBot.start)],
            states={
            # старт вертає ентер груп, ентер груп оброблює повідомлення користувача фільтрує шоб це був текст і не команда і визиває шоу дата
               TelegramBotConstants.ENTER_GROUP_HANDLER_CODE: [MessageHandler(filters.TEXT & ~filters.COMMAND, TelegramBot.show_data)],
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
