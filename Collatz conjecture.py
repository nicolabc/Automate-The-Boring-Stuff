#This is a program exploring what is called "The simplest impossible math problem" called Collatz sequence.
# You can read more about it here: https://en.wikipedia.org/wiki/Collatz_conjecture
#This is from chapter 3 (Practice project)

def collatz(num):
    if num%2 == 0:
        return num//2
    else:
        return 3*num+1

if __name__ == '__main__':
    num = input('Input an integer: ')
    num = int(num)
    i = 0
    while num != 1:
        num = collatz(num)
        print(num)
        i += 1
    print('Sequence length: ',i)

