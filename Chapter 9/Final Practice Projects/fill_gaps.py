#! python3
import sys,re,os,shutil


def findMissingPrefix(myList):
    highestVal = max(myList)
    smallesVal = min(myList)

    # Create a list of values in between smallest and biggest value
    newList = list(range(smallesVal,highestVal+1))

    #Create a list with all values not found in myList
    newList = [elem for elem in newList if elem not in myList]
    return newList


if __name__ == '__main__':
    #wholeFileName = re.compile(r'[a-zA-Z0-9._%+-]+\d\d\d[a-zA-Z0-9.-]+')
    prefixLength = 3 #Change these two if different zero padding is used for the prefix
    prefix = re.compile(r'\d\d\d')
    foundPrefixes = []

    # Find all files with prefix and add to list
    for root, dirs, files in os.walk("."):
        for d in dirs:
            #print(os.path.relpath(os.path.join(root, d), "."))
            continue
        for f in files:
            path = os.path.relpath(os.path.join(root, f), ".")
            if prefix.search(f) != None: #If a result is not empty
                generalFileName = f.split(prefix.search(f).group(0).zfill(prefixLength))
                foundPrefixes.append(int(prefix.search(f).group(0)))

    missingFiles = findMissingPrefix(foundPrefixes)
    i = 0
    for val in foundPrefixes:
        if missingFiles[i]<val:
            missingPrefix = str(missingFiles[i]).zfill(prefixLength)
            newFileName = generalFileName[0]+missingPrefix+generalFileName[1]
            print(newFileName)
            #shutil.move()
            i += 1
    sys.exit()




