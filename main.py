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
                if whitemove == True:
                    if(piecesclicked[0][0]) == "w":
                        if(piecesclicked[0][1]) == "P":
                            if placesclicked[0][0] == 6:
                                if (placesclicked[0][0]-2 == placesclicked[1][0] or placesclicked[0][0]-1 == placesclicked[1][0]) and placesclicked[0][1] == placesclicked[1][1] and board[(placesclicked[1])[0]][(placesclicked[1])[1]] == "..":
                                    board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0]
                                    board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                    piecesclicked = []
                                    placesclicked = []
                                    whitemove = not whitemove
                                else:
                                    piecesclicked = []
                                    placesclicked = []
                            else:
                                if (placesclicked[0][0]-1 == placesclicked[1][0] and placesclicked[0][1] == placesclicked[1][1]) and board[(placesclicked[1])[0]][(placesclicked[1])[1]] == "..":    
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
                elif whitemove == False:
                    if(piecesclicked[0][0]) == "b":
                        if(piecesclicked[0][1]) == "P":
                            if placesclicked[0][0] == 1:
                                if (placesclicked[0][0]+2 == placesclicked[1][0] or placesclicked[0][0]+1 == placesclicked[1][0]) and placesclicked[0][1] == placesclicked[1][1] and board[(placesclicked[1])[0]][(placesclicked[1])[1]] == "..":
                                    board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0]
                                    board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".."
                                    piecesclicked = []
                                    placesclicked = []
                                    whitemove = not whitemove
                                else:
                                    piecesclicked = []
                                    placesclicked = []        
                            else:
                                if (placesclicked[0][0]+1 == placesclicked[1][0] and placesclicked[0][1] == placesclicked[1][1]) and board[(placesclicked[1])[0]][(placesclicked[1])[1]] == "..":    
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
            else:
                piecesclicked = []
                placesclicked = []
    drawboard()
    drawpieces()
    p.display.flip()
