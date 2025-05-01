# make class for chord progression parser

from musicCore.chord import Chord
from musicCore.note import Note
from musicCore.chordType import ChordType

class ChordChange:
    def __init__(self, chord: Chord, duration: float):
        self.chord = chord
        self.duration = duration

    def __str__(self):
        return f"ChordChange(chord={self.chord}, duration={self.duration})"

    def __repr__(self):
        return self.__str__()

class ChordProgressionParser:
    def parseProgression(self, progression: str) -> list:
        return []
    
    def parseChordChange(self, chordChange: str) -> ChordChange:
        parts = chordChange.split(':')
        if len(parts) == 2:
            chord = self.parseChord(parts[0])
            duration = float(parts[1])
        else:
            chord = self.parseChord(parts[0])
            duration = 1.0

        return ChordChange(chord, duration) 
    
    def parseChord(self, chord: str) -> Chord:

        chord1 = chord.strip()

        # check if the chord ends in 'M' or 'm'
        if chord1.endswith('m'):
            chord1 = chord1[:-1]
            chordType = ChordType.MINOR
        else:
            chordType = ChordType.MAJOR
                
        chord1 = chord1 + '2'

        # create note from chord
        rootNote = Note.from_note_name(chord1)

        # create chord from note
        response = Chord(rootNote, chordType) 
        return response
