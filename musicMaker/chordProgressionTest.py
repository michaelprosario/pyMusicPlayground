import mido
from typing import List, Dict, Optional

from composition import Composition
from musicCore.chord import Chord
from musicCore.chordType import ChordType
from musicCore.note import Duration, Note
from musicCore.track import Track
from musicCore.chordProgressionMaker import ChordProgressionMaker




chordProgression = ChordProgressionMaker().make_chord_progression("C - Am - F - G", 4)
print(chordProgression)
