##
# File Name: math_quiz_5.py
# Author: Nathan Wong
# Version: 5.0.0
# Date Created: 18/8/2021
# Date Modifided: 25/8/2021

# Import libraries.
import random

def force_number(user_input):
    """ Check if number is a valid interger and returns input """
    while True:
        try:
            # Checks if value is an interger.
            number = int(input(user_input))
            break
        except ValueError:
            print("Please enter a valid number")
    return number

# Set up maths question generator.
def math_question_genrator():
    # Generate 2 random numbers.
    num_one = random.randrange(1,100)
    num_two = random.randrange(1,100)
    answer = (num_one + num_two)
    # Print 2 numbers to users.
    print("What does {} + {} =".format(num_one,num_two))
    # Return two values
    return(num_one,num_two,answer)

# Set up maths question answer input.
def math_question_answer(num_one,num_two,answer):
    # Ask user for answer input.
    answer_input = force_number("Enter the answer: ")
    # Print correct if input = sum of question values.
    if answer_input == answer:
        print("Correct!")
    # Print incorrect if input != sum of question values.
    elif answer != answer_input:
        print("Incorrect!")

# Set up score function.

# Set up Coin flip function.
    
    # Flip a coin.

# Set up __main__ == __name__ function.
if __name__ == "__main__":
    choice = ""
    # Print the welcome screen
    print("""Kia ora & Welcome!
We are excited to have you here.
Get ready for the questions.\n""")
    # Runs program until user enters 'q' to quit.
    while choice != 'q':
        # Runs the math question generator function, and stores values
        num_one,num_two,answer = math_question_genrator()
        # Runs answer input function and passes in values
        math_question_answer(num_one,num_two,answer)
        choice = input("Type 'q' to quit or press enter to continue: ").lower()
    print("Exiting program")
