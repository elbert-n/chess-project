import pygame as p
whitemove = True
running = True
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
width = height = 600
SIZE = (width, height)
square_size = width // 8
board = [[".." for i in range(8)] for j in range(8)]
imagepieces = {}
truepossiblemoves = []
possiblemoves = []
piecesclicked = []
placesclicked = []
#setting up the board
def initboard():
    global board
    board[0][0] = "bR"
    board[0][1] = "bN"
    board[0][2] = "bB"
    board[0][3] = "bQ"
    board[0][4] = "bK"
    board[0][5] = "bB"
    board[0][6] = "bN"
    board[0][7] = "bR"
    for i in range(8):
        board[1][i] = "bP"
    board[7][0] = "wR"
    board[7][1] = "wN"
    board[7][2] = "wB"
    board[7][3] = "wQ"
    board[7][4] = "wK"
    board[7][5] = "wB"
    board[7][6] = "wN"
    board[7][7] = "wR"
    for i in range(8):
        board[6][i] = "wP"

def initimages():
    pieces = ["bP", "bR", "bN", "bB", "bQ", "bK", "wP", "wR", "wN", "wB", "wQ", "wK"]
    for piece in pieces:
        imagepieces[piece] = p.transform.scale(p.image.load(piece+".png"), (square_size, square_size))


def drawpieces():
    for x in range(8):
        for y in range(8):
            piece = board[x][y]
            if piece != '..':
                screen.blit(imagepieces[piece], p.Rect(y*square_size, x*square_size, square_size, square_size))

def drawboard():
    colors = [WHITE, GRAY]
    for x in range(8):
        cindex =  x % 2
        for y in range (8):
            square = (x*square_size, y*square_size, square_size, square_size)
            p.draw.rect(screen, colors[cindex], square)
            cindex = ((cindex+1) % 2)

def getpawnmoves(r, c):
    if whitemove == True and board[r][c][0] == "w":
        if r == 6 and board[r-2][c] == ".." and board[r-1][c] == "..":
            truepossiblemoves.append(((r,c), (r-2, c)))
        if board[r-1][c] == "..":
            truepossiblemoves.append(((r, c), (r-1,c)))
        if c-1 >= 0:
            if board[r-1][c-1][0] == "b":
                truepossiblemoves.append(((r,c), (r-1,c-1)))
        if c+1 <= 7:
            if board[r-1][c+1][0] == "b":
                truepossiblemoves.append(((r,c), (r-1,c+1)))
    elif whitemove == False and board[r][c][0] == "b":
        if r == 1 and board[r+2][c] == ".." and board[r+1][c] == ".." :
            truepossiblemoves.append(((r,c), (r+2,c)))
        if board[r+1][c] == "..":
            truepossiblemoves.append(((r, c), (r+1, c)))
        if c-1 >= 0:
            if board[r+1][c-1][0] == "w":
                truepossiblemoves.append(((r,c), (r+1,c-1)))
        if c+1 <= 7:
            if board[r+1][c+1][0] == "w":
                truepossiblemoves.append(((r,c), (r+1, c+1)))

def checkbounds(r, c):
    if (r < 0 or r > 7) or (c < 0 or c> 7):
        return False
    else:
        return True

def getknightmoves(r, c):
    if whitemove == True and board[r][c][0] == "w":
        for i in range(8):
            if i == 0:
                roffset = -2
                coffset = -1
            elif i == 1:
                roffset = -2
                coffset = 1
            elif i == 2:
                roffset = 2
                coffset = -1
            elif i == 3:
                roffset = 2
                coffset = 1
            elif i == 4:
                roffset = -1
                coffset = -2
            elif i == 5:
                roffset = -1
                coffset = 2
            elif i == 6:
                roffset = 1
                coffset = -2
            elif i == 7:
                roffset = 1
                coffset = 2
            if checkbounds(r+roffset, c+coffset):
                if board[r+roffset][c+coffset][0] != "w":
                    print(r, c)
                    truepossiblemoves.append(((r,c), (r+roffset, c+coffset)))
    elif whitemove == False and board[r][c][0] == "b":
        for i in range(8):
            if i == 0:
                roffset = -2
                coffset = -1
            elif i == 1:
                roffset = -2
                coffset = 1
            elif i == 2:
                roffset = 2
                coffset = -1
            elif i == 3:
                roffset = 2
                coffset = 1
            elif i == 4:
                roffset = -1
                coffset = -2
            elif i == 5:
                roffset = -1
                coffset = 2
            elif i == 6:
                roffset = 1
                coffset = -2
            elif i == 7:
                roffset = 1
                coffset = 2
            if checkbounds(r+roffset, c+coffset):
                if board[r+roffset][c+coffset][0] != "b":
                    print(r, c)
                    truepossiblemoves.append(((r,c), (r+roffset, c+coffset)))

def getrookmoves(r, c):
    if whitemove == True and board[r][c][0] == "w":
        for i in range(r-1, -1, -1):
            if board[i][c][0] == "w":
                break
            elif board[i][c][0] == "b":
                truepossiblemoves.append(((r, c), (i, c)))
                break
            else:
                truepossiblemoves.append(((r, c), (i, c)))
        for i in range(r+1, 8):
            if board[i][c][0] == "w":
                break
            elif board[i][c][0] == "b":
                truepossiblemoves.append(((r, c), (i, c)))
                break
            else:
                truepossiblemoves.append(((r, c), (i, c)))
        for i in range(c-1, -1, -1):
            if board[r][i][0] == "w":
                break
            elif board[r][i][0] == "b":
                truepossiblemoves.append(((r, c), (r, i)))
                break
            else:
                truepossiblemoves.append(((r, c), (r, i)))
        for i in range(c+1, 8):
            if board[r][i][0] == "w":
                break
            elif board[r][i][0] == "b":
                truepossiblemoves.append(((r, c), (r, i)))
                break
            else:
                truepossiblemoves.append(((r, c), (r, i)))
    elif whitemove == False and board[r][c][0] == "b":
        for i in range(r-1, -1, -1):
            if board[i][c][0] == "b":
                break
            elif board[i][c][0] == "w":
                truepossiblemoves.append(((r, c), (i, c)))
                break
            else:
                truepossiblemoves.append(((r, c), (i, c)))
        for i in range(r+1, 8):
            if board[i][c][0] == "b":
                break
            elif board[i][c][0] == "w":
                truepossiblemoves.append(((r, c), (i, c)))
                break
            else:
                truepossiblemoves.append(((r, c), (i, c)))
        for i in range(c-1, -1, -1):
            if board[r][i][0] == "b":
                break
            elif board[r][i][0] == "w":
                truepossiblemoves.append(((r, c), (r, i)))
                break
            else:
                truepossiblemoves.append(((r, c), (r, i)))
        for i in range(c+1, 8):
            if board[r][i][0] == "b":
                break
            elif board[r][i][0] == "w":
                truepossiblemoves.append(((r, c), (r, i)))
                break
            else:
                truepossiblemoves.append(((r, c), (r, i)))

def getbishopmoves(r, c):
    if whitemove == True and board[r][c][0] == "w":
        for i, j in zip(range(r-1, -1, -1), range(c-1, -1, -1)):
            if board[i][j][0] == "w":
                break
            elif board[i][j][0] == "b":
                truepossiblemoves.append(((r, c), (i, j)))
                break
            else:
                truepossiblemoves.append(((r, c), (i, j)))
        for i, j in zip(range(r-1, -1, -1), range(c+1, 8)):
            if board[i][j][0] == "w":
                break
            elif board[i][j][0] == "b":
                truepossiblemoves.append(((r, c), (i, j)))
                break
            else:
                truepossiblemoves.append(((r, c), (i, j)))     
        for i, j in zip(range(r+1, 8), range(c-1, -1, -1)):
            if board[i][j][0] == "w":
                break
            elif board[i][j][0] == "b":
                truepossiblemoves.append(((r, c), (i, j)))
                break
            else:
                truepossiblemoves.append(((r, c), (i, j)))       
        for i, j in zip(range(r+1, 8), range(c+1, 8)):
            if board[i][j][0] == "w":
                break
            elif board[i][j][0] == "b":
                truepossiblemoves.append(((r, c), (i, j)))
                break
            else:
                truepossiblemoves.append(((r, c), (i, j)))
    if whitemove == False and board[r][c][0] == "b":
        for i, j in zip(range(r-1, -1, -1), range(c-1, -1, -1)):
            if board[i][j][0] == "b":
                break
            elif board[i][j][0] == "w":
                truepossiblemoves.append(((r, c), (i, j)))
                break
            else:
                truepossiblemoves.append(((r, c), (i, j)))
        for i, j in zip(range(r-1, -1, -1), range(c+1, 8)):
            if board[i][j][0] == "b":
                break
            elif board[i][j][0] == "w":
                truepossiblemoves.append(((r, c), (i, j)))
                break
            else:
                truepossiblemoves.append(((r, c), (i, j)))     
        for i, j in zip(range(r+1, 8), range(c-1, -1, -1)):
            if board[i][j][0] == "b":
                break
            elif board[i][j][0] == "w":
                truepossiblemoves.append(((r, c), (i, j)))
                break
            else:
                truepossiblemoves.append(((r, c), (i, j)))       
        for i, j in zip(range(r+1, 8), range(c+1, 8)):
            if board[i][j][0] == "b":
                break
            elif board[i][j][0] == "w":
                truepossiblemoves.append(((r, c), (i, j)))
                break
            else:
                truepossiblemoves.append(((r, c), (i, j)))

def getqueenmoves(r, c):
    getbishopmoves(r, c)
    getrookmoves(r, c)

def getkingmoves(r, c):
    if whitemove == True and board[r][c][0] == "w":
        for i in range(8):
            if i == 0:
                roffset = 0
                coffset = -1
            elif i == 1:
                roffset = 0
                coffset = 1
            elif i == 2:
                roffset = -1
                coffset = -1
            elif i == 3:
                roffset = -1
                coffset = 0
            elif i == 4:
                roffset = -1
                coffset = 1
            elif i == 5:
                roffset = 1
                coffset = -1
            elif i == 6:
                roffset = 1
                coffset = 0
            elif i == 7:
                roffset = 1
                coffset = 1
            if checkbounds(r+roffset, c+coffset):
                if board[r+roffset][c+coffset][0] != "w":
                    truepossiblemoves.append(((r,c), (r+roffset, c+coffset)))
    elif whitemove == False and board[r][c][0] == "b":
        for i in range(8):
            if i == 0:
                roffset = 0
                coffset = -1
            elif i == 1:
                roffset = 0
                coffset = 1
            elif i == 2:
                roffset = -1
                coffset = -1
            elif i == 3:
                roffset = -1
                coffset = 0
            elif i == 4:
                roffset = -1
                coffset = 1
            elif i == 5:
                roffset = 1
                coffset = -1
            elif i == 6:
                roffset = 1
                coffset = 0
            elif i == 7:
                roffset = 1
                coffset = 1
            if checkbounds(r+roffset, c+coffset):
                if board[r+roffset][c+coffset][0] != "b":
                    truepossiblemoves.append(((r,c), (r+roffset, c+coffset)))
def getallmoves():
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece[1] == "P":
                getpawnmoves(r, c)
            elif piece[1] == "N":
                getknightmoves(r, c)
            elif piece[1] == "R":
                getrookmoves(r, c)
            elif piece[1] == "B":
                getbishopmoves(r, c)
            elif piece[1] == "Q":
                getqueenmoves(r, c)
            elif piece[1] == "K":
                getkingmoves(r, c)
    print(whitemove)

def pawnpromotion():
    for c in range(8):
        if board[7][c] == "bP":
            board[7][c] = "bQ"
        if board[0][c] == "wP":
            board[0][c] = "wQ"

initboard()
initimages()
p.init()
screen = p.display.set_mode(SIZE)
while running:
    for evnt in p.event.get():
        if evnt.type == p.QUIT:
            running = False
        if evnt.type == p.MOUSEBUTTONDOWN:
            pos = p.mouse.get_pos()
            posx = pos[0]//square_size
            posy = pos[1]//square_size
            pieceselected = board[posy][posx]
            piecesclicked.append(pieceselected)
            placesclicked.append((posy, posx))
        if len(placesclicked) == 2:
            print(piecesclicked)
            if(piecesclicked[0] != ".."):
                if ((placesclicked[0][0], placesclicked[0][1]), (placesclicked[1][0], placesclicked[1][1])) in truepossiblemoves:
                    board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0]
                    board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                    piecesclicked = []
                    placesclicked = []
                    truepossiblemoves = []
                    whitemove = not whitemove
                else:
                    piecesclicked = []
                    placesclicked = []
                """
                if whitemove == True:
                    if(piecesclicked[0][0]) == "w":
                        if(piecesclicked[0][1]) == "P":
                            if placesclicked[0][0] == 6:
                                if (placesclicked[0][0]-2 == placesclicked[1][0] or placesclicked[0][0]-1 == placesclicked[1][0]) and placesclicked[0][1] == placesclicked[1][1] and board[(placesclicked[1])[0]][(placesclicked[1])[1]] == ".." and board[(placesclicked[0])[0]-1][(placesclicked[0])[1]] == "..":
                                    board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0]
                                    board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                    piecesclicked = []
                                    placesclicked = []
                                    whitemove = not whitemove
                                elif placesclicked[0][0]-1 == placesclicked[1][0] and (placesclicked[0][1]+1 == placesclicked[1][1] or placesclicked[0][1]-1 == placesclicked[1][1]) and board[(placesclicked[1])[0]][(placesclicked[1])[1]][0] != "w":
                                    board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0]
                                    board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                    piecesclicked = []
                                    placesclicked = []
                                    whitemove = not whitemove
                                else:
                                    piecesclicked = []
                                    placesclicked = []
                            elif placesclicked[1][0] == 0:
                                board[(placesclicked[1])[0]][(placesclicked[1])[1]] = "wQ"
                                board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                piecesclicked = []
                                placesclicked = []
                                whitemove = not whitemove
                            else:
                                if (placesclicked[0][0]-1 == placesclicked[1][0] and placesclicked[0][1] == placesclicked[1][1]) and board[(placesclicked[1])[0]][(placesclicked[1])[1]] == "..":    
                                    board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0]
                                    board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                    piecesclicked = []
                                    placesclicked = []
                                    whitemove = not whitemove
                                elif placesclicked[0][0]-1 == placesclicked[1][0] and (placesclicked[0][1]+1 == placesclicked[1][1] or placesclicked[0][1]-1 == placesclicked[1][1]) and board[(placesclicked[1])[0]][(placesclicked[1])[1]][0] == "b":
                                    board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0]
                                    board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                    piecesclicked = []
                                    placesclicked = []
                                    whitemove = not whitemove
                                else:
                                    piecesclicked = []
                                    placesclicked = [] 
                        elif (piecesclicked[0][1]) == "N":
                            if ((placesclicked[0][0]-2 == placesclicked[1][0] and placesclicked[0][1]-1 == placesclicked[1][1]) or (placesclicked[0][0]-2 == placesclicked[1][0] and placesclicked[0][1]+1 == placesclicked[1][1]) or (placesclicked[0][0]+2 == placesclicked[1][0] and placesclicked[0][1]-1 == placesclicked[1][1]) or (placesclicked[0][0]+2 == placesclicked[1][0] and placesclicked[0][1]+1 == placesclicked[1][1]) or (placesclicked[0][0]-1 == placesclicked[1][0] and placesclicked[0][1]+2 == placesclicked[1][1]) or (placesclicked[0][0]-1 == placesclicked[1][0] and placesclicked[0][1]-2 == placesclicked[1][1]) or (placesclicked[0][0]+1 == placesclicked[1][0] and placesclicked[0][1]-2 == placesclicked[1][1]) or (placesclicked[0][0]+1 == placesclicked[1][0] and placesclicked[0][1]+2 == placesclicked[1][1])) and board[(placesclicked[1])[0]][(placesclicked[1])[1]][0] != "w":
                                print(piecesclicked)
                                print(placesclicked)
                                print(board[(placesclicked[1])[0]][(placesclicked[1])[1]][0])
                                board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0]
                                board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                piecesclicked = []
                                placesclicked = []
                                whitemove = not whitemove
                            else:
                                piecesclicked = []
                                placesclicked = []
                        elif (piecesclicked[0][1]) == "R":
                            for i in range(placesclicked[0][0]-1, -1, -1):
                                if board[i][placesclicked[0][1]][0] == "w":
                                   break
                                elif board[i][placesclicked[0][1]][0] == "b":
                                    possiblemoves.append((i, placesclicked[0][1]))
                                    break
                                else:
                                    possiblemoves.append((i, placesclicked[0][1]))
                            for i in range(placesclicked[0][0]+1, 8):
                                if board[i][placesclicked[0][1]][0] == "w":
                                   break
                                elif board[i][placesclicked[0][1]][0] == "b":
                                    possiblemoves.append((i, placesclicked[0][1]))
                                    break
                                else:
                                    possiblemoves.append((i, placesclicked[0][1]))
                            for i in range(placesclicked[0][1]-1, -1, -1):
                                if board[placesclicked[0][0]][i][0] == "w":
                                   break
                                elif board[placesclicked[0][0]][i][0] == "b":
                                    possiblemoves.append((placesclicked[0][0], i))
                                    break
                                else:
                                    possiblemoves.append((placesclicked[0][0], i))
                            for i in range(placesclicked[0][1]+1, 8):
                                if board[placesclicked[0][0]][i][0] == "w":
                                   break
                                elif board[placesclicked[0][0]][i][0] == "b":
                                    possiblemoves.append((placesclicked[0][0], i))
                                    break
                                else:
                                    possiblemoves.append((placesclicked[0][0], i))
                            print(possiblemoves)
                            if (placesclicked[1][0], placesclicked[1][1]) in possiblemoves:
                                board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0]
                                board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                piecesclicked = []
                                placesclicked = []
                                possiblemoves = []
                                whitemove = not whitemove
                            else:
                                piecesclicked = []
                                placesclicked = []
                                possiblemoves = []
                        elif (piecesclicked[0][1]) == "B":
                            for i, j in zip(range(placesclicked[0][0]-1, -1, -1), range(placesclicked[0][1]-1, -1, -1)):
                                if board[i][j][0] == "w":
                                    break
                                elif board[i][j][0] == "b":
                                    possiblemoves.append((i, j))
                                    break
                                else:
                                    possiblemoves.append((i, j))
                            for i, j in zip(range(placesclicked[0][0]-1, -1, -1), range(placesclicked[0][1]+1, 8)):
                                if board[i][j][0] == "w":
                                    break
                                elif board[i][j][0] == "b":
                                    possiblemoves.append((i, j))
                                    break
                                else:
                                    possiblemoves.append((i, j))     
                            for i, j in zip(range(placesclicked[0][0]+1, 8), range(placesclicked[0][1]-1, -1, -1)):
                                if board[i][j][0] == "w":
                                    break
                                elif board[i][j][0] == "b":
                                    possiblemoves.append((i, j))
                                    break
                                else:
                                    possiblemoves.append((i, j))        
                            for i, j in zip(range(placesclicked[0][0]+1, 8), range(placesclicked[0][1]+1, 8)):
                                if board[i][j][0] == "w":
                                    break
                                elif board[i][j][0] == "b":
                                    possiblemoves.append((i, j))
                                    break
                                else:
                                    possiblemoves.append((i, j))   
                            if (placesclicked[1][0], placesclicked[1][1]) in possiblemoves:
                                board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0]
                                board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                piecesclicked = []
                                placesclicked = []
                                possiblemoves = []
                                whitemove = not whitemove
                            else:
                                piecesclicked = []
                                placesclicked = []
                                possiblemoves = []
                        elif (piecesclicked[0][1]) == "Q":
                            for i, j in zip(range(placesclicked[0][0]-1, -1, -1), range(placesclicked[0][1]-1, -1, -1)):
                                if board[i][j][0] == "w":
                                    break
                                elif board[i][j][0] == "b":
                                    possiblemoves.append((i, j))
                                    break
                                else:
                                    possiblemoves.append((i, j))
                            for i, j in zip(range(placesclicked[0][0]-1, -1, -1), range(placesclicked[0][1]+1, 8)):
                                if board[i][j][0] == "w":
                                    break
                                elif board[i][j][0] == "b":
                                    possiblemoves.append((i, j))
                                    break
                                else:
                                    possiblemoves.append((i, j))     
                            for i, j in zip(range(placesclicked[0][0]+1, 8), range(placesclicked[0][1]-1, -1, -1)):
                                if board[i][j][0] == "w":
                                    break
                                elif board[i][j][0] == "b":
                                    possiblemoves.append((i, j))
                                    break
                                else:
                                    possiblemoves.append((i, j))        
                            for i, j in zip(range(placesclicked[0][0]+1, 8), range(placesclicked[0][1]+1, 8)):
                                if board[i][j][0] == "w":
                                    break
                                elif board[i][j][0] == "b":
                                    possiblemoves.append((i, j))
                                    break
                                else:
                                    possiblemoves.append((i, j))   
                            for i in range(placesclicked[0][0]-1, -1, -1):
                                if board[i][placesclicked[0][1]][0] == "w":
                                   break
                                elif board[i][placesclicked[0][1]][0] == "b":
                                    possiblemoves.append((i, placesclicked[0][1]))
                                    break
                                else:
                                    possiblemoves.append((i, placesclicked[0][1]))
                            for i in range(placesclicked[0][0]+1, 8):
                                if board[i][placesclicked[0][1]][0] == "w":
                                   break
                                elif board[i][placesclicked[0][1]][0] == "b":
                                    possiblemoves.append((i, placesclicked[0][1]))
                                    break
                                else:
                                    possiblemoves.append((i, placesclicked[0][1]))
                            for i in range(placesclicked[0][1]-1, -1, -1):
                                if board[placesclicked[0][0]][i][0] == "w":
                                   break
                                elif board[placesclicked[0][0]][i][0] == "b":
                                    possiblemoves.append((placesclicked[0][0], i))
                                    break
                                else:
                                    possiblemoves.append((placesclicked[0][0], i))
                            for i in range(placesclicked[0][1]+1, 8):
                                if board[placesclicked[0][0]][i][0] == "w":
                                   break
                                elif board[placesclicked[0][0]][i][0] == "b":
                                    possiblemoves.append((placesclicked[0][0], i))
                                    break
                                else:
                                    possiblemoves.append((placesclicked[0][0], i))
                            print(possiblemoves)
                            if (placesclicked[1][0], placesclicked[1][1]) in possiblemoves:
                                board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0]
                                board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                piecesclicked = []
                                placesclicked = []
                                possiblemoves = []
                                whitemove = not whitemove
                            else:
                                piecesclicked = []
                                placesclicked = []
                                possiblemoves = []
                        elif piecesclicked[0][1] == "K":
                            if (((placesclicked[0][0]+1 == placesclicked[1][0] or placesclicked[0][0]-1 == placesclicked[1][0]) and (placesclicked[0][1] == placesclicked[1][1] or placesclicked[0][1]+1 == placesclicked[1][1] or placesclicked[0][1]-1 == placesclicked[1][1])) or (placesclicked[0][0] == placesclicked[1][0] and (placesclicked[0][1]+1 == placesclicked[1][1] or placesclicked[0][1]-1 == placesclicked[1][1]))) and piecesclicked[1][0] != "w":
                                board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0]
                                board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                piecesclicked = []
                                placesclicked = []
                                whitemove = not whitemove
                            else:
                                piecesclicked = []
                                placesclicked = []         
                        else:
                            piecesclicked = []
                            placesclicked = []
                    else:
                        piecesclicked = []
                        placesclicked = []
                elif whitemove == False: #black pieces
                    if(piecesclicked[0][0]) == "b":
                        if(piecesclicked[0][1]) == "P":
                            if placesclicked[0][0] == 1:
                                if (placesclicked[0][0]+2 == placesclicked[1][0] or placesclicked[0][0]+1 == placesclicked[1][0]) and placesclicked[0][1] == placesclicked[1][1] and board[(placesclicked[1])[0]][(placesclicked[1])[1]] == "..":
                                    board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0]
                                    board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                    piecesclicked = []
                                    placesclicked = []
                                    whitemove = not whitemove
                                elif placesclicked[0][0]+1 == placesclicked[1][0] and (placesclicked[0][1]+1 == placesclicked[1][1] or placesclicked[0][1]-1 == placesclicked[1][1]) and board[(placesclicked[1])[0]][(placesclicked[1])[1]] != "..":
                                    board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0]
                                    board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                    piecesclicked = []
                                    placesclicked = []
                                    whitemove = not whitemove
                                else:
                                    piecesclicked = []
                                    placesclicked = []  
                            elif placesclicked[1][0] == 7:
                                board[(placesclicked[1])[0]][(placesclicked[1])[1]] = "bQ"
                                board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                piecesclicked = []
                                placesclicked = []
                                whitemove = not whitemove
                            else:
                                if (placesclicked[0][0]+1 == placesclicked[1][0] and placesclicked[0][1] == placesclicked[1][1]) and board[(placesclicked[1])[0]][(placesclicked[1])[1]] == "..":    
                                    board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0]
                                    board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                    piecesclicked = []
                                    placesclicked = []
                                    whitemove = not whitemove
                                elif placesclicked[0][0]+1 == placesclicked[1][0] and (placesclicked[0][1]+1 == placesclicked[1][1] or placesclicked[0][1]-1 == placesclicked[1][1]) and board[(placesclicked[1])[0]][(placesclicked[1])[1]] != "..":
                                    board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0]
                                    board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                    piecesclicked = []
                                    placesclicked = []
                                    whitemove = not whitemove
                                else:
                                    piecesclicked = []
                                    placesclicked = []
                        elif (piecesclicked[0][1]) == "N":
                            if ((placesclicked[0][0]-2 == placesclicked[1][0] and placesclicked[0][1]-1 == placesclicked[1][1]) or (placesclicked[0][0]-2 == placesclicked[1][0] and placesclicked[0][1]+1 == placesclicked[1][1]) or (placesclicked[0][0]+2 == placesclicked[1][0] and placesclicked[0][1]-1 == placesclicked[1][1]) or (placesclicked[0][0]+2 == placesclicked[1][0] and placesclicked[0][1]+1 == placesclicked[1][1]) or (placesclicked[0][0]-1 == placesclicked[1][0] and placesclicked[0][1]+2 == placesclicked[1][1]) or (placesclicked[0][0]-1 == placesclicked[1][0] and placesclicked[0][1]-2 == placesclicked[1][1]) or (placesclicked[0][0]+1 == placesclicked[1][0] and placesclicked[0][1]-2 == placesclicked[1][1]) or (placesclicked[0][0]+1 == placesclicked[1][0] and placesclicked[0][1]+2 == placesclicked[1][1])) and board[(placesclicked[1])[0]][(placesclicked[1])[1]][0] != "b":
                                print(piecesclicked)
                                print(placesclicked)
                                print(board[(placesclicked[1])[0]][(placesclicked[1])[1]][0])
                                board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0]
                                board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                piecesclicked = []
                                placesclicked = []
                                whitemove = not whitemove
                            else:
                                piecesclicked = []
                                placesclicked = []
                        elif (piecesclicked[0][1]) == "R":
                            for i in range(placesclicked[0][0]-1, -1, -1):
                                if board[i][placesclicked[0][1]][0] == "b":
                                   break
                                elif board[i][placesclicked[0][1]][0] == "w":
                                    possiblemoves.append((i, placesclicked[0][1]))
                                    break
                                else:
                                    possiblemoves.append((i, placesclicked[0][1]))
                            for i in range(placesclicked[0][0]+1, 8):
                                if board[i][placesclicked[0][1]][0] == "b":
                                   break
                                elif board[i][placesclicked[0][1]][0] == "w":
                                    possiblemoves.append((i, placesclicked[0][1]))
                                    break
                                else:
                                    possiblemoves.append((i, placesclicked[0][1]))
                            for i in range(placesclicked[0][1]-1, -1, -1):
                                if board[placesclicked[0][0]][i][0] == "b":
                                   break
                                elif board[placesclicked[0][0]][i][0] == "w":
                                    possiblemoves.append((placesclicked[0][0], i))
                                    break
                                else:
                                    possiblemoves.append((placesclicked[0][0], i))
                            for i in range(placesclicked[0][1]+1, 8):
                                if board[placesclicked[0][0]][i][0] == "b":
                                   break
                                elif board[placesclicked[0][0]][i][0] == "w":
                                    possiblemoves.append((placesclicked[0][0], i))
                                    break
                                else:
                                    possiblemoves.append((placesclicked[0][0], i))
                            if (placesclicked[1][0], placesclicked[1][1]) in possiblemoves:
                                board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0]
                                board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                piecesclicked = []
                                placesclicked = []
                                possiblemoves = []
                                whitemove = not whitemove
                            else:
                                piecesclicked = []
                                placesclicked = []
                                possiblemoves = []
                        elif (piecesclicked[0][1]) == "B":
                            for i, j in zip(range(placesclicked[0][0]-1, -1, -1), range(placesclicked[0][1]-1, -1, -1)):
                                if board[i][j][0] == "b":
                                    break
                                elif board[i][j][0] == "w":
                                    possiblemoves.append((i, j))
                                    break
                                else:
                                    possiblemoves.append((i, j))
                            for i, j in zip(range(placesclicked[0][0]-1, -1, -1), range(placesclicked[0][1]+1, 8)):
                                if board[i][j][0] == "b":
                                    break
                                elif board[i][j][0] == "w":
                                    possiblemoves.append((i, j))
                                    break
                                else:
                                    possiblemoves.append((i, j))     
                            for i, j in zip(range(placesclicked[0][0]+1, 8), range(placesclicked[0][1]-1, -1, -1)):
                                if board[i][j][0] == "b":
                                    break
                                elif board[i][j][0] == "w":
                                    possiblemoves.append((i, j))
                                    break
                                else:
                                    possiblemoves.append((i, j))        
                            for i, j in zip(range(placesclicked[0][0]+1, 8), range(placesclicked[0][1]+1, 8)):
                                if board[i][j][0] == "b":
                                    break
                                elif board[i][j][0] == "w":
                                    possiblemoves.append((i, j))
                                    break
                                else:
                                    possiblemoves.append((i, j))
                            if (placesclicked[1][0], placesclicked[1][1]) in possiblemoves:
                                board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0]
                                board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                piecesclicked = []
                                placesclicked = []
                                possiblemoves = []
                                whitemove = not whitemove
                            else:
                                piecesclicked = []
                                placesclicked = []
                                possiblemoves = []
                        elif piecesclicked[0][1] == "Q":
                            for i, j in zip(range(placesclicked[0][0]-1, -1, -1), range(placesclicked[0][1]-1, -1, -1)):
                                if board[i][j][0] == "b":
                                    break
                                elif board[i][j][0] == "w":
                                    possiblemoves.append((i, j))
                                    break
                                else:
                                    possiblemoves.append((i, j))
                            for i, j in zip(range(placesclicked[0][0]-1, -1, -1), range(placesclicked[0][1]+1, 8)):
                                if board[i][j][0] == "b":
                                    break
                                elif board[i][j][0] == "w":
                                    possiblemoves.append((i, j))
                                    break
                                else:
                                    possiblemoves.append((i, j))     
                            for i, j in zip(range(placesclicked[0][0]+1, 8), range(placesclicked[0][1]-1, -1, -1)):
                                if board[i][j][0] == "b":
                                    break
                                elif board[i][j][0] == "w":
                                    possiblemoves.append((i, j))
                                    break
                                else:
                                    possiblemoves.append((i, j))        
                            for i, j in zip(range(placesclicked[0][0]+1, 8), range(placesclicked[0][1]+1, 8)):
                                if board[i][j][0] == "b":
                                    break
                                elif board[i][j][0] == "w":
                                    possiblemoves.append((i, j))
                                    break
                                else:
                                    possiblemoves.append((i, j))
                            for i in range(placesclicked[0][0]-1, -1, -1):
                                if board[i][placesclicked[0][1]][0] == "b":
                                   break
                                elif board[i][placesclicked[0][1]][0] == "w":
                                    possiblemoves.append((i, placesclicked[0][1]))
                                    break
                                else:
                                    possiblemoves.append((i, placesclicked[0][1]))
                            for i in range(placesclicked[0][0]+1, 8):
                                if board[i][placesclicked[0][1]][0] == "b":
                                   break
                                elif board[i][placesclicked[0][1]][0] == "w":
                                    possiblemoves.append((i, placesclicked[0][1]))
                                    break
                                else:
                                    possiblemoves.append((i, placesclicked[0][1]))
                            for i in range(placesclicked[0][1]-1, -1, -1):
                                if board[placesclicked[0][0]][i][0] == "b":
                                   break
                                elif board[placesclicked[0][0]][i][0] == "w":
                                    possiblemoves.append((placesclicked[0][0], i))
                                    break
                                else:
                                    possiblemoves.append((placesclicked[0][0], i))
                            for i in range(placesclicked[0][1]+1, 8):
                                if board[placesclicked[0][0]][i][0] == "b":
                                   break
                                elif board[placesclicked[0][0]][i][0] == "w":
                                    possiblemoves.append((placesclicked[0][0], i))
                                    break
                                else:
                                    possiblemoves.append((placesclicked[0][0], i))
                            if (placesclicked[1][0], placesclicked[1][1]) in possiblemoves:
                                board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0]
                                board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                piecesclicked = []
                                placesclicked = []
                                possiblemoves = []
                                whitemove = not whitemove
                            else:
                                piecesclicked = []
                                placesclicked = []
                                possiblemoves = []
                        elif piecesclicked[0][1] == "K":
                            if (((placesclicked[0][0]+1 == placesclicked[1][0] or placesclicked[0][0]-1 == placesclicked[1][0]) and (placesclicked[0][1] == placesclicked[1][1] or placesclicked[0][1]+1 == placesclicked[1][1] or placesclicked[0][1]-1 == placesclicked[1][1])) or (placesclicked[0][0] == placesclicked[1][0] and (placesclicked[0][1]+1 == placesclicked[1][1] or placesclicked[0][1]-1 == placesclicked[1][1]))) and piecesclicked[1][0] != "b":
                                board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0]
                                board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                piecesclicked = []
                                placesclicked = []
                                whitemove = not whitemove
                            else:
                                piecesclicked = []
                                placesclicked = []         
                        else:
                            piecesclicked = []
                            placesclicked = []          
                    else:
                        piecesclicked = []
                        placesclicked = []
            """
            else:
                piecesclicked = []
                placesclicked = []
    getallmoves()
    pawnpromotion()            
    drawboard()
    drawpieces()
    #for r in board:
    #    print(r)
    p.display.flip()
