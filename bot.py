import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


ADMIN_ID = 0  # بعداً آیدی خودت را اینجا می‌گذاریم


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        "سلام 👋\n"
        "به SecretLink خوش آمدید.\n\n"
        "ربات پیام ناشناس در حال راه‌اندازی است."
    )

    print(
        f"User joined: {user.id} | @{user.username}"
    )


async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == ADMIN_ID:
        await update.message.reply_text(
            "پنل مدیریت فعال است ✅"
        )
    else:
        await update.message.reply_text(
            "دسترسی ندارید."
        )


def main():
    token = os.getenv("BOT_TOKEN")

    if not token:
        raise ValueError("BOT_TOKEN is missing")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin))

    print("Bot started...")

    app.run_polling()


if __name__ == "__main__":
    main()
