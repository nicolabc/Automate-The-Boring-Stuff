import os,sys,re

if __name__ == '__main__':
    print("Please input the regex which will be used to search for matches in all .txt files in the current directory: ")
    regex = input()
    #regex = "ADJECTIVE"
    #regex = re.compile(r.join(str(regex)))
    searchResults = []
    ## TODO: Search for all .txt files in current directory
    filename = "panda.txt"
    
    currentFile = open(filename,'r')
    allWords = map(lambda l: l.split(" "), currentFile.readlines())
    allWords = list(allWords)
    for line in allWords:
            for word in line:
                if re.search(regex,word):  #If the word is found
                    searchResults.append(word) #Append the search result to the list
                
    print(searchResults)
    sys.exit()
