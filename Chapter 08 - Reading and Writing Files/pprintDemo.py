import sys,pprint


if __name__ == '__main__':
    cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
    pprint.pformat(cats)

    fileObj = open('myCats.py', 'w')
    fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
    fileObj.close()
    sys.exit()