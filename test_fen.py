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
    test = Fen(fen = 5) # integer passed
    assert test.fen == startingFen

def test_nonStringFenFloat():
    test = Fen(fen = 5.45) # float passed
    assert test.fen == startingFen

def test_nonStringFenBool():
    test = Fen(fen = True) # bool passed
    assert test.fen == startingFen

# ------------------------------------------------------------ 4 tests: total 4
# -------------------- test sub-string assumptions ----------------------------

# In handling a string input I have made the following assumptions
#       1) the last sub-string is always the move counter IF A DIGIT
#       2) the penultimate sub-string is always the half move clock IF A DIGIT

def test_noBoardSubstring():
    with mock.patch('builtins.input',side_effect = ['rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R']):
        # other elements should be accepted
        test = Fen(fen = 'w KQkq - 5 20')
        # no board element passed
        assert test.fen == 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 5 20'

def test_singleDigit():
    # half move will be reset to 0, move to 1
    test = Fen(fen = 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2')
    assert test.fen == 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 0 1'

def test_NoDigit():
    # half move will be reset to 0, move to 1
    test = Fen(fen = 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -')
    assert test.fen == 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 0 1'

def test_negativeHalfMove():
    # reset in preprocessing
    test = Fen(fen = 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - -5 20')
    assert test.fen == 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 0 1'

def test_negativeMove():
    # reset in preprocessing
    test = Fen(fen = 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 5 -20')
    assert test.fen == 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 0 1'

def test_floatHalfMove():
    # reset in preprocessing
    test = Fen(fen = 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 5.6 20')
    assert test.fen == 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 0 1'

def test_negativeMove():
    # reset in preprocessing
    test = Fen(fen = 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 5 20.1')
    assert test.fen == 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 0 1'

# ----------------------------------------------------------- 7 tests: total 11
