# Course Project: Game
The course project is a game or learning tool that plays intervals/chords/scales and offers the user a list to choose the their answer from. The game starts with a theme song and the user choosing how many rounds to play. Then the program plays a randomly selected interval, chord, or scale. If the user guesses correctly, the program plays a sound effect (which changes based on how many total correct). This continues until the user selected number of rounds have been completed or the user chooses to quit early.  

## How it Went  
This project, written in Python, started with a proposal for a choose your own adventure type game with voice recognition to parse user choices and speech synthesis to provide user choices. It ended up as a interval/chord/scale game with no voice recognition or speech synthesis. Sometimes that's the way it goes. Installing the CMU Sphinx libraries for C and Python (see below) was a challenge. We got basic functionality going using examples from the Python Pockesphinx documentation, but opted to use the old standby, keyboard text input, to gather user responses. On the other hand, we couldn't even get Festival/Speech-Tools/Festvox fully installed and running, and abandoned that venture in favor of ensuring we'd have enough time to develop a working game.  



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
The jumping off points were the RealPython article Bart mentioned in the HW1 assignment, and Bart's portaudio-py-demos repository:  
* https://realpython.com/playing-and-recording-sound-python/  
* https://github.com/pdx-cs-sound/portaudio-py-demos  
