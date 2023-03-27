from pydub import AudioSegment
import pydub.playback as playback
import keyboard
import threading
import time

sound = AudioSegment.from_mp3("poppo.mp3")
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
            PlaySong(0-shift_offset*4)
        case "z":
            PlaySong(0-shift_offset*3)
        case "e":
            PlaySong(0-shift_offset*2)
        case "r":
            PlaySong(0-shift_offset)
        case "t":
            PlaySong(0)
        case "y":
            PlaySong(0+shift_offset)
        case "u":
            PlaySong(0+shift_offset*2)
        case "i":
            PlaySong(0+shift_offset*3)
        case "o":
            PlaySong(0+shift_offset*4)
        case "p":
            PlaySong(-30)
        case "m":
            PlaySong(20)


keyboard.on_press(on_press_reaction)

while True:
    pass
