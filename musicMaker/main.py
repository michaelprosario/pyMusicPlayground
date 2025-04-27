from enum import Enum
import mido
from typing import List, Dict, Optional

from composition import Composition
from musicCore.chord import Chord
from musicCore.chordType import ChordType
from musicCore.note import Duration, Note
from musicCore.track import Track

composition = Composition("My First Composition", tempo=120)
piano_track = Track("Piano", instrument=0)  # 0 is piano in General MIDI

x = 0

chords = []

# add c major chord
c_major = Chord(Note.from_note_name("C4"), ChordType.MAJOR)
chords.append(c_major)

# a minor chord 
a_minor = Chord(Note.from_note_name("A4"), ChordType.MINOR)
chords.append(a_minor)

# f major chord
f_major = Chord(Note.from_note_name("F4"), ChordType.MAJOR)
chords.append(f_major)

# g major chord
g_major = Chord(Note.from_note_name("G4"), ChordType.MAJOR)
chords.append(g_major)

# Create a chord and add it to the track

for chord in chords:
    print("Chord should start at", x)
    piano_track.add_chord(chord, x, Duration.WHOLE)
    x += Duration.WHOLE.value


# Add the track to the composition
composition.add_track(piano_track)

# Save the composition as a MIDI file
composition.save("out2.mid")
