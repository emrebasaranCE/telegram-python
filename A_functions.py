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
import download_histroy
from natsort import natsorted
# this is for ignoring warnings
from warnings import filterwarnings
from telegram.warnings import PTBUserWarning
filterwarnings(action="ignore", message=r".*CallbackQueryHandler", category=PTBUserWarning)

import inlineKeyboardMain_v2 as main_codes

async def showing_deluxe_categories(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    file_path_of_files = "A"
    deluxe_files_list = os.listdir(file_path_of_files)
    query = update.callback_query
    await query.answer()
    keyboard = []
    for lines in deluxe_files_list:
        newa = [InlineKeyboardButton(lines, callback_data=f"{lines}")]
        keyboard.append(newa)

    newb = [InlineKeyboardButton("Back⬅️", callback_data="subs_types")]
    keyboard.append(newb)
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="--- Deluxe Package ---", reply_markup=reply_markup
    )
    return main_codes.CATEGROIES_WHEN_SELECTING_DELUXE_1


# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------

async def show_c_1_parts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print("we are at the deluxe_categories_each")
    query = update.callback_query
    input_data = query.data
    print(f"input data : {input_data}")
    file_path_of_files = f"A/{input_data}"
    food_files_list = os.listdir(file_path_of_files)
    food_files_list = natsorted(food_files_list)
    await query.answer()
    keyboard = []
    for lines in food_files_list:
        newa = [InlineKeyboardButton(lines, callback_data=f"{file_path_of_files}/{lines}")]
        keyboard.append(newa)

    newb = [InlineKeyboardButton("Back⬅️", callback_data="Deluxe Pack")]
    keyboard.append(newb)
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=f"Deluxe Pack/{input_data}", reply_markup=reply_markup
    )
    return main_codes.PARTS_OF_CONTENTS_WHEN_SELECTING_DELUXE_2

async def show_c_2_parts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print("we are at the deluxe_categories_each")
    query = update.callback_query
    input_data = query.data
    print(f"input data : {input_data}")
    file_path_of_files = f"A/{input_data}"
    food_files_list = os.listdir(file_path_of_files)
    food_files_list = natsorted(food_files_list)
    await query.answer()
    keyboard = []
    for lines in food_files_list:
        newa = [InlineKeyboardButton(lines, callback_data=f"{file_path_of_files}/{lines}")]
        keyboard.append(newa)

    newb = [InlineKeyboardButton("Back⬅️", callback_data="Deluxe Pack")]
    keyboard.append(newb)
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=f"Deluxe Pack/{input_data}", reply_markup=reply_markup
    )
    return main_codes.PARTS_OF_CONTENTS_WHEN_SELECTING_DELUXE_2

async def show_c_3_parts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print("we are at the deluxe_categories_each")
    query = update.callback_query
    input_data = query.data
    print(f"input data : {input_data}")
    file_path_of_files = f"A/{input_data}"
    food_files_list = os.listdir(file_path_of_files)
    food_files_list = natsorted(food_files_list)
    await query.answer()
    keyboard = []
    for lines in food_files_list:
        newa = [InlineKeyboardButton(lines, callback_data=f"{file_path_of_files}/{lines}")]
        keyboard.append(newa)

    newb = [InlineKeyboardButton("Back⬅️", callback_data="Deluxe Pack")]
    keyboard.append(newb)
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=f"Deluxe Pack/{input_data}", reply_markup=reply_markup
    )
    return main_codes.PARTS_OF_CONTENTS_WHEN_SELECTING_DELUXE_2

async def show_c_4_parts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print("we are at the deluxe_categories_each")
    query = update.callback_query
    input_data = query.data
    print(f"input data : {input_data}")
    file_path_of_files = f"A/{input_data}"
    food_files_list = os.listdir(file_path_of_files)
    food_files_list = natsorted(food_files_list)
    await query.answer()
    keyboard = []
    for lines in food_files_list:
        newa = [InlineKeyboardButton(lines, callback_data=f"{file_path_of_files}/{lines}")]
        keyboard.append(newa)

    newb = [InlineKeyboardButton("Back⬅️", callback_data="Deluxe Pack")]
    keyboard.append(newb)
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=f"Deluxe Pack/{input_data}", reply_markup=reply_markup
    )
    return main_codes.PARTS_OF_CONTENTS_WHEN_SELECTING_DELUXE_2

async def show_c_5_parts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print("we are at the deluxe_categories_each")
    query = update.callback_query
    input_data = query.data
    print(f"input data : {input_data}")
    file_path_of_files = f"A/{input_data}"
    food_files_list = os.listdir(file_path_of_files)
    food_files_list = natsorted(food_files_list)
    await query.answer()
    keyboard = []
    for lines in food_files_list:
        newa = [InlineKeyboardButton(lines, callback_data=f"{file_path_of_files}/{lines}")]
        keyboard.append(newa)

    newb = [InlineKeyboardButton("Back⬅️", callback_data="Deluxe Pack")]
    keyboard.append(newb)
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=f"Deluxe Pack/{input_data}", reply_markup=reply_markup
    )
    return main_codes.PARTS_OF_CONTENTS_WHEN_SELECTING_DELUXE_2

async def show_c_6_parts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print("we are at the deluxe_categories_each")
    query = update.callback_query
    input_data = query.data
    print(f"input data : {input_data}")
    file_path_of_files = f"A/{input_data}"
    food_files_list = os.listdir(file_path_of_files)
    food_files_list = natsorted(food_files_list)
    await query.answer()
    keyboard = []
    for lines in food_files_list:
        newa = [InlineKeyboardButton(lines, callback_data=f"{file_path_of_files}/{lines}")]
        keyboard.append(newa)

    newb = [InlineKeyboardButton("Back⬅️", callback_data="Deluxe Pack")]
    keyboard.append(newb)
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=f"Deluxe Pack/{input_data}", reply_markup=reply_markup
    )
    return main_codes.PARTS_OF_CONTENTS_WHEN_SELECTING_DELUXE_2

async def show_c_7_parts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print("we are at the deluxe_categories_each")
    query = update.callback_query
    input_data = query.data
    print(f"input data : {input_data}")
    file_path_of_files = f"A/{input_data}"
    food_files_list = os.listdir(file_path_of_files)
    food_files_list = natsorted(food_files_list)
    await query.answer()
    keyboard = []
    for lines in food_files_list:
        newa = [InlineKeyboardButton(lines, callback_data=f"{file_path_of_files}/{lines}")]
        keyboard.append(newa)

    newb = [InlineKeyboardButton("Back⬅️", callback_data="Deluxe Pack")]
    keyboard.append(newb)
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=f"Deluxe Pack/{input_data}", reply_markup=reply_markup
    )
    return main_codes.PARTS_OF_CONTENTS_WHEN_SELECTING_DELUXE_2


# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------

async def deluxe_parts_content_each(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    input_data = query.data
    file_path_of_files = f"{input_data}"
    print(f"aaaa input data : {input_data}")
    turn_back = "Deluxe Pack"
    for i in range(1, 8):
        if input_data == f"Category_{i}":
            return_route = turn_back
        else:
            print(f"input_data before splitting: {input_data}")
            return_route = input_data.split('/')[-2]
    return_route = return_route.strip()

    deluxe_files_list = os.listdir(file_path_of_files)
    deluxe_files_list = natsorted(deluxe_files_list)
    query = update.callback_query
    await query.answer()
    current_file_path = file_path_of_files
    histroy_of_download = await download_histroy.get_history_download(query.message.chat_id, current_file_path)
    
    i = 0
    keyboard = []
    newa = []
    newb = []
    for lines in deluxe_files_list:
        # if this file has been downloaded before, update the text.
        is_downloaded = ""
        if lines in histroy_of_download:
            is_downloaded = "✅"
        else:
            is_downloaded = ""
        temp_lines = ""
        # if user dont have any key, dont let it see the content.
        bool_for_user_dir_exists = await user_info_functions.check_users_epoch_time(query.message.chat_id, "A")
        if (bool_for_user_dir_exists): 
            temp_lines = lines
        else:
            temp_lines = "****.txt"
        
        
        if i % 2 == 0:
            newa = [InlineKeyboardButton(is_downloaded + temp_lines, callback_data=f"{file_path_of_files}/{lines}"),]
        else:
            newa.append(InlineKeyboardButton(is_downloaded + temp_lines, callback_data=f"{file_path_of_files}/{lines}"),)
            keyboard.append(newa)
            newa = []
        i = i + 1

    if i % 2 != 0:
        newa.append(InlineKeyboardButton("Back⬅️ (Double click)", callback_data=return_route))
        keyboard.append(newa)
    else:
        newb = [InlineKeyboardButton("Back⬅️ (Double click)", callback_data=return_route)]
        keyboard.append(newb)
    reply_markup = InlineKeyboardMarkup(keyboard)
    if (bool_for_user_dir_exists):
        await query.edit_message_text(
            text=f"{input_data.split('/')[-2]}/{input_data.split('/')[-1]}", reply_markup=reply_markup
        )
    else:
        await query.edit_message_text(
            text="To see content, buy key.", reply_markup=reply_markup
        )
    return main_codes.PROCESS_DELUXE_CONTENT_3


# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------

async def process_deluxe_combo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    input_data = query.data
    await query.answer()
    print("Process deluxe combo function... _---------------------")
    print(f"input_data : {input_data}")
    input_data = str(input_data).strip()
    input_data = input_data.replace(' ','')
    # input_data = input_data.strip()
    list_of_things = {"Category_1", "Category_2", "Category_3", "Category_4", "Category_5", "Category_6", "Category_7"}
    for lines in list_of_things:
        if input_data == lines:
            print(f"Turning back to:lines: {lines} / input_data: {input_data}")
            return main_codes.CATEGROIES_WHEN_SELECTING_DELUXE_1
    
    
    # await context.bot.send_message(chat_id=query.message.chat_id, text=f"you selected : {input_data}")
    # await query.edit_message_text(text=f"You selected file : {input_data}")
    await deluxe_button(update, context)
    

    
## button
async def deluxe_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    package_type = "A"
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    await query.answer()
    print(f"user wanted to download in A : {query.data}")
    boolean_for_epoch_time = await user_info_functions.check_users_epoch_time(query.message.chat_id, package_type)
    if boolean_for_epoch_time:
        if (await user_info_functions.check_users_left_daily_download_time(query.message.chat_id, boolean_for_epoch_time, package_type)):
            if (await user_info_functions.send_file_to_the_user(query, context, package_type)):
                await user_info_functions.increase_daily_download_time_by_one(query.message.chat_id, package_type)
                await download_histroy.save_path_to_download_file_history(query.message.chat_id, query.data)
        else:
            text_to_print="Daily download limit exceeded."
            await context.bot.send_message(chat_id=query.message.chat_id, text=text_to_print)
    else:
        text_to_print="Your key has expired or you didnt enter a key."
        await context.bot.send_message(chat_id=query.message.chat_id, text=text_to_print)
    