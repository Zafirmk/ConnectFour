import pygame
import numpy
pygame.init()


# Initializing the board
board = numpy.zeros((6, 7))
print(board)

def main_menu():
    main_menu = True

    while main_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()


def depth(board, column): # To check at which depth piece should be dropped
    for row in range(5, -1, -1):
        if board[row][column] == 0:
            return row



def winning(column): # To Check for Winning combination
# Horizontal
    for x in range(0, 6):
        for y in range(0, 4):
            if board[x][y] == board[x][y+1] == board[x][y+2] == board[x][y+3] and board[x][y] != 0:
                return True

# Vertical
    y = column
    for x in range(0, 3):
        if board[x][y] == board[x+1][y] == board[x+2][y] == board[x+3][y] and board[x][y] != 0:
            return True

# Diagonal Positive
    for x in range(5, -1, -1):
        for y in range(0, 4):
            if board[x][y] == board[x-1][y+1] == board[x-2][y+2] == board[x-3][y+3] and board[x][y] != 0:
                return True

# Diagonal Negative
    for x in range(5, -1, -1):
        for y in range(3, 7):
            if board[x][y] == board[x-1][y-1] == board[x-2][y-2] == board[x-3][y-3] and board[x][y] != 0:
                return True



def winning_message(): # To display winning message
    pygame.draw.rect(window, white, [0, 560, 200, 100])
    message_display("Player " + str(turn) + " Wins!", red)


def message_display(msg, color): # Text Attributes
    screen_text = font.render(msg, True, color)
    window.blit(screen_text, (0, 560))
    return False


def main_game(turn): # Main game working
    column = dictionary_column[x]
    row = depth(board, column)
    board[row][column] = turn
    print(board)
    return row



def arrow(x, y, turn): # Draw Cursor
    if turn == 1:
        window.blit(arrow_img, (x, y))
    else:
        window.blit(arrow_img_yellow, (x, y))


# Declatation of Variables
width = 640
gameloop = True
turn = 1
dictionary_column = {
    # Pixel Position(X): Column
    # Key : Value
    15: 0,
    105: 1,
    195: 2,
    285: 3,
    375: 4,
    465: 5,
    555: 6,
}
dictionary_row = {
    # Row: Pixel Position(Y)
    0: 106,
    1: 186,
    2: 266,
    3: 346,
    4: 426,
    5: 506,
}
height = 580
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Connect Four")
board_img = pygame.image.load("Connect4Board.png")
arrow_img = pygame.image.load("ArrowPointer.png")
arrow_img_yellow = pygame.image.load("ArrowPointerYellow.png")
yellow_img = pygame.image.load("YellowChip.png")
red_img = pygame.image.load("RedChip.png")
font = pygame.font.SysFont(None, 30, True)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
x = 15
y = 20
x_change = 0
window.blit(board_img, (0, 100))

# Main Game Loop
while gameloop:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -90
            elif event.key == pygame.K_RIGHT:
                x_change = 90
            elif event.key == pygame.K_DOWN:
                column = dictionary_column[x]
                if board[0][column] == 0:
                    if turn == 1:
                        rw = main_game(turn)
                        window.blit(red_img, (x, dictionary_row[rw]))
                        winning(column)
                        if winning(column):
                            print ('winner')
                            winning_message()
                            gameloop = False
                        turn = 2
                    else:
                        rw = main_game(turn)
                        window.blit(yellow_img, (x, dictionary_row[rw]))
                        winning(column)
                        if winning(column):
                            print ('winner')
                            winning_message()
                            gameloop = False
                        turn = 1
                else:
                    print "Invalid"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 0
    x = x + x_change

    pygame.draw.rect(window, black, [0, 0, width, 100])
    arrow(x, y, turn)

    if x < 15:
        x = 555
    elif x > 555:
        x = 15
    pygame.display.update()
main_menu()
pygame.quit()
