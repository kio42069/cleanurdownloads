import os

path = os.getcwd()

list_of_dirs = ["music","videos","pictures","executables","folders", "documents","zips","codes"] # add any new folders you want to this list
for i in list_of_dirs:
    try:
        os.mkdir(i)
    except FileExistsError:
        continue

list_of_files = os.listdir()

for i in list_of_files:
    if i == "downloadsCleaner.py":
        continue
    elif i.split(".")[-1] in ["webp", "PNG", "png", "JPG", "jpg", "svg", "jpeg","gif","CR2","pixil"]:  # add any image file extensions you want to move into the images folder
        fromname = path + "/" + i
        toname = path + "/images/" + i  
        os.rename(fromname, toname)
    elif i.split(".")[-1] in ["mp3","wav"]: # add any music file extensions you want to move into the music folder
        fromname = path + "/" + i
        toname = path + "/music/" + i
        os.rename(fromname, toname)
    elif i.split(".")[-1] in ["mp4","MOV","mov"]:  # add any video file extensions you want to move into the video folder
        fromname = path + "/" + i
        toname = path + "/videos/" + i
        os.rename(fromname, toname)
    elif i.split(".")[-1] in ["docx","pdf","txt"]:  # add any documents file extensions you want to move into the documents folder
        fromname = path + "/" + i
        toname = path + "/documents/" + i
        os.rename(fromname, toname)
    elif i.split(".")[-1] in ["zip","7zip","rar"]:  # add any zip file extensions you want to move into the zipped folder
        fromname = path + "/" + i
        toname = path + "/zips/" + i
        os.rename(fromname, toname)
    elif i.split(".")[-1] in ["exe","apk","bin","part","iso","msi","EXE","torrent"]:  # add any executable file extensions you want to move into the executables folder
        fromname = path + "/" + i
        toname = path + "/executables/" + i
        os.rename(fromname, toname)
    elif i.split(".")[-1] in ["c","cpp","py","m","brd","sch"]:  # add any code file extensions you want to move into the code folder
        fromname = path + "/" + i
        toname = path + "/codes/" + i
        os.rename(fromname, toname)
    elif not os.path.isfile(os.path.join(path + "/",i)) and i not in list_of_dirs: 
        print(i)
        fromname = path + "/" + i
        toname = path + "/folders/" + i
        os.rename(fromname, toname)

print("Downloads cleanup completed!")