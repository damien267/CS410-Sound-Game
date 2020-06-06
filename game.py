#Damien Jones, Jesse Emerson
#©2020 PSU CS410P Music and Sound project
#Project is written in python3 and can be compiled and ran using the python3 
#prefix followed by the file name. ex: 
#   python3 file_name.py

import time
import random

from note import envelope, Note, SAMPLE_RATE
from interval import play, rand_interval, rand_chord, rand_scale, play_arpeg, Interval, Chord, Scale   
from data import *
from theme import play_theme

# Dummy container for saved sounds, to check compilation
playable = ["snd1.wav", "snd2.wav"] #NOT USED YET<-------------
# List to add sounds once played.
played = [] #NOT USED YET<-------------
#Remove interval playable list OR add to a played list.


SCORE = 0
# *** Changed var name so it wouldn't clash with round() function:
game_round = 1
GUESSES = 0
AWARD_POINTS = 5
COUNT = 1

# Get interval/chord/scale object:
interval_to_guess = rand_interval()
chord_to_guess = rand_chord()
scale_to_guess = rand_scale()

# DEFINE CORRECT ANSWER HERE
correct_answer = interval_to_guess.name
#correct_answer = chord_to_guess.name
#correct_answer = scale_to_guess.name

# Getting a random selection from possible_answers to fill multiple choice options

# Intervals/Chords/Scales defined in data.py list intervals:
possible_answers = intervals 
#possible_answers = list(chords.keys())
#possible_answers = list(scales.keys())

# Uncomment to add more false values to possible answers
#false_answers = ["P5","M5","m5","A4/d3","m8"]
#possible_answers.extend(false_answers)

answers_used = []
choices = []
choices.append(correct_answer)
possible_answers.remove(correct_answer)

temp_list = possible_answers.copy() #NOT USED <---------------


def increment_COUNT():
    global COUNT
    COUNT += 1

def count_reset():
    global COUNT
    COUNT = 1

def increment_SCORE():
    global SCORE
    SCORE += AWARD_POINTS

def reset_SCORE():
    global SCORE
    SCORE = 0

def increment_GUESSES():
    global GUESSES
    GUESSES += 1

def increment_round():
    global game_round
    game_round += 1

def decrement_round():
    global game_round
    game_round -= 1


def fill_choices():
    random_choice = random.choice(possible_answers)

    while COUNT < 4:
        if random_choice in answers_used:
            fill_choices()
        else:
            answers_used.append(random_choice)
            choices.append(random_choice)
            #print("Choice " + str(COUNT), " = " + str(choices))
            increment_COUNT()
            break


# -------------------------->Game start<-------------------------------------#

print ("Welcome to CS410P Sound, the game!!\n")

# PLAY THEME MUSIC <-----------
play_theme()

name = input("Please enter your name:")
print("\n   Welcome, " + name, "Lets get started...\n")

# PAUSE 1 sec
time.sleep(1)

# Declare how many rounds to play
while game_round < 2:

    
    print("Beginning round " + str(game_round), "...\n")
    print("   -------------       ---------------")
    print("   |  Round " + str(game_round), " |       |  Score - " + str(SCORE), " |")  
    print("   -------------       ---------------")
    print("\n")

    time.sleep(1)
    #Play random sound here
    print("Playing interval...\n")
    time.sleep(0.5)

# PLAY INTERVAL<--------------------------------------

    # Play a random interval/chord/scale for user to guess: 
    interval_to_guess.play_interval()
    #chord_to_guess.play_chord()
    #scale_to_guess.play_scale()

    # REPLAY INTERVAL loop. Will continue to ask until y,n,q is pressed
    replay_interval = None
    while replay_interval not in ("c","q"):
        print("Would you like to: ")
        print("\n (r)eplay sound again")
        print(" (p)lay notes seperately")
        print(" (c)ontinue\n")
        replay_interval = input("Enter choice followed by the ENTER key: ")
        if replay_interval == "r":
            print("Replaying interval...\n")
            time.sleep(1)

            # If user wants to hear the interval/chord/scale again: 
            interval_to_guess.play_interval()
            #chord_to_guess.play_chord()
            #scale_to_guess.play_scale()

        elif replay_interval == "c":
            break

        # If Interval/Chord, possible option to hear notes separately (Interval) or arpeggio (Chord):
        elif replay_interval == "p":
            chord_to_guess.play_arpeg()

        else: 
            print("Invalid input, please try again...\n")

    # USER CHOICE SELECTION loop.

    print("\n          Here are your choices...\n")
    time.sleep(0.5)


    user_selection = None

    for a in range(0,4):
        fill_choices()


    while user_selection not in ("1", "2", "3", "4", "q"):
        random.shuffle(choices)


        #print("\n 1) " + str(choices[0]), "\n 2) " + str(choices[1]), "\n 3) " + str(choices[2]), "\n 4) " + str(choices[3]), "\n q) QUIT\n")
        print("\n 1) " + str(choices[0]))
        print(" 2) " + str(choices[1])) 
        print(" 3) " + str(choices[2])) 
        print(" 4) " + str(choices[3])) 
        print(" q) QUIT\n")
        
        user_selection = input("Enter choice followed by the ENTER key:")
        print("\n")

        if user_selection == "1":
        #print("choices " + str(choices[0]), "  correct answer " + str(correct_answer[0]), "\n")
            if choices[0] == correct_answer:
                print("CORRECT ANSWER, YOU WIN " + str(AWARD_POINTS), " POINTS!")
                increment_SCORE()
            else:
                print("selection 1 is incorrect") # CHOICE 1
                time.sleep(1)

        elif user_selection == "2":
            #print("choices " + str(choices[1]), "  correct answer " + str(correct_answer[0]), "\n")
            if choices[1] == correct_answer:
                print("CORRECT ANSWER, YOU WIN " + str(AWARD_POINTS), " POINTS!")
                increment_SCORE()
            else:
                print("selection 2 is incorrect") # CHOICE 2
                time.sleep(1)

        elif user_selection == "3":
            #print("choices " + str(choices[2]), "  correct answer " + str(correct_answer[0]), "\n")
            if choices[2] == correct_answer:
                print("CORRECT ANSWER, YOU WIN " + str(AWARD_POINTS), " POINTS!")
                increment_SCORE()
            else:
                print("selection 3 is incorrect") # CHOICE 3
                time.sleep(1)

        elif user_selection == "4":
            #print("choices " + str(choices[3]), "  correct answer " + str(correct_answer[0]), "\n")
            if choices[3] == correct_answer:
                print("CORRECT ANSWER, YOU WIN " + str(AWARD_POINTS), " POINTS!")
                increment_SCORE()
            else:
                print("selection 4 is incorrect") # CHOICE 4
                time.sleep(1)

        elif user_selection == "q":
            print("Thank you for playing, goodbye...") # QUIT
            # PAUSE 1 sec
            time.sleep(1)
            break
        else:
            print("Invalid input, please try again")

    print("\n\n")
    increment_round()

decrement_round()
print("Your final score is " + str(SCORE), ", after " + str(game_round), " rounds!")
if SCORE == (game_round * 5):
    print("      PERFECT SCORE!!!!!!!!!!!!")
elif SCORE > 5:
    print("      GREAT JOB!!!!")
elif SCORE > 10:
    print("      EXCELLENT JOB!!!!!!!!")
time.sleep(1)
print("\nThank you for playing, goodbye...\n") # QUIT
# PAUSE 1 sec
time.sleep(1)


