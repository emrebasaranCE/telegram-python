import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update,ForceReply
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import threading
import os
import datetime
import requests
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
)
import user_info_functions
import IMPORTANThandle_key
import A_functions
from keyauth import api
import hashlib
import sys
import IMPORTANTtelegram_bot_api_key

# this is for ignoring warnings
"""
from warnings import filterwarnings
from telegram.warnings import PTBUserWarning
filterwarnings(action="ignore", message=r".*CallbackQueryHandler", category=PTBUserWarning)
"""

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


SUBSCRIPTION_TYPE_ROUTE = 1
SELECTING_SUBSCRIPTION_TYPE = 2

CATEGORIES_WHEN_SELECTING_DELUXE = 13
CATEGROIES_WHEN_SELECTING_DELUXE_1 = 14
PARTS_OF_CONTENTS_WHEN_SELECTING_DELUXE_2 = 15  
PROCESS_DELUXE_CONTENT_3 = 16


B_CHOICES = 50
B1_CONTENT = 51 
B1_PARTS = 52
B1_PROCESS = 53


B2_CONTENT = 80
B2_PARTS = 81
B2_PROCESS = 82

ENTER_KEY_ROUTE = 200


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info(f"User {user.first_name}({user.id}) started the conversation.")
    keyboard = [
            [  
                InlineKeyboardButton("Access Files", callback_data="subs_types"),
            ],
            [
                InlineKeyboardButton("💲BUY KEY💲", callback_data="buy_key"),
                InlineKeyboardButton("🔑Enter Key🔑", callback_data="enter_key"),
            ],
            [InlineKeyboardButton("Show User Info", callback_data="get_user_info"),],
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to the Test Telegram Bot.", reply_markup=reply_markup)
    return SUBSCRIPTION_TYPE_ROUTE

async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
            [  
                InlineKeyboardButton("Access Files", callback_data="subs_types"),
            ],
            [
                InlineKeyboardButton("💲BUY KEY💲", callback_data="buy_key"),
                InlineKeyboardButton("🔑Enter Key🔑", callback_data="enter_key"),
            ],
            [InlineKeyboardButton("Show User Info", callback_data="get_user_info"),],
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Welcome to the Test Telegram Bot.", reply_markup=reply_markup)
    return SUBSCRIPTION_TYPE_ROUTE


async def subscription_types(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    query = update.callback_query
    await query.answer()
    keyboard = [
        [InlineKeyboardButton("Deluxe Pack", callback_data=f"Deluxe Pack")], 
        [InlineKeyboardButton("Back⬅️", callback_data="start_over")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Please select your subscription type.", reply_markup=reply_markup
    )
    return SELECTING_SUBSCRIPTION_TYPE



async def show_users_infos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    username = query.from_user.first_name
    user_id = query.from_user.id
    text_to_show = f"Username : {username}\nUser ID : {user_id}\n"
    # get subscription type. check if its has epoch time.
    epoch_file_A = await user_info_functions.return_epoch_file_for_showing_info(user_id, "A")
    epoch_file_A = int(epoch_file_A)
    epoch_file_B1 = await user_info_functions.return_epoch_file_for_showing_info(user_id, "B1")
    epoch_file_B1 = int(epoch_file_B1)
    epoch_file_B2 = await user_info_functions.return_epoch_file_for_showing_info(user_id, "B2")
    epoch_file_B2 = int(epoch_file_B2)
    if int(epoch_file_A) > 100:
        text = f"\n✅Deluxe Pack Expire:\n{await user_info_functions.unix_to_datetime(epoch_file_A)}"
        text_to_show = text_to_show + text
    else:
        text = f"\n❌Deluxe Pack"
        text_to_show = text_to_show + text

    if epoch_file_B1 > 100:
        text = f"\n✅Standart Plus Pack Expire:\n{await user_info_functions.unix_to_datetime(epoch_file_B1)}"
        text_to_show = text_to_show + text
    else:
        text = f"\n❌Standart Plus Pack"
        text_to_show = text_to_show + text

    if epoch_file_B2 > 100:
        text = f"\n✅Standart Pack Expire:\n{await user_info_functions.unix_to_datetime(epoch_file_B2)}"
        text_to_show = text_to_show + text
    else:
        text = f"\n❌Standart Pack"
        text_to_show = text_to_show + text

    await query.answer()
    await context.bot.send_message(chat_id=query.message.chat_id, text=text_to_show)
    # await query.edit_message_text(text=text_to_show)
    return SUBSCRIPTION_TYPE_ROUTE


async def enter_key_function(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    text_to_show = "Please enter your key:"
    await context.bot.send_message(chat_id=query.message.chat_id, text=text_to_show)
    return ENTER_KEY_ROUTE

async def buy_key_function(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    text_to_show = "www.google.com"
    await context.bot.send_message(chat_id=query.message.chat_id, text=text_to_show)


async def received_information(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Store info provided by user and ask for the next category."""
    text = update.message.text
    user = update.message.from_user
    user_id = user.id
    user_username = user.username
    print(f"User writed : {text}")
    await update.message.reply_text(text="Key processing...")
    output_from_key = await handle_key.check_key(user_id, text, user_username)
    if output_from_key == 0:
        await update.message.reply_text(text="Your key is not valid.")
    elif output_from_key == 1:
        await update.message.reply_text(text="Your key is valid.\n""Thank you for your purchase.")
    elif output_from_key == 2:
        await update.message.reply_text(text="Your expire time and the package type is the same before.\n""Nothing changed.")
    elif output_from_key == 4:
        await update.message.reply_text(text="There has been a problem.\nPlease try againg later.")
    
    return SUBSCRIPTION_TYPE_ROUTE


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(IMPORTANTtelegram_bot_api_key.API_KEY).build()

    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    """
    MAIN_PAGE_ROUTE: [
        CallbackQueryHandler(enter_key, pattern="^" + "enterKey" + "$"),
        CallbackQueryHandler(buy_key, pattern="^" + "buyKey" + "$"),
    ],
    """
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            SUBSCRIPTION_TYPE_ROUTE:[
                CallbackQueryHandler(buy_key_function, pattern="^" + "buy_key" + "$"),
                CallbackQueryHandler(subscription_types, pattern="^" + "subs_types" + "$"),
                CallbackQueryHandler(enter_key_function, pattern="^" + "enter_key" + "$"),
                CallbackQueryHandler(show_users_infos, pattern="^" + "get_user_info" + "$"),
            ],
            SELECTING_SUBSCRIPTION_TYPE:[
                CallbackQueryHandler(A_functions.showing_deluxe_categories, pattern="^" + "Deluxe Pack" + "$"),
                CallbackQueryHandler(start_over, pattern="^" + "start_over" + "$"),
            ],
            CATEGROIES_WHEN_SELECTING_DELUXE_1:[
                # this is for going back
                CallbackQueryHandler(A_functions.showing_deluxe_categories, pattern="^" + "Deluxe Pack" + "$"),
                CallbackQueryHandler(A_functions.show_c_1_parts, pattern="^" + "Category_1" + "$"),
                CallbackQueryHandler(A_functions.show_c_2_parts, pattern="^" + "Category_2" + "$"),
                CallbackQueryHandler(A_functions.show_c_3_parts, pattern="^" + "Category_3" + "$"),
                CallbackQueryHandler(A_functions.show_c_4_parts, pattern="^" + "Category_4" + "$"),
                CallbackQueryHandler(A_functions.show_c_5_parts, pattern="^" + "Category_5" + "$"),
                CallbackQueryHandler(A_functions.show_c_6_parts, pattern="^" + "Category_6" + "$"),
                CallbackQueryHandler(A_functions.show_c_7_parts, pattern="^" + "Category_7" + "$"),
                CallbackQueryHandler(subscription_types, pattern="^" + "subs_types" + "$"),
            ],
            PARTS_OF_CONTENTS_WHEN_SELECTING_DELUXE_2:[
                CallbackQueryHandler(A_functions.showing_deluxe_categories, pattern="^" + "Deluxe Pack" + "$"),
                CallbackQueryHandler(A_functions.show_c_1_parts, pattern="^" + "Category_1" + "$"),
                CallbackQueryHandler(A_functions.show_c_2_parts, pattern="^" + "Category_2" + "$"),
                CallbackQueryHandler(A_functions.show_c_3_parts, pattern="^" + "Category_3" + "$"),
                CallbackQueryHandler(A_functions.show_c_4_parts, pattern="^" + "Category_4" + "$"),
                CallbackQueryHandler(A_functions.show_c_5_parts, pattern="^" + "Category_5" + "$"),
                CallbackQueryHandler(A_functions.show_c_6_parts, pattern="^" + "Category_6" + "$"),
                CallbackQueryHandler(A_functions.show_c_7_parts, pattern="^" + "Category_7" + "$"),
                CallbackQueryHandler(A_functions.deluxe_parts_content_each),
            ],
            PROCESS_DELUXE_CONTENT_3:[
                CallbackQueryHandler(A_functions.process_deluxe_combo),
            ],
            ENTER_KEY_ROUTE: [
                MessageHandler(
                    filters.TEXT & ~(filters.COMMAND),
                    received_information,
                )
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    # Add ConversationHandler to application that will be used for handling updates
    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    user_info_functions.check_user_files_if_not_create_one()
    main()
