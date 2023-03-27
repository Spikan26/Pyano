from pydub import AudioSegment
import pydub.playback as playback
import keyboard
import threading
import time

sound = AudioSegment.from_mp3("Pyano\qp.mp3")
shift_offset = 3


def PlaySong(pitch_shift):

    new_sample_rate = int(sound.frame_rate * (2.0 ** (float(pitch_shift)/12)))

    lowpitch_sound = sound._spawn(sound.raw_data, overrides={
        'frame_rate': new_sample_rate})

    lowpitch_shift = lowpitch_sound.set_frame_rate(sound.frame_rate)

    # Play pitch changed sound
    playback._play_with_simpleaudio(lowpitch_shift)


def on_press_reaction(event):
    match event.name:
        case "a":
            PlaySong(0-shift_offset*10)
        case "q":
            PlaySong(0-shift_offset*9)
        case "z":
            PlaySong(0-shift_offset*8)
        case "s":
            PlaySong(0-shift_offset*7)
        case "e":
            PlaySong(0-shift_offset*6)
        case "d":
            PlaySong(0-shift_offset*5)
        case "r":
            PlaySong(0-shift_offset*4)
        case "f":
            PlaySong(0-shift_offset*3)
        case "t":
            PlaySong(0-shift_offset*2)
        case "g":
            PlaySong(0-shift_offset)
        case "y":
            PlaySong(0)
        case "h":
            PlaySong(0+shift_offset)
        case "u":
            PlaySong(0+shift_offset*2)
        case "j":
            PlaySong(0+shift_offset*3)
        case "i":
            PlaySong(0+shift_offset*4)
        case "k":
            PlaySong(0+shift_offset*5)
        case "o":
            PlaySong(0+shift_offset*6)
        case "l":
            PlaySong(0+shift_offset*7)
        case "p":
            PlaySong(0+shift_offset*8)
        case "m":
            PlaySong(0+shift_offset*9)
        case "^":
            PlaySong(0+shift_offset*10)


keyboard.on_press(on_press_reaction)

while True:
    pass
