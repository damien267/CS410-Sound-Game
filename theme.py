from note import envelope, Note, SAMPLE_RATE
from interval import play, rand_interval, rand_chord, rand_scale, play_arpeg, Interval, Chord, Scale   
from data import *

def play_theme(theTheme=0): 
  themes =[
      [45,57,56,57,54,57,52,57,50,57,47,57,52,57,40,57,33,45,44,45,42,45,40,45,38,45,35,45,40,45,28,45,33], 
      [33,33,47,48,38,36,38,36,33,33,47,48,43,39,38,36,33],
      [33,33,45,33,33,45,33,45,33,45,33,33,47,48,50,51,33,45,33,36,33,45,43,45,33,33,45,33,33,39,38,36],
      [33,28,31,32,33,39,38,36, 33,39,38,36,33,28,31,32] ]
  theme_audio = []
  for n in themes[theTheme]:
    # create notes
    a_note = Note(all_notes[n][0], all_notes[n][2])
    # calc audio
    theme_audio.append(a_note.calc_audio(.1))
  # play audio
  for a in theme_audio:
    play(a)

