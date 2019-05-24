import os

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