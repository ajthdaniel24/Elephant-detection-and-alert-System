import os
import time

folder_path = 'C:\\out'
processed_files = []
flag = False

while True:
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Loop through each file in the folder
    for file_name in files:
        if file_name not in processed_files:
            print("Yes")
            flag = True
            break
    if flag:
        break
    else:
        time.sleep(5)




