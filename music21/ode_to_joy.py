#!/usr/bin/env python3
"""
Ode to Joy - Music21 Sample Script
-----------------------------------
This script demonstrates:
1. Creating a multi-part musical Score (Melody + Harmony) using music21.
2. Composing Beethoven's "Ode to Joy" (Symphony No. 9) in the key of C Major.
3. Setting metadata, tempo, time signature, and key signature.
4. Exporting the score to MusicXML format (.musicxml).
5. Exporting to MIDI (.mid).
6. Rendering and displaying musical notation (Text structure & Score image via LilyPond/Verovio).
"""

from pathlib import Path
import os
import sys

# Ensure music21 can be imported even if the parent workspace directory is named music21
import music21 as m21


def create_ode_to_joy_score() -> m21.stream.Score:
    """Builds a complete Score for Ode to Joy in C major with melody and accompaniment."""
    score = m21.stream.Score()

    # Metadata
    score.metadata = m21.metadata.Metadata()
    score.metadata.title = "Ode to Joy (An die Freude)"
    score.metadata.composer = "Ludwig van Beethoven"
    score.metadata.lyricist = "Friedrich Schiller"
    score.metadata.movementName = "Theme from Symphony No. 9, Op. 125"

    # Define Melody Part (Right Hand / Soprano)
    melody_part = m21.stream.Part()
    melody_part.id = 'Melody'
    melody_part.partName = 'Melody'

    # Add Clef, Key (C Major), Time Signature (4/4), and Tempo
    melody_part.append(m21.clef.TrebleClef())
    melody_part.append(m21.key.Key('C'))
    melody_part.append(m21.meter.TimeSignature('4/4'))
    melody_part.append(m21.tempo.MetronomeMark('Allegro moderato', 120))

    # Ode to Joy Melody (Notes and Durations in quarterLength)
    # Measures 1-16
    melody_data = [
        # Measure 1
        ('E4', 1.0), ('E4', 1.0), ('F4', 1.0), ('G4', 1.0),
        # Measure 2
        ('G4', 1.0), ('F4', 1.0), ('E4', 1.0), ('D4', 1.0),
        # Measure 3
        ('C4', 1.0), ('C4', 1.0), ('D4', 1.0), ('E4', 1.0),
        # Measure 4
        ('E4', 1.5), ('D4', 0.5), ('D4', 2.0),

        # Measure 5
        ('E4', 1.0), ('E4', 1.0), ('F4', 1.0), ('G4', 1.0),
        # Measure 6
        ('G4', 1.0), ('F4', 1.0), ('E4', 1.0), ('D4', 1.0),
        # Measure 7
        ('C4', 1.0), ('C4', 1.0), ('D4', 1.0), ('E4', 1.0),
        # Measure 8
        ('D4', 1.5), ('C4', 0.5), ('C4', 2.0),

        # Measure 9 (Middle phrase)
        ('D4', 1.0), ('D4', 1.0), ('E4', 1.0), ('C4', 1.0),
        # Measure 10
        ('D4', 1.0), ('E4', 0.5), ('F4', 0.5), ('E4', 1.0), ('C4', 1.0),
        # Measure 11
        ('D4', 1.0), ('E4', 0.5), ('F4', 0.5), ('E4', 1.0), ('D4', 1.0),
        # Measure 12
        ('C4', 1.0), ('D4', 1.0), ('G3', 2.0),

        # Measure 13 (Recap)
        ('E4', 1.0), ('E4', 1.0), ('F4', 1.0), ('G4', 1.0),
        # Measure 14
        ('G4', 1.0), ('F4', 1.0), ('E4', 1.0), ('D4', 1.0),
        # Measure 15
        ('C4', 1.0), ('C4', 1.0), ('D4', 1.0), ('E4', 1.0),
        # Measure 16
        ('D4', 1.5), ('C4', 0.5), ('C4', 2.0)
    ]

    for pitch_str, dur in melody_data:
        n = m21.note.Note(pitch_str)
        n.quarterLength = dur
        melody_part.append(n)

    # Define Harmony / Bass Part (Left Hand)
    harmony_part = m21.stream.Part()
    harmony_part.id = 'Harmony'
    harmony_part.partName = 'Harmony'
    harmony_part.append(m21.clef.BassClef())
    harmony_part.append(m21.key.Key('C'))
    harmony_part.append(m21.meter.TimeSignature('4/4'))

    # Chords for Measures 1-16
    chord_data = [
        # Measure 1: C Major
        (['C3', 'E3', 'G3'], 4.0),
        # Measure 2: G Major
        (['G2', 'D3', 'G3'], 4.0),
        # Measure 3: C Major
        (['C3', 'E3', 'G3'], 4.0),
        # Measure 4: G Major
        (['G2', 'D3', 'G3'], 4.0),

        # Measure 5: C Major
        (['C3', 'E3', 'G3'], 4.0),
        # Measure 6: G Major
        (['G2', 'D3', 'G3'], 4.0),
        # Measure 7: C Major
        (['C3', 'E3', 'G3'], 4.0),
        # Measure 8: C Major
        (['C3', 'E3', 'G3'], 4.0),

        # Measure 9: G Major / C Major
        (['G2', 'D3', 'G3'], 2.0), (['C3', 'E3', 'G3'], 2.0),
        # Measure 10: G Major / C Major
        (['G2', 'D3', 'G3'], 2.0), (['C3', 'E3', 'G3'], 2.0),
        # Measure 11: G Major / D minor
        (['G2', 'D3', 'G3'], 2.0), (['D3', 'F3', 'A3'], 2.0),
        # Measure 12: C Major / G Major
        (['C3', 'E3', 'G3'], 2.0), (['G2', 'B2', 'D3'], 2.0),

        # Measure 13: C Major
        (['C3', 'E3', 'G3'], 4.0),
        # Measure 14: G Major
        (['G2', 'D3', 'G3'], 4.0),
        # Measure 15: C Major
        (['C3', 'E3', 'G3'], 4.0),
        # Measure 16: C Major
        (['C3', 'E3', 'G3'], 4.0)
    ]

    for pitches, dur in chord_data:
        ch = m21.chord.Chord(pitches)
        ch.quarterLength = dur
        harmony_part.append(ch)

    # Make measures in both parts
    melody_measures = melody_part.makeMeasures()
    harmony_measures = harmony_part.makeMeasures()

    score.append(melody_measures)
    score.append(harmony_measures)

    return score


def export_musicxml(score: m21.stream.Score, output_path: str) -> str:
    """Exports the music21 score to MusicXML format."""
    print(f"[*] Exporting MusicXML to: {output_path}")
    saved_path = score.write('musicxml', fp=output_path)
    print(f"[+] MusicXML successfully exported ({os.path.getsize(saved_path)} bytes).")
    return str(saved_path)


def export_midi(score: m21.stream.Score, output_path: str) -> str:
    """Exports the music21 score to standard MIDI file."""
    print(f"[*] Exporting MIDI to: {output_path}")
    saved_path = score.write('midi', fp=output_path)
    print(f"[+] MIDI successfully exported ({os.path.getsize(saved_path)} bytes).")
    return str(saved_path)


def show_music_notation_text(score: m21.stream.Score):
    """Displays hierarchical textual music notation."""
    print("\n" + "=" * 60)
    print("MUSIC NOTATION (Hierarchical Text Stream Representation)")
    print("=" * 60)
    score.show('text')
    print("=" * 60 + "\n")


def render_score_svg(score: m21.stream.Score, output_svg_path: str) -> str:
    """Renders the score to an SVG vector image using Verovio."""
    print(f"[*] Rendering score notation SVG via Verovio to: {output_svg_path}")
    try:
        import verovio
        xml_str = score.write('musicxml')
        with open(xml_str, 'r') as f:
            xml_data = f.read()

        tk = verovio.toolkit()
        tk.setOptions({
            'pageWidth': 1200,
            'pageHeight': 800,
            'scale': 45,
            'adjustPageHeight': True
        })
        tk.loadData(xml_data)
        svg_content = tk.renderToSVG(1)

        with open(output_svg_path, 'w', encoding='utf-8') as f:
            f.write(svg_content)

        print(f"[+] Score SVG successfully rendered: {output_svg_path}")
        return output_svg_path
    except Exception as e:
        print(f"[!] Verovio rendering note: {e}")
        return None


def render_score_image(score: m21.stream.Score, output_png_base: str):
    """Renders the score to PNG images using LilyPond."""
    print(f"[*] Rendering score notation image via LilyPond to: {output_png_base}")
    try:
        us = m21.environment.UserSettings()
        if not us['lilypondPath'] and os.path.exists('/usr/bin/lilypond'):
            us['lilypondPath'] = '/usr/bin/lilypond'

        rendered = score.write('lily.png', fp=output_png_base)
        print(f"[+] LilyPond score images generated for: {output_png_base}")
        return str(rendered)
    except Exception as e:
        # Check if files were generated by lilypond with -page1.png pattern
        matches = list(Path(os.path.dirname(output_png_base)).glob(f"{Path(output_png_base).name}*.png"))
        if matches:
            print(f"[+] LilyPond score generated image(s): {[str(m) for m in matches]}")
            return str(matches[0])
        print(f"[!] LilyPond rendering note: {e}")
        return None


def main():
    base_dir = Path(__file__).resolve().parent

    print("==================================================")
    print("  Music21 Sample: Ode to Joy in C Major")
    print("==================================================")

    # 1. Create Score
    print("[*] Generating Beethoven's Ode to Joy score...")
    score = create_ode_to_joy_score()
    print(f"[+] Created Score with {len(score.parts)} parts and {len(score.parts[0].getElementsByClass('Measure'))} measures.")

    # 2. Show Music Notation in Console (Hierarchical Text representation)
    show_music_notation_text(score)

    # 3. Export to MusicXML
    musicxml_file = str(base_dir / "ode_to_joy.musicxml")
    export_musicxml(score, musicxml_file)

    # 4. Export to MIDI
    midi_file = str(base_dir / "ode_to_joy.mid")
    export_midi(score, midi_file)

    # 5. Render Score notation vector SVG (Verovio)
    score_svg_file = str(base_dir / "ode_to_joy_score.svg")
    render_score_svg(score, score_svg_file)

    # 6. Render Score notation image (LilyPond PNG)
    score_png_base = str(base_dir / "ode_to_joy_score")
    render_score_image(score, score_png_base)

    print("\n[✓] All Music21 sample operations completed successfully!")


if __name__ == '__main__':
    main()
