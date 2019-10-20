import os,sys,re

# This is the code for the final project in chapter 8. Usage: "py MadLib.py panda.txt" in terminal
# Follow screen instructions. Finally open your_text.txt to see result
if __name__ == '__main__':

    if len(sys.argv) >= 2 and ('.txt' in sys.argv[1]):
        myFile = open(sys.argv[1],'r+')
        allWords = map(lambda l: l.split(" "), myFile.readlines())
        allWords = list(allWords)
        newAllWords = []
        # Create Regex to search for the specified words
        wordRegex = re.compile(r'ADJECTIVE|NOUN|VERB')
        # Go through each word and replace with input
        for line in allWords:
            for word in line:
                if wordRegex.search(word.upper()):  #If the word is found
                #could also used a modified version of the following, but need to take "," and "." into account
                #if word.upper() == 'ADJECTIVE' or word.upper() == 'NOUN' or word.upper() == 'VERB':
                    foundWord = wordRegex.search(word.upper())
                    a = 'an' if foundWord.group() == 'ADJECTIVE' else 'a'  # Simply to print an or a depending on the word
                    print('Please enter ' + a + ' ' + foundWord.group().lower() + ":")
                    newAllWords.append(wordRegex.sub(input(),word))     # Replace the word with the input word
                    continue
                newAllWords.append(word)
        newFileName = sys.argv[1].split(".")[0].join("Completed")
        with open('your_text.txt', 'w') as saveFile:
            for item in newAllWords:
                saveFile.write(str(item)+' ')
        saveFile.close()
        myFile.close()
    else:
        print('ERROR: Missing a .txt file as input argument to file')
    sys.exit()





