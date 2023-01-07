
import os
import pickle


def initialization():
    # gets Current Directory, and makes a new folder in for all processed files
    currentDir = os.getcwd()
    workingDir = currentDir + '\\excelFormatter'
    # if the folder does not exists, creates it.
    while not os.path.exists(workingDir):
        os.mkdir(workingDir)

    # Makes all needed files in working directory
    Settings = os.path.join(workingDir, 'Settings.config')
    programNames = os.path.join(workingDir, 'programNames.txt')
    programDates = os.path.join(workingDir, 'dates.txt')
    programDescription = os.path.join(workingDir, 'desc.txt')
    programLocation = os.path.join(workingDir, 'location.txt')
    programTiming = os.path.join(workingDir, 'timing.txt')
    descriptorArray = [programNames, programDates, programDescription, programLocation, programTiming, pickleSettings]

    # Checks and creates needed files
    for descriptorFiles in descriptorArray:
        while not os.path.exists(descriptorFiles):
            open(descriptorFiles, 'x')

    # Writes Descriptor to the .config file, to allow it to use it for future usage.
    with open(Settings, 'wb') as config:
        pickle.dump(descriptorArray, config)

    # Reads off the settings file
    with open(Settings, 'rb') as config:
        descriptorArray = pickle.load(config)
        descriptorArray = descriptorArray

userInput = None

userInput = input("Welcome to ExcelAutoFormatter! If this is your first time or you are coming back, enter GO to get started. If you would like to exit, please enter EXIT.")

if userInput = 'GO' or 'go' or 'Go' or 'gO':

