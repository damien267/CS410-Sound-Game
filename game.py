#Damien Jones, Jesse Emerson
#©2020 PSU CS410P Music and Sound project
#Project is written in python3 and can be compiled and ran using the python3 
#prefix followed by the file name. ex: 
#   python3 file_name.py

import time
import random
import simpleaudio as sa

# Modules created for the Course Project:
from note import envelope, Note, SAMPLE_RATE
from interval import play, rand_interval, rand_chord, rand_scale, Interval, Chord, Scale   
from data import *
from theme import play_theme

SCORE = 0
game_round = 1

# Default rounds is 1, player asked for number of rounds below
num_rounds = 1
GUESSES = 0
AWARD_POINTS = 5
COUNT = 1
num_correct = 0
sound_type = -1
correct_answer = ""
possible_answers = []
answers_used = []
choices = []

# Play sound effect:
def play_wav(filename):
    waveObject = sa.WaveObject.from_wave_file(filename)
    playObject = waveObject.play()
    playObject.wait_done()

# Get interval/chord/scale object:
def choose_sound():
    global sound_type
    sound_type = random.randint(0,2)
    if sound_type == 0:
        to_guess = rand_interval() 
    elif sound_type == 1:
        to_guess = rand_chord() 
    elif sound_type == 2:
        to_guess = rand_scale() 

    # DEFINE CORRECT ANSWER HERE
    global correct_answer
    correct_answer = to_guess.name

    # Determine possible answers based on sound type:
    global possible_answers
    possible_answers = list(sound_types[sound_type])

    global answers_used
    answers_used = []
    global choices
    choices = []
    choices.append(correct_answer)
    possible_answers.remove(correct_answer)

    return to_guess

def increment_COUNT():
    global COUNT
    COUNT += 1

def increment_SCORE():
    global SCORE
    SCORE += AWARD_POINTS

def increment_round():
    global game_round
    game_round += 1

def decrement_round():
    global game_round
    game_round -= 1

# Fill the list of possible choices for a question: 
def fill_choices():
    random_choice = random.choice(possible_answers)

    while COUNT < 4:
        if random_choice in answers_used:
            fill_choices()
        else:
            answers_used.append(random_choice)
            choices.append(random_choice)
            increment_COUNT()
            break

# Print the interval/chord/scale choices user can guess from: 
def print_choices(first_print=True):
    print("\n          Here are your choices...\n")
    time.sleep(0.5)

    for a in range(0,4):
        fill_choices()

    if first_print == True:
        random.shuffle(choices)

    print("\n 1) " + str(choices[0]))
    print(" 2) " + str(choices[1])) 
    print(" 3) " + str(choices[2])) 
    print(" 4) " + str(choices[3]) + "\n")  
    #print(" q) QUIT\n")
        
# Get the user choice for the question:
def get_choice():
    user_selection = input("Enter choice followed by the ENTER key: ")
    print("\n")
    while user_selection not in ("1","2","3","4"):
        user_selection = input(
        "That wasn't a valid selection. Choose '1', '2', '3', '4', followed by the ENTER key: ")
    return user_selection

# Determine if user choice is correct. Play a sound effect if it is:
def eval_choice(user_selection):
    
    user_choice = choices[int(user_selection) - 1] 
    if user_choice == correct_answer:
        print("CORRECT ANSWER, YOU WIN " + str(AWARD_POINTS), " POINTS!")
        increment_SCORE()
        time.sleep(.5)

        # Play sound effect for correct answer:
        global num_correct
        play_wav(correct_indicator[num_correct % 13])
        num_correct += 1
    elif user_selection == "q":
        return
    elif user_selection not in ("1","2","3","4","q"):
        print("Invalid input, please try again")
    else:
        print("\n" + user_choice + " is INCORRECT.\nThe CORRECT answer is:", correct_answer)
        time.sleep(3)

# Perform start game tasks:
def start_game():

   print("\n")
   print("     C        S   410PS  O       OUN     D&    M     U  SICFI")
   print("     N   A    L   P      R      O   J   E  C   TB   YD  A    ")
   print("      M I E  N    JON    E      S      A    N  D J E S  SEE  ")
   print("      ME   RS     O      N      T   H   A  N   K  Y  O  U    ")
   print("       F   O      RPLAY  ING!!   ENJ     OY    !     !  !!!!!")
   print("\n")


   # PLAY THEME MUSIC <-----------
   # Choose from list of themes in theme.py:
   play_theme(0)

   name = input("Please enter your name: ")

   print("\n                     OK " + name,", Lets get started...\n")
   global num_rounds
   num_rounds = int(input("               How many rounds would you like to play? "))
   print("\n")

   time.sleep(1)

# Perform end game tasks:
def end_game():
    decrement_round()
    print("     Your final score is " + str(SCORE), ", after " + str(game_round), " rounds!")
    if SCORE == game_round * 5 and SCORE > 0:
        print("      PERFECT SCORE!!!!!!!!!!!!")
    elif SCORE > 5:
        print("      GREAT JOB!!!!")
    elif SCORE > 10:
        print("      EXCELLENT JOB!!!!!!!!")
    time.sleep(1)
    print("\nThank you for playing, goodbye...\n")
    time.sleep(1)

# -------------------------->Game start<-------------------------------------#

start_game()

##### MAIN LOOP #####
while game_round <= num_rounds:

    print("                         Beginning round " + str(game_round), "...\n")
    print("                 -------------       ---------------")
    print("                 |  Round {:^2d}".format(game_round), "|       |  Score: {:^3d}".format(SCORE), "|")  
    print("                 -------------       ---------------")
    print("\n")
    time.sleep(1)
    
   # PLAY INTERVAL<--------------------------------------
    to_guess = choose_sound() 
   
    #Play randomly selected sound here:
    print("Playing " + sound_type_name[sound_type] + "...\n")
    time.sleep(0.5)

    # Play a random interval/chord/scale for user to guess, and print the choices: 
    to_guess.play_sound()
    print_choices()

    # REPLAY SOUND loop. Will continue to ask until y,n,q is pressed
    replay_sound = None
    while replay_sound not in ("q","1","2","3","4"):
        print("You can use the numbers to select the correct answer.\n")
        print("OR, if you'd like to hear the " + sound_type_name[sound_type] + " again: ")
        print("\n (r)eplay ", sound_type_name[sound_type])
        if sound_type != 2:
            print(" (p)lay notes seperately")
        replay_sound = input("\nEnter choice followed by the ENTER key: ")
        if replay_sound == "1" or replay_sound == "2" or replay_sound == "3" or replay_sound == "4":
            eval_choice(replay_sound)
        elif replay_sound == "r":
            print("Replaying " + str(sound_type_name[sound_type])  + "...\n")
            time.sleep(1)

            # If user wants to hear the interval/chord/scale again: 
            to_guess.play_sound()

        # If Interval/Chord, possible option to hear notes separately (Interval) or arpeggio (Chord):
        elif replay_sound == "p":
            print("Playing " + str(sound_type_name[sound_type])  + " notes separately ...\n")
            time.sleep(1)
            to_guess.play_arpeg()

        elif replay_sound == "q":
            break

        else: 
            print("Invalid input, please try again...\n")
    
    increment_round()
    print("\n\n")
    COUNT = 1
    
    if replay_sound == "1" or replay_sound == "2" or replay_sound == "3" or replay_sound == "4":
        continue
    else:
        # Show choices, get user selection and evalute:
        print_choices(False)
        user_selection = get_choice()
        eval_choice(user_selection)

##### END MAIN LOOP #####

end_game()

# -------------------------->Game end<-------------------------------------#

