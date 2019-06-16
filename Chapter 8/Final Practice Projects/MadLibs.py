import os,sys,re

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
        #fileContent = myFile.read()
        #print(fileContent)

        # Use RegEx to find all words (upper- and lowercase) larger than 4 and smaller than 9 (covers possible NOUN, VERB and ADJECTIVE)
        #allMatchingWords = re.findall(r'\b[a-åA-Å]{4,9}\b', fileContent)
        # Could also have split each line by space
        # for i in lines:
        #    thisline = i.split(" ");
        # or this snippet:
        allWords = map(lambda l: l.split(" "), myFile.readlines())
        allWords = list(allWords)
        #print(allWords[0][0])
        i = 0
        # Go through each word and replace with input
        for i in allWords:
            for j in i:
                print(i)
                print(j)
            '''if word.upper() == 'ADJECTIVE' or word.upper() == 'NOUN' or word.upper() == 'VERB':
                a = 'an' if word.upper() == 'ADJECTIVE' else 'a'  # Simply to print an or a depending on word
                print('Please enter ' + a + ' ' + word.lower() + ":")
                # try:
                allWords = input()
                # except:'''
        '''for word in allWords:#allMatchingWords:
            if word.upper() == 'ADJECTIVE' or word.upper() == 'NOUN' or word.upper() == 'VERB':
                a = 'an' if word.upper() == 'ADJECTIVE' else 'a' #Simply to print an or a depending on word
                print('Please enter '+ a +' '+ word.lower()+":")
                #try:
                allWords = input()
                #except:
            i+=1'''



        myFile.close()
    else:
        print('ERROR: Missing a .txt file as input argument to file')
    sys.exit()





