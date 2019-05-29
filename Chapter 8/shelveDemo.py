import os,sys,shelve


if __name__ == '__main__':
    shelfFile = shelve.open('mydata')
    cats = ['Zophie', 'Pooka', 'Simon']
    shelfFile['cats'] = cats
    shelfFile.close()

    shelfFile = shelve.open('mydata')
    print(shelfFile['cats'])
    print(list(shelfFile.keys()))
    print(list(shelfFile.values()))
    shelfFile.close()
    sys.exit()