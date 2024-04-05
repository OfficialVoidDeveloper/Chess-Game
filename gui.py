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

def deco(function):
    def wrapper(*args, **kwargs):
        print("================================")
        return function(*args, **kwargs)
    
    return wrapper




@deco
def get_list_of_pieces(pieces: dict) -> list:
    retvalue = []
    for value in pieces: 
        retvalue += pieces[value]
    return retvalue

@deco
def get_list_of_values(pieces: dict) -> list:
    retvalue = []
    for value in pieces: 
        retvalue.append(value)
    return retvalue


def append_to_list(board: list, piece: list) -> list:
    finished = []
    




print(get_list_of_pieces(pieces))
print(get_list_of_values(pieces))


# finished = []



# for i in range(len(board)):
#     for p in pieces:
#         find = pieces[p].find(board[i])
#         print(find)

    # print(board[i], end=" ")