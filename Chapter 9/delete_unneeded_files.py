#! python3
import sys,os
if __name__ == '__main__':

    mainFolder = os.getcwd()

    # Does a three walk of all folders and files in os.walk(PATH)
    for folderName, subfolders, filenames in os.walk(os.getcwd()):
        #print('The current folder is ' + folderName)
        path = mainFolder
        for subfolder in subfolders:
            #print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
            continue
        for filename in filenames:
            #print('FILE INSIDE ' + folderName + ': ' + filename)

            path = os.path.join(path, filename)
            print(os.path.abspath('selective_copy.py')) #Ikke riktig path...
            print(os.path.getsize(os.path.abspath(filename)))

        print('')

    sys.exit()