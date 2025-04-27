
from musicCore.musicalEvent import ChordEvent, NoteEvent
from musicCore.chordType import ChordType
from musicCore.note import Duration, Note
from musicCore.track import Track
from typing import List
import mido

class Composition:
    def __init__(self, name: str, tempo: int = 120):
        self.name = name
        self.tempo = tempo  # BPM
        self.tracks: List[Track] = []
        
    def add_track(self, track: Track):
        """Add a track to the composition"""
        self.tracks.append(track)
        return self
    
    def to_midi(self) -> mido.MidiFile:
        """Convert the composition to a MIDI file"""
        mid = mido.MidiFile(type=1)  # Type 1 allows multiple tracks
        ticks_per_beat = 480  # Standard resolution
        mid.ticks_per_beat = ticks_per_beat
        
        # Create a tempo track
        tempo_track = mido.MidiTrack()
        mid.tracks.append(tempo_track)
        
        # Calculate tempo in microseconds per beat
        tempo_us = mido.bpm2tempo(self.tempo)
        tempo_track.append(mido.MetaMessage('set_tempo', tempo=tempo_us, time=0))
        
        # Add each musical track
        for track in self.tracks:
            midi_track = mido.MidiTrack()
            mid.tracks.append(midi_track)
            
            # Set track name
            midi_track.append(mido.MetaMessage('track_name', name=track.name, time=0))
            
            # Set instrument
            midi_track.append(mido.Message('program_change', program=track.instrument, time=0))
            
            # Prepare events (note_on and note_off)
            events = []
            ticks_per_16th = ticks_per_beat // 4  # 16th note duration in ticks
            
            # Process all musical events and convert to MIDI events
            for event in track.events:
                if isinstance(event, NoteEvent):
                    # Calculate tick positions
                    start_tick = event.start_time * ticks_per_16th
                    end_tick = start_tick + (event.duration.value * ticks_per_16th)
                    
                    # Add note_on and note_off events
                    events.append((start_tick, 'note_on', event.note.pitch, event.note.velocity))
                    events.append((end_tick, 'note_off', event.note.pitch, 0))
                    
                elif isinstance(event, ChordEvent):
                    # Calculate tick positions
                    start_tick = event.start_time * ticks_per_16th
                    end_tick = start_tick + (event.duration.value * ticks_per_16th)
                    
                    # Add note_on and note_off events for each note in the chord
                    for note in event.chord.notes:
                        events.append((start_tick, 'note_on', note.pitch, note.velocity))
                        events.append((end_tick, 'note_off', note.pitch, 0))
            
            # Sort events by time
            events.sort()
            
            # Convert to mido messages with relative timing
            last_time = 0
            for tick, msg_type, pitch, velocity in events:
                delta_time = tick - last_time
                last_time = tick
                
                midi_track.append(
                    mido.Message(
                        msg_type, 
                        note=pitch,
                        velocity=velocity,
                        time=delta_time
                    )
                )
            
            # End of track
            midi_track.append(mido.MetaMessage('end_of_track', time=0))
            
        return mid
    
    def save(self, filename: str):
        """Save the composition as a MIDI file"""
        midi_file = self.to_midi()
        midi_file.save(filename)
