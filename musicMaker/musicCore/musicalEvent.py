from musicCore.chord import Chord
from musicCore.note import Duration, Note

class MusicalEvent:
    def __init__(self, start_time: int, duration: Duration):
        self.start_time = start_time  # In sixteenth notes from the beginning
        self.duration = duration
    
    @property
    def end_time(self) -> int:
        return self.start_time + self.duration.value

class NoteEvent(MusicalEvent):
    def __init__(self, note: Note, start_time: int, duration: Duration):
        super().__init__(start_time, duration)
        self.note = note

class ChordEvent(MusicalEvent):
    def __init__(self, chord: Chord, start_time: int, duration: Duration):
        super().__init__(start_time, duration)
        self.chord = chord
