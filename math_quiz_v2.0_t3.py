##
# File Name: math_quiz_v2.0_t3.py
# Author: Nathan Wong
# Version: 2.0
# Date Created: 18/8/2021
# Date Modifided: 30/8/2021

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
def math_question_answer(num_one,num_two,answer,points):
    # Ask user for answer input.
    answer_input = force_number("Enter the answer: ")
    # Print correct if input = sum of question values.
    if answer_input == answer:
        points += 1
        print("Correct!")
    # Print incorrect if input != sum of question values.
    elif answer != answer_input:
        print("Incorrect!")
    return points

# Set up score function.

# Set up Coin flip function.
def coin_flip(points,question_count):
    flip = input("Would you like to flip a coin? ")
    if flip == "yes":
        heads_tails = input("Would you like to bet on heads or tails? ")
        flip_times = force_number("How many time to flip the coin? ")
        for i in range(flip_times):
            coin = random.randrange(0,2)
            if coin == 0:
                print("Heads!")
                if heads_tails == "heads":
                    print("You double your Koru!")
                    points = (points*2)
                else:
                    print("You lose")
                    points = 0
            elif coin == 1:
                print("Tails!")
                if heads_tails == "tails":
                    print("You double your Koru!")
                    points = (points*2)
                else:
                    print("You lose")
                    points = 0
    else:
        print("No flip!")

# Set up __main__ == __name__ function.
if __name__ == "__main__":
    choice = ""
    points = 0
    question_count = 0
    # Print the welcome screen
    print("""Kia ora & Welcome!
We are excited to have you here.
Get ready for the questions.\n""")
    # Runs program until user enters 'q' to quit.
    while choice != 'q':
        # Runs the math question generator function, and stores values
        num_one,num_two,answer = math_question_genrator()
        # Runs answer input function and passes in values
        points = math_question_answer(num_one,num_two,answer,points)
        question_count += 1
        # Every 3 questions run coin flip function
        if question_count % 3 == 0:
            coin_flip(points,question_count)
        choice = input("Type 'q' to quit or press enter to continue: ").lower()

    print("Exiting program")
