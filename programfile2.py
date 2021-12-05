# Program 2: Guess the number

print('Welcome to the game')
print("Let's start!")

import random 

def guess_number():
    random_number = random.randint(0,100)  # Generate 1 random number (0-100)
    print(random_number)
    guess = int(input('Enter your guess number: ')) # Ask the user to guess the number
    while guess != random_number:
        if guess > random_number:   # Display "Greater than" if the inputed number is greater than the random number
            print('Greater than') 
            guess = int(input('Enter another guess number: '))
        if guess < random_number:   # Display "Less than" if the inputed number is less than the random number
            print('Less than')
            guess = int(input('Enter another guess number: '))
        # Repeat asking the user until the random number has been guessed correctly.
    print("You've got it!")

guess_number()


# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display "Greater than" if the inputed number is greater than the random number
# Display "Less than" if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.