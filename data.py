import pandas as pd

df = pd.read_csv('freq.csv', delimiter=',')
allNotes = [list(row) for row in df.values]

df = pd.read_csv('frequencies.csv', delimiter=',')
noteDict = [list(row) for row in df.values]
nd = dict(noteDict)

df = pd.read_csv('freq_to_note.csv', delimiter=',')
freq2note = [list(row) for row in df.values]
freq_to_note = dict(freq2note)

# Should fix to import indices as int:
df = pd.read_csv('freq_to_index.csv', delimiter=',')
freq2index = [list(row) for row in df.values]
freq_to_index = dict(freq2index)

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
  'minor' : [0,3,7]
}

