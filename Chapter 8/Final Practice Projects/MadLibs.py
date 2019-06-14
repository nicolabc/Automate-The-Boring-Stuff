import os,sys

'''
## The commented code are notes/tests from chapter 8 of the book
## They may be ignored for now

#print(os.path.join('usr', 'bin', 'spam'))

print('My print: ')
#print(os.getcwd())
#os.chdir('C:\\Windows\\System32')
#print(os.getcwd())

#print(os.path.abspath('.'))

print(os.path.relpath('C:\\Windows', 'C:\\Users\\nicol\\PycharmProjects'))
os.chdir('C:\\Windows')
os.chdir('C:\\')

#print(os.getcwd())
'''
## TODO: Read file & imput word corresponding to correct word class

if __name__ == '__main__':
    if len(sys.argv) >= 3 and ".txt" in sys.argv[1].lower():
        myFile = open(sys.argv[1],'w')
        print(sys.argv[1])
        myFile.close()
    else:
        print('ERROR: Missing a .txt file as input argument to file')
    sys.exit()
