import os
import time

original_path = os.getcwd()
downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
os.chdir(downloads_path)
path = os.getcwd()

file_extensions = {
    "images": ["webp", "png", "jpg", "svg", "jpeg", "gif", "cr2", "bmp", "ico"],
    "music": ["mp3", "wav"],
    "videos": ["mp4", "mov", "mkv"],
    "documents": ["docx", "pdf", "txt", "html", "ppt", "odt", "xls", "csv", "rtf", "ppt", ".md"],
    "zips": ["zip", "7zip", "rar", "tar", "gz", "bz2"],
    "executables": ["exe", "apk", "bin", "part", "iso", "msi", "torrent", "sh"], #Can name them Drivers
    "codes": ["c", "cpp", "py", "m", "brd", "sch", "fxml", "java", "conf", "html", "json", "xlsx", "mobi", "css", "scss", "js","ipynb"]
}

#Print Logs
print("Initializing File Cleanup...")
time.sleep(1)  # Simulating some work being done
print("Hacking Your PC.....")
time.sleep(1)
print("JKJK!")
time.sleep(0.5)
print("Checking for unnecessary files...")
time.sleep(1)  # Simulating more work
print("Organizing remaining files...")

errorFileCount = 0
miscalFileCount = 0

list_of_dirs = file_extensions.keys()

#Making Directories for Sorting
for i in list_of_dirs:
    try:
        os.mkdir(i)
    except FileExistsError:
        continue

list_of_files = os.listdir()
print("Running Cleanup in " +path)

#Script For Organizing
for i in list_of_files:
    print("Organizing file: " +i)
    try:
        if i == "cleanurdownloads":
            continue
        elif i.split(".")[-1] in file_extensions["images"]:
            fromname = path + "/" + i
            toname = path + "/images/" + i  
            os.rename(fromname, toname)
        elif i.split(".")[-1] in file_extensions["music"]:
            fromname = path + "/" + i
            toname = path + "/music/" + i
            os.rename(fromname, toname)
        elif i.split(".")[-1] in file_extensions["videos"]:
            fromname = path + "/" + i
            toname = path + "/videos/" + i
            os.rename(fromname, toname)
        elif i.split(".")[-1] in file_extensions["documents"]:
            fromname = path + "/" + i
            toname = path + "/documents/" + i
            os.rename(fromname, toname)
        elif i.split(".")[-1] in file_extensions["zips"]:
            fromname = path + "/" + i
            toname = path + "/zips/" + i
            os.rename(fromname, toname)
        elif i.split(".")[-1] in file_extensions["executables"]:
            fromname = path + "/" + i
            toname = path + "/executables/" + i
            os.rename(fromname, toname)
        elif i.split(".")[-1] in file_extensions["codes"]:
            fromname = path + "/" + i
            toname = path + "/codes/" + i
            os.rename(fromname, toname)
        elif not os.path.isfile(os.path.join(path + "/",i)) and i not in file_extensions.keys():
            print(i)
            fromname = path + "/" + i
            toname = path + "/folders/" + i
            os.rename(fromname, toname)
        else: #Miscallenous
            miscalFileCount += 1
    except (PermissionError, FileExistsError, FileNotFoundError) as e:
        # print(f"Error: {e}")
        errorFileCount += 1 #For counting files that give error
        continue
    
fileOrganized = str(len(list_of_files)-errorFileCount -miscalFileCount)
print(fileOrganized +" Files have been organized")
time.sleep(0.5)
print("Downloads cleanup completed! Enjoy the tidiness.")
print('''
Contributors:
Surat
Mehul
''')