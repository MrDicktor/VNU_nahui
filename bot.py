from typing import Dict
from dotenv import load_dotenv
import os

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ConversationHandler, CallbackQueryHandler, filters, ContextTypes

import pars


load_dotenv()
TOKEN: str | None = os.getenv("TOKEN")

IDS: Dict[str, str] = {}

ENTER_GROUP: int = 2
CANCEL: int = 4


class TelegramBot:
#загружаєм ідішкі з файла
    @staticmethod
    def load_ids() -> None:
        IDS.clear()
        try:
            with open("IDS", "r", encoding="utf-8") as f:
                ids = f.read().split("\n")
            for user in ids:
                if not user: continue
                user_id, group = user.split(" ")
                IDS[user_id] = group
            print(IDS)
        except FileNotFoundError:
            pass

#старт тут, якшо ідішка записана сразу виводить розклад, якшо не то просить ввести групу і вертає команду в конв хендлер
    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        TelegramBot.load_ids()
        user_id: str = str(update.effective_user.id)
        if user_id not in IDS:
            await update.message.reply_text("Введіть назву групи")
            return ENTER_GROUP
        context.user_data["group"] = IDS[user_id]
        pars.parsing(IDS[user_id])
        await TelegramBot.show_saved(update, context)
        return ConversationHandler.END

#коли група збережена ця функція для вивода 
    @staticmethod
    async def show_saved(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        file_name: str = context.user_data["group"] + ".txt"
        with open(file_name, "r", encoding="utf-8") as f:
            file_content: str = f.read()
        await update.message.reply_text(file_content[:4000])
        return ConversationHandler.END

#коли не збережена оця
    @staticmethod
    async def show_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        result: str = await pars.save_data(update, context)
        if result == "not found":
            await update.message.reply_text("Групу не знайдено або розкладу немає 😕\n\nСпробуйте ще раз. Введіть назву групи:")
            return ENTER_GROUP
        user_id: str = str(update.effective_user.id)
        group: str = context.user_data["group"]
        with open("IDS", "a", encoding="utf-8") as f:
            f.write(f"{user_id} {group}\n")
        IDS[user_id] = group
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

        application: Application = Application.builder().token(TOKEN).build()
#конв хандлер тут обробляється діалог
#на команду старт він запускається і визиває старт
# старт вертає ентер груп, ентер груп оброблює повідомлення користувача фільтрує шою це був текс і не команда і визиває шоу дата
# в майбутньому в конв хендлері будуть ше стейтс
# фолбек  це причини чо конв хедлер зупиняєтсья і фунція туд просто якісь текст пихнути
# reentry це під час робти конв хендлера можна нажати старт комнду і він заново запкуститься
        conversation: ConversationHandler = ConversationHandler(
            entry_points=[CommandHandler("start", TelegramBot.start)],
            states={
                ENTER_GROUP: [MessageHandler(filters.TEXT & ~filters.COMMAND, TelegramBot.show_data)],
            },
            fallbacks=[CommandHandler("cancel", TelegramBot.cancel)],
            allow_reentry=True,
        )

        application.add_handler(conversation)
        application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    TelegramBot.main()
