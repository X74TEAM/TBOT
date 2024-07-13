import sqlite3
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Initialize the database
conn = sqlite3.connect('referrals.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, referred_by INTEGER)''')
conn.commit()

# Function to start the bot
def start(update: Update, context: CallbackContext) -> None:
    referrer_id = None
    if context.args:
        referrer_id = context.args[0]

    user_id = update.message.from_user.id

    # Check if the user is already in the database
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO users (user_id, referred_by) VALUES (?, ?)", (user_id, referrer_id))
        conn.commit()

        if referrer_id:
            update.message.reply_text(f'Thanks for joining! You were referred by user {referrer_id}.')
        else:
            update.message.reply_text('Hello! Welcome to the bot.')
    else:
        update.message.reply_text('Welcome back!')

# Function to generate a referral link
def refer(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    referral_link = f'https://t.me/{context.bot.username}?start={user_id}'
    update.message.reply_text(f'Share this link to refer others: {referral_link}')

def main() -> None:
    # Replace 'YOUR_TOKEN' with your bot's API token
    updater = Updater('6866396151:AAFRNNZLyHb8EFZEV1DA3nA_BBnk968UJqc')

    dispatcher = updater.dispatcher

    # Register the start and refer handlers
    dispatcher.add_handler(CommandHandler('start', start, pass_args=True))
    dispatcher.add_handler(CommandHandler('refer', refer))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()