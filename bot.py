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
    TOKEN: str | None = os.getenv("TOKEN")
    ENTER_GROUP: int = 2
    CANCEL: int = 4
    START: str = 'start'

class TelegramBot:

    """загружаєм ід з файла"""

    @staticmethod
    def load_ids() -> None:
        user_ids.clear()
        try:
            with open("IDS", "r", encoding="utf-8") as f:
                ids = f.read().split("\n")
            for user in ids:
                if not user: continue
                user_id, group = user.split(";")
                user_ids[user_id] = group
            print(user_ids)
        except FileNotFoundError:
            pass

    """старт тут, якщо ідішка записана сразу виводить розклад"""
    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        TelegramBot.load_ids()
        user_id: str = str(update.effective_user.id)
        print(user_id)
        if user_id not in user_ids:
            await update.message.reply_text("Введіть назву групи")
            return TelegramBotConstants.ENTER_GROUP
        #якщо не, то просить ввести групу і вертає команду в конв хендлер
        else:
            context.user_data["group"] = user_ids[user_id]
            pars.parsing(user_ids[user_id])
            await TelegramBot.show_saved(update, context)
            return ConversationHandler.END

    """коли група збережена ця функція для вивода"""
    @staticmethod
    async def show_saved(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        file_name: str = context.user_data["group"] + ".txt"
        with open(file_name, "r", encoding="utf-8") as f:
            file_content: str = f.read()
        await update.message.reply_text(file_content[:4000])
        return ConversationHandler.END

    """коли не збережена оця"""
    @staticmethod
    async def show_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        try:
            await pars.save_data(update, context)
        except GroupNotFoundException:
            await update.message.reply_text("Групу не знайдено або розкладу немає 😕\n\nСпробуйте ще раз. Введіть назву групи:")
            return TelegramBotConstants.ENTER_GROUP
        user_id: str = str(update.effective_user.id)
        group: str = context.user_data["group"]
        with open("IDS", "a", encoding="utf-8") as f:
            f.write(f"{user_id};{group}\n")
        user_ids[user_id] = group
        file_name: str = group + ".txt"
        with open(file_name, "r", encoding="utf-8") as f:
            file_content: str = f.read()
        await update.message.reply_text(file_content[:4000])
        return ConversationHandler.END
#вирубає все якшо команда кансел
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
            entry_points=[CommandHandler(TelegramBotConstants.START, TelegramBot.start)],
            states={
# старт вертає ентер груп, ентер груп оброблює повідомлення користувача фільтрує шоб це був текст і не команда і визиває шоу дата
               TelegramBotConstants.ENTER_GROUP: [MessageHandler(filters.TEXT & ~filters.COMMAND, TelegramBot.show_data)],
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
