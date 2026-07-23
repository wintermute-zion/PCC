import board

#import extensions/modules
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler

encoder_handler = EncoderHandler()
keyboard.modules = [encoder_handler]
keyboard.extensions.append(MediaKeys())
keyboard = KMKKeyboard()

#specify encoder GPIO pins
encoder_handler.pins = ((board.GP27, board.GP26, board.GP28))

#specify key matrix GPIO pins and diode orientation
keyboard.col_pins = (board.GP0, board.GP1, board.GP2)
keyboard.row_pins = (board.GP3, board.GP4)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

#keypad key mapping
keyboard.keymap = [
    [KC.MEDIA_PLAY_PAUSE, KC.MEDIA_STOP, KC.LGUI(KC.D),
     KC.MEDIA_PREV_TRACK, KC.MEDIA_NEXT_TRACK, KC.LGUI(KC.L)
    ]
]

#encoder key mapping
encoder_handler.map = [((KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN, KC.AUDIO_MUTE))]

if __name__ == '__main__':
    keyboard.go()