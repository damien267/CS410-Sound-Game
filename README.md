# Course Project: Speech Adventure Game
**Note:** We're calling the Course Project by the name Bart selected (as requested in the Course Project instructions), however it does not accurately reflect what the Course Project turned out to be!  
  
The Course Project is a game and/or educational tool that plays intervals/chords/scales and offers the user a list from which to choose the answer. The game starts with a theme song (generated using the program itself) and some user input (name, number of rounds to play). Then the program plays a randomly selected interval, chord, or scale. If the user guesses correctly, the program plays a sound effect (which changes based on how many total correct the user has). This continues until the user selected number of rounds have been completed or the user chooses to quit early.  

## Authors  
Jesse Emerson: jemerson@pdx.edu  
Damien Jones: damien2@pdx.edu  

## GitHub  
The program repo is at:  

`https://github.com/mrloquacious/game`

The sound effects were generated using the code in the `effect1` branch of the repo at:  

`https://github.com/mrloquacious/mel`

## How To Use  
This program requires `Python 3` libraries `numpy`, `pandas`, and `simpleaudio` as well as `time`, `math`, and `random`.  
To run, enter:  

`python3 game.py`

## How it Went  
This project, written in Python, started with a proposal for a choose your own adventure type game with voice recognition to parse user choices and speech synthesis to provide user choices. It ended up as a interval/chord/scale game with no voice recognition or speech synthesis. Sometimes that's the way it goes. Installing the CMU Sphinx libraries for C and Python (see below) was a challenge. We got basic functionality going using examples from the Python Pockesphinx documentation, but opted to use the old standby, keyboard text input, to gather user responses. On the other hand, we couldn't even get Festival/Speech-Tools/Festvox fully installed and running, and abandoned that venture in favor of ensuring we'd have enough time to develop a working game.  
  
In the end, it's a basic program that works nicely! Not the most ambitious project, perhaps, but the program does successfully run as intended. Of course, it could be improved in a number of ways (generate and add more sound effects, incorporate chord inversions, use sounds other than sine wave, etc.), but we got the program to a good stopping place. What didn't go well was ... well, the *original* idea for the Course Project outlined in the Project Proposal didn't even remotely happen, so that's the big thing.  

## Testing
Testing was limited to informal tests as we worked on the project. No unit tests were performed and no systematic approach to testing was taken. However, enough informal testing was done to know that it's pretty hard to "break" the program in its current form.  

## Technology  

Along with basic libraries like `math`, `random`, we also used:  
* `numpy`  
* `simpleaudio`  
* `pandas`

Also, didn't end up using these libraries for the project, but did explore them:  
* `sphinxbase`, `pocketsphinx`, `python-pocketsphinx`  
* `festival`, `speech-tools`, `festvox`  

Finally, to create the sound effects, also used:  
* `wavio`  

## Credits  
The `RealPython` article Bart mentioned in the `HW1` assignment, Bart's collection of repositories at `pdx-cs-sound`, and `HW1` and `HW2` assignments formed the foundation of knowledge for the course project.  
* https://github.com/pdx-cs-sound  
* https://realpython.com/playing-and-recording-sound-python/  

