from idlelib import query
from dotenv import load_dotenv
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters,  ConversationHandler, CallbackQueryHandler
import pars

load_dotenv()
TOKEN = os.getenv("TOKEN")

IDS = {}

def load_ids():
    IDS.clear()
    with open("IDS", "r", encoding="utf-8") as f:
        ids = f.read()
    ids = ids.split("\n")
    for user_id in ids:
        if not user_id:
            continue
        user_id = user_id.split(" ")
        IDS[user_id[0]] = user_id[1]
    print(IDS)

async def start(update, context):
    load_ids()
    user_id = str(update.effective_user.id)
    if user_id not in IDS:
        await update.message.reply_text("Введіть назву групи")
        return 2
    else:
        context.user_data["group"] = IDS[user_id]
        pars.parsing(IDS[user_id])
        await show_saved(update, context)
        return ConversationHandler.END


async def show_saved(update, context):
    file_name = context.user_data["group"] + ".txt"
    with open(file_name, "r", encoding="utf-8") as f:
        file_content = f.read()
    await update.message.reply_text(file_content[:4000])

    return ConversationHandler.END






async def show_data(update, context):
    result = await pars.save_data(update, context)
    if result == "not found":
        await update.message.reply_text(
            "Групу не знайдено або розкладу немає 😕\n\n"
            "Спробуйте ще раз. Введіть назву групи:"
        )
        return 2
    user_id = update.effective_user.id
    with open("IDS", "a", encoding="utf-8") as f:
        f.write(str(user_id) +  " " + context.user_data["group"] + "\n")
    IDS[user_id] = context.user_data["group"]
    file_name = context.user_data["group"] + ".txt"
    with open(file_name, "r", encoding="utf-8") as f:
        file_content = f.read()

    await update.message.reply_text(file_content[:4000])

    return ConversationHandler.END



async def cancel(update, context):
    return ConversationHandler.END


def main():
    application = Application.builder().token(TOKEN).build()

    conversation = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, show_data)],
            4: [CallbackQueryHandler(cancel, pattern="cancel")],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        allow_reentry=True,
    )

    application.add_handler(conversation)
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
