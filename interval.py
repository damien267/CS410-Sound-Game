
# Interval:
# To play a random interval use randInterval(). The default time is 2 seconds.
# Chord:
# To play a random chord, use randChord(). The default time is 2 seconds.
# Scale:
# To play a random scale, use randScale(). The default time is .25 seconds per note.
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

def randInterval():
  lo_index = random.randint(45, 57)
  hi_index = lo_index + random.randint(0, 12)
  theIntrvl = Interval([lo_index, hi_index])
  theIntrvl.playInterval()
  return theIntrvl

def randChord():
  randChrd = random.randint(0, 24)  
  aChord = list(chords)[randChrd] 
  theChord = Chord(aChord)
  theChord.playChord()
  return theChord

def randScale():
  randScl = random.randint(0, 13)
  aScale = list(patterns)[randScl]  
  theScale = Scale(aScale)
  theScale.playScale()
  return theScale

def playArpeg(chordName, seconds=.5):
  theChord = Chord(chordName)
  for note in theChord.notes:
    n = note.calcAudio(seconds)
    #TODO Needs to play more smoothly:
    play(n)

##### Interval #####
class Interval(object):
  def __init__(self, theNotes):
    self.lo = theNotes[0] 
    self.hi = theNotes[len(theNotes) - 1]
    self.name = intrvl[(int(self.hi) - int(self.lo)) % 12]
    self.notes = [] # These are Note objects.
    for note in theNotes:
      self.notes.append(Note(allNotes[note][0], allNotes[note][2]))

  def playInterval(self, seconds=2, arpeg=False):
    audio = self.sumSines(seconds)
    play(audio)

   # Add ability to play argeggio, if desired:
  def replayInterval(self, arpeg=False):
    self.playInterval(arpeg)

  def sumSines(self, seconds):
    num_samples = seconds * SAMPLE_RATE
    y = np.zeros(num_samples)
    for n in self.notes:
      sound = n.calcSine(seconds)
      y += sound
    #Not sure if floor division is OK?:
    audio = envelope(seconds) * y * (2**15 - 1) // np.max(np.abs(y))
    audio = audio.astype(np.int16)
    return audio

  def playSeparately(self, seconds=.25):
    for note in self.notes:
      n = note.calcAudio(seconds)
      #TODO Needs to play more smoothly:
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
      self.notes.append(Note(allNotes[note + self.offset][0], allNotes[note + self.offset][2]))

  def playChord(self, seconds=2, arpeg=False):
    audio = self.sumSines(seconds)
    play(audio)

  def replayChord(self, arpeg=False):
    self.playChord(self.name, arpeg)
 
##### Scale #####
class Scale(Interval):
  # A few scales have different pattern on the way down:
  diffDown = False
  def __init__(self, pattern):
    self.offset = 48
    self.name = pattern  
    self.pattern = patterns[pattern]
    self.notes = [] # These are Note objects.
    for n in self.pattern:
      self.notes.append(Note(allNotes[n + self.offset][0], \
          allNotes[n + self.offset][2]))

  #TODO Need to add descending:
  def playScale(self, seconds=.25):
    aScale = []
    for n in self.notes:
      audio = n.calcAudio(seconds)
      aScale.append(audio)
    #TODO Needs to play more smoothly:
    for s in aScale:
      play(s)

def replayScale(self, seconds=.25):
  self.playScale()

def main():
  ### Tests ###
  i = randInterval()
  print(i.name)
  c = randChord();
  print(c.name)
  s = randScale();
  print(s.name)

if __name__ == "__main__":
  main()

