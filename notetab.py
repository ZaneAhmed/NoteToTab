import sys
argv = sys.argv
argc = len (sys.argv)
FRETBOARD_LENGTH = 24
note = 0
octave = 0

"""
Calling with arguments:
python3 main.py C#3
python3 main.py C# 3

Without arguments:
python3 main.py
"""

def midiToNote (midinote) :
    note = notes [midinote % 12]
    octave = int ((midinote / 12) - 1)
    return (note, octave)

if argc == 1:
    note = input ("Input note + octave\n\t> ").upper()
elif argc == 2:
    note = sys.argv[1]
elif argc == 3:
    note = sys.argv[1]
    octave = sys.argv[2]

note = note.replace (' ', '')
if (not octave):octave = ''.join ( [octave for octave in note if octave.isdigit()] ) # Extract digits from string
note = ''.join ( [n for n in note if not n.isdigit()] ) # Remove digits from string


notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
fretboard = {
    "High_E": 64,
    "B": 59,
    "G": 55,
    "D": 50,
    "A": 45, 
    "Low_E": 40, 
}

# Creating the fretboard
for string in fretboard:
    value = fretboard[string]
    fretboard[string] = list (range(value, value + FRETBOARD_LENGTH))
    same = []
    for fret in range(len(fretboard[string])):
        midinote = fretboard[string][fret]
        fretboard[string][fret] = midiToNote (midinote)
        if note == fretboard[string][fret][0] and int(octave) == fretboard[string][fret][1]:
            same.append (fret)
    print ("String", string, ": ", same)

input ("\nPress enter to exit...")