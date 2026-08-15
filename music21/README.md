# Music21 Exploration & Samples

This directory provides working examples for **music21**, including Python scripts and an interactive **Jupyter Notebook**.

---

## 🎼 Included Files

| File | Description |
|---|---|
| [**`music21_tutorial.ipynb`**](file:///workspaces/pyMusicPlayground/music21/music21_tutorial.ipynb) | Interactive Jupyter Notebook demonstrating notes, chords, streams, music notation, MusicXML export/import, and key/pitch analysis. |
| [**`ode_to_joy.py`**](file:///workspaces/pyMusicPlayground/music21/ode_to_joy.py) | Standalone Python script composing Beethoven's *Ode to Joy* in **C Major** (Melody + Harmony), rendering score notation (SVG and PNG), and exporting to MusicXML & MIDI. |
| [**`ode_to_joy.musicxml`**](file:///workspaces/pyMusicPlayground/music21/ode_to_joy.musicxml) | Exported MusicXML score (importable into MuseScore, Sibelius, Finale, Dorico). |
| [**`ode_to_joy.mid`**](file:///workspaces/pyMusicPlayground/music21/ode_to_joy.mid) | Standard MIDI audio file export of the arrangement. |
| [**`ode_to_joy_score.svg`**](file:///workspaces/pyMusicPlayground/music21/ode_to_joy_score.svg) | High-resolution scalable vector score notation rendered via Verovio. |
| [**`requirements.txt`**](file:///workspaces/pyMusicPlayground/music21/requirements.txt) | Python dependencies (`music21`, `matplotlib`, `verovio`). |

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

*(Optional for engraved PNG images: LilyPond via `sudo apt-get install -y lilypond`)*

---

### 2. Run the Python Script
```bash
cd /workspaces/pyMusicPlayground/music21
python3 ode_to_joy.py
```

This will:
1. Build Beethoven's **Ode to Joy** in C Major (Treble melody + Bass chord harmony).
2. Print hierarchical text notation tree to the console (`score.show('text')`).
3. Export **`ode_to_joy.musicxml`**.
4. Export **`ode_to_joy.mid`**.
5. Render **`ode_to_joy_score.svg`** (vector notation via Verovio) and PNG score images (via LilyPond).

---

### 3. Open the Jupyter Notebook
Open [`music21_tutorial.ipynb`](file:///workspaces/pyMusicPlayground/music21/music21_tutorial.ipynb) in VS Code or JupyterLab:
- Step-by-step music composition.
- Inline sheet music notation rendering (SVG & PNG).
- MusicXML round-trip inspection.
- Algorithmic Key Analysis & Pitch Frequency Histogram plotting.
