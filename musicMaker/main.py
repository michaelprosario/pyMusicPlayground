from enum import Enum
import mido
from typing import List, Dict, Optional

from composition import Composition
from chord import Chord
from chordType import ChordType
from note import Duration, Note
from track import Track

composition = Composition("My First Composition", tempo=120)
piano_track = Track("Piano", instrument=0)  # 0 is piano in General MIDI

quarterNoteLength = Duration.QUARTER.value
x = 0

piano_track.add_note(Note.from_note_name("C4"), x, Duration.QUARTER)
x += quarterNoteLength

piano_track.add_note(Note.from_note_name("E4"), x, Duration.QUARTER)
x += quarterNoteLength

piano_track.add_note(Note.from_note_name("G4"), x, Duration.QUARTER)
x += quarterNoteLength

piano_track.add_note(Note.from_note_name("C3"), x, Duration.QUARTER)
x += quarterNoteLength

# Create a chord and add it to the track
c_major = Chord(Note.from_note_name("C4"), ChordType.MAJOR)
piano_track.add_chord(c_major, x, Duration.HALF)

# Add the track to the composition
composition.add_track(piano_track)

# Save the composition as a MIDI file
composition.save("out.mid")
