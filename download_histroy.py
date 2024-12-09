import os


async def save_path_to_download_file_history(user_id, resently_sended_file_path):
    # lets say input is "A/Dating/part15/yur__mum.txt"
    sended_file_name = resently_sended_file_path.split('/')[-1].strip()
    resently_sended_file_path = '_'.join(resently_sended_file_path.split('/')[0:-1])
    resently_sended_file_path = f"{resently_sended_file_path}.txt"
    # the output will be => A_Dating_part15.txt
    file_path_for_history = f"user_info/{user_id}/history"
    file_path_to_save = f"{file_path_for_history}/{resently_sended_file_path}"
    print(f"file_path_to_save : {file_path_to_save}")
    if not os.path.exists(file_path_for_history):
        os.makedirs(file_path_for_history)
    if os.path.exists(file_path_to_save):
        with open(file_path_to_save, "a") as file:
            file.write(sended_file_name + "\n")
    else:
        with open(file_path_to_save, "w") as file:
            file.write(sended_file_name + "\n")

async def get_history_download(user_id, current_file_path):
    file_path_of_history = f"user_info/{user_id}/history"
    current_file_path = current_file_path.replace('/','_')
    current_file_path = f"{file_path_of_history}/{current_file_path}.txt"
    if os.path.exists(current_file_path):
        with open(current_file_path, "r") as file:
            file_contents = file.readlines()
            # Optionally, you can strip newline characters from the end of each line
            file_contents = [line.strip() for line in file_contents]
        return file_contents
    else:
        emtpy_list = []
        return emtpy_list