import os
import time
import requests
import threading
import datetime
# done - 1 - check for user's epoch_time
# done - 2 - check for left_daily_download 
# done - 3 - check subscription_type of user
# 4 - increase left_daily_download when a user downloads a file.

# send file to the user if there isnt any problem.

# add a downloaded file to a txt for tracking what user downloaded.

# ++++++++++++++++++++++++++++++++++ done ++++++++++++++++++++++++++++++++++
async def check_users_left_daily_download_time(input_user_id, boolean_for_user_epoch_time, package_type):
    users_directory_path = f"user_info/{input_user_id}"
    if os.path.exists(users_directory_path):
        user_left_daily_txt_file_path = f"{users_directory_path}/left_daily_download_{package_type}.txt"
        if boolean_for_user_epoch_time:
            if os.path.exists(user_left_daily_txt_file_path):
                left_daily_value = 0
                with open(user_left_daily_txt_file_path, "r") as left_daily_txt:
                    for lines in left_daily_txt:
                        if lines != "":
                            left_daily_value = lines
                if int(left_daily_value) > 0:
                    return True
                else:
                    return False              
# ++++++++++++++++++++++++++++++++++ done ++++++++++++++++++++++++++++++++++
async def get_users_left_daily_download_time(input_user_id, package_type):
    if(await check_users_epoch_time(input_user_id, package_type)):
        users_directory_path = f"user_info/{input_user_id}"
        if os.path.exists(users_directory_path):
            user_left_daily_txt_file_path = f"{users_directory_path}/left_daily_download_{package_type}.txt"
            if os.path.exists(user_left_daily_txt_file_path):
                left_daily_value = 0
                with open(user_left_daily_txt_file_path, "r") as left_daily_txt:
                    for lines in left_daily_txt:
                        if lines != "":
                            left_daily_value = lines
                if int(left_daily_value) > 0:
                    return left_daily_value
                else:
                    return 0
# ++++++++++++++++++++++++++++++++++ done ++++++++++++++++++++++++++++++++++
lock02 = threading.Lock()
async def increase_daily_download_time_by_one(input_user_id,package_type):
    users_directory_path = f"user_info/{input_user_id}"
    if os.path.exists(users_directory_path):
        user_left_daily_txt_file_path = f"{users_directory_path}/left_daily_download_{package_type}.txt"
        if os.path.exists(user_left_daily_txt_file_path):
            left_daily_value = 0
            with lock02:
                with open(user_left_daily_txt_file_path, "r") as left_daily_txt:
                    for lines in left_daily_txt:
                        if lines != "":
                            left_daily_value = lines
                left_daily_value = int(left_daily_value) - 1
                left_daily_value = str(left_daily_value)
                with open(user_left_daily_txt_file_path, "w") as left_daily_txt:
                    left_daily_txt.write(left_daily_value)
# --------------------------- not done ---------------------------
async def check_users_epoch_time(input_user_id, package_type):
    users_directory_path = f"user_info/{input_user_id}"
    if os.path.exists(users_directory_path):
        epoch_time_file_path = f"{users_directory_path}/epoch_time_{package_type}.txt"
        if os.path.exists(epoch_time_file_path):
            with open(epoch_time_file_path, "r") as epoch_file_txt:
                for lines in epoch_file_txt:
                    if lines != "":
                        epoch_time_value = lines
            current_unix_time = await get_current_unix_time()
            if int(epoch_time_value) > current_unix_time:
                return True
            else:
                return False
        else:
            return False 
async def return_users_epoch_time(input_user_id, package_type):
    users_directory_path = f"user_info/{input_user_id}"
    if os.path.exists(users_directory_path):
        epoch_time_file_path = f"{users_directory_path}/epoch_time_{package_type}.txt"
        if os.path.exists(epoch_time_file_path):
            with open(epoch_time_file_path, "r") as epoch_file_txt:
                for lines in epoch_file_txt:
                    if lines != "":
                        epoch_time_value = lines
                return epoch_time_value
        else:
            return False 
    else:
        return False 
# //////////////////////////////////////////////////////////////////////////////////////////// update_user_download_time_for_one_time
async def update_user_download_time_for_one_time(user_id, package_type):
    # call this function when a user entered a new key 
    # and when entered, the left_daily_download should be resetted. 
    # Therefore update it one time.
    users_directory_path = f"user_info/{user_id}"
    if os.path.exists(users_directory_path):
        file_path = f"user_info/{user_id}/left_daily_download_{package_type}.txt"
        with open(file_path, "w") as file:
            file.write("5")

# //////////////////////////////////////////////////////////////////////////////////////////// check_and_create_userId_dir
async def check_and_create_userId_dir(user_id):
    # after user entered a new valid key. Create a new dir for him.
    users_directory_path = f"user_info/{user_id}"
    if not os.path.exists(users_directory_path):
        os.makedirs(users_directory_path)
        return True
    else:
        return True
# //////////////////////////////////////////////////////////////////////////////////////////// create_epoch_time_file_from_scratch
async def create_epoch_time_file_from_scratch(user_id, epoch_time_to_write, package_type):
    # after user entered a new valid key. Create a epoch_time file as his package type.
    users_directory_path = f"user_info/{user_id}"
    epoch_time_file_path = f"{users_directory_path}/epoch_time_{package_type}.txt"
    if os.path.exists(users_directory_path):
        with open(epoch_time_file_path, "w") as file:
            file.write(epoch_time_to_write)
# ////////////////////////////////////////////////////////////////////////////////////////////

async def create_a_username_file(user_id, username):
    file_path_for_subscription_file = f"user_info/{user_id}/username_{user_id}_{username}.txt"
    try:
        with open(file_path_for_subscription_file, "w") as file:
            file.write("")
    except Exception as error:
        print("username did not saved")

async def return_epoch_file_for_showing_info(user_id, package_type):
    file_path_for_epoch_time_file = f"user_info/{user_id}/epoch_time_{package_type}.txt"
    if os.path.exists(file_path_for_epoch_time_file):
        with open(file_path_for_epoch_time_file, "r") as epoch_file_txt:
            for lines in epoch_file_txt:
                if lines != "":
                    epoch_time_value = lines
            return epoch_time_value
    else:
        return 0
    
######################
async def check_epoch_time_file_exists(user_id, package_type):
    file_path = f"user_info/{user_id}"
    if (os.path.exists(file_path)):
        epoch_file_path = f"{file_path}/epoch_time_{package_type}.txt"
        if (os.path.exists(epoch_file_path)):
            return True
        else:
            return False

###############################################################
###############################################################
## update daily_download_times of the user.
async def update_every_users_download_time_end_of_the_day():
    dir_file_path_for_each_user = f"user_info"
    deluxe_files_list = os.listdir(dir_file_path_for_each_user)
    for lines in deluxe_files_list:
        dir_path = f"{dir_file_path_for_each_user}/{lines}"
        if (await check_users_epoch_time(lines, "A")):
            await update_user_download_time_for_one_time(lines, "A")
        if (await check_users_epoch_time(lines, "B1")):
            await update_user_download_time_for_one_time(lines, "B1")
        if (await check_users_epoch_time(lines, "B2")):
            await update_user_download_time_for_one_time(lines, "B2")
        if (await check_users_epoch_time(lines, "S")):
            await update_user_download_time_for_one_time(lines, "A")
            await update_user_download_time_for_one_time(lines, "B1")
            await update_user_download_time_for_one_time(lines, "B2")
            # check for epoch_time file, if exists and valid, then update the daily_download_time.txt

###############################################################
###############################################################



async def get_current_unix_time():
    return int(time.time())

async def unix_to_datetime(unix_time):
    return datetime.datetime.fromtimestamp(unix_time).date()

lock = threading.Lock()
async def send_file_to_the_user(update, context, package_type):
    try:
        with lock:
            print(f"package type : {package_type}")
            file_path = update.data
            document = open(file_path, 'rb')
            caption_text = await get_users_left_daily_download_time(update.message.chat_id, package_type)
            caption_text = int(caption_text) - 1
            caption_text = f"Left daily download: {caption_text}"
            await context.bot.send_document(update.message.chat_id, document,caption=caption_text)
            return True
    except Exception as error:
        print(f"Error while sending the file: {error}")
        return False
    




async def turn_half_to_stars(input_string):
    length = len(input_string)
    midpoint = length // 2
    stars = '*' * (length - midpoint)
    return input_string[:midpoint] + stars  


def check_user_files_if_not_create_one():
    file_path_of_user_files = "user_info"
    if not os.path.exists(file_path_of_user_files):
        os.makedirs(file_path_of_user_files)