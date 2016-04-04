import os

def rename_files():
    # (1) get file name from the folder 
    file_list = os.listdir(r"/home/mdora/pythonPrograms/prank")
    # r is used to say python to take input as it is,and not interpret other    #  way
    print(file_list)
    saved_path= os.getcwd()
    print("Current working directory"+saved_path)
    os.chdir(r"/home/mdora/pythonPrograms/prank")
    # (2) rename the file
    for file_name in file_list:
        print("Old Name of the file: "+file_name)
        os.rename(file_name,file_name.translate(None,"0123456789"))
        print("New Name of the file: "+file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
    

rename_files()
