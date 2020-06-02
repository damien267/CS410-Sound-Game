
# Interval:
# To play an interval use playInterval(seconds), where seconds is optional. The default is 2 seconds.
# Chord:
# To play a chord, use playChord(chordName), where chordName is a choice from the chords dict in data.py.
# 
# Scale:
#

import numpy as np
import simpleaudio as sa
import math
from note import envelope, Note, SAMPLE_RATE
from data import *

def play(audio):
  play = sa.play_buffer(audio, 1, 2, SAMPLE_RATE)
  play.wait_done()

def randInterval():
   # Choose from range for lo note:
  lo_index = random.randint(45, 57)
  hi_index = lo_index + random.randint(0, 12)
  theIntrvl = Interval([lo_index, hi_index])
  theIntrvl.playInterval()
  return [theIntervl.name, theInterval.notes]

# Add ability to play argeggio, if desired:
def replayInterval(arpeg=False):
  audio = self.sumSines(seconds)
  play(audio)
  theIntrvl = Interval([lo_index, hi_index])
  theIntrvl.playInterval()

def randChord():
  #TODO Choose randomly from the list:
  randChrd =  
  aChord = chords[randChrd] 
  theChord = Chord(aChord)
  theChord.playChord()
  # Not sure I'm returning the right thing: 
  return(randChrd)

def replayChord(chordName, arpeg=False):
  aChord = chords[chordName] 
  theChord = Chord(aChord)
  theChord.playChord()
 
def playArpeg(chordName, seconds=.5):
  theChord = Chord(chordName)
  for note in theChord.notes:
    n = note.calcAudio(seconds)
    #TODO Needs to play more smoothly:
    play(n)

def randScale():
  #TODO Choose randomly from the list:
  randScl = 
  aScale = patterns[randScl]  
  theScale = Scale(aScale)
  theScale.playScale()
  # Not sure I'm returning the right thing: 
  return(randScl)

def replayScale(scaleName):
  aScale = patterns[scaleName]  
  theScale = Scale(aScale)
  theScale.playScale()

##### Interval #####
class Interval(object):
  def __init__(self, theNotes):
    self.lo = theNotes[0] 
    self.hi = theNotes[len(theNotes) - 1]
    self.name = intrvl[(int(self.hi) - int(self.lo)) % 12]
    self.notes = [] # These are Note objects
    for note in theNotes:
      self.notes.append(Note(allNotes[note][0], allNotes[note][2]))

  # Want notes to be self.notes (notes of calling obj), unless arg passed. How to do?
  def playInterval(seconds=2):
    audio = self.sumSines(seconds)
    play(audio)

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

# TODO Need to add chords to data.py
##### Chord #####
class Chord(Interval):
  inversion = 0 
  offset = 48
  def __init__(self, name):
    self.name = name
    self.chord = chords[name] 
    self.notes = [] # These are Note objects
    for note in self.chord:
      self.notes.append(Note(allNotes[note + self.offset][0], allNotes[note + self.offset][2]))

def playChord(chordName, seconds=2):
  audio = theChord.sumSines(seconds)
  play(audio)

##### Scale #####
class Scale(Interval):
  # A few scales have different pattern on the way down:
  diffDown = False
  def __init__(self, pattern):
    self.offset = 48
    self.name = pattern  
    self.pattern = patterns[pattern]
    self.notes = []
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

def main():
  ##### INTERVAL TEST #####
  #intrval = Interval([55,57])
  #intrval.playSeparately()
  randIntervl()


if __name__ == "__main__":
  main()

