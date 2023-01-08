
import os
import pickle
import pandas as pd
import time

userInput = input("Welcome to ExcelAutoFormatter! If this is your first time or you are coming back, enter GO to get started. If you would like to exit, please enter EXIT.").lower()

if userInput == 'go':
    # gets Current Directory, and makes a new folder in for all processed files
    currentDir = os.getcwd()
    workingDir = currentDir + '\\excelFormatter'
    # if the folder does not exist, creates it.
    while not os.path.exists(workingDir):
        os.mkdir(workingDir)

    #Creates new folder in the directory, and stores the various files in there.
    Settings = os.path.join(workingDir, 'Settings.config')
    programNames = os.path.join(workingDir, 'programNames.txt')
    programDates = os.path.join(workingDir, 'dates.txt')
    programDescription = os.path.join(workingDir, 'desc.txt')
    programLocation = os.path.join(workingDir, 'location.txt')
    programTiming = os.path.join(workingDir, 'timing.txt')
    #starts array for all stored locations. Saves this array to the config file, as to simplify the storage file.
    descriptorsLocation = [programNames, programDates, programDescription, programLocation, programTiming, Settings]

    # Checks and creates needed files
    for descriptorFiles in descriptorsLocation:
        while not os.path.exists(descriptorFiles):
            open(descriptorFiles, 'x')

    # Writes Descriptor to the .config file, to allow it to use it for future usage.
    with open(Settings, 'wb') as config:
        pickle.dump(descriptorsLocation, config)
#Catches invalid and input and exits the program
elif userInput == 'exit':
    exit()
else:
    print("Invalid Input. Exiting...")
    time.sleep(5)
    exit()

 # Reads off the settings file before any thing is used
with open((os.path.join((os.getcwd() + '\\excelFormatter'), 'Settings.config')), 'rb') as config:
    descriptorsLocation = pickle.load(config)

#Double checks that the files are filled in before reading and exporting, as to prevent an out of range error
userInput = input("Are you ready to make the final file? If so, please enter Y (Make sure the files have the same "
                  "amount of items & are filled in.)\n If not, enter N to exit.").lower()
None if userInput == 'y' else exit()

#Opens all files for reading, as well as removes all newline separators
currentNames = open(descriptorsLocation[0], "r").read().splitlines()
currentDate = open(descriptorsLocation[1], "r").read().splitlines()
currentDesc = open(descriptorsLocation[2], "r").read().splitlines()
currentLocation = open(descriptorsLocation[3], "r").read().splitlines()
currentTiming = open(descriptorsLocation[4], "r").read().splitlines()

#Makes main data frame for import/exporting. Uses the list created from reading the files made.
formattedEXCL= pd.DataFrame({"Program Name": currentNames, "Program Date": currentDate, "Program Description:": currentDesc, "Program Location:": currentLocation, "Program Timing:": currentTiming})

#Asks user for what format the final file should be, and exports depending on the input.
userInput = input("What format would you like? HTML or XLSX?").lower()
#Simple conditonal for outputs, and makes it in the same script.
if userInput == 'xlsx':
    formattedEXCL.to_excel('./output.xlsx')
elif userInput == 'html':
    formattedEXCL.html('./output.html')
else:
    "Invalid Input. Exiting..."
    time.sleep(5)
    exit()