from pydub import AudioSegment
import pydub.playback as playback
import keyboard

sound = AudioSegment.from_mp3("Pyano\poppo.mp3")

keybinding = {
    "a": -10,
    "q": -9,
    "z": -8,
    "s": -7,
    "e": -6,
    "d": -5,
    "r": -4,
    "f": -3,
    "t": -2,
    "g": -1,
    "y": 0,
    "h": 1,
    "u": 2,
    "j": 3,
    "i": 4,
    "k": 5,
    "o": 6,
    "l": 7,
    "p": 8,
    "m": 9,
    "^": 10
}


def PlaySong(pitch_shift):

    new_sample_rate = int(sound.frame_rate * (2.0 ** (float(pitch_shift)/12)))

    lowpitch_sound = sound._spawn(sound.raw_data, overrides={
        'frame_rate': new_sample_rate})

    lowpitch_shift = lowpitch_sound.set_frame_rate(sound.frame_rate)

    # Play pitch changed sound
    playback._play_with_simpleaudio(lowpitch_shift)


def on_press_piano(event):
    try:
        PlaySong(keybinding[event.name])
    except:
        pass


keyboard.on_press(on_press_piano)

while True:
    pass
