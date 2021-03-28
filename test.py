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
# -------------------- test sub-string assumptions ----------------------------

# In handling a string input I have made the following assumptions
#       1) the first sub-string is always the board
#       2) the last sub-string is always the move counter IF A DIGIT
#       3) the penultimate sub-string is always the half move clock IF A DIGIT

def test_noBoardSubstring():
    with mock.patch('builtins.input',side_effect = ['rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R', 'w', 'KQkq', '-','5', '20']):
        test = Fen(fen = 'w KQkq - 5 20')
        # no board element passed
        assert test.fen == 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 5 20'
