import numpy as np
import simpleaudio as sa
import random
import pandas as pd
import math

##### GLOBALS #####

SAMPLE_RATE = 8000

df = pd.read_csv('freq.csv', delimiter=',')
allNotes = [list(row) for row in df.values]

##### ENVELOPE #####

def envelope(seconds, attack_time=.001, release_time=.001):
  num_samples = seconds * SAMPLE_RATE
  att_env = np.linspace(0, 1, int(attack_time * SAMPLE_RATE), False)
  ones = np.ones(num_samples - int(attack_time * SAMPLE_RATE) \
      - int(release_time * SAMPLE_RATE))
  rel_env = np.linspace(1, 0, int(release_time * SAMPLE_RATE), False)
  env = np.append(att_env, ones)
  env = np.append(env, rel_env)
  return env

##### Note #####

class Note(object):

  altname = None

  def __init__(self, name, octave, freq, seconds):
    self.name = name
    self.octave = octave
    self.freq = freq
    self.seconds = seconds

  def calcSine(self, freq, seconds):
    x = np.linspace(0, seconds, seconds * SAMPLE_RATE, False)
    y = np.sin(x * freq * 2 * np.pi)
    return y

  def calcAudio(self, freq, seconds):
    num_samples = seconds * SAMPLE_RATE
    y = self.calcSine(freq, seconds)
    audio = envelope(seconds) * y * (2**15 - 1) /np.max(np.abs(y)) 
    audio = y * (2**15 - 1) /np.max(np.abs(y)) 
    audio = audio.astype(np.int16)
    return audio

  def calcNotes(self, notes):
    sines = np.zeros(0)
    for note in notes:
      sine = note.calcSine()
      np.append(sines, sine)
    return sines

  def playNote(self, audio):
    play = sa.play_buffer(audio, 1, 2, SAMPLE_RATE)
    play.wait_done()

def main():

  aNote = Note(allNotes[48][0], allNotes[48][1], allNotes[48][2], 1)
  audio = aNote.calcAudio(aNote.freq, aNote.seconds)
  aNote.playNote(audio)

if __name__ == "__main__":
  main()

