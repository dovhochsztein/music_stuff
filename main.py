from util.music_util import play_music
from mido import MidiFile, MidiTrack

midi_file = 'temp.midi'
play_music(midi_file)

input_midi = MidiFile('temp.midi')
input_midi.play()
