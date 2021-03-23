import math
import numpy as np


def reduce_note(note):
    note = int(round(note))
    octave = note // 12 - 1
    note = note % 12
    return note, octave


def note2cyclic(note):
    note_reduced, octave = reduce_note(note)
    x, y = math.cos(2 * math.pi * note_reduced / 12),\
           math.sin(2 * math.pi * note_reduced / 12)
    return x, y


def cyclic2note(x, y):
    angle = np.arctan2(y, x)
    note = int(round(angle / (2 * math.pi) * 12))
    return note


def circle_of_fifths_transform(note):
    return 7 * note % 12


sharp_note_dict = {0: 'C',
                   1: 'C#',
                   2: 'D',
                   3: 'D#',
                   4: 'E',
                   5: 'F',
                   6: 'F#',
                   7: 'G',
                   8: 'G#',
                   9: 'A',
                   10: 'A#',
                   11: 'B'}

flat_note_dict = {0: 'C',
                  1: 'Db',
                  2: 'D',
                  3: 'Eb',
                  4: 'E',
                  5: 'F',
                  6: 'Gb',
                  7: 'G',
                  8: 'Ab',
                  9: 'A',
                  10: 'Bb',
                  11: 'B'}

reversed_sharp_note_dict = {note: value for value, note in sharp_note_dict.items()}
reversed_flat_note_dict = {note: value for value, note in flat_note_dict.items()}
reversed_note_dict = reversed_flat_note_dict.copy()
reversed_note_dict.update(reversed_sharp_note_dict)

def full_note_name(note, note_dict):
    note, octave = reduce_note(note)
    return note_dict[note] + str(octave)
