##
# File Name: math_quiz_v1.2.py
# Author: Nathan Wong
# Version: 1.2
# Date Created: 18/8/2021
# Date Modifided: 21/8/2021

# Import libraries.
import random

# Set up maths question generator.
def math_question_genrator():
    # Generate 2 random numbers.
    num_one = random.randrange(1,1000)
    num_two = random.randrange(1,1000)
    answer = (num_one + num_two)
    # Print 2 numbers to users.
    print(num_one)
    print(num_two)
    # Print sum of 2 numbers to users.
    print(answer)
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

# Set up Coin flip function
    
    # Flip a coin

# Set up __main__ == __name__ function.
while __name__ == "__main__":
    num_one,num_two,answer = math_question_genrator()
    math_question_answer(num_one,num_two,answer)
    # Set up menu for program
