import unittest

from musicCore.chordProgressionParser import ChordProgressionParser
from musicCore.chordType import ChordType

class TestCalculations(unittest.TestCase):

    def test_parseChord__onCMajor(self):
        # arrange
        parser = ChordProgressionParser()

        # act
        chord = parser.parseChord('C')

        # assert
        self.assertEqual(chord.root_note.pitch, 36)
        self.assertEqual(chord.chord_type, ChordType.MAJOR)

    def test_parseChord__onCMinor(self):
        # arrange
        parser = ChordProgressionParser()

        # act
        chord = parser.parseChord('Cm')

        # assert
        self.assertEqual(chord.root_note.pitch, 36)
        self.assertEqual(chord.chord_type, ChordType.MINOR)

    def test_parseChord__onCSharp(self):
        # arrange
        parser = ChordProgressionParser()

        # act
        chord = parser.parseChord('C#')

        # assert
        self.assertEqual(chord.root_note.pitch, 37)
        self.assertEqual(chord.chord_type, ChordType.MAJOR)

    def test_parseChord__onCSharpMinor(self):
        # arrange
        parser = ChordProgressionParser()

        # act
        chord = parser.parseChord('C#m')

        # assert
        self.assertEqual(chord.root_note.pitch, 37)
        self.assertEqual(chord.chord_type, ChordType.MINOR)

    def test_parseChord(self):
        # arrange
        parser = ChordProgressionParser()

        # act
        chord = parser.parseChord('C')
        chord = parser.parseChord('Dm')
        chord = parser.parseChord('Em')
        chord = parser.parseChord('F')
        chord = parser.parseChord('G')
        chord = parser.parseChord('Am')

    def test_parseChordAndLength__onCSharpMinor4(self):
        # arrange
        parser = ChordProgressionParser()

        # act
        chordChange = parser.parseChordChange('C#m:4')

        # assert
        self.assertEqual(chordChange.chord.root_note.pitch, 37)
        self.assertEqual(chordChange.chord.chord_type, ChordType.MINOR)
        self.assertEqual(chordChange.duration, 4.0)

    def test_parseChordAndLength__onCSharpMinor2(self):
        # arrange
        parser = ChordProgressionParser()

        # act
        chordChange = parser.parseChordChange('C#m:2')

        # assert
        self.assertEqual(chordChange.chord.root_note.pitch, 37)
        self.assertEqual(chordChange.chord.chord_type, ChordType.MINOR)
        self.assertEqual(chordChange.duration, 2.0)



if __name__ == '__main__':
    unittest.main()
    #parser = ChordProgressionParser()

    # act
    #chordChange = parser.parseChordChange('C#m:4')
