import time
import os

print ("This Program started on "+ time.ctime())

def rename_files():
    # (1) Get the file names from a folder
    file_list = os.listdir(r"/Users/Anand/GitHub/udacity-PFwP/ProjectPrank/r_prank")
    print (file_list)
    current_path = os.getcwd()
    print("Current Working Directory is  " + current_path)
    os.chdir(r"/Users/Anand/GitHub/udacity-PFwP/ProjectPrank/r_prank")

    # (2) for each file, rename filename
    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New Name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))

    os.chdir(current_path)
rename_files()

print ("This Program finished on "+ time.ctime())
