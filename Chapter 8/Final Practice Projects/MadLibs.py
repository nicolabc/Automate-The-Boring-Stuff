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

    if len(sys.argv) >= 2 and ('.txt' in sys.argv[1]):
        myFile = open(sys.argv[1],'r+')
        fileContent = myFile.read()
        print(fileContent)
        # Go through each word and replace with input
        for word in fileContent:
            if word.toUpper() == 'ADJECTIVE' or word.toUpper() == 'NOUN' or word.toUpper() == 'VERB':
                print('Please enter a word for the '+ word)
            print(word)
        myFile.close()
    else:
        print('ERROR: Missing a .txt file as input argument to file')
    sys.exit()





