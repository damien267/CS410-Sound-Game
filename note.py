import numpy as np
import simpleaudio as sa
import random
import pandas as pd
import math

##### GLOBALS #####

SAMPLE_RATE = 8000

##### ENVELOPE #####

def envelope(seconds, attack_time=.001, release_time=.001):
  num_samples = int(seconds * SAMPLE_RATE)
  attack = int(attack_time * SAMPLE_RATE)
  release =  int(release_time * SAMPLE_RATE)
  att_env = np.linspace(0, 1, attack, False)
  ones = np.ones(num_samples - attack - release)
  rel_env = np.linspace(1, 0, release, False)
  env = np.append(att_env, ones)
  env = np.append(env, rel_env)
  return env

##### Note #####
class Note(object):
  altname = None
  def __init__(self, name, freq):

    self.name = name
    self.freq = freq

  def calcSine(self, seconds):
    x = np.linspace(0, seconds, int(seconds * SAMPLE_RATE), False)
    y = np.sin(x * self.freq * 2 * np.pi)
    return y

  def calcAudio(self, seconds):
    num_samples = seconds * SAMPLE_RATE
    y = self.calcSine(seconds)
    audio = envelope(seconds) * y * (2**15 - 1) /np.max(np.abs(y)) 
    audio = y * (2**15 - 1) /np.max(np.abs(y)) 
    audio = audio.astype(np.int16)
    return audio

  # Don't think this is used yet. Might need revamping:
  def calcNotes(self, seconds):
    sines = np.zeros(0)
    for note in notes:
       audio = note.calcAudio(seconds)
       np.append(sines, sine)
    return sines

def main():
  print("dogs")

if __name__ == "__main__":
  main()

