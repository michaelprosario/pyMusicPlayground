from enum import Enum

class Duration(Enum):
    WHOLE = 64      # 64 sixteenth notes
    HALF = 32       # 32 sixteenth notes
    QUARTER = 16    # 16 sixteenth notes
    EIGHTH = 8      # 8 sixteenth notes
    SIXTEENTH = 4   # 4 sixteenth notes (smallest unit in our model)

class Note:
    def __init__(self, pitch: int, velocity: int = 64):
        self.pitch = pitch  # MIDI note number (0-127)
        self.velocity = velocity  # MIDI velocity (0-127)
    
    @classmethod
    def from_note_name(cls, note_name: str, velocity: int = 64):
        """Create a Note from a note name (e.g. 'C4', 'F#5')"""
        # Implementation for converting note names to MIDI numbers
        notes = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 
                 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
        
        # Parse note name and octave
        if len(note_name) == 2:
            note = note_name[0].upper()
            octave = int(note_name[1])
        else:
            note = note_name[0:2].upper()
            octave = int(note_name[2])
            
        # Calculate MIDI number
        midi_number = notes[note] + (octave + 1) * 12
        return cls(midi_number, velocity)
