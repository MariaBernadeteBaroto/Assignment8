# Program 2: Guess the number

import random 

def guess_number():
    random_number = random.randint(0,100)  # Generate 1 random number (0-100)
    guess = int(input('Enter your guess number: ')) # Ask the user to guess the number
    while guess != random_number:


# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display "Greater than" if the inputed number is greater than the random number
# Display "Less than" if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.