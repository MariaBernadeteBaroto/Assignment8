# Program 1. Lottery
# steps

print('Welcome to the game!')
print('Lets start!')

# ask for 3 numbers (0-9)
import random


def lottery():
    more_game = 'yes'
    while more_game[0] == 'y':

        random_number1 = random.randint(0,9)
        random_number2 = random.randint(0,9)
        random_number3 = random.randint(0,9)

        random_numbers = random_number1, random_number2, random_number3  # generated three(3) random numbers
        print(random_numbers)

        number1 = int(input('Enter first number: '))
        number2 = int(input('Enter second number: '))
        number3 = int(input('Enter three number: '))

        numbers = number1, number2, number3    # ask for three numbers

        if numbers == random_numbers:
            print('Winner!')    # Display 'winner' if all 3 input numbers matched the generated numbers
        else:
            print('You loss!')   # Display ' You loss' if not

        more_game = input('Wanna try again? (y or n): ')  # Display 'Try again y/n'
    # if the user enter 'y' the user will play again
    # if 'n' the program will exit 

lottery_game = lottery()

