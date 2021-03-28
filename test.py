import pytest
from fen import Fen
import chess
import mock

startingFen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

# -------------------- tests: non-string fen ----------------------------------

def test_missingFen():
    test = Fen() # nothing passed
    assert test.fen == startingFen

def test_nonStringFenInteger():
    with mock.patch('builtins.input',side_effect = ['rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR',
                            'w','KQkq','-','0','1']): # reset to starting position
        test = Fen(fen = 5) # integer passed
        assert test.fen == startingFen

def test_nonStringFenFloat():
    with mock.patch('builtins.input',side_effect = ['rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR',
                            'w','KQkq','-','0','1']): # reset to starting position
        test = Fen(fen = 5.45) # float passed
        assert test.fen == startingFen

def test_nonStringFenBool():
    with mock.patch('builtins.input',side_effect = ['rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR',
                            'w','KQkq','-']): # full reset to starting position
        test = Fen(fen = True) # bool passed
        # 5 is a valid fen character, so the board element consists of 5
        # blank squares
        assert test.fen == startingFen

# ------------------------------------------------------------ 4 tests: total 4
