import pandas as pd

df = pd.read_csv('freq.csv', delimiter=',')
allNotes = [list(row) for row in df.values]

intrvl = \
    ['U','m2','M2','m3','M3','P4','A4/d5','P5','m6','M6','m7','M7','O']  

patterns = {
  'major' : [0,2,4,5,7,9,11,12], \
  'dorian' : [0,2,3,5,7,9,10,12], \
  'phrygian' : [0,1,3,5,7,8,10,12], \
  'lydian' : [0,2,4,6,7,9,11,12], \
  'mixolydian' : [0,2,4,5,7,9,10,12], \
  'minor' : [0,2,3,5,7,8,10,12], \
  'locrian' : [0,1,3,5,6,8,10,12], \
  'melodic_minor' : [0,2,3,5,7,9,11,12,10,8,7,5,3,2,0], \
  'harmonic_minor' : [0,2,3,5,7,8,11,12,10,8,7,5,3,2,0], \
  'pentatonic_major' : [0,2,4,7,9,12], \
  'pentatonic_minor' : [0,2,3,7,9,12], \
  'half_diminshed' : [0,2,3,5,6,8,9,11,12], \
  'chromatic' : [0,1,2,3,4,5,6,7,8,9,10,11,12], \
  'whole_tone' : [0,2,4,6,8,10,12],
}

chords = {
  'major' : [0,4,7],
  'minor' : [0,3,7],
  'diminished' : [0,3,6],
  'augmented' : [0,4,8],
  'dominant 7th' : [0,4,7,10],
  'dominant 7th (b5)' : [0,4,7,10],
  'major 7th' : [0,4,7,10],
  'major 7th (minor)' : [0,3,7,11],
  'diminished 7th' : [0,4,7,10],
  'half diminished' : [0,4,7,10],
  'augmented 7th' : [0,4,8,10],
  '6th (major)' : [0,4,7,9],
  '6th (minor)' : [0,4,7,9],
  'add 9' : [0,4,7,14],
  '6-9' : [0,4,7,9,14],
  '9th' : [0,4,7,10,14], 
  'minor 9th' : [0,3,7,10,14], 
  'flat 9th' : [0,4,7,10,13], 
  'sharp 9th' : [0,4,7,10,15], 
  '9th (major 7th)' : [0,4,7,11,15], 
  'minor 11th' : [0,3,7,10,14,16,17], 
  'sharp 11th' : [0,4,7,10,14,16,18], 
  '13th' : [0,4,7,10,14,16,20], 
  'minor 13th' : [0,3,7,10,14,16,20], 
  'flat 13th' : [0,4,7,10,14,16,19], 
}

