##
# File Name: math_quiz_v3.0_t2.py
# Author: Nathan Wong
# Version: 3.0
# Date Created: 18/8/2021
# Date Modifided: 15/9/2021

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
def math_question_genrator(level):
    # Generate 2 random numbers.
    num_one = random.randrange(1,level)
    num_two = random.randrange(1,level)
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
        print("The correct answer was {}.".format(answer))
    return points

# Set up score function.

# Set up Coin flip function.
def coin_flip(points,question_count):
    print("You currently have {} Korus, you choose to gamble or play it safe".format(points))
    while True:
        try:
            flip = input("Would you like to flip a coin? ").lower()
            if not flip:
                raise Exception
            if flip.isnumeric():
                raise Exception
        except Exception:
            print("Please type 'yes' or 'no'.\n")
            continue
        else:
            break
    if flip == "yes":
        while True:
            try:
                heads_tails = input("Would you like to bet on heads or tails? ").lower()
                if not heads_tails:
                    raise Exception
                if heads_tails.isnumeric():
                    raise Exception
            except Exception:
                print("Please  type 'heads' or 'tails.\n")
                continue
            else:
                break
                    
        while True:
            coin = random.randrange(0,2)
            if coin == 0:
                print("Heads!")
                if heads_tails == "heads":
                    print("You double your Koru!")
                    points = (points*2)
                    double_down = input("Would you like to risk it and double down? ")
                    if double_down == "yes":
                        continue
                    else:
                        break
                else:
                    print("You lose")
                    points = 0
                    break
            elif coin == 1:
                print("Tails!")
                if heads_tails == "tails":
                    print("You double your Koru!")
                    points = (points*2)
                    double_down = input("Would you like to risk it and double down? ")
                    if double_down == "yes":
                        continue
                    else:
                        break
                else:
                    print("You lose")
                    points = 0
                    break
        else:
            print("No flip!")
    return points

# Set up __main__ == __name__ function.
if __name__ == "__main__":
    choice = ""
    points = 0
    question_count = 0
    level = 100
    # Print the welcome screen
    print("""Kia ora & Welcome!
We are excited to have you here.
Get ready for the questions.\n""")
    # Runs program until user enters 'q' to quit.
    while choice != 'q':
        # Runs the math question generator function, and stores values
        num_one,num_two,answer = math_question_genrator(level)
        # Runs answer input function and passes in values
        points = math_question_answer(num_one,num_two,answer,points)
        question_count += 1
        # Every 3 questions run coin flip function
        if question_count % 3 == 0 and points != 0:
            points = coin_flip(points,question_count)
            level += 100
        choice = input("Type 'q' to quit or press enter to continue: ").lower()

    print("Exiting program")
