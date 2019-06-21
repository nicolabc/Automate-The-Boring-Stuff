#! python3
import sys
if __name__ == '__main__':


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