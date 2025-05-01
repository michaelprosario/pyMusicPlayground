import mido
from typing import List, Dict, Optional

from composition import Composition
from musicCore.chord import Chord
from musicCore.chordType import ChordType
from musicCore.note import Duration, Note
from musicCore.track import Track
from musicCore.chordProgressionParser import ChordProgressionParser


chordProgressionParser = ChordProgressionParser()
chordChanges = chordProgressionParser.parseProgression("Am:4 | G:4 | F:4 | E:4 | Am:4 | G:4 | F:4 | E:4")

for chordChange in chordChanges:
    print(chordChange)
    
composition = Composition("My First Composition", tempo=120)
piano_track = Track("Piano", instrument=0)  # 0 is piano in General MIDI

x = 0

# Create a chord and add it to the track
def getDuration(d):
    duration = Duration.WHOLE
    if d == 1:
        duration = Duration.QUARTER
    elif d == 2:
        duration = Duration.HALF
    elif d == 4:
        duration = Duration.WHOLE
    return duration

for chordChange in chordChanges:
    print("Chord should start at", x)
    d = chordChange.duration
    duration = getDuration(d)

    piano_track.add_chord(chordChange.chord, x, duration)
    x += duration.value

# Add the track to the composition
composition.add_track(piano_track)

# Save the composition as a MIDI file
composition.save("foo.mid")
