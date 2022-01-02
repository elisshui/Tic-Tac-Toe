import pygame
import sys

#-----------------checking winner and drawing winner's line--------------------------
def findWinner():
    WinPlayer = None
    #--------------defining colors-------------
    green = (125,225,100)
    blue = (25,75,125)
    WinnerLineColor = (207,23,10)
    #------------------------------------------
    #TopRow
    if ((squares[0][0])[1] == (squares[0][1])[1] == (squares[0][2])[1]) and ((squares[0][0])[1] != (225,225,225) and (squares[0][1])[1] != (225,225,225) and (squares[0][2])[1] != (225,225,225)): #TopRow
        colorWin = ((squares[0][0])[1])
        if colorWin == green:
            WinPlayer = "green"
            pygame.draw.line(gridBckgrd, (WinnerLineColor), (10, 83), (488, 83), 5) 
        elif colorWin == blue:
            WinPlayer = "blue"
            pygame.draw.line(gridBckgrd, (WinnerLineColor), (10, 83), (488, 83), 5) 
    #MidRow
    if ((squares[1][0])[1] == (squares[1][1])[1] == (squares[1][2])[1]) and ((squares[1][0])[1] != (225,225,225) and (squares[1][1])[1] != (225,225,225) and (squares[1][2])[1] != (225,225,225)): #MidRow
        colorWin = ((squares[1][0])[1])    
        if colorWin == green:
            WinPlayer = "green"
            pygame.draw.line(gridBckgrd, (WinnerLineColor), (10, 83+166), (488, 83+166), 5) 
        elif colorWin == blue:
            WinPlayer = "blue"
            pygame.draw.line(gridBckgrd, (WinnerLineColor), (10, 83+166), (488, 83+166), 5)
    #BottRow
    if ((squares[2][0])[1] == (squares[2][1])[1] == (squares[2][2])[1]) and ((squares[2][0])[1] != (225,225,225) and (squares[2][1])[1] != (225,225,225) and (squares[2][2])[1] != (225,225,225)): #BottRow
        colorWin = ((squares[2][0])[1])
        if colorWin == green:
            WinPlayer = "green" 
            pygame.draw.line(gridBckgrd, (WinnerLineColor), (10, 83+(166*2)), (488, 83+(166*2)), 5)
        elif colorWin == blue:
            WinPlayer = "blue"
            pygame.draw.line(gridBckgrd, (WinnerLineColor), (10, 83+(166*2)), (488, 83+(166*2)), 5)
    #LeftCol
    if ((squares[0][0])[1] == (squares[1][0])[1] == (squares[2][0])[1]) and ((squares[0][0])[1] != (225,225,225) and (squares[1][0])[1] != (225,225,225) and (squares[2][0])[1] != (225,225,225)): #LeftCol
        colorWin = ((squares[0][0])[1])
        if colorWin == green:
            WinPlayer = "green"
            pygame.draw.line(gridBckgrd, (WinnerLineColor), (83, 10), (83, 488), 5) 
        elif colorWin == blue:
            WinPlayer = "blue"
            pygame.draw.line(gridBckgrd, (WinnerLineColor), (83, 10), (83, 488), 5) 
    #MidCol
    if ((squares[0][1])[1] == (squares[1][1])[1] == (squares[2][1])[1]) and ((squares[0][1])[1] != (225,225,225) and (squares[1][1])[1] != (225,225,225) and (squares[2][1])[1] != (225,225,225)): #MidCol
        colorWin = ((squares[0][1])[1])        
        if colorWin == green:
            WinPlayer = "green"
            pygame.draw.line(gridBckgrd, (WinnerLineColor), (83+166, 10), (83+166, 488), 5) 
        elif colorWin == blue:
            WinPlayer = "blue"
            pygame.draw.line(gridBckgrd, (WinnerLineColor), (83+166, 10), (83+166, 488), 5) 
    #RightCol
    if ((squares[0][2])[1] == (squares[1][2])[1] == (squares[2][2])[1]) and ((squares[0][2])[1] != (225,225,225) and (squares[1][2])[1] != (225,225,225) and (squares[2][2])[1] != (225,225,225)): #RightCol
        colorWin = ((squares[0][2])[1])               
        if colorWin == green:
            WinPlayer = "green" 
            pygame.draw.line(gridBckgrd, (WinnerLineColor), (83+(166*2), 10), (83+(166*2), 488), 5) 
        elif colorWin == blue:
            WinPlayer = "blue"
            pygame.draw.line(gridBckgrd, (WinnerLineColor), (83+(166*2), 10), (83+(166*2), 488), 5) 
    #DiagLeftRight
    if ((squares[0][0])[1] == (squares[1][1])[1] == (squares[2][2])[1]) and ((squares[0][0])[1] != (225,225,225) and (squares[1][1])[1] != (225,225,225) and (squares[2][2])[1] != (225,225,225)): #DiagLeftRight
        colorWin = ((squares[0][0])[1])
        if colorWin == green:
            WinPlayer = "green"
            pygame.draw.line(gridBckgrd, (WinnerLineColor), (10, 10), (488, 488), 5)  
        elif colorWin == blue:
            WinPlayer = "blue"
            pygame.draw.line(gridBckgrd, (WinnerLineColor), (10, 10), (488, 488), 5)
    #DiagRightLeft
    if ((squares[2][0])[1] == (squares[1][1])[1] == (squares[0][2])[1]) and ((squares[2][0])[1] != (225,225,225) and (squares[1][1])[1] != (225,225,225) and (squares[0][2])[1] != (225,225,225)): #DiagRightLeft
        colorWin = ((squares[2][0])[1])
        if colorWin == green:
            WinPlayer = "green" 
            pygame.draw.line(gridBckgrd, (WinnerLineColor), (488, 10), (10, 488), 5)
        elif colorWin == blue:
            WinPlayer = "blue"
            pygame.draw.line(gridBckgrd, (WinnerLineColor), (488, 10), (10, 488), 5)
    
    elif turns == 9 and winner == None:
        WinPlayer = "Draw game"

    return WinPlayer
#------------------------------------------------------------------------------------

#---------------------------------drawing circle-------------------------------------
def draw_circle():     
    if event.type == pygame.MOUSEBUTTONDOWN:
        posClick = pygame.mouse.get_pos()
        if 0 < posClick[0] < 166 and 0 < posClick[1] < 166: #top left 
            circle = pygame.draw.circle(gridBckgrd, (0,0,0), ((166/2), (166/2)), 50, 3) 
        if 166 < posClick[0] < 166*2 and 0 < posClick[1] < 166: #top mid
            circle = pygame.draw.circle(gridBckgrd, (0,0,0), (((166/2)+166), (166/2)), 50, 3)
        if 166*2 < posClick[0] < 166*3 and 0 < posClick[1] < 166: #top right
            circle = pygame.draw.circle(gridBckgrd, (0,0,0), (((166/2)+(166*2)), (166/2)), 50, 3)

        if 0 < posClick[0] < 166 and 166 < posClick[1] < 166*2: #mid left 
            circle = pygame.draw.circle(gridBckgrd, (0,0,0), ((166/2), ((166/2)+166)), 50, 3) 
        if 166 < posClick[0] < 166*2 and 166 < posClick[1] < 166*2: #mid mid
            circle = pygame.draw.circle(gridBckgrd, (0,0,0), (((166/2)+166), ((166/2)+166)), 50, 3)
        if 166*2 < posClick[0] < 166*3 and 166 < posClick[1] < 166*2: #mid right
            circle = pygame.draw.circle(gridBckgrd, (0,0,0), (((166/2)+(166*2)), ((166/2)+166)), 50, 3)

        if 0 < posClick[0] < 166 and 166*2 < posClick[1] < 166*3: #top left 
            circle = pygame.draw.circle(gridBckgrd, (0,0,0), ((166/2), ((166/2)+(166*2))), 50, 3) 
        if 166 < posClick[0] < 166*2 and 166*2 < posClick[1] < 166*3: #top mid
            circle = pygame.draw.circle(gridBckgrd, (0,0,0), (((166/2)+166), ((166/2)+(166*2))), 50, 3)
        if 166*2 < posClick[0] < 166*3 and 166*2 < posClick[1] < 166*3: #top right
            circle = pygame.draw.circle(gridBckgrd, (0,0,0), (((166/2)+(166*2)), ((166/2)+(166*2))), 50, 3)
#------------------------------------------------------------------------------------

#-----------------------------------drawing cross------------------------------------
def draw_cross():
    if event.type == pygame.MOUSEBUTTONDOWN:
        posClick = pygame.mouse.get_pos()
        xCord = 30
        yCord = 136

        if 0 < posClick[0] < 166 and 0 < posClick[1] < 166: #top left 
            crossLR = pygame.draw.line(gridBckgrd, (0,0,0), (xCord, xCord), (yCord, yCord), 3)
            crossRL = pygame.draw.line(gridBckgrd, (0,0,0), (xCord, yCord), (yCord, xCord), 3)
        if 166 < posClick[0] < 166*2 and 0 < posClick[1] < 166: #top mid
            crossLR = pygame.draw.line(gridBckgrd, (0,0,0), (xCord+166, xCord), (yCord+166, yCord), 3)
            crossRL = pygame.draw.line(gridBckgrd, (0,0,0), (xCord+166, yCord), (yCord+166, xCord), 3)
        if 166*2 < posClick[0] < 166*3 and 0 < posClick[1] < 166: #top right
            crossLR = pygame.draw.line(gridBckgrd, (0,0,0), ((xCord+(166*2), xCord)), (yCord+(166*2), yCord), 3)
            crossRL = pygame.draw.line(gridBckgrd, (0,0,0), (xCord+(166*2), yCord), (yCord+(166*2), xCord), 3)

        if 0 < posClick[0] < 166 and 166 < posClick[1] < 166*2: #mid left 
            crossLR = pygame.draw.line(gridBckgrd, (0,0,0), (xCord, xCord+166), (yCord, yCord+166), 3)
            crossRL = pygame.draw.line(gridBckgrd, (0,0,0), (xCord, yCord+166), (yCord, xCord+166), 3)
        if 166 < posClick[0] < 166*2 and 166 < posClick[1] < 166*2: #mid mid
            crossLR = pygame.draw.line(gridBckgrd, (0,0,0), (xCord+166, xCord+166), (yCord+166, yCord+166), 3)
            crossRL = pygame.draw.line(gridBckgrd, (0,0,0), (xCord+166, yCord+166), (yCord+166, xCord+166), 3)
        if 166*2 < posClick[0] < 166*3 and 166 < posClick[1] < 166*2: #mid right
            crossLR = pygame.draw.line(gridBckgrd, (0,0,0), (xCord+(166*2), xCord+166), (yCord+(166*2), yCord+166), 3)
            crossRL = pygame.draw.line(gridBckgrd, (0,0,0), (xCord+(166*2), yCord+166), (yCord+(166*2), xCord+166), 3)

        if 0 < posClick[0] < 166 and 166*2 < posClick[1] < 166*3: #top left 
            crossLR = pygame.draw.line(gridBckgrd, (0,0,0), (xCord, xCord+(166*2)), (yCord, yCord+(166*2)), 3)
            crossRL = pygame.draw.line(gridBckgrd, (0,0,0), (xCord, yCord+(166*2)), (yCord, xCord+(166*2)), 3)
        if 166 < posClick[0] < 166*2 and 166*2 < posClick[1] < 166*3: #top mid
            crossLR = pygame.draw.line(gridBckgrd, (0,0,0), (xCord+166, xCord+(166*2)), (yCord+166, yCord+(166*2)), 3)
            crossRL = pygame.draw.line(gridBckgrd, (0,0,0), (xCord+166, yCord+(166*2)), (yCord+166, xCord+(166*2)), 3)
        if 166*2 < posClick[0] < 166*3 and 166*2 < posClick[1] < 166*3: #top right
            crossLR = pygame.draw.line(gridBckgrd, (0,0,0), (xCord+(166*2), xCord+(166*2)), (yCord+(166*2), yCord+(166*2)), 3)
            crossRL = pygame.draw.line(gridBckgrd, (0,0,0), (xCord+(166*2), yCord+(166*2)), (yCord+(166*2), xCord+(166*2)), 3)
#------------------------------------------------------------------------------------

#----------------------------------Installizing--------------------------------------
gridBckgrdWidth = 498
gridBckgrdHeight = 700
squareSize = 166
Black = (0,0,0)

pygame.init()


gridBckgrd = pygame.display.set_mode((gridBckgrdWidth, gridBckgrdHeight))
pygame.display.set_caption("Tic Tac Toe")
#------------------------------------------------------------------------------------

#---------------------------creating tic tac toe squares-----------------------------
squares = []
for y in range(0, gridBckgrdHeight-300, squareSize): #only makes 3 rows of squares
    row = []
    for x in range(0, gridBckgrdWidth, squareSize): #makes 3 columns
        rect = pygame.Rect(x, y, squareSize-1, squareSize-1) #the squares in the grid
        row.append([rect, (225,225,225)]) #background color of squares            
    squares.append(row)

for row in squares:
    for s in row:
        rect, color = s
        pygame.draw.rect(gridBckgrd, color, rect)
            
pygame.display.flip()
#------------------------------------------------------------------------------------

#-------------------------------code for running game--------------------------------
turns = 0 #even = x, odd = o
command = "Start game - X goes first!" #text to go in text bar
winner = None
GameRun = 1

while GameRun == 1:
    
    winner = findWinner()
    if winner == "green":
        command = ("The winner is X!")       
    if winner == "blue":
        command = ("The winner is O!")
    if winner == "Draw game":
        command = ("Draw game!")

    for event in pygame.event.get():   

        if event.type == pygame.MOUSEBUTTONDOWN: #close window
            clickpos = pygame.mouse.get_pos()
            if 50 <= clickpos[0] <= 230 and 635 <= clickpos[1] <= 681:
                pygame.quit()
                sys.exit()
                
        if event.type == pygame.QUIT: #close window
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN: #Reset Game
            clickpos = pygame.mouse.get_pos()
            if 260 <= clickpos[0] <= 440 and 635 <= clickpos[1] <= 681: 
                turns = 0 #even = x, odd = o
                command = "Start game - X goes first!" #text to go in text bar
                winner = None
                squares = []
                for y in range(0, gridBckgrdHeight-300, squareSize): #only makes 3 rows of squares
                    row = []
                    for x in range(0, gridBckgrdWidth, squareSize): #makes 3 columns
                        rect = pygame.Rect(x, y, squareSize-1, squareSize-1) #the squares in the grid
                        row.append([rect, (225,225,225)]) #background color of squares            
                    squares.append(row)
                for row in squares: #for loop to draw over the dots and crosses
                    for s in row:
                        rect, color = s
                        pygame.draw.rect(gridBckgrd, color, rect)
                pygame.display.flip()                   

        if event.type == pygame.MOUSEBUTTONDOWN and winner == None: #check which square was clicked and change its color on list          
            if (turns%2) == 0:
                #print("x's turn") //used to test program (terminal)
                for row in squares:
                    for s in row:
                        rect, color = s
                        if rect.collidepoint(event.pos):
                            if color == (225,225,225):
                                draw_cross()
                                pygame.display.update() #draws cross over grid
                                s[1] = (125,225,100) #color changes (green) --> allows code to run
                                turns += 1
                                command = "O's turn!"
                            else:
                                command = "Square taken, X's turn!"
            else:
                #print("0's turn") //used to test program (terminal)
                for row in squares:
                    for s in row:
                        rect, color = s
                        if rect.collidepoint(event.pos):
                            if color == (225,225,225):
                                draw_circle() 
                                pygame.display.update() #draws circle over grid
                                s[1] = (25, 75, 125) #color changes (blue) --> allows code to run
                                turns += 1
                                command = "X's turn!"
                            else:
                                command = "Square taken, O's turn!"
        pygame.display.update()
#------------------------------------------------------------------------------------ 
  
#---------------------------creating bottom command bar------------------------------
    font = pygame.font.SysFont("Arial", 30) #text graphics
    text = font.render(command, 1, (0, 0, 0)) #creating text surface
    textCenter = text.get_rect(center = (243,565)) #setting center point for text

    bottBar = pygame.draw.rect(gridBckgrd, (225,225,225), (50, 520, 390, 96)) #adding bottom command bar
    gridBckgrd.blit(text, textCenter) #adding text to surface

    exitButton = pygame.draw.rect(gridBckgrd, (225,179,90), (50, 635, 180, 46)) #adding exit game button
    ExitCommand = font.render("Exit Game", 1, (0,0,0)) #creating text surface
    PosExit = ExitCommand.get_rect(center = (140,656)) #setting position of words on button
    gridBckgrd.blit(ExitCommand, PosExit) #adding text to surface

    GameResetButton = pygame.draw.rect(gridBckgrd, (225,179,90), (260, 635, 180, 46)) #adding game reset button
    ResetCommand = font.render("Reset Game", 1, (0,0,0))
    PosReset = ResetCommand.get_rect(center = (350,656))
    gridBckgrd.blit(ResetCommand, PosReset) #adding text to surface
#------------------------------------------------------------------------------------
