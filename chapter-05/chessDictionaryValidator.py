fullChessSet = {
    "bking": 1,
    "bqueen": 1,
    "bbishop": 2,
    "bknight": 2,
    "brook": 2,
    "bpawn": 8,
    "wking": 1,
    "wqueen": 1,
    "wbishop": 2,
    "wknight": 2,
    "wrook": 2,
    "wpawn": 8,
}
allSpaces = [f"{num}{letter}" for num in range(1, 9) for letter in "abcdefgh"]


def hasValidKings(pieces: list):
    return pieces.count("wking") == 1 and pieces.count("bking") == 1


def hasValidSpaces(spaces: list):
    for space in spaces:
        if space not in allSpaces:
            return False
    return True


def hasValidPieceCounts(pieces: list):
    pieceCounts = {piece: 0 for piece in pieces}
    for piece in pieces:
        pieceCounts[piece] += 1
    for piece in pieceCounts:
        if pieceCounts[piece] > fullChessSet[piece]:
            return False
    return True


def isValidChessBoard(board: dict):
    if not hasValidKings(list(board.values())):
        return False
    if not hasValidSpaces(list(board.keys())):
        return False
    if not hasValidPieceCounts(list(board.values())):
        return False
    return True


myGoodBoard = {
    "1h": "bking",
    "6c": "wqueen",
    "2g": "bbishop",
    "5h": "bqueen",
    "3e": "wking",
}
myBadKingsBoard = {
    "1h": "bking",
    "6c": "wqueen",
    "2g": "bbishop",
    "5h": "bking",
    "3e": "wking",
}
myBadSpacesBoard = {
    "1h": "bking",
    "6c": "wqueen",
    "2g": "bbishop",
    "5h": "bqueen",
    "9e": "wking",
}
myBadPiecesBoard = {
    "1h": "bking",
    "6c": "wqueen",
    "2g": "bbishop",
    "5h": "wqueen",
    "3e": "wking",
    "4e": "wqueen",
}


for board in [myGoodBoard, myBadKingsBoard, myBadSpacesBoard, myBadPiecesBoard]:
    print(isValidChessBoard(board))
