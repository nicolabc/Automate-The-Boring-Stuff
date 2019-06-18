import shutil,os,sys

if __name__ == '__main__':
    os.chdir("./test folder")
    # Create a copy of file1 named file2. If file already exist, nothing happens
    shutil.copy('eggs.txt','eggs2.txt')
    sys.exit()
