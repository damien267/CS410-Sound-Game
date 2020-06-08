# This file contains the data used for the program game.py 

import pandas as pd

df = pd.read_csv('freq.csv', delimiter=',')
all_notes = [list(row) for row in df.values]

intervals = \
    ['Unison','minor 2nd','Major 2nd','minor 3rd','Major 3rd','Perfect 4th','Augmented 4th / diminished 5th',
        'Perfect 5th','minor 6th','Major 6th','minor 7th','Major 7th','Octave']  

scales = {
    'major' : [0,2,4,5,7,9,11,12],
    'dorian' : [0,2,3,5,7,9,10,12],
    'phrygian' : [0,1,3,5,7,8,10,12],
    'lydian' : [0,2,4,6,7,9,11,12],
    'mixolydian' : [0,2,4,5,7,9,10,12],
    'minor' : [0,2,3,5,7,8,10,12],
    'locrian' : [0,1,3,5,6,8,10,12],
    'melodic minor' : [0,2,3,5,7,9,11,12,10,8,7,5,3,2,0],
    'harmonic minor' : [0,2,3,5,7,8,11,12,10,8,7,5,3,2,0],
    'pentatonic major' : [0,2,4,7,9,12],
    'pentatonic minor' : [0,3,5,7,10,12],
    'half_diminshed' : [0,2,3,5,6,8,9,11,12],
    'chromatic' : [0,1,2,3,4,5,6,7,8,9,10,11,12],
    'whole_tone' : [0,2,4,6,8,10,12],
}

chords = {
    'Major' : [0,4,7],
    'minor' : [0,3,7],
    'diminished' : [0,3,6],
    'augmented' : [0,4,8],
    'Dominant 7th' : [0,4,7,10],
    'Dominant 7th (b5)' : [0,4,6,10],
    'Major 7th' : [0,4,7,11],
    'minor (Major 7)' : [0,3,7,11],
    'diminished 7th' : [0,3,6,9],
    'half diminished' : [0,3,6,10],
    'augmented (7th)' : [0,4,8,10],
    'Major 6th' : [0,4,7,9],
    'minor 6th' : [0,3,7,9],
    'add 9' : [0,4,7,14],
    '6-9' : [0,4,7,9,14],
    '9th' : [0,4,7,10,14], 
    'minor 9th' : [0,3,7,10,14], 
    'flat 9th' : [0,4,7,10,13], 
    'sharp 9th' : [0,4,7,10,15], 
    '9th (Major 7)' : [0,4,7,11,14], 
    'minor 11th' : [0,3,7,10,14,17], 
    'sharp 11th' : [0,4,7,10,14,18], 
    '13th' : [0,4,7,10,14,21], 
    'minor 13th' : [0,3,7,10,14,16,21], 
    'flat 13th' : [0,4,7,10,13,20], 
}

sound_types = [intervals, chords, scales]

sound_type_name = ['interval', 'chord', 'scale']

correct_indicator = ["effects/base_12.wav","effects/base_13.wav",
    "effects/base_14.wav","effects/base_15.wav","effects/base_16.wav",
    "effects/base_17.wav","effects/base_18.wav","effects/base_19.wav",
    "effects/base_20.wav","effects/base_21.wav","effects/base_22.wav",
    "effects/base_23.wav","effects/base_24.wav"]

