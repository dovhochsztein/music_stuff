from util.music_util import play_music, write_mid64_to_midi
from util.notes_util import sharp_note_dict, reduce_note, full_note_name
from mido import MidiFile, MidiTrack, open_output, tick2second
import matplotlib.ticker as plticker
from mido.messages.messages import Message
from mido.midifiles.meta import MetaMessage
from music_data.music_data import FishPolka_mid64
from settings import SETTINGS
import numpy as np
import math
import matplotlib.pyplot as plt
from pylab import *


# midi_file = 'temp.midi'
#
# write_mid64_to_midi(FishPolka_mid64, midi_file)
#
# play_music(midi_file)

input_midi = MidiFile('temp.midi')

message_list = list(input_midi)

play_music(input_midi)

# input_midi.save('temp.midi')

# message_list = input_midi.tracks[4].messages

message_1 = input_midi.tracks[5][8]

play = input_midi.play()


drums_from_midi = [ii for ii in message_list if isinstance(ii, Message) and ii.channel == 9]
drums_from_track = [ii for ii in input_midi.tracks[5] if isinstance(ii, Message)]

accordian_high_from_midi = [ii for ii in message_list if isinstance(ii, Message) and ii.channel == 1] #time in seconds
accordian_high_from_track = [ii for ii in input_midi.tracks[1] if isinstance(ii, Message)] # time in ticks (32nd notes, since the ticks per beat is 144)

accordian_high_from_midi = []


port = open_output()

for ii in input_midi:
    print(ii)





def convert_track_to_time_series(track, quantization=8, ticks_per_beat=144, length=100):
    total_length = sum([ii.time for ii in track if isinstance(ii, Message)])
    length = int(math.ceil(total_length / 144 * quantization))
    name = track.name
    notes_on = set()
    time_series = np.full(length, None)
    time_point_ticks = 0
    for message in track:
        if isinstance(message, Message) and message.type == 'note_on':

            if message.time > 0:
                old_time_point_quantization = int(round(time_point_ticks / ticks_per_beat * quantization))
                time_point_ticks += message.time
                new_time_point_quantization = int(round(time_point_ticks / ticks_per_beat * quantization))
                time_series[old_time_point_quantization: new_time_point_quantization+message.time].fill(list(notes_on))


            if message.velocity == 0:
                if message.note in notes_on:
                    notes_on.remove(message.note)
            else:
                if message.note not in notes_on:
                    notes_on.add(message.note)


        elif isinstance(message, MetaMessage):
            pass
    return time_series


def visualize_time_series(time_series):
    x = list()
    y = list()
    for ii, item in enumerate(time_series):
        for note in item:
            x.append(ii)
            y.append((note))
    axes = figure().add_subplot(111)
    axes.scatter(x,y)

    loc = plticker.MultipleLocator(base=1.0)  # this locator puts ticks at regular intervals
    axes.yaxis.set_major_locator(loc)
    a = axes.get_yticks().tolist()
    b = [full_note_name(ii, sharp_note_dict) for ii in a]
    axes.set_yticklabels(b)



visualize_time_series(convert_track_to_time_series(track = input_midi.tracks[4]))