import datetime
import time
import user_info_functions
import os

async def check_every_minute():
    while True:
        now = datetime.datetime.now()
        if now.hour == 17:
            # time is 23 oclock. Reset the daily download times.
            current_date = now.date()
            
            current_hour = now.hour
            info_to_check_or_write = str(current_date) + ":" + str(current_hour)
            # user_info_functions.reset_all_users_donwload_time()
            file_path_of_last_updated_time_of_downloads = "IMPORTANT_dont_delete.txt"
            if (os.path.exists(file_path_of_last_updated_time_of_downloads)):
                with open(file_path_of_last_updated_time_of_downloads, "r") as file:
                    for lines in file:
                        if lines != "":
                            last_udpated_time = lines
                    
                last_update_date = last_udpated_time.split(':')[0]
                last_update_hour = last_udpated_time.split(':')[1]


                current_date = str(current_date).strip()
                last_update_hour = str(last_update_hour).strip()
                last_update_hour = last_update_hour.strip()
                current_hour = str(current_hour).strip()

                print(f"{last_update_date}/{current_date}")
                print(f"{last_update_hour}/{current_hour}")
                if (last_update_date == str(current_date)) and (last_update_hour == current_hour):
                    print("Nothing happaned because date is same as before.")
                else:
                    print("date changed...")
                    # call functions to update user's download time.
                    with open(file_path_of_last_updated_time_of_downloads, "w") as file:
                        file.write(info_to_check_or_write)   
            else:
                with open(file_path_of_last_updated_time_of_downloads, "w") as file:
                    file.write(info_to_check_or_write)    
            # --!!!!!IMPORTANT!!!!!-- save a file that contains last updated time. This is important
        print("sleeping 10 seconds.")
        time.sleep(10)
    
# await check_every_minute()