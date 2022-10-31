# implement a program that:
#Prompts the user for a level n, . If the user does not input 1, 2, or 3, the program should prompt again.
#Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with n digits.
#  No need to support operations other than addition (+).
#Prompts the user to solve each of those problem. If an answer is not correct (or not even a number), the program should output
#  EEE and prompt the user again, allowing the user up to three tries in total. If the user has still not answered correctly after
#  three tries, the program should output the correct answer.
#The program should ultimately output the user’s score, a number out of 10.
#Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, 
# or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is
#  not 1, 2, or 3:

import random


def main():
    
        score = 0
        level = get_level()
        for i in range (10) :
            x = generate_integer(level)
            y = generate_integer(level)
            try:
                question = input(f'{x} + {y}= ')
                if int(question) != x + y :
                    print('EEE')
                    question = input(f'{x} + {y}= ')
                    if int(question) != x + y :
                        print('EEE')
                        question = input(f'{x} + {y}= ')
                        if int(question) != x + y :
                            print('EEE')
                            print(f'{x} + {y}= ',x + y)
                            pass
                    
                elif int(question) == x+y :
                    score = score + 1
                    pass
            except ValueError :
                print('EEE')
                pass
        print('score=',score)
        
def get_level():
    while True:
        level = input('Level: ')
        if (level) in ('123'):
            return int(level)
            break

def generate_integer(level):
    if level == 1 :
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    else:
        raise ValueError

    return x and y

if __name__ == "__main__":
    main()






















