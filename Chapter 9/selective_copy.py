#! python3
import sys,os,shutil,pathlib
if __name__ == '__main__':
    # Select which file extension to copy to the new folder
    fileExtension = '.txt'

    mainFolder = os.getcwd()#'C:\\Users\\nicol\\PycharmProjects\\AutomateTheBoringStuff\\Automate-The-Boring-Stuff\\Chapter 9'
    destinationFolder = mainFolder + '\\selective_copy_folder'

    pathlib.Path(destinationFolder).mkdir(parents=True, exist_ok=True)


    # Does a three walk of all folders and files in os.walk(PATH)
    for folderName, subfolders, filenames in os.walk(mainFolder):
        print('The current folder is ' + folderName)

        for subfolder in subfolders:
            print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': ' + filename)
            if filename.endswith(fileExtension):
                path = os.path.join(destinationFolder, filename)
                shutil.copy(os.path.join(subfolder,filename),path)

        print('')

    sys.exit()