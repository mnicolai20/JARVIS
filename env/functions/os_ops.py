import os
import subprocess as sp

paths = {
    "notepad":"C:\Program Files\Git\usr\bin\notepad",
    "discord":"C:\Users\mattr\OneDrive\Desktop\discord",
    "calculator":"C:\Program Files\Git\usr\bin\calculator"
}

# open camera
def openCamera():
    sp.run("start microsoft.windows.camera", shell=True)

# open notepad
def openNotepad():
    os.startfile(paths["notepad"]);

# open discord
def openDiscord():
    os.startfile(paths["discord"]);

# open command prompt
def openCmd():
    os.system("start cmd");

#open calculator
def openCalculator():
    sp.Popen(paths["calculator"])