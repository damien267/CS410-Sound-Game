# Interval:
# To play a random interval use rand_interval(). The default time is 2 seconds.
# Chord:
# To play a random chord, use rand_chord(). The default time is 2 seconds.
# Scale:
# To play a random scale, use rand_scale(). The default time is .25 seconds per note.
#

import numpy as np
import simpleaudio as sa
import math
import random
from note import envelope, Note, SAMPLE_RATE
from data import *

def play(audio):
    play = sa.play_buffer(audio, 1, 2, SAMPLE_RATE)
    play.wait_done()

def rand_interval():
    lo_index = random.randint(45, 57)
    hi_index = lo_index + random.randint(0, len(intervals) - 1)
    the_interval = Interval([lo_index, hi_index])
    return the_interval

def rand_chord():
    rand_chord = random.randint(0, len(chords) - 1)  
    a_chord = list(chords)[rand_chord] 
    the_chord = Chord(a_chord)
    return the_chord

def rand_scale():
    rand_scale = random.randint(0, len(scales) - 1)
    a_scale = list(scales)[rand_scale]  
    the_scale = Scale(a_scale)
    return the_scale

def play_arpeg(chord_name, seconds=.5):
    the_chord = Chord(chord_name)
    for note in the_chord.notes:
        n = note.calc_audio(seconds)
        play(n)

##### Interval #####
class Interval(object):
    def __init__(self, the_notes):
        self.lo = the_notes[0] 
        self.hi = the_notes[len(the_notes) - 1]
        self.name = intervals[(int(self.hi) - int(self.lo)) % 12]
        self.notes = [] # These are Note objects.
        for note in the_notes:
            self.notes.append(Note(all_notes[note][0], all_notes[note][2]))
      
    def sum_sines(self, seconds):
        num_samples = seconds * SAMPLE_RATE
        y = np.zeros(num_samples)
        for n in self.notes:
            sound = n.calc_sine(seconds)
            y += sound
        audio = envelope(seconds) * y * (2**15 - 1) // np.max(np.abs(y))
        audio = audio.astype(np.int16)
        return audio
   
    def play_sound(self, seconds=2, arpeg=False):
        audio = self.sum_sines(seconds)
        play(audio)

    def play_arpeg(self, seconds=.25):
        for note in self.notes:
            n = note.calc_audio(seconds)
            play(n)

##### Chord #####
class Chord(Interval):
    inversion = 0 
    def __init__(self, name):
        self.offset = 48
        self.name = name
        self.chord = chords[name] 
        self.notes = [] # These are Note objects.
        for note in self.chord:
            self.notes.append(Note(all_notes[note + self.offset][0], all_notes[note + self.offset][2]))

    def play_sound(self, seconds=2, arpeg=False):
        audio = self.sum_sines(seconds)
        play(audio)
 
##### Scale #####
class Scale(Interval):
    def __init__(self, pattern):
        self.offset = 48
        self.name = pattern  
        self.pattern = scales[pattern]
        self.notes = [] # These are Note objects.
        for n in self.pattern:
            self.notes.append(Note(all_notes[n + self.offset][0], \
                all_notes[n + self.offset][2]))

    def play_sound(self, seconds=.25):
        a_scale = []
        for n in self.notes:
            audio = n.calc_audio(seconds)
            a_scale.append(audio)
        if self.name != 'harmonic minor' and self.name != 'melodic minor':
            rev = self.notes.copy() 
            rev.reverse()
            rev = rev[1:len(rev)] 
            for n in rev:
                audio = n.calc_audio(seconds)
                a_scale.append(audio)
        for s in a_scale:
            play(s)

def main():
    ### Tests ###
    i = rand_interval()
    print(i.name)
    c = rand_chord();
    print(c.name)
    s = rand_scale();
    print(s.name)

if __name__ == "__main__":
    main()

