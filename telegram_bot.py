#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""
import logging

from telegram import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes, MessageHandler, ConversationHandler, CallbackContext, filters



# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
    [InlineKeyboardButton(text='Start Now! ', url='http://t.me/PrigManBot/app')],
    [InlineKeyboardButton(text='Join Community ', url='https://t.me/share/url?url=%reflink%')],
    [InlineKeyboardButton("Help ", callback_data="Use /help to helping you this bot.")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    user = update.effective_user
    await update.message.reply_html(f'<b>Hey, {user.mention_html()}! Welcome to PrigMan!</b> \nTap on the coin and see your balance rise.\n\nDo you have friends, relatives, or co-workers?\nBring them all into the game\nMore buddies, more coins!',reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    await query.edit_message_text(text=f"{query.data}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to run this bot.\n\nIf you need any help please Join our community or contact to The PrigMan, he is the owner of this bot")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)
    
def main() -> None:
    application = Application.builder().token("6866396151:AAFRNNZLyHb8EFZEV1DA3nA_BBnk968UJqc").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))


    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
