print("Updater V2, credit to: (discord) sania212")
import requests
import os
try:
    url = "https://github.com/username/repository/raw/master/file.txt"
    Git_code = requests.get(url).content
except:
    print("Bad internet connection")
print("Checking for updates, please wait...")
Mfile = open("Main.exe", "r")
Current_code = Mfile.read()
Current_code = os.linesep.join([line for line in Current_code.splitlines() if line.strip() != ""])
Git_code = os.linesep.join([line for line in Git_code.splitlines()  if line.strip() != ""])
Current_code = Current_code.replace('\r\n', '\n')
Git_code = Git_code.replace('\r\n', '\n')

def check():
    F11 = open("1.txt", "w+", encoding='utf-8')
    F11.write(Current_code)
    F11.close()
    F21 = open("2.txt", "w+", encoding='utf-8')
    F21.write(Git_code)
    F21.close()

if(Git_code == Current_code):
    print("Your version already up to date")
else:
    if(str(input("Update found, are you want to install update? (T or F): ")) == "T"):
        F1 = open("Main.exe", "w+", encoding='utf-8')
        F1.write(Git_code)
        F1.close()
        print("Restart Redactor to see changes")
    else:
        print("Deleting changes...")

Mfile.close()