import os 
import getpass

def createBatFile(progrs):
    with open("progrs.bat", "w") as f:
        f.write("@echo off" + "\n")

    for j in progrs:
        with open("progrs.bat", "w") as f2:
            f2.write(j)

def add_to_startup(path):
    user = getpass.getuser()

    bat_path = f'C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'

    with open(bat_path + '\\' + "open.bat", "w+") as but_file:
        but_file.write(f"start {path}")


inp = input("Введите полный путь до программ через запятую: ").split(",")

createBatFile(inp)
add_to_startup(r"C:\Users\user\Desktop\autorun\progrs.bat")