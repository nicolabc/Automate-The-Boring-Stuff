import os,sys


if __name__ == '__main__':

    helloFile = open('hello.txt') #Opens the txt file in read mode
    helloContent = helloFile.read() #Returns the content as a string

    helloFile = open('hello.txt')
    helloRead = helloFile.readlines() #Returns the content as a list

    print(helloContent)
    print()
    print(helloRead)

    baconFile = open('bacon.txt','w')
    baconFile.write('Hello world \n')
    baconFile.write('Bacon is not a vegetable')
    baconFile.close()

    sys.exit()