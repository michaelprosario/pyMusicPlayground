from chorder import Chord, Dechorder

from miditoolkit import MidiFile
from miditoolkit.midi.utils import example_midi_file

path_midi = "minuet_in_g.mid"
midi_obj = MidiFile(path_midi)

chords = Dechorder.dechord(midi_obj, scale=None, consider_bass=False)

i = 0
chordTypes = {
    "m": "m",
    "M": "",
    "m7": "m",
    "7": "",
    "M7": "Maj7",
    "o": "open",
    "sus2": "sus",
    "+": "+",
}
for chord in chords:
    if i % 4 == 0 and chord.root_pc is not None:
        noteName = chord.scale[chord.root_pc]
        quality = chord.quality
        qualityName = chordTypes[quality]
        print(f"{noteName}{qualityName}")
    i = i + 1



