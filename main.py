from util.music_util import play_music
from mido import MidiFile, MidiTrack, open_output

midi_file = 'temp.midi'
play_music(midi_file)

input_midi = MidiFile('temp.midi')
play = input_midi.play()

port = open_output()

for ii in play:
    pass
