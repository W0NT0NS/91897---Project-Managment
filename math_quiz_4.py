##
# File Name: math_quiz_4.py
# Author: Nathan Wong
# Version: 4.0.0
# Date Created: 18/8/2021
# Date Modifided: 24/8/2021

# Import libraries.
import random

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
    answer_input = int(input("Enter the answer: "))
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
    # Runs program until user enters 'q' to quit.
    while choice != 'q':
        # Runs the math question generator function, and stores values
        num_one,num_two,answer = math_question_genrator()
        # Runs answer input function and passes in values
        math_question_answer(num_one,num_two,answer)
        choice = input("Type 'q' to quit or press enter to continue: ")
    print("Exiting program")
