from typing import List
from musicCore.chord import Chord
from musicCore.musicalEvent import ChordEvent, MusicalEvent, NoteEvent
from musicCore.note import Duration, Note

class Track:
    def __init__(self, name: str, instrument: int = 0):
        self.name = name
        self.instrument = instrument  # MIDI program/instrument number
        self.events: List[MusicalEvent] = []
    
    def add_note(self, note: Note, start_time: int, duration: Duration):
        """Add a note to the track"""
        self.events.append(NoteEvent(note, start_time, duration))
        return self
    
    def add_chord(self, chord: Chord, start_time: int, duration: Duration):
        """Add a chord to the track"""
        self.events.append(ChordEvent(chord, start_time, duration))
        return self
