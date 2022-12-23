#import midi :) there no such library. There is py-midi which lets you communicate with MIDI devices (https://pypi.org/project/py-midi/)
import random

# Set the tempo
tempo = 120  # Beats per minute

# Define a scale of notes
scale = [60, 62, 64, 65, 67, 69, 71]  # Middle C, D, E, F, G, A, B

# Set the number of measures in the pattern
measures = 8

# Set the number of beats per measure
beats_per_measure = 4

# Set the number of ticks per beat (based on the tempo)
ticks_per_beat = 480

# Create a MIDI pattern object
pattern = midi.Pattern()

# Create a MIDI track object
track = midi.Track()

# Add the tempo to the track
tempo_event = midi.SetTempoEvent(tick=0, bpm=tempo)
track.append(tempo_event)

# Generate the notes for the pattern
for measure in range(measures):
    for beat in range(beats_per_measure):
        # Choose a random note from the scale
        note = random.choice(scale)

        # Choose a random duration for the note
        duration = random.uniform(0.25, 0.75)

        # Create MIDI events for the note
        on = midi.NoteOnEvent(tick=0, velocity=100, pitch=note)
        off = midi.NoteOffEvent(tick=int(duration * ticks_per_beat), pitch=note)
        
        # Add the events to the track
        track.append(on)
        track.append(off)

# Add the track to the pattern
pattern.append(track)

# Save the pattern to a MIDI file
midi.write_midifile("techno.mid", pattern)
