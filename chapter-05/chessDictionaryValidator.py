fullChessSet = {'bking': 1,
                'bqueen': 1,
                'bbishop': 2,
                'bknight': 2,
                'brook': 2,
                'bpawn' : 8,
                'wking': 1,
                'wqueen': 1,
                'wbishop': 2,
                'wknight': 2,
                'wrook': 2,
                'wpawn' : 8}
allSpaces = [f'{num}{letter}' for num in range(1,9) for letter in 'abcdefgh']


def hasValidKings(pieces: list):
    return pieces.count('wking') == 1 and pieces.count('bking') == 1


def hasValidSpaces(spaces: list):
    for space in spaces:
        if space not in allSpaces:
            return False
    return True


def hasValidPieceCounts(pieces: list):
    pieceCounts = {}
    for piece in pieces:
        pieceCounts.setdefault(piece, 0)
        pieceCounts[piece] += 1



def isValidChessBoard(board: dict):
    if not hasValidKings(list(board.values())):
        return False
    if not hasValidSpaces(list(board.keys()):
        return False
    if not hasValidPieceCounts(list(board.values()):
        return False
    return True
