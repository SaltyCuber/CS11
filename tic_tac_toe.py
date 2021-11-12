import tkinter
from tkinter.constants import *
from math import inf # infinity

# constant values
tilecoords = {0:(78,63),1:(203,63),2:(328,63),3:(78,188),4:(203,188),5:(328,188),6:(78,313),7:(203,313),8:(328,313)} #gives the coordinates of the top left corner of each tile
lineColour = '#DDD'
P1 = -1
P2 = 1
window = tkinter.Tk()
player_input = -1


# these functions are used for game functionality, along with ai functionality
def gameOver(board):
    o = False
    try:
        board.index(0)
    except ValueError:
        o = True
    return o
def checkWin(b):
    w = 0
    wl = []
    if b[0]==b[1]==b[2] and b[0] != 0:
        w = b[0]
        wl.append([0,2])
    if b[3]==b[4]==b[5] and b[3] != 0:
        w = b[3]
        wl.append([3,5])
    if b[6]==b[7]==b[8] and b[6] != 0:
        w = b[6]
        wl.append([6,8])
    if b[0]==b[3]==b[6] and b[0] != 0:
        w = b[0]
        wl.append([0,6])
    if b[1]==b[4]==b[7] and b[1] != 0:
        w = b[1]
        wl.append([1,7])
    if b[2]==b[5]==b[8] and b[2] != 0:
        w = b[2]
        wl.append([2,8])
    if b[0]==b[4]==b[8] and b[0] != 0:
        w = b[0]
        wl.append([0,8])
    if b[2]==b[4]==b[6] and b[2] != 0:
        w = b[2]
        wl.append([2,6])
    return [w,wl]
def emptyCells(board):
    cells = []
    for i in range(len(board)):
        if board[i] == 0:
            cells.append(i)
    return cells
def validMove(board,move):
    if move == -1:
        return False
    else:
        return True if board[move] == 0 else False
def minimax(board, d, p):
    # minimax is a recursive algorithm that generates all possible moves,
    # then picks the best move based on the amount of possible wins vs possible losses, assuming the opponent picks the best possible move.
    # because minimax generates all possible moves, then picks the best path of moves,
    # with no restriction on how deep the ai can generate the ai becomes unbeatable, with the best outcome for the player being a draw.
    # however, since the human player goes first, it may be possible to beat the ai if you can play a perfect game (i haven't tested the algorithm enough to know for certain...)
    if p == P2:
        bestMove = [-1, -inf]
    else:
        bestMove = [-1, +inf]
    
    if d == 0 or checkWin(board)[0] != 0:
        score = checkWin(board)[0]
        return [-1, score]
    for c in emptyCells(board):
        board[c] = p
        score = minimax(board, d-1, -p) # this is what makes this function recursive
        board[c] = 0 # undo the move just made
        score[0] = c
        if p == P2:
            if score[1] > bestMove[1]: # if the current move is better than the best move, replace the best move with the current move
                bestMove = score
        else: # best possible move for the opponent to make is the lowest negative amount of points.
            if score[1] < bestMove[1]:
                bestMove = score
    return bestMove

# these functions are for interfacing with tkinter
def drawX(tilepos):
    # draws an x in the tile passed to the function
    global screen,game,b,lineColour,tilecoords
    x = tilecoords[tilepos][0]
    y = tilecoords[tilepos][1]
    screen.create_polygon(7+x,17+y,17+x,7+y,54+x,44+y,91+x,7+y,101+x,17+y,64+x,54+y,101+x,91+y,91+x,101+y,54+x,64+y,17+x,101+y,7+x,91+y,44+x,54+y,fill=lineColour)
    # offsets the positions of each point in the x shape by the top left corner in the tile selected.
def drawO(tilepos):
    # draws an o in the tile passed to the function
    global screen,game,b,lineColour,tilecoords
    x = tilecoords[tilepos][0]
    y = tilecoords[tilepos][1]
    screen.create_oval(12+x,12+y,96+x,96+y,outline=lineColour,width=12)
def drawWin(pos1, pos2):
    pass
def gety(ypos):
    # this gets the y coordinate of the square clicked on the game board
    # i did it this way because it's slightly faster than a big long chain of elif's for all 9 options, at worst you have 4 failed condition checks
    # as opposed to a max of 8 failed checks with a big chain of elif's (with an average of 2 failed condition checks as opposed to 4 with elif chain)
    if 45<=ypos<=170:
        out = 0
    elif 180<=ypos<=300:
        out = 1
    elif 310<=ypos<=430:
        out = 2
    else:
        out = -1 # click is outside of game board
    return out
def getorigin(eventorigin):
    # whenever a click happens this code runs
    global GameType,turn,b,player_input
    x = eventorigin.x
    y = eventorigin.y
    # handle click event here
    # detect which square, if any, on the board was clicked        
    if 70<=x<=190:
        clicked_x = 0
        clicked_y = gety(y)
    elif 200<=x<=314:
        # yes ik elif chains are gross but i didn't feel like reading through syntax documentation to figure out how i'm supposed to do this with pattern matching...
        clicked_x = 1
        clicked_y = gety(y)
    elif 325<=x<=450:
        clicked_x = 2
        clicked_y = gety(y)
    else:
        clicked_x = -1 # click was outside of game board
        clicked_y = gety(y)            
            
    # make sure click is in the game board
    if clicked_x == -1 or clicked_y == -1:
        player_input = -1
    else:
        # check if clicked tile is empty
        clicked_tile = clicked_y * 3 + clicked_x
        if b[clicked_tile] == 0:
            player_input = clicked_tile
def initGame():
    global game,screen,p1TurnIndicator,p2TurnIndicator,lineColour
    # load in all objects needed for the game
    bgColour = '#022'
    game = tkinter.Tk()
    game.bind("<Button 1>",getorigin)
    screen = tkinter.Canvas(game,bg=bgColour,height=500,width=500)
    #draw lines on the canvas to make the game board
    screen.create_polygon(187,63,202,63,202,421,187,421,fill=lineColour)
    screen.create_polygon(312,421,327,421,327,63,312,63,fill=lineColour)
    screen.create_polygon(78,172,78,187,436,187,436,172,fill=lineColour)
    screen.create_polygon(436,312,436,297,78,297,78,312,fill=lineColour)
    #draw circles to make the board lines have rounded ends
    screen.create_oval(70,186,85,172,fill=lineColour,width=0)
    screen.create_oval(429,172,444,186,fill=lineColour,width=0)
    screen.create_oval(70,311,85,297,fill=lineColour,width=0)
    screen.create_oval(429,297,444,311,fill=lineColour,width=0)
    screen.create_oval(187,70,201,55,fill=lineColour,width=0)
    screen.create_oval(187,414,201,429,fill=lineColour,width=0)
    screen.create_oval(326,70,312,55,fill=lineColour,width=0)
    screen.create_oval(326,429,312,414,fill=lineColour,width=0)
    #game status text
    P2text = "Player 2's Turn" if GameType == "2P" else "Computer's Turn"
    p1TurnIndicator = screen.create_text(250,470,fill='#0F0',text='Player 1\'s Turn')
    p2TurnIndicator = screen.create_text(250,470,fill='#F00',state=HIDDEN,text=P2text)
    screen.pack()
    game.update()
    startGame()
def init_1P_game():
    global GameType,turn,b,game
    GameType = "1P"
    turn = P1
    b = [0,0,0,0,0,0,0,0,0]
    try:
        game.destroy()
    except Exception:
        pass
    initGame()
def init_2P_game():
    global GameType,turn,b,game
    GameType = "2P"
    turn = P1 
    b = [0,0,0,0,0,0,0,0,0]
    try:
        game.destroy()
    except Exception:
        pass
    initGame()
def switchTurn():
    # all this does is change the turn indicator on the bottom of the screen
    global turn,p1TurnIndicator,p2TurnIndicator
    if turn == P1:
        screen.itemconfigure(p1TurnIndicator,state=NORMAL)
        screen.itemconfigure(p2TurnIndicator,state=HIDDEN)
    else:
        screen.itemconfigure(p2TurnIndicator,state=NORMAL)
        screen.itemconfigure(p1TurnIndicator,state=HIDDEN)
def drawWinLines(wl, p):
    # takes in a list of lines to draw, then draws them
    ctile = {0:(132,117),1:(257,117),2:(382,117),3:(132,242),4:(257,242),5:(382,242),6:(132,367),7:(257,367),8:(382,367)} # center pos of each tile
    # attatched is a png image that i used for reference to get all the seemingly arbitrary pixel coordinates
    for i in wl:
        spos = ctile[i[0]]
        epos = ctile[i[1]]
        colour = '#F00' if p == P2 else '#0F0'
        screen.create_line(spos[0],spos[1],epos[0],epos[1],fill=colour,width=10)

# this is the main game loop
def startGame():
    global b,turn,GameType,p1TurnIndicator,p2TurnIndicator,game,screen,player_input
    while checkWin(b)[0] == 0 and not gameOver(b):
        if GameType != "1P" or turn != P2:
            player_input = -1
            # wait for user to input a valid move
            while not validMove(b,player_input):
                while player_input == -1:
                    try:
                        game.update()
                    except tkinter.TclError:
                        # this error only happens if the user closes the game screen while the game is waiting for input
                        return
            # player_input is known to be a valid move
            # put move in board, draw game piece on board, win detection will be done by the while loop.
            b[player_input] = turn
            if turn == P1:
                drawX(player_input)
            else:
                drawO(player_input)
            game.update()
            turn = -turn
            switchTurn()
        
        else:
            # do ai move here
            d = len(emptyCells(b))
            if d == 0 or checkWin(b)[0] != 0:
                return
            else:
                move = minimax(b, d, P2)
                if move[0] == -1:
                    return
                b[move[0]] = P2
                drawO(move[0])
                turn = -turn
                switchTurn()
                game.update()

    # draw win line(s), put win text on bottom of screen
    screen.itemconfigure(p2TurnIndicator,state=HIDDEN)
    screen.itemconfigure(p1TurnIndicator,state=HIDDEN)
    if checkWin(b)[0] == P1:
        screen.create_text(250,470,fill='#0F0',text='Player 1 Wins!')
        drawWinLines(checkWin(b)[1], P1)
    elif checkWin(b)[0] == P2:
        if GameType == "1P":
            screen.create_text(250,470,fill='#F00',text='Computer Wins!')
            drawWinLines(checkWin(b)[1], P2)
        else:
            screen.create_text(250,470,fill='#F00',text='Player 2 Wins!')
            drawWinLines(checkWin(b)[1], P2)
    else:
        screen.create_text(250,470,fill='#FF0',text='Draw!')

two_player = tkinter.Button(window,text = "Start 2 Player Game",command = init_2P_game)
one_player = tkinter.Button(window,text = "Start game against Computer",command = init_1P_game)
two_player.pack()
one_player.pack()
window.mainloop()