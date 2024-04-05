class ChessGame:
    def __init__(self):
        self.board = []
        self.x = {}

        self.pieces = {
            'p': 'Pawn',
            'n': 'Knight',
            'b': 'Bishop',
            'r': 'Rook',
            'q': 'Queen',
            'k': 'King'
        }
        self.pieces_points = {
            'p': 1,
            'n': 3,
            'b': 3,
            'r': 5,
            'q': 9,
            'k': 99
        }
        self.board_layout = [
            [["a8"],["b8"],["c8"],["d8"],["e8"],["f8"],["g8"],["h8"]],
            [["a7"],["b7"],["c7"],["d7"],["e7"],["f7"],["g7"],["h7"]],
            [["a6"],["b6"],["c6"],["d6"],["e6"],["f6"],["g6"],["h6"]],
            [["a5"],["b5"],["c5"],["d5"],["e5"],["f5"],["g5"],["h5"]],
            [["a4"],["b4"],["c4"],["d4"],["e4"],["f4"],["g4"],["h4"]],
            [["a3"],["b3"],["c3"],["d3"],["e3"],["f3"],["g3"],["h3"]],
            [["a2"],["b2"],["c2"],["d2"],["e2"],["f2"],["g2"],["h2"]],
            [["a1"],["b1"],["c1"],["d1"],["e1"],["f1"],["g1"],["h1"]]
        ]


    
    def Update(self):
        ...
    
    def get_board(self):
        ...
    
    def set_board(self, pieces):
        ...

    def move_piece(self):
        ...
    
    def get_piece(self):
        for piece in self.pieces:
            self.x[self.pieces[piece]] = self.pieces_points[piece]

        return self.x
        