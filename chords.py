# chords
# A class for abstract chord, key-independent chord qualities.

class Chord:

    def __init__(self, name: str):
        self.numeral
        self.quality
        self.alters
        self.duration


Examples:
    iii7    =       minor 7 on 3
    V7      =       dom 7 on 5
    bVII7   =       dom 7 on b7
    vii0    =       half-dim 7 on b7
    IVmaj   =       maj7 on 4
    II7b5   =       dom 7 b5 on 2
    vio     =       dim on 6
    ivmaj   =       minor/major 7 on 4

Changes:
    ii7 - V7 - Imaj
    vii0 - III7#5b9 - vimaj
    Imaj - vi7 - ii7 - V7
    iii7 - biii7 - ii7 - V7b5
