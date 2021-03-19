import pygame
import base64
from settings import SETTINGS
import os
from mido import MidiFile


def play_midi_file(midi_file):
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    freq = 44100  # audio CD quality
    bitsize = -16  # unsigned 16 bit
    channels = 2  # 1 is mono, 2 is stereo
    buffer = 1024  # number of samples
    pygame.mixer.init(freq, bitsize, channels, buffer)

    # optional volume 0 to 1.0
    pygame.mixer.music.set_volume(0.8)
    try:
        # use the midi file you just saved
        clock = pygame.time.Clock()
        try:
            pygame.mixer.music.load(midi_file)
            print(f'playing from {midi_file}')
        except pygame.error:
            print("File %s not found! (%s)" % (midi_file, pygame.get_error()))
            return
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            # check if playback has finished
            clock.tick(30)
    except KeyboardInterrupt:
        # if user hits Ctrl/C then exit
        # (works only in console mode)
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.stop()
        return


def play_music(obj, name='temp.midi'):
    temp_file_path = os.path.join(SETTINGS.TEMP_DIR, name)
    temp_written_success = False
    try:
        if isinstance(obj, str):
            write_mid64_to_midi(obj, temp_file_path)
            temp_written_success = False
        elif isinstance(obj, MidiFile):
            obj.save(temp_file_path)
            temp_written_success = False
    except:
        print('midi save failed')

    try:
        play_midi_file(temp_file_path)
    except:
        pass
    finally:
        os.remove(temp_file_path)


def write_mid64_to_midi(mid64, filepath):
    output = base64.b64decode(mid64)
    fout = open(filepath, "wb")
    fout.write(output)
    fout.close()


def read_midi_to_mid64(file_path):
    return base64.encodebytes(open(file_path, 'rb').read())
