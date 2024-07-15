from telegram.ext import Updater, MessageHandler, Filters
from telegram import Bot

def send_message_to_all_members(bot_token, group_id, message):
    # Create a bot instance using the bot's token
    bot = Bot(token=bot_token)

    # Create an updater instance
    updater = Updater(bot=bot)

    # Get a list of all the members of the group
    members = updater.bot.get_chat_members(chat_id=group_id)

    # Iterate over the list of members and send a message to each one
    for member in members:
        user_id = member.user.id
        bot.send_message(chat_id=user_id, text=message)

# Example usage: send a message to all members of a group with ID 12345
send_message_to_all_members(bot_token='6866396151:AAFRNNZLyHb8EFZEV1DA3nA_BBnk968UJqc', group_id=1002080185898, message='Hello, group members!')