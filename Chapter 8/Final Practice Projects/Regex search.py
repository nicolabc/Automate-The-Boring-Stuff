import os,sys,re

if __name__ == '__main__':
    print("Please input the regex which will be used to search for matches in all .txt files in the current directory: ")
    regex = input()
    searchResults = []
    
    # Search for all .txt files in current directory
    allFiles = os.listdir(os.getcwd())
    txtFiles = []
    for file in allFiles:
        if re.search('.txt',file):
            txtFiles.append(file)
            
    # Loop through all .txt files in the folder
    for filename in txtFiles:
        currentFile = open(filename,'r')
        allWords = map(lambda l: l.split(" "), currentFile.readlines())
        allWords = list(allWords)
        for line in allWords:
                for word in line:
                    if re.search(regex,word):  #If the word is found
                        searchResults.append(word) #Append the search result to the list
                    
    print(searchResults)
    sys.exit()
