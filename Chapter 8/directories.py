import os
os.path.join('usr','bin','spam')
os.getcwd()
#os.chdir('C:\\Windows\\System32')
print(os.listdir('..'))


totalBitSize = 0
os.chdir('..')              #Change current directory to parent directory
for i in os.listdir('.'):   #For each file in current directory
    totalBitSize = totalBitSize + os.path.getsize(i)
