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


    
    def Update(self):
        ...
    
    def get_board(self):
        ...
    
    def set_board(self, board):
        ...

    def move_piece(self):
        ...
    
    def get_piece(self):
        for piece in self.pieces:
            self.x[self.pieces[piece]] = self.pieces_points[piece]

        return self.x
        