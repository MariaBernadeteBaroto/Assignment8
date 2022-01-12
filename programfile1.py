# Program 1. Lottery
# steps

print('Welcome to the game!')
print('Lets start!')

# ask for 3 numbers (0-9)
import random


def lottery():
    more_game = 'yes'
    while more_game[0] == 'y':

        list_numbers = [0,1,2,3,4,5,6,7,8,9]
        random_numbers = random.sample(list_numbers, 3)  # generated three(3) random numbers
        print(random_numbers)
        
        guess_numbers = []

        while len(guess_numbers) < 3:
            UserInput = int(input("Enter a number: "))
            if UserInput not in guess_numbers:
                UserInput = guess_numbers.append(UserInput)
                print(guess_numbers)
            else:
                print("You already use this number, try to use another one (0-9): ")
            

        def count_char(guess_numbers, random_numbers):
            count = 0
            for c in random_numbers:
                for d in guess_numbers:
                    if c == d:
                        count = count + 1
            return count
        result = count_char(guess_numbers, random_numbers)

        if result == 3:
            print('Winner!')    # Display 'winner' if all 3 input numbers matched the generated numbers
        else:
            print('You loss!')   # Display ' You loss' if not

        more_game = input('Wanna try again? (y or n): ')  # Display 'Try again y/n'
    # if the user enter 'y' the user will play again
    # if 'n' the program will exit 

lottery()

