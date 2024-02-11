import os
import shutil
from time import sleep


if __name__ == "__main__":
    current_user = os.getlogin()
    DOWNLOADS_FOLDER = f"/home/{current_user}/Downloads/"

    download_folder_exists = os.path.isdir(DOWNLOADS_FOLDER)

    #extension lists
    file_ext = ('.c', '.cpp', '.py', '.html', '.css', '.js', '.java', '.txt', '.rs')
    video_ext = ('.mp4', '.aac', '.mkv', '.mov')
    music_ext = ('.mp3', '.wav', '.aac')
    image_ext = ('.png', '.jpeg', '.jpg', '.gif', '.eps', '.dwg', '.psd')

    #folders path for sorting 
    PICTURES_FOLDER = f"/home/{current_user}/Pictures/"
    VIDEOS_FOLDER = f"/home/{current_user}/Videos/"
    MUSIC_FOLDER = f"/home/{current_user}/Music/"
    DOCUMENTS_FOLDER = f"/home/{current_user}/Documents/"
    PERSONAL_FOLDER = f"/home/{current_user}/Documents/Common/.MyPersonal/"


    if download_folder_exists:
        for item in os.listdir(DOWNLOADS_FOLDER):
            
            if item.endswith(file_ext):
                    shutil.move(DOWNLOADS_FOLDER + item, DOCUMENTS_FOLDER)
                    sleep(1)
            
            if item.endswith(video_ext):
                    shutil.move(DOWNLOADS_FOLDER + item, VIDEOS_FOLDER)
                    sleep(1)
            
            if item.endswith(music_ext):
                    shutil.move(DOWNLOADS_FOLDER + item, MUSIC_FOLDER)
                    sleep(1)

            if item.endswith(image_ext):
                    shutil.move(DOWNLOADS_FOLDER + item, PICTURES_FOLDER)
                    sleep(1)

            else:
                if not os.path.exists(PERSONAL_FOLDER):
                        print("no")
                        os.makedirs(PERSONAL_FOLDER)
                        shutil.move(DOWNLOADS_FOLDER + item, PERSONAL_FOLDER)      
                        sleep(1)

                else:
                      shutil.move(DOWNLOADS_FOLDER + item, PERSONAL_FOLDER)
                      sleep(1)


    else:
        print("cant locate downloads folder")