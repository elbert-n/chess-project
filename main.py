import pygame as p
p.init() #init pygame
global whitemove #global variable to see if it's white turn to move
whitemove = True #white moves first
running = True 
WHITE = (255, 255, 255) #colors
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255,0,0)
BGCOLOUR = (2, 7, 93)
width = height = 600 #size of screen
SIZE = (width, height)
square_size = width // 8 #chess board is 8x8
board = [[".." for i in range(8)] for j in range(8)] #create blank board which is 8x8 array filled with blank
imagepieces = {} #create dictionary that has piece name associated with image
validmoves = [] #legal moves
possiblemoves = [] #all moves including pseudolegal moves 
piecesclicked = [] #the pieces that the user clicked
placesclicked = [] #the places the user clicked
pieceslog = [] #past history of piece moves
log = [] #past history of moves
movecount = 0 
wkinglocation = (7, 4) #init wkinglocation so it's defined
bkinglocation = (0, 4) #init bkinglocation so it's defined
state_menu = 0 #game states
state_game = 1
state_help = 2
state_quit = 3
state = state_menu
menuFont = p.font.SysFont("calibri", 42) #initialize fonts
titleFont = p.font.SysFont("calibri", 60)
textFont = p.font.SysFont("calibri", 25)
miniFont = p.font.SysFont("calibri", 20)
#setting up the board
def initboard():
    global board
    board[0][0] = "bR" #black backrow pieces
    board[0][1] = "bN"
    board[0][2] = "bB"
    board[0][3] = "bQ"
    board[0][4] = "bK"
    board[0][5] = "bB"
    board[0][6] = "bN"
    board[0][7] = "bR"
    for i in range(8): #pawns
        board[1][i] = "bP"
        board[6][i] = "wP"
    board[7][0] = "wR" #white backrow pieces
    board[7][1] = "wN"
    board[7][2] = "wB"
    board[7][3] = "wQ"
    board[7][4] = "wK"
    board[7][5] = "wB"
    board[7][6] = "wN"
    board[7][7] = "wR"

def initimages(): #initialize images in our dictionary
    pieces = ["bP", "bR", "bN", "bB", "bQ", "bK", "wP", "wR", "wN", "wB", "wQ", "wK"]
    for piece in pieces:
        imagepieces[piece] = p.transform.scale(p.image.load(piece+".png"), (square_size, square_size))

def endgame(): #function to check if the game ended
    stalematetext = textFont.render("The game has ended as a stalemate in " + str(movecount) + "moves.", 1, RED)
    endtext = textFont.render("Press E to exit or R to restart.", 1, RED)
    if wcheckmate:
        wcheckmatetext = textFont.render("White has won the game by checkmate in " + str(movecount) + " moves.", 1, RED) #tell the user it's checkmate
        screen.blit(wcheckmatetext, (50, height//2-25))
        screen.blit(endtext, (50,height//2+25))
    elif bcheckmate:
        bcheckmatetext = textFont.render("Black has won the game by checkmate in " + str(movecount) + " moves.", 1, RED)
        screen.blit(bcheckmatetext, (50, height//2-25))
        screen.blit(endtext, (50,height//2+25))
    elif stalemate:
        screen.blit(stalematetext, (50, height))
        screen.blit(endtext, (50,height//2+25))

def drawMenu(screen, button, pos, state): #code taken from Ms. Bokhari Pong example
    blockWidth = width//3
    blockHeight = height//7
    rectList = [p.Rect(blockWidth, blockHeight+50, blockWidth, blockHeight), # game choice
                p.Rect(blockWidth, 3*blockHeight+50, blockWidth, blockHeight), #help choice
                p.Rect(blockWidth, 5*blockHeight+50, blockWidth, blockHeight)] # quite choice
    stateList = [state_game, state_help, state_quit]
    titleList = ["Play Game", "Help", "Quit Game"]
    p.draw.rect(screen, BGCOLOUR, (0, 0, width, height))
    titletext = titleFont.render("CHESS", 1, WHITE)
    screen.blit(titletext, (width//2-75, 15))
    for i in range(len(rectList)):
        rect = rectList[i] # get the current Rect
        p.draw.rect(screen, GRAY, rect)  # draw the Rect
        text = menuFont.render(titleList[i] , 1, BLACK)	# make the font`
        textWidth, textHeight = menuFont.size(titleList[i]) # get the font size
        useW = (blockWidth - textWidth)//2  #use for centering
        useH = (blockHeight - textHeight)//2
        # getting a centered Rectangle
        textRect = p.Rect(rect[0] + useW, rect[1] + useH, textWidth, textHeight)
        screen.blit(text, textRect)	# draw to screen
        
        if rect.collidepoint(pos):
            p.draw.rect(screen, BLACK, rect, 2)
            if button == 1:
                state = stateList[i]
    return state

def drawHelp(screen, button, state): 
    p.draw.rect(screen, BGCOLOUR, (0, 0, width, height))
    titlehelptext = titleFont.render("Help and Credits", 1, WHITE) #render text
    creditstext1 = miniFont.render("Created by Elbert", 1, WHITE)
    creditstext2 = miniFont.render("Credit to Ms. Bokhari for Menu Code", 1, WHITE)
    creditstext3 = miniFont.render("Credit to Dongtai for helping me with checkmates", 1, WHITE)
    creditstext4 = miniFont.render("Credit to stackoverflow for setting up vscode + general help ", 1, WHITE)
    creditstext5 = miniFont.render("Eddie Sharick has a great series on youtube on programming chess", 1, WHITE)
    controltext1 = miniFont.render("Press E to exit at anytime", 1, WHITE)
    controltext2 = miniFont.render("Press Z to undo moves", 1, WHITE)
    controltext3 = miniFont.render("Press M3 to go back to the menu", 1, WHITE)
    screen.blit(titlehelptext, (100, 50)) #draw text, maybe this should be done in a for loop...
    screen.blit(creditstext1, (25, 150))
    screen.blit(creditstext2, (25, 210))
    screen.blit(creditstext3, (25, 270))
    screen.blit(creditstext4, (25, 330))
    screen.blit(creditstext5, (25, 390))
    screen.blit(controltext1, (25, 450))
    screen.blit(controltext2, (25, 510))
    screen.blit(controltext3, (25, 570))
    if button == 3: #go back to main menu if m3 is pressed
        state = state_menu
    return state

def drawpieces(): #go through the 8x8 array
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece != '..': #if there's a piece draw it
                screen.blit(imagepieces[piece], p.Rect(c*square_size, r*square_size, square_size, square_size))

def drawboard(): #draw the board
    colors = [WHITE, GRAY] #color list for squares
    for r in range(8):
        rindex =  r % 2 #whether the first square of the row is white or black
        for c in range (8):
            square = (r*square_size, c*square_size, square_size, square_size) #draw the square
            p.draw.rect(screen, colors[rindex], square)
            rindex = ((rindex+1) % 2) #the next square in the row, ie. the next column will swap colors

def getpawnmoves(r, c):
    if whitemove == True and board[r][c][0] == "w": #white pawn moves
        if r == 6 and board[r-2][c] == ".." and board[r-1][c] == "..": #pawn moves two squares up if it's on the second row (6th row in array)
            possiblemoves.append(((r,c), (r-2, c)))
        if board[r-1][c] == "..": #pawn moves up one square if the square is empty
            possiblemoves.append(((r, c), (r-1,c)))
        if c-1 >= 0: #captures to the left only if black piece
            if board[r-1][c-1][0] == "b":
                possiblemoves.append(((r,c), (r-1,c-1)))
        if c+1 <= 7: #captures to the right only if black piece
            if board[r-1][c+1][0] == "b":
                possiblemoves.append(((r,c), (r-1,c+1)))
    elif whitemove == False and board[r][c][0] == "b": #black pawn moves
        if r == 1 and board[r+2][c] == ".." and board[r+1][c] == ".." : #pawn moves two squares down if it's on the seventh row (1st row in array
            possiblemoves.append(((r,c), (r+2,c)))
        if board[r+1][c] == "..": #pawn moves up one square if the square is empty
            possiblemoves.append(((r, c), (r+1, c)))
        if c-1 >= 0:
            if board[r+1][c-1][0] == "w": #captures to the left only if white piece
                possiblemoves.append(((r,c), (r+1,c-1)))
        if c+1 <= 7:
            if board[r+1][c+1][0] == "w": #captures to the right only if white piece
                possiblemoves.append(((r,c), (r+1, c+1)))

def checkbounds(r, c): #check if r and c are within the board
    if (r < 0 or r > 7) or (c < 0 or c> 7):
        return False
    else:
        return True

def getknightmoves(r, c): #generate possible knight moves
    if whitemove == True and board[r][c][0] == "w": #white knight moves
        for i in range(8): #knight has 8 possible L shapes that it can go to 
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
            if checkbounds(r+roffset, c+coffset): #make sure that it's within bounds, so not out of bounds array
                if board[r+roffset][c+coffset][0] != "w": #as long as it's not a teammate piece it can move
                    possiblemoves.append(((r,c), (r+roffset, c+coffset)))
    elif whitemove == False and board[r][c][0] == "b": #black knight moves
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
                if board[r+roffset][c+coffset][0] != "b": #as long as it's not a teammate piece it can move
                    possiblemoves.append(((r,c), (r+roffset, c+coffset)))

def getrookmoves(r, c): #generate possible rook moves
    if whitemove == True and board[r][c][0] == "w": #white rook moves
        for i in range(r-1, -1, -1): #possible moves above
            if board[i][c][0] == "w": #break immediately if teammate piece
                break
            elif board[i][c][0] == "b": #you can capture the piece, then break
                possiblemoves.append(((r, c), (i, c)))
                break
            else: #otherwise you're good
                possiblemoves.append(((r, c), (i, c)))
        for i in range(r+1, 8): #possible moves below
            if board[i][c][0] == "w": 
                break
            elif board[i][c][0] == "b": 
                possiblemoves.append(((r, c), (i, c)))
                break
            else: #otherwise you're good
                possiblemoves.append(((r, c), (i, c)))
        for i in range(c-1, -1, -1): #possible moves to the left
            if board[r][i][0] == "w":
                break
            elif board[r][i][0] == "b":
                possiblemoves.append(((r, c), (r, i)))
                break
            else:
                possiblemoves.append(((r, c), (r, i)))
        for i in range(c+1, 8): #possible moves to the right
            if board[r][i][0] == "w":
                break
            elif board[r][i][0] == "b":
                possiblemoves.append(((r, c), (r, i)))
                break
            else:
                possiblemoves.append(((r, c), (r, i)))
    elif whitemove == False and board[r][c][0] == "b": #black moves
        for i in range(r-1, -1, -1): #moves above
            if board[i][c][0] == "b":
                break
            elif board[i][c][0] == "w":
                possiblemoves.append(((r, c), (i, c)))
                break
            else:
                possiblemoves.append(((r, c), (i, c)))
        for i in range(r+1, 8): #moves below
            if board[i][c][0] == "b":
                break
            elif board[i][c][0] == "w":
                possiblemoves.append(((r, c), (i, c)))
                break
            else:
                possiblemoves.append(((r, c), (i, c)))
        for i in range(c-1, -1, -1): #moves left
            if board[r][i][0] == "b":
                break
            elif board[r][i][0] == "w":
                possiblemoves.append(((r, c), (r, i)))
                break
            else:
                possiblemoves.append(((r, c), (r, i)))
        for i in range(c+1, 8): #moves right
            if board[r][i][0] == "b":
                break
            elif board[r][i][0] == "w":
                possiblemoves.append(((r, c), (r, i)))
                break
            else:
                possiblemoves.append(((r, c), (r, i)))

def getbishopmoves(r, c): #bishop moves
    if whitemove == True and board[r][c][0] == "w": #top left diagonal
        for i, j in zip(range(r-1, -1, -1), range(c-1, -1, -1)):
            if board[i][j][0] == "w": #break right away if it's a white piece
                break
            elif board[i][j][0] == "b": #break after a black piece
                possiblemoves.append(((r, c), (i, j))) 
                break
            else:
                possiblemoves.append(((r, c), (i, j)))
        for i, j in zip(range(r-1, -1, -1), range(c+1, 8)): #top right diagonal
            if board[i][j][0] == "w":
                break
            elif board[i][j][0] == "b":
                possiblemoves.append(((r, c), (i, j)))
                break
            else:
                possiblemoves.append(((r, c), (i, j)))     
        for i, j in zip(range(r+1, 8), range(c-1, -1, -1)): #bottom left diagonal
            if board[i][j][0] == "w":
                break
            elif board[i][j][0] == "b":
                possiblemoves.append(((r, c), (i, j)))
                break
            else:
                possiblemoves.append(((r, c), (i, j)))
        for i, j in zip(range(r+1, 8), range(c+1, 8)): #bottom right diagonal
            if board[i][j][0] == "w":
                break
            elif board[i][j][0] == "b":
                possiblemoves.append(((r, c), (i, j)))
                break
            else:
                possiblemoves.append(((r, c), (i, j)))
    if whitemove == False and board[r][c][0] == "b": #black bishop moves
        for i, j in zip(range(r-1, -1, -1), range(c-1, -1, -1)): #top left diagonal
            if board[i][j][0] == "b":
                break
            elif board[i][j][0] == "w":
                possiblemoves.append(((r, c), (i, j)))
                break
            else:
                possiblemoves.append(((r, c), (i, j)))
        for i, j in zip(range(r-1, -1, -1), range(c+1, 8)): #top right diagonal
            if board[i][j][0] == "b":
                break
            elif board[i][j][0] == "w":
                possiblemoves.append(((r, c), (i, j)))
                break
            else:
                possiblemoves.append(((r, c), (i, j)))     
        for i, j in zip(range(r+1, 8), range(c-1, -1, -1)): #bottom left diagonal
            if board[i][j][0] == "b":
                break
            elif board[i][j][0] == "w":
                possiblemoves.append(((r, c), (i, j)))
                break
            else:
                possiblemoves.append(((r, c), (i, j)))       
        for i, j in zip(range(r+1, 8), range(c+1, 8)): #bottom right diagonal
            if board[i][j][0] == "b":
                break
            elif board[i][j][0] == "w":
                possiblemoves.append(((r, c), (i, j)))
                break
            else:
                possiblemoves.append(((r, c), (i, j)))

def getqueenmoves(r, c): #the queen is basically a bishop and rook together
    getbishopmoves(r, c)
    getrookmoves(r, c)

def getkingmoves(r, c): #generate possible king moves
    if whitemove == True and board[r][c][0] == "w": #white king moves
        for i in range(8): #cycle through offsets all the squares around the king
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
            if checkbounds(r+roffset, c+coffset): #make sure that it's in bounds
                if board[r+roffset][c+coffset][0] != "w":
                    possiblemoves.append(((r,c), (r+roffset, c+coffset)))
    elif whitemove == False and board[r][c][0] == "b": #black king moves
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
                    possiblemoves.append(((r,c), (r+roffset, c+coffset)))


def getallmoves(): 
    global possiblemoves
    possiblemoves = []
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
                global wkinglocation
                global bkinglocation
                if piece[0] == "w":
                    wkinglocation = (r, c)
                else:
                    bkinglocation = (r, c)
    return possiblemoves

def isunderattack(r, c):
    global whitemove
    whitemove = not whitemove #switch to enemy turn to see enemy move perspectives
    enemymoves = getallmoves() #get all the moves when its the enemy move
    whitemove = not whitemove #switch back so it doesn't mess up turn order
    for move in enemymoves: #in all the enemy moves
        if move[1] == (r, c): #do any of them end up attacking the r,c we want
            #print(move[0]) #attacker
            return True
    return False

def incheck(): #use the is under attack fcn to determine whether or not we're in check
    getallmoves()
    if whitemove == True: #check if wking is in check
        if isunderattack(wkinglocation[0], wkinglocation[1]) == True: #if the wking gets under attack then it's check
            #print("im in check w")
            return True
        else:
            return False
    else:
        if isunderattack(bkinglocation[0], bkinglocation[1]) == True: #if the bking gets under attack then it's check
            #print("im in check b")
            return True
        else:
            return False

def getvalidmoves():
    global validmoves #make it a global variable so we can access
    validmoves = getallmoves() #first get all the possible moves, we'll trim the list
    #print(len(validmoves))
    for i in range(len(validmoves)-1, -1, -1): #cycle through the validmoves
        #print(validmoves[i])
        removemove = False #start as false, we'll turn to true if we remove a piece
        temppiece = board[validmoves[i][1][0]][validmoves[i][1][1]] #temp piece
        board[validmoves[i][1][0]][validmoves[i][1][1]] = board[validmoves[i][0][0]][validmoves[i][0][1]] #make the move
        board[validmoves[i][0][0]][validmoves[i][0][1]] = ".."
        if incheck(): #if the move caused us to be in check then it must be an illegal move
            removemove = True #we should remove the move now
            #print("removed...")
        board[validmoves[i][0][0]][validmoves[i][0][1]] = board[validmoves[i][1][0]][validmoves[i][1][1]] #undo the move
        board[validmoves[i][1][0]][validmoves[i][1][1]] = temppiece
        if removemove: #if we removemove is true, then we should remove it
            validmoves.remove(validmoves[i]) #remove the item from the list
    return validmoves #send the narrowed down list back

def pawnpromotion():
    for c in range(8):
        if board[7][c] == "bP": #if a black pawn reaches the opposite rank it promotes
            board[7][c] = "bQ"
        if board[0][c] == "wP": #if a white pawn reaches the opposite rank it promotes
            board[0][c] = "wQ"

def ischeckmate():
    if len(validmoves) == 0: #if there are no valid moves, ie. moves that don't end with the king being in check then it must be stalemate or checkmate
        if whitemove:
            if incheck():
                global bcheckmate
                bcheckmate = True #if white has no legal moves then black checkmated him
            else:
                global stalemate
                stalemate = True #stalemate if he's not in check but no legal moves
        else:
            if incheck():
                global wcheckmate
                wcheckmate = True #if black has no legal moves then white checkmated him
            else:
                stalemate = True #stalemate if he's not in check but no legal moves
    else:
        bcheckmate = False #if length of valid moves is not 0 then it's not checkmate
        wcheckmate = False 
        stalemate = False 

initboard() #init board
initimages() #init images for the pieces
#print(p.font.get_fonts())
screen = p.display.set_mode(SIZE)
pos = (0, 0) #set a pos so we don't get an error
button = 0
while running:
    for evnt in p.event.get():
        if evnt.type == p.QUIT: #quit program if running is false
            running = False
        if evnt.type == p.MOUSEBUTTONDOWN: #if mouse button down
            pos = p.mouse.get_pos() #get pos
            button = evnt.button #get mouse button pressed
            if state == state_game: #if we're in the game
                posx = pos[0]//square_size #getting the row
                posy = pos[1]//square_size #gettin the column
                pieceselected = board[posy][posx] #get the piece on the board
                piecesclicked.append(pieceselected) #put the pieces or blank space clicked onto a list
                placesclicked.append((posy, posx)) #put the location of where you clicked onto a list
        if len(placesclicked) == 2: #when that list gets to length 2 ie, user clicked twice they probably want to make a move
            print(piecesclicked)
            if(piecesclicked[0] != ".."): #if there is a piece there
                if ((placesclicked[0][0], placesclicked[0][1]), (placesclicked[1][0], placesclicked[1][1])) in validmoves: #if it's in valid moves
                    board[(placesclicked[1])[0]][(placesclicked[1])[1]] = piecesclicked[0] #move the piece to the square
                    board[(placesclicked[0])[0]][(placesclicked[0])[1]] = ".." #make this square blank
                    log.append(((placesclicked[0][0], placesclicked[0][1]), (placesclicked[1][0], placesclicked[1][1]))) #put into log for undo move
                    pieceslog.append((piecesclicked[0], piecesclicked[1])) #put into pieceslog to undo move
                    piecesclicked = [] #reset user clicks
                    placesclicked = []
                    possiblemoves = [] #reset possible moves
                    whitemove = not whitemove #switch turns
                    movecount += 1 #turn count up
                    #print(log)
                    #print(pieceslog)
                else: #user try again
                    piecesclicked = []
                    placesclicked = []
            else: #user try again
                piecesclicked = []
                placesclicked = []
        if evnt.type == p.KEYDOWN:
            if evnt.key == p.K_r and (stalemate == True or wcheckmate == True or bcheckmate == True): #restart the game if it has ended
                board[0][0] = "bR" #reset black backrow pieces
                board[0][1] = "bN"
                board[0][2] = "bB"
                board[0][3] = "bQ"
                board[0][4] = "bK"
                board[0][5] = "bB"
                board[0][6] = "bN"
                board[0][7] = "bR"
                for i in range(8): #reset pawns + middle of the board
                    board[1][i] = "bP"
                    board[2][i] = ".."
                    board[3][i] = ".."
                    board[4][i] = ".."
                    board[5][i] = ".."
                    board[6][i] = "wP"
                board[7][0] = "wR" #reset white backrow pieces
                board[7][1] = "wN"
                board[7][2] = "wB"
                board[7][3] = "wQ"
                board[7][4] = "wK"
                board[7][5] = "wB"
                board[7][6] = "wN"
                board[7][7] = "wR"
                whitemove = True #white turn to move again
                piecelog = [] #reset the logs so it doesn't carry over from game to game
                log = []
                movecount = 0
            if evnt.key == p.K_z: #undo move
                if movecount > 0: #a move must have been made or else we get out of bounds
                    board[log[movecount-1][0][0]][log[movecount-1][0][1]] = pieceslog[movecount-1][0] #change back the square we move from
                    board[log[movecount-1][1][0]][log[movecount-1][1][1]] = pieceslog[movecount-1][1] #change back the square we move to
                    whitemove = not whitemove #change back turn
                    movecount -= 1 #take back a move, so move counter doesn't get messed up
                    del log[movecount] #take out log entry so it doesn't mess up next one
                    del pieceslog[movecount]
                    #print(log)
                    #print(pieceslog)
            if evnt.key == p.K_e: #e to exit the game
                running = False
    #print(whitemove)
    #incheck()
    #getallmoves()
    #print(state)
    if state == state_menu:
        state = drawMenu(screen, button, pos, state)
    elif state == state_game:
        validmoves=[]
        getvalidmoves()
        ischeckmate()
        pawnpromotion()            
        drawboard()
        drawpieces()
        endgame()
    elif state == state_help:
        state = drawHelp(screen, button, state)
    elif state == state_quit:
        running = False
    #for r in board:
    #    print(r)
    p.display.flip()
