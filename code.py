import time
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.kmk_keyboard import KC
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB
from kmk.extensions.RGB import AnimationModes
from kmk.modules.macros import Macros
from kmk.modules.macros import Delay, Press, Release, Tap
from kmk.modules.holdtap import HoldTap
#define keyboard
keyboard = KMKKeyboard()
layers = Layers()
encoder_handler = EncoderHandler()
macros = Macros()
holdtap = HoldTap()
keyboard.modules = [layers, encoder_handler, macros, holdtap]
keyboard.col_pins = (board.D4, board.D3, board.D2)
keyboard.row_pins = (board.A3, board.A2, board.A1, board.A0)
keyboard.diode_direction = DiodeOrientation.COLUMNS
#rgb
rgb = RGB(pixel_pin = board.MISO,
    num_pixels = 12,
    val_limit = 255,
    val_default = 100,
    animation_speed = 5,
    animation_mode = AnimationModes.SWIRL,
    refresh_rate = 30,
    )
keyboard.extensions.append(rgb)
#layers
LYR_BASE, LYR_ALTBASE, LYR_SR, LYR_ALTSR, LYR_SWARM = 0, 1, 2, 3, 4
#custom keys
ALTTAB = KC.LALT(KC.TAB)
LEARNQ = KC.LCTL(KC.Q)
LEARNW = KC.LCTL(KC.W)
LEARNE = KC.LCTL(KC.E)
LEARNR = KC.LCTL(KC.R)
SRSHIFT = KC.MO(LYR_ALTSR)
BASESHIFT = KC.MO(LYR_ALTBASE)
#macros
prev_animation = None
TO_SWRM = KC.MACRO(
    Tap(KC.TG(LYR_SWARM)),
    Tap(KC.RGB_MODE_BREATHE_RAINBOW)
)
TO_SR = KC.MACRO(
    Tap(KC.TO(LYR_SR)),
    Tap(KC.RGB_MODE_BREATHE)
)
TO_BASE = KC.MACRO(
    Tap(KC.TO(LYR_BASE)),
    Tap(KC.RGB_MODE_SWIRL)
)
keyboard.keymap = [
    #LYR_BASE
    [
    BASESHIFT, KC.TRNS, KC.N1,
    KC.A, KC.R, KC.N2,
    KC.S, KC.W, KC.N4,
    KC.D, KC.E, KC.TAB
    ],
    #LYR_ALTBASE
    [
    KC.TRNS, KC.TRNS, KC.N1,
    KC.A, KC.R, KC.N2,
    KC.S, KC.W, KC.N4,
    KC.D, KC.E, KC.TAB
    ],
    #LYR_SR
    [
    SRSHIFT, KC.Q, KC.N1,
    KC.ESC, KC.W, KC.N2,
    KC.D, KC.E, KC.N3,
    KC.F, KC.R, KC.N4
    ],
    #LYR_ALTSR
    [
    KC.TRNS, LEARNQ, KC.N1,
    KC.O, LEARNW, KC.N2,
    KC.TRNS, LEARNE, KC.P,
    KC.LCTL, LEARNR, KC.TAB
    ],
    #LYR_SWARM
    [
    KC.TRNS, KC.TRNS, KC.N1,
    KC.A, KC.R, KC.N2,
    KC.S, KC.W, KC.N4,
    KC.D, KC.E, KC.TAB
    ],
]
#define encoder
encoder_handler.pins = (
    (board.D7, board.D6, board.D5),
)
encoder_handler.map = [
    ((KC.RGB_VAD, KC.RGB_VAI, TO_SR),),
    ((KC.RGB_AND, KC.RGB_ANI, TO_SWRM),),
    ((KC.RGB_VAD, KC.RGB_VAI, TO_SWRM),),
    ((KC.RGB_VAD, KC.RGB_VAI, TO_BASE),),
    ((KC.RGB_VAD, KC.RGB_VAI, TO_BASE),),
]
keyboard.tap_time = 250
keyboard.debug_enabled = True
if __name__ == "__main__":
    keyboard.go()
