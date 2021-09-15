##
# File Name: math_quiz_v3.2.py
# Author: Nathan Wong
# Version: 3.2
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


def math_question_genrator(level, MIN_RANGE):
    """ Generates math questions, and displays the question to the users
        returns values to the main function. """
    # Generate 2 random numbers, level increases per 3 questions answered.
    num_one = random.randrange(MIN_RANGE, level)
    num_two = random.randrange(MIN_RANGE, level)
    # Sets the answer equal to the 2 values multipled.
    answer = (num_one * num_two)
    # Print 2 numbers to users.
    print("What does {} * {} =".format(num_one, num_two))
    # Return two values
    return(num_one, num_two, answer)


# Set up maths question answer input.
def math_question_answer(num_one, num_two, answer, points,
                         POINTS_PER_QUESTION):
    """ Asks user to enter answer of the question and gives points
        if the user enters the correct answer. """
    # Ask user for answer input.
    answer_input = force_number("Enter the answer: ")
    # Print correct if input = sum of question values.
    if answer_input == answer:
        points += POINTS_PER_QUESTION
        print("Correct!\n")
    # Print incorrect if input != sum of question values.
    elif answer != answer_input:
        print("Incorrect!\n")
        print("The correct answer was {}.".format(answer))
    return points


# Set up Coin flip function.
def coin_flip(points, question_count, ZERO_VALUE, MAX_FLIP_RANGE,
              POINTS_MULTIPLER, TAILS):
    """ Displays points to user and asks if they want to flip a coin
        If user selects flip then asks user for heads or tails. If
        The user gets it right then the users 2* there points. It then
        Asks if the user want's to double down there points. """
    # Ask if user want's to gamble points, and displays total points.
    print("You currently have {} Korus, do you keep it safe?".format(points))
    while True:
        try:
            # Asks user if they would like to flip a coin.
            flip = input("Would you like to flip a coin? ").lower()
            # Null protection.
            if not flip:
                raise Exception
            # Interger protection.
            if flip.isnumeric():
                raise Exception
        # If exception was raised, ask user to enter valid and loop.
        except Exception:
            print("Please type 'yes' or 'no'.\n")
            continue
        else:
            # If successful end loop.
            break
    # Checks if user want's to flip a coin.
    if flip == "yes":
        heads_tails = ""
        while True:
            try:
                # Asks user if they want to bet on heads or tails.
                while heads_tails != "heads" and heads_tails != "tails":
                    heads_tails = input("""Would you like to bet on heads
or tails? """).lower()
                    # Null proection.
                    if not heads_tails:
                        raise Exception
                    # Interger protection.
                    if heads_tails.isnumeric():
                        raise Exception
            # If exception is raised tell user to enter valid input and loop
            except Exception:
                print("Please  type 'heads' or 'tails.\n")
                continue
            else:
                break

        # if user selected yes to flip a coin.
        while True:
            # Flip a number between 0 and 1.
            coin = random.randrange(ZERO_VALUE, MAX_FLIP_RANGE)
            # Checks if value is 0.
            if coin == ZERO_VALUE:
                print("Heads!")
                if heads_tails == "heads":
                    print("You double your Koru!")
                    # Double the users points if they land correct head/tail.
                    points = (points*POINTS_MULTIPLER)
                    double_down = ""
                    while double_down != "yes" and double_down != "no":
                        double_down = input("""Would you like to risk it
and double down? """).lower()
                    if double_down == "yes":
                        continue
                    else:
                        break
                else:
                    print("You lose")
                    # Sets the users point(s) to zero if they lose
                    points = ZERO_VALUE
                    break
            # If coin lands on 1 then display tails
            elif coin == TAILS:
                print("Tails!")
                if heads_tails == "tails":
                    print("You double your Koru!")
                    # Double the users points if they land correct head/tail.
                    points = (points*POINTS_MULTIPLER)
                    # Asks user if they would like to double down.
                    double_down = ""
                    while double_down != "yes" and double_down != "no":
                        double_down = input("""Would you like to risk it
and double down? """).lower()
                    if double_down == "yes":
                        continue
                    else:
                        break
                else:
                    print("You lose")
                    points = ZERO_VALUE
                    break
        else:
            # If user chooses to not flip a coin, display no flip.
            print("No flip!")
    return points

# Set up __main__ == __name__ function.
if __name__ == "__main__":
    choice = ""
    # The minimum value each number can be for the problem.
    MIN_RANGE = 1
    # The amount question count increases per question.
    QUESTION_INCREASE = 1
    # How many questions before the program asks the user to flip a coin.
    FLIP_COIN = 3
    # Set's Zero constant.
    ZERO_VALUE = 0
    # Sets the amount the max range increases for each number generated.
    DIFFICULTY_INCREASE = 5
    # The number of sides to the coin.
    MAX_FLIP_RANGE = 2
    # The Multipler of points if user lands flip.
    POINTS_MULTIPLER = 2
    # Value of tails, on a 2 sided coin
    TAILS = 1
    # Amount of points the program awards per given question being correct.
    POINTS_PER_QUESTION = 1
    # Sets users total points to zero,
    points = 0
    # Rests question count to zero,
    question_count = 0
    # Sets the base level of the Program.
    level = 10
    # Print the welcome screen
    print("""Kia ora & Welcome!
We are excited to have you here.
Get ready for the questions.\n""")
    # Runs program until user enters 'q' to quit.
    while choice != 'q':
        # Runs the math question generator function, and stores values
        num_one, num_two, answer = math_question_genrator(level, MIN_RANGE)
        # Runs answer input function and passes in values
        points = math_question_answer(num_one, num_two, answer, points,
                                      POINTS_PER_QUESTION)
        question_count += QUESTION_INCREASE
        # Every 3 questions run coin flip function
        if question_count % FLIP_COIN == ZERO_VALUE and points != ZERO_VALUE:
            points = coin_flip(points, question_count, ZERO_VALUE,
                               MAX_FLIP_RANGE, POINTS_MULTIPLER, TAILS)
            level += DIFFICULTY_INCREASE
        print("""You currently have {} Koru(s), get answers correct
to get more!\n""".format(points))
        choice = input("Type 'q' to quit or press enter to continue: ").lower()
        print("\n")

    print("Exiting program")

