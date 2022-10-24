from PIL import Image
import os

from numpy import tile

if __name__ == "__main__":
    def message():
        title_text = "Mover And Order Python Script"
        title=title_text.center(100,"-")
        print(title)
        print("""
        Sort and move files to their dependent folders.

Ex: .mp3 extensions, in the downloads folder will be automatically moved to the audio folder

Advanced Options:

"WTF" mode, scans all folders and moves ALL EXTENSIONS to their corresponding folder

""")
    def convert(foldir):
        for filename in os.listdir(foldir):
            name, extension = os.path.splitext(foldir + filename)
            if extension in pics:
                os.rename(foldir + filename, picturesFolder + filename)
            if extension in audio:
                os.rename(foldir + filename, musicFolder + filename)
            if extension in video:
                os.rename(foldir + filename, videoFolder + filename)
            if extension in docs:
                os.rename(foldir + filename, fileFolder + filename)
            if extension in exe:
                os.rename(foldir + filename, exeFolder + filename)
            if extension in download:
                os.rename(foldir + filename, Download_Folder + filename)
    user_name = os.getlogin()
    Download_Folder = f"/home/{user_name}/Downloads/"
    picturesFolder = f"/home/{user_name}/Pictures/"
    musicFolder = f"/home/{user_name}/Music/"
    videoFolder = f"/home/{user_name}/Videos/"
    fileFolder = f"/home/{user_name}/Documents/"
    exeFolder = f"/home/{user_name}/Ejecutables/"
    download = [".zip",".rar",".jar",".sql.gz",".tar",".gz",".dmg",".ttf",".glb"]
    docs = [".doc",".docm",".docx",".htm",".html",".mhtml",".mht",".pdf" , ".rtf" , ".txt" ,".xml"]
    pics = [".jpg", ".jpeg", ".png",".gif",".bmp", ".webp"]
    audio = [".mp3",".wav",".midi",".ogg",".mp2",".mp1",".m4a"]
    video = [".mp4",".mov", ".mkv", ".wmv", ".flv"]
    exe = [".py", ".cmd", ".wsf", ".ipa", ".gadget", ".exe", ".bat", ".bin", ".apk", ".app", ".dll"]
    message()
    wtfMode = str(input("""
(1) Normal execution (from downloads folder to their respective folders)

(2)Advanced execution (all plugin folders to their respective plugin folders)

Select 1 or 2:  
    """))
    if wtfMode == ("1"):
        convert(Download_Folder)
    elif wtfMode == ("2"):
        convert(Download_Folder)
        convert(picturesFolder)
        convert(musicFolder)
        convert(videoFolder)
        convert(fileFolder)
        convert(exeFolder)
        print("Advanced execution mode has ended")
        print("Exit ...")
        exit()
    else:
        print("An error has occurred in the response selection, please make your response 1 or 2.")
        exit()