import numpy as np
import simpleaudio as sa
import math
from note import *
from data import *

def play(audio):
  play = sa.play_buffer(audio, 1, 2, SAMPLE_RATE)
  play.wait_done()

##### Interval #####
class Interval(object):
  def __init__(self, theNotes):
    # freq_to_index returns float, for whatever reason:
    self.lo = freq_to_index[theNotes[0]] 
    self.hi = freq_to_index[theNotes[len(theNotes) - 1]]
    self.name = intrvl[(int(self.hi) - int(self.lo)) % 12]
    # These are Note objects:
    self.notes = []
    for note in theNotes:
      self.notes.append(Note(freq_to_note[note], note))

  def sumSines(self, seconds):
    num_samples = seconds * SAMPLE_RATE
    y = np.zeros(num_samples)
    for n in self.notes:
      sound = n.calcSine(seconds)
      y += sound
    #Not sure if the floor division is a problem:
    audio = envelope(seconds) * y * (2**15 - 1) // np.max(np.abs(y))
    audio = audio.astype(np.int16)
    return audio
  
  def playArpeg(self, seconds=.25):
    for note in self.notes:
      n = note.calcAudio(seconds)
      #TODO Needs to play more smoothly:
      play(n)

# TODO Need to add chords to data.py
##### Chord #####
class Chord(Interval):
  inversion = 0 
  start = 4
  def __init__(self, notes):
    self.name = ""
    super().__init__(notes)

##### Scale #####
class Scale(Interval):
  diffDown = False

  def __init__(self, pattern):
    self.offset = 48
    self.name = pattern  
    self.pattern = patterns[pattern]
    self.notes = []
    for n in self.pattern:
      self.notes.append(Note(allNotes[n + self.offset][0], \
        allNotes[n + self.offset][2]))
    #for n in self.pattern:
      #self.notes.append(Note(nd[n + self.offset]))

  #TODO Need to add descending:
  def playScale(self, seconds=.25):
    aScale = []
    for n in self.notes:
       audio = n.calcAudio(seconds)
       aScale.append(audio)
    #TODO Needs to play more smoothly:
    for s in aScale:
      play(s)

def main():
  ##### SCALE TEST #####
  maj = Scale('lydian')
  #print(maj.hi)
  maj.playScale()


if __name__ == "__main__":
  main()

