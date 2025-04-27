from typing import List, Dict
from .chord import Chord
from .chordType import ChordType
from .note import Note

class ChordProgressionMaker:
    """
    A class to create chord progressions from string representations
    """
    
    # Map chord suffixes to chord types
    CHORD_TYPE_MAP = {
        "": ChordType.MAJOR,
        "m": ChordType.MINOR,
        "dim": ChordType.DIMINISHED,
        "aug": ChordType.AUGMENTED,
        "7": ChordType.DOMINANT_SEVENTH,
        "maj7": ChordType.MAJOR_SEVENTH
    }
        
    def make_chord_progression(cls, progression_str: str, octave: int = 4) -> List[Chord]:
        """
        Create a chord progression from a string representation
        
        Args:
            progression_str: String representation of chord progression (e.g. "C - Am - F - G")
            octave: Default octave for chord root notes
            
        Returns:
            List of Chord objects
        """
        # Split the progression string and remove any whitespace
        chord_symbols = [symbol.strip() for symbol in progression_str.split('-')]
        
        chords = []
        for symbol in chord_symbols:
            if not symbol:  # Skip empty strings
                continue
                
            # Parse the chord symbol
            root_note, chord_type = cls._parse_chord_symbol(symbol, octave)
            chord = Chord(root_note, chord_type)
            chords.append(chord)
            
        return chords
    
    @classmethod
    def _parse_chord_symbol(cls, symbol: str, octave: int) -> tuple:
        """
        Parse a chord symbol into root note and chord type
        
        Args:
            symbol: A chord symbol like "C", "Am", "Fmaj7", etc.
            octave: Default octave for the root note
            
        Returns:
            tuple: (root_note, chord_type)
        """
        # Extract the root note (first character, or first two if second is # or b)
        if len(symbol) > 1 and symbol[1] in ['#', 'b']:
            root_name = symbol[:2]
            suffix = symbol[2:]
        else:
            root_name = symbol[0]
            suffix = symbol[1:]
        
        # Create the root note with the specified octave
        root_note = Note.from_note_name(f"{root_name}{octave}")
        
        # Determine the chord type based on the suffix
        chord_type = cls.CHORD_TYPE_MAP.get(suffix, ChordType.MAJOR)
        
        return root_note, chord_type
