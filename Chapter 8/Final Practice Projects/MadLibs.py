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
        allWords = map(lambda l: l.split(" "), myFile.readlines())
        allWords = list(allWords)
        newAllWords = []
        wordRegex = re.compile(r'ADJECTIVE|NOUN|VERB')
        # Go through each word and replace with input
        for line in allWords:
            for word in line:
                if wordRegex.search(word.upper()):
                #could also used a modified version of the following, but need to take "," and "." into account
                #if word.upper() == 'ADJECTIVE' or word.upper() == 'NOUN' or word.upper() == 'VERB':
                    foundWord = wordRegex.search(word.upper())
                    a = 'an' if foundWord.group() == 'ADJECTIVE' else 'a'  # Simply to print an or a depending on the word
                    print('Please enter ' + a + ' ' + word.lower() + ":")
                    # try:
                    newAllWords.append(input())
                    # except:
                    continue
                newAllWords.append(word)
        #print(newAllWords)
        saveFile = open(sys.argv[1]+'Completed','w')
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





