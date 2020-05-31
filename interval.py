import numpy as np
import simpleaudio as sa
import math

import note

SAMPLE_RATE = note.SAMPLE_RATE

##### Interval #####
class Interval(object):

  octave = 4

  def __init__(self, name, notes):
    self.name = name
    self.notes = []
	
  def sumSines(self, notes, seconds):
    num_samples = seconds * SAMPLE_RATE
    y = np.zeros(num_samples)
    for anote in notes:
      sound = anote.calcSine(anote.freq, seconds)
      y += sound
    audio = note.envelope(seconds) * y * (2**15 - 1) /np.max(np.abs(y))
    audio = audio.astype(np.int16)
    return audio
  
  def playArpeg(self, notes, seconds):
    env = envelope(seconds)
    for note in notes:
      aNote = Note(note[0], note[1], note[2], seconds)
      audio = aNote.calcAudio()
      play(audio)
      
  def play(self, audio):
    play = sa.play_buffer(audio, 1, 2, SAMPLE_RATE)
    play.wait_done()

##### Chord #####

class Chord(Interval):
  inversion = 1
  start = 4
  def __init__(self, name, notes):
	  pass	
##### Scale #####

class Scale(Interval):
	
  diffDown = False
  patterns = { 'major' : [0,2,4,5,7,9,11,12], 'dorian' : [0,2,3,5,7,9,10,12] }

  def __init__(self, name, notes, pattern):
    self.pattern = patterns[pattern]

	#def playScale(pattern):
  #  for aNote in pattern:


def main():

  aNote = note.Note(note.allNotes[48][0], note.allNotes[48][1], 
      note.allNotes[48][2], 1)
  audio = aNote.calcAudio(aNote.freq, aNote.seconds)
  aNote.playNote(audio)

  n1 = note.Note(note.allNotes[33][0], note.allNotes[33][1], 
      note.allNotes[33][2], 1)
  n2 = note.Note(note.allNotes[37][0], note.allNotes[37][1], 
      note.allNotes[37][2], 1)
  I1 = Interval("intrvl", [n1,n2]) 
  #audio = I1.sumSines([n1, n2], 2)
  audio = I1.sumSines([n1, n2], 1)
  I1.play(audio)

  n3 = note.Note(note.allNotes[40][0], note.allNotes[40][1], 
      note.allNotes[40][2], 1)
  c1 = Chord("chrd", [n1,n2,n3]) 
  audio = I1.sumSines([n1, n2, n3], 1)
  c1.play(audio)

if __name__ == "__main__":
  main()

