board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
mode = "startup"
turn = 1
counter1 = 0
counter2 = 0


def setup():
    size(1000,800)
def draw():
    global mode, turn, board, counter1, counter2
    background(120)
    x = 150
    y = 99
    if mode == "startup":
        background(66,102,227)
        fill(255)
        rect(290,440,130,80) #play
        rect(290,540,300,80) #instructions
        textSize(70)
        fill(0)
        text("Connect Four",300,100)
        textSize(50)
        text("Start",300,500)
        text("Instructions",300,600)
    if mode == "instructions":
        background(255)
        fill(255)
        rect(10,20,100,70)
        textSize(40)
        fill(0)
        text("Instructions",440,50)
        text("Back",10,70)
        textSize(20)
        text("Each player takes turns placing pieces in the board.",50,150)
        text("The objective is to get four pieces in a row.",50,200)
        text("The first player to get ten wins, wins the game!",50,250)
    if mode == "winscreen1":
        background(255)
        fill(255)
        rect(440,400,150,80)
        textSize(30)
        fill(0)
        text("winner player 1!",400,350)
        text("play again",440,450)
        board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    if mode == "winscreen2":
        background(255)
        fill(255)
        rect(440,400,150,80)
        textSize(30)
        fill(0)
        text("winner player 2!",400,350)
        text("play again",440,450)
        board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    if mode == "finalwinscreen1":
        background(255)
        fill(255)
        rect(420,440,260,100)
        fill(0)
        textSize(50)
        text("player 1 wins match!",100,80)
        text("play again",430,500)
        counter1 = 0
        counter2 = 0
        board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    if mode == "finalwinscreen2":
        background(255)
        fill(255)
        rect(420,440,260,100)
        fill(0)
        textSize(50)
        text("player 2 wins match!",100,80)
        text("play again",430,500)
        counter1 = 0
        counter2 = 0
        board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    if mode == "tiegame":
        background(255)
        fill(255)
        rect(440,450,170,80)
        fill(0)
        textSize(50)
        text("Tied game!",80,80)
        textSize(30)
        text("play again",450,500)
        board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

        
    
    
    if mode == "game":
        background(66,102,227)
        for row in board: #draw the game board
        
            for col in row:
                fill(230,250,50)
                rect(x,y,100,100)
                if col == 1:
                    fill(255,0,0)# red (p1)                
                elif col == 2: 
                    fill(0) #black (p2)
                else:
                    fill(255)
                 
                ellipse(x+50,y+50,100,100)
                x+=100
            x=150
            y+=100
        ellipse(70,700,100,100)
        if turn == 1: #player turn indicator
            fill(255,0,0)
            ellipse(70,700,100,100)
        elif turn == 2:
            fill(0)
            ellipse(70,700,100,100)
        fill(255)
        rect(340,40,50,50) #box
        rect(790,40,50,50) #box
        fill(0)
        textSize(40)
        text("player 1",150,80) #scoreboard p1
        text("player 2",600,80) #scoreboard p2
        text(counter1,350,80)
        text(counter2,800,80)
        if counter1 >= 10:  #check for final winner
            mode = "finalwinscreen1"
        elif counter2 >= 10: 
            mode = "finalwinscreen2"
   
        if board[0][0] != 0 and board[0][1] != 0  and board[0][2] != 0 and board[0][3] != 0  and board[0][4] != 0 and board[0][5] != 0 and board[0][6] != 0 and board[1][0] != 0 \
        and board[1][1] != 0 and board[1][2] != 0  and board[1][3] != 0  and board[1][4] != 0  and board[1][5] != 0  and board[1][6] != 0  and board[2][0] != 0 \
        and board[2][1] != 0  and board[2][2] != 0  and board[2][3] != 0  and board[2][4] != 0  and board[2][5] != 0  and board[2][6] != 0  and board[3][0] != 0 \
        and board[3][1] != 0 and board[3][2] != 0 and board[3][3] != 0  and board[3][4] != 0 and board[3][5] != 0 and board[3][6] != 0 and board[4][0] != 0 \
        and board[4][1] != 0 and board[4][2] != 0  and board[4][3] != 0  and board[4][4] != 0  and board[4][5] != 0  and board[4][6] != 0  and board[5][0] != 0 \
        and board[5][1] != 0  and board[5][2] != 0  and board[5][3] != 0  and board[5][4] != 0  and board[5][5] != 0  and board[5][6] != 0  and board[6][0] != 0 \
        and board[6][1] != 0  and board[6][2] != 0  and board[6][3] != 0  and board[6][4] != 0  and board[6][5] != 0  and board[6][6] != 0: #check for tie game
            mode = "tiegame"
            

def mousePressed():
    global mode, turn, counter1, counter2
    if mode == "game":
        if (150 <= mouseX and mouseX <= 850) and (100 <= mouseY and mouseY <= 800):
            col = (mouseX-150)/100 
            for row in range(6,-1,-1): #stacking
                if board[row][col] == 0:
                    board[row][col] = turn
                    break 
            if turn == 1: #player turn alternate
                turn = 2
            else: 
                turn = 1
            for n in range(4):  #horizontal win
                for row in range(7):
                    if board[row][0+n] == board[row][1+n] == board[row][2+n] == board[row][3+n] != 0:
                        print("winner!", "player", board[row][0+n])
                        if board[row][0+n] == 1:
                            counter1 += 1
                            mode = "winscreen1"
                        elif board[row][0+n] == 2:
                            counter2 += 1
                            mode = "winscreen2"
            for n in range(4): #vertical win
                for col in range(7):
                    if board[0+n][col] == board[1+n][col] == board[2+n][col] == board[3+n][col] != 0:
                        print("winner!", "player", board[0+n][col])
                        if board[0+n][col] == 1:
                            counter1 += 1
                            mode = "winscreen1"
                        elif board[0+n][col] == 2:
                            counter2 += 1
                            mode = "winscreen2"
            for row in range(4): #diagonal win
                for col in range(4):
                    if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] != 0:
                        print("diagonal", "player", board[row][col])
                        if board[row][col] == 1:
                            counter1 += 1
                            mode = "winscreen1"
                        elif board[row][col] == 2:
                            counter2 += 1
                            mode = "winscreen2"
            for row in range(4): #diagonal win
                for col in range(4):
                    if board[row][col] == board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3] != 0:
                        print("diagonal", "player", board[row][col])
                        if board[row][col] == 1:
                            counter1 += 1
                            mode = "winscreen1"
                        elif board[row][col] == 2:
                            counter2 += 1
                            mode = "winscreen2"
            for row in range(4): #diagonal win
                for col in range(4):
                    if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] != 0:
                        print("diagonal", "player", board[row][col])
                        if board[row][col] == 1:
                            counter1 += 1
                            mode = "winscreen1"
                        elif board[row][col] == 2:
                            counter2 += 1
                            mode = "winscreen2" 
            for row in range(4): #diagonal win
                for col in range(4):
                    if board[row][col] == board[row-1][col-1] == board[row-2][col-2] == board[row-3][col-3] != 0:
                        print("diagonal", "player", board[row][col])
                        if board[row-3][col-3] == 1:
                            counter1 += 1
                            mode = "winscreen1"
                        elif board[row+3][col-3] == 2:
                            counter2 += 1
                            mode = "winscreen2"
    
    
    
    if mode == "winscreen1": #play again
        if (440 <= mouseX <= 590) and (400 <= mouseY <= 480):
            mode = "game"
    if mode == "winscreen2": #play again
        if (440 <= mouseX <= 590) and (400 <= mouseY <= 480):
            mode = "game"
    if mode == "startup": #play
        if (290 <= mouseX <= 420) and (440 <= mouseY <= 520):
            mode = "game"
    if mode == "startup": #instructions
        if (290 <= mouseX <= 590) and (540 <= mouseY <= 620):
            mode = "instructions"
    if mode == "instructions": #back to main menu
        if (10 <= mouseX <= 110) and (20 <= mouseY <= 70):
            mode = "startup"
    if mode == "tiegame": #play again
        if (440 <= mouseX <= 610) and (450 <= mouseY <= 530):
            mode = "game"
    if mode == "finalwinscreen1": #play new game
        if (420 <= mouseX <= 680) and (440 <= mouseY <= 540):
            mode = "startup"
    if mode == "finalwinscreen2": #play new game
        if (420 <= mouseX <= 680) and (440 <= mouseY <= 540):
            mode = "startup"
