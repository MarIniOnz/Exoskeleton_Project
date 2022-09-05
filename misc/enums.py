from enum import Enum

class Side(Enum):
    NONE = None
    LEFT = "left"
    RIGHT = "right"

class ExoState(Enum):
    STOP = 0
    OPEN = 1
    CLOSE = 2
    START = 3

    HIDE_STOP = 5
    HIDE_OPEN = 6
    HIDE_CLOSE = 7

    OPEN_ARM = 11
    CLOSE_ARM = 22
    HIDE_OPEN_ARM = 66
    HIDE_CLOSE_ARM = 77

    NEUTRAL_HAND = 8
    LOCK = 9



class Cue(Enum):
    EMPTY: int = 0
    CLOSE: int = 1
    RELAX: int = 2
    STARTIN5: int = 3
    END: int = 4
    HOVLEFT: int = 5
    HOVRIGHT: int = 6
    
    CLOSE_LEFT: int = 7
    CLOSE_RIGHT: int = 8
    HOVLEFT_LONG: int = 9
    HOVRIGHT_LONG: int = 10
    HOLD_STILL: int = 11
    LIFT: int = 12

    EXO_INACTIVE = 1000000000
    EXO_ACTIVE = 1255255255
    EXO_READY = 1000255000
    EXO_BLOCKED = 1255000000

DisplayText: dict = {
    Cue.EMPTY.value: '',
    Cue.CLOSE.value: 'close',
    Cue.RELAX.value: 'relax',
    Cue.CLOSE_LEFT.value: 'close left',
    Cue.CLOSE_RIGHT.value: 'close right',
    Cue.HOLD_STILL.value: 'hold still',
    Cue.LIFT.value: 'lift',

    Cue.HOVLEFT.value: '<<<',
    Cue.HOVRIGHT.value: '>>>',
    Cue.HOVLEFT_LONG.value: '<<<<<<',
    Cue.HOVRIGHT_LONG.value: '>>>>>>',

    Cue.STARTIN5.value: 'start in 5 seconds',
    Cue.END.value: 'END'
}
