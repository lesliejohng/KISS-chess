import chess

class Fen():

    def __init__(self, fen = chess.STARTING_FEN):
        self.fen = fen
        # check fen is a sring
        if not isinstance(self.fen, str): # non-string input
            self.fen = chess.STARTING_FEN
            self.board = chess.Board(self.fen)
        else:
            #pre-processing of fen
            self.fen = self.fen.strip()
            fenList = fen.split(' ')
            lenFenList = len(fenList)
            # rebuild fen if elements out of order
            amendedFenList = ['?','?','?','?','?','?']
            for element in fenList:
                if element.count('/') == 7:
                    amendedFenList[0] = element
                elif element == 'w' or element == 'b':
                    amendedFenList[1] = element
                elif element in ['q','k','kq','Q','Qq','Qk','Qkq','K',
                           'Kq','Kk','Kkq','KQ','KQq','KQk','KQkq']:
                    amendedFenList[2] = element
                elif element in ['a6','b6','c6','d6','e6','f6','g6','h6',
                                 'a3','b3','c3','d3','e3','f3','g3','h3']:
                    amendedElement[3] = element
            # check whether last two items are digits and reposition in fenList
            if fenList[-1].isdigit() and fenList[-2].isdigit():
                amendedFenList[4] = fenList[-2]
                amendedFenList[5] = fenList[-1]
            else:
                # reset halfMove and move elements of fen
                amendedFenList[4] = '0'
                amendedFenList[5] = '1'
            #allocate '-' items if possible
            if fenList.count('-') > 1:
                if amendedFenList[2] == '?':
                    amendedFenList[2] = '-'
                if amendedFenList[3] == '?':
                    amendedFenList[3] = '-'
            if fenList.count('-') == 1:
                if amendedFenList[2] == '?' and amendedFenList[3] != '?':
                    amendedFenList[2] = '-'
                if amendedFenList[2] != '?' and amendedFenList[3] == '?':
                    amendedFenList[3] = '-'
            # reset fenList and fen
            fenList = amendedFenList
            self.fen = self.fenReconstruct(fenList = fenList)
            print(self.fen)
            # main processing
            while True:
                try:
                    self.board = chess.Board(self.fen)
                    break
                except ValueError as e:
                    print(e)
                    if str(e) == "expected 'w' or 'b' for turn part of fen: " + "'" + self.fen + "'":
                        self.inputFen(fen = fen, selector = 't')
                    elif str(e) == "invalid castling part in fen: " + "'" + self.fen + "'":
                        self.inputFen(fen = fen, selector = 'c')
                    elif str(e) == "invalid en passant part in fen: " + "'" + self.fen + "'":
                        self.inputFen(fen = fen, selector = 'e')
                    elif str(e) == "invalid half-move clock in fen: " + "'" + self.fen + "'":
                        self.inputFen(fen = fen, selector = 'h')
                    elif str(e) == "half-move clock cannot be negative: " +  "'" + self.fen + "'":
                        self.inputFen(fen = fen, selector = 'h')
                    elif str(e) == "invalid fullmove number in fen: " +  "'" + self.fen + "'":
                        self.inputFen(fen = fen, selector = 'm')
                    elif str(e) == "fullmove number cannot be negative: " +  "'" + self.fen + "'":
                        self.inputFen(fen = fen, selector = 'm')
                    elif str(e) == "expected 8 rows in position part of fen: " + "'" + fenList[0] + "'":
                        self.inputFen(fen = fen, selector = 'b')

            print(self.board)

    def __str__(self):
        return self.board.board

    def __repr__(self):
        return self.board

    def inputFen(self, fen, selector = '?'):
        fenList = self.fen.split(' ')
        print('original fen: ' + fen)
        print('current fen: ' + self.fen)
        while selector not in ['b','t','c','e','h','m','x']:
            print("""
            What element of the FEN do you want to amend?
                (b)oard
                (t)urn
                (c)astling rights
                (e)p square
                (h)alf move
                e(x)it
                """)
            selector = input("Please input selection (b,t,c,e,h,m or x)\n")

        if selector == 'b':
            board = ''
            while len(board) < 15:
                print('present board element: '+fenList[0]+'\n')
                board = input('input corrected board element of fen:\n')
            fenList[0] = board
            self.fen = self.fenReconstruct(fenList)
            print('new fen: ' + self.fen)

        elif selector == 't':
            turn = ''
            while turn not in 'wb' or len(turn) != 1:
                print('present Turn element: '+fenList[1]+'\n')
                turn = input('input turn to play (w/b):\n')
            fenList[1] = turn
            self.fen = self.fenReconstruct(fenList)
            print('new fen: ' + self.fen)

        elif selector == 'c':
            castling = ''
            validCastling = ['-','q','k','kq',
                    'Q','Qq','Qk','Qkq','K', 'Kq','Kk','Kkq','KQ',
                    'KQq','KQk','KQkq']
            while castling not in validCastling:
                print('present castling element: '+fenList[2]+'\n')
                castling = input('input castling rights in form "KQkq" or "-" for none:\n')
            fenList[2] = castling
            self.fen = self.fenReconstruct(fenList)
            print('new fen: '+ self.fen)

        elif selector == 'e':
            ep = ''
            validep = ['-', 'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
                        'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6']
            while not ep in validep:
                print('present ep element: '+fenList[3]+'\n')
                ep = input("input corrected ep square or '-' if none:\n")
            fenList[3] = ep
            self.fen = self.fenReconstruct(fenList)
            print('new fen:' + self.fen)

        elif selector == 'h':
            halfMove = ''
            while not halfMove.isdigit():
                print('present halfMoveClock is :'+fenList[4]+'\n')
                halfMove = input('input half move, or "?" if unknown\n')
                if halfMove == '?':
                    halfMove = '0' #reset halfMove
            fenList[4] = halfMove
            self.fen = self.fenReconstruct(fenList)
            print('newFen: ' + self.fen)

        elif selector == 'm':
            move = ''
            while not move.isdigit():
                print('present move counter is :'+fenList[5]+'\n')
                move = input('input move number, or "?" if unknown\n')
                if move == '?': #reset move
                    move = '1'
            fenList[5] = move
            self.fen = self.fenReconstruct(fenList)
            print('new fen: ' + self.fen)

        elif selector == 'x':
            print('no changes made\n')
            print('current fen: ' + self.fen)

    def fenReconstruct(self, fenList):
        fen = fenList[0]+' '+fenList[1]+' '+fenList[2]+' '+fenList[3]+' '+fenList[4]+' '+fenList[5]
        return fen


# test
test = Fen('rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2')
print(type(test.board))
print(test.board)
