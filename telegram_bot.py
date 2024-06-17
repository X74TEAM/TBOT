from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(f'<b>Hey, @{update.effective_user.username}! Welcome to xEarningBot!</b>\nAre you ready to Earn using our bot.?')


app = ApplicationBuilder().token("7201274655:AAGtMzZy40Lu4A1T3v_42hW1GrOizHQMZu8").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()