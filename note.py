# Herein lies the code for the envelope (used to eliminate clicks upon note changes),
# as well as the Note class and its functions.

import numpy as np
import simpleaudio as sa
import random
import math

##### GLOBALS #####
SAMPLE_RATE = 48000

##### ENVELOPE #####
def envelope(seconds, attack_time=0.001, release_time=0.005):
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
    def __init__(self, name, freq):
        self.name = name
        self.freq = freq

    def calc_sine(self, seconds):
        x = np.linspace(0, seconds, int(seconds * SAMPLE_RATE), False)
        y = np.sin(x * self.freq * 2 * np.pi)
        return y

    def calc_audio(self, seconds):
        num_samples = seconds * SAMPLE_RATE
        y = self.calc_sine(seconds)
        audio = envelope(seconds) * y * (2**15 - 1) /np.max(np.abs(y)) 
        audio = audio.astype(np.int16)
        return audio

def main():
    print("")

if __name__ == "__main__":
    main()

