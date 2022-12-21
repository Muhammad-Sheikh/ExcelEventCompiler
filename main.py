
import os
import pickle

currentDir = os.getcwd()
workingDir = currentDir + '\\testingGrounds'
while not os.path.exists(workingDir):
    os.mkdir(workingDir)

pickleSettings = os.path.join(workingDir, 'Settings.pk')

while not os.path.exists(os.path.join(workingDir, "Settings.pk")):
    open(pickleSettings, 'x')

with open(pickleSettings, 'wb') as pk:
    pickle.dump(workingDir, pk)
print(workingDir)

workingDir = "lmao"
print(workingDir)

with open(pickleSettings, 'rb') as pk:
    workingDir = pickle.load(pk)
print(workingDir)


#open("settings.pk", "x")
#workingDir = input("Welcome to the AutoFormatter! Please add your working directory below!\n")
