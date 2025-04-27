from typing import List
from musicCore.note import Note
from musicCore.chordType import ChordType

class Chord:
    def __init__(self, root_note: Note, chord_type: ChordType):
        self.root_note = root_note
        self.chord_type = chord_type
        self.notes = self._generate_notes()
    
    def _generate_notes(self) -> List[Note]:
        """Generate the notes for this chord based on the root note and chord type"""
        notes = [self.root_note]
        root_pitch = self.root_note.pitch
        velocity = self.root_note.velocity
        
        if self.chord_type == ChordType.MAJOR:
            notes.append(Note(root_pitch + 4, velocity))  # Major third
            notes.append(Note(root_pitch + 7, velocity))  # Perfect fifth
        elif self.chord_type == ChordType.MINOR:
            notes.append(Note(root_pitch + 3, velocity))  # Minor third
            notes.append(Note(root_pitch + 7, velocity))  # Perfect fifth
        # Add other chord types here
        
        return notes
