import os, sys
import shutil



if __name__ == "__main__":
    current_user = os.getlogin()
    list_ = os.listdir(f"/home/{current_user}")
    download_folder = os.path.isdir(f"/home/{current_user}/Downloads")
    print(download_folder)
    for i in list_:
        print(i)