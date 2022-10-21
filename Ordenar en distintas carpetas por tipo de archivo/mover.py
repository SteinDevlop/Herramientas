from PIL import Image
import os

if __name__ == "__main__":
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

    user_name = "user"
    main_Folder = f"/home/{user_name}/Downloads/"
    picturesFolder = f"/home/{user_name}/Pictures/"
    musicFolder = f"/home/{user_name}/Music/"
    videoFolder = f"/home/{user_name}/Videos/"
    fileFolder = f"/home/{user_name}/Documents/"
    exeFolder = f"/home/{user_name}/Ejecutables/"
    docs = [".doc",".docm",".docx",".htm",".html",".mhtml",".mht",".pdf" , ".rtf" , ".txt" ,".xml"]
    pics = [".jpg", ".jpeg", ".png",".gif",".bmp", ".webp"]
    audio = [".mp3",".wav",".midi",".ogg",".mp2",".mp1",".m4a"]
    video = [".mp4",".mov", ".mkv", ".wmv", ".flv"]
    exe = [".py", ".cmd", ".wsf", ".ipa", ".gadget", ".exe", ".bat", ".bin", ".apk", ".app", ".dll"]
    wtfMode = str(input("Use the all folder mode?: (Y or N)  "))
    if wtfMode == ("N" and "n"):
        pass
    elif wtfMode == ("Y" and "y"):
        convert(main_Folder)
        convert(picturesFolder)
        convert(musicFolder)
        convert(videoFolder)
        convert(fileFolder)
        convert(exeFolder)
        print("WTF mode terminated")
        print("Exit program")
        exit()
    else:
        print("Unexpected Error")
        exit()
    for filename in os.listdir(main_Folder):
        name, extension = os.path.splitext(main_Folder + filename)
        if extension in pics:
            os.rename(main_Folder + filename, picturesFolder + filename)
        if extension in audio:
            os.rename(main_Folder + filename, musicFolder + filename)
        if extension in video:
            os.rename(main_Folder + filename, videoFolder + filename)
        if extension in docs:
            os.rename(main_Folder + filename, fileFolder + filename)
        if extension in exe:
            os.rename(main_Folder + filename, exeFolder + filename)