
board = [
    "a8","b8","c8","d8","e8","f8","g8","h8",
    "a7","b7","c7","d7","e7","f7","g7","h7",
    "a6","b6","c6","d6","e6","f6","g6","h6",
    "a5","b5","c5","d5","e5","f5","g5","h5",
    "a4","b4","c4","d4","e4","f4","g4","h4",
    "a3","b3","c3","d3","e3","f3","g3","h3",
    "a2","b2","c2","d2","e2","f2","g2","h2",
    "a1","b1","c1","d1","e1","f1","g1","h1"
]

pieces = {
    "wp" : ["a2","b2","c2","d2","e2","f2", "g2","h2"],
    "bp" : ["a7", "b7","c7","d7","e7","f7","g7","h7"],
    "wr" : ["a1","h1"],
    "br" : ["a8","h8"],
    "wn" : ["b1","g1"],
    "bn" : ["b8","g8"],
    "wb" : ["c1","f1"],
    "bb" : ["c8","f8"],
    "wq" : ["d1"],
    "bq" : ["d8"],
    "wk" : ["e1"],
    "bk" : ["e8"]
}


def printboard(board):
    count = 1
    for i in range(len(board)):
        if count == 8:
            print(board[i], end="\n")
            count = 1
        else:
            count += 1
            print(board[i], end=" ")

def set_board(board, pieces):
    finished =  []
    switched = False
    for piece in pieces:
        for tile in pieces[piece]:
            for i in range(len(board)):
                if board[i] == tile:
                    board[i] = pieces[piece]
                    switched = True
                else: switched = False
        if switched:
            finished.append(board[i])
    return finished




# Main Functions 
def main():
    printboard(set_board(board, pieces))

# Run the Program
if __name__  == "__main__":
    main();