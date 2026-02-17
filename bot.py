import logging
from typing import Dict
from dotenv import load_dotenv
import os

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ConversationHandler, CallbackQueryHandler, \
    filters, ContextTypes, Updater

import pars
from exceptions import GroupNotFoundException

load_dotenv()


user_ids: Dict[str, str] = {}

class TelegramBotConstants:
    TOKEN: str = os.getenv("TOKEN")
    ENTER_GROUP_HANDLER_CODE: int = 2
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
                user_ids[user_id] = group
            logging.info(user_ids)
        except FileNotFoundError:
            pass


    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """старт тут, якщо ідішка записана сразу виводить розклад"""
        TelegramBot.load_ids()
        user_id: str = str(update.effective_user.id)
        print(user_id)
        if user_id not in user_ids:
            await update.message.reply_text("Введіть назву групи")
            return TelegramBotConstants.ENTER_GROUP_HANDLER_CODE
        #якщо не, то просить ввести групу і вертає команду в конв хендлер
        else:
            context.user_data["group"] = user_ids[user_id]
            pars.parsing(user_ids[user_id])
            await TelegramBot.show_saved(update, context)
            return ConversationHandler.END


    @staticmethod
    async def show_saved(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """коли група збережена ця функція для вивода"""
        file_name: str = context.user_data["group"] + ".txt"
        with open(file_name, "r", encoding="utf-8") as f:
            file_content: str = f.read()
        await update.message.reply_text(file_content[:TelegramBotConstants.MAX_MESSAGE_LENGTH])
        return ConversationHandler.END


    @staticmethod
    async def show_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """коли не збережена оця"""
        try:
            await pars.save_data(update, context)
        except GroupNotFoundException:
            await update.message.reply_text("Групу не знайдено або розкладу немає 😕\n\nСпробуйте ще раз. Введіть назву групи:")
            return TelegramBotConstants.ENTER_GROUP_HANDLER_CODE
        user_id: str = str(update.effective_user.id)
        group: str = context.user_data["group"]
        with open("user_ids.txt", "a", encoding="utf-8") as f:
            f.write(f"{user_id};{group}\n")
        user_ids[user_id] = group
        file_name: str = group + ".txt"
        with open(file_name, "r", encoding="utf-8") as f:
            file_content: str = f.read()
        await update.message.reply_text(file_content[:4000])
        return ConversationHandler.END
    #вирубає все якщо команда кенсел
    @staticmethod
    async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        return ConversationHandler.END

    @staticmethod
    def main() -> None:

        application: Application = Application.builder().token(TelegramBotConstants.TOKEN).build()
        #конв хандлер тут обробляється діалог
        # в майбутньому в конв хендлері будуть ше стейтс


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
        application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    TelegramBot.main()
