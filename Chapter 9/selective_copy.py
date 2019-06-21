#! python3
import sys,os,shutil

if __name__ == '__main__':
    # Select which file extension to copy to the new folder
    fileExtension = '.txt'

    mainFolder = 'C:\\Users\\nicol\\PycharmProjects\\AutomateTheBoringStuff\\Automate-The-Boring-Stuff\\Chapter 9'
    destinationFolder = mainFolder + '\\selective_copy_folder'

    # Does a three walk of all folders and files in os.walk(PATH)
    for folderName, subfolders, filenames in os.walk(mainFolder):
        print('The current folder is ' + folderName)

        for subfolder in subfolders:
            print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': ' + filename)
            if filename.endswith(fileExtension):
                shutil.copy(filename,destinationFolder)

        print('')

    sys.exit()