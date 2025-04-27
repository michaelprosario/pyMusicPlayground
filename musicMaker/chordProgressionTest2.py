import mido
from typing import List, Dict, Optional

from composition import Composition
from musicCore.chord import Chord
from musicCore.chordType import ChordType
from musicCore.note import Duration, Note
from musicCore.track import Track
from musicCore.chordProgressionMaker import ChordProgressionMaker


chordsMaker = ChordProgressionMaker()
chords = chordsMaker.make_chord_progression("Am - G - F - E", 4)


composition = Composition("My First Composition", tempo=120)
piano_track = Track("Piano", instrument=0)  # 0 is piano in General MIDI

x = 0

# Create a chord and add it to the track
for chord in chords:
    print("Chord should start at", x)
    piano_track.add_chord(chord, x, Duration.WHOLE)
    x += Duration.WHOLE.value

# Add the track to the composition
composition.add_track(piano_track)

# Save the composition as a MIDI file
composition.save("out3.mid")
