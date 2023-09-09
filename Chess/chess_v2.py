import pygame
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
"""
white = 1###
black = 0###
king = #111
queen = #110
rook = #101
bishop = #100
knight = #011
pawn = #010
empty = 0000
"""

white_king_image = pygame.transform.scale(pygame.image.load("chess_images/white_chess_king.png"), (100, 100))
white_queen_image = pygame.transform.scale(pygame.image.load("chess_images/white_chess_queen.png"), (100, 100))
white_rook_image = pygame.transform.scale(pygame.image.load("chess_images/white_chess_rook.png"), (100, 100))
white_bishop_image = pygame.transform.scale(pygame.image.load("chess_images/white_chess_bishop.png"), (100, 100))
white_knight_image = pygame.transform.scale(pygame.image.load("chess_images/white_chess_knight.png"), (100, 100))
white_pawn_image = pygame.transform.scale(pygame.image.load("chess_images/white_chess_pawn.png"), (100, 100))

black_king_image = pygame.transform.scale(pygame.image.load("chess_images/black_chess_king.png"), (100, 100))
black_queen_image = pygame.transform.scale(pygame.image.load("chess_images/black_chess_queen.png"), (100, 100))
black_rook_image = pygame.transform.scale(pygame.image.load("chess_images/black_chess_rook.png"), (100, 100))
black_bishop_image = pygame.transform.scale(pygame.image.load("chess_images/black_chess_bishop.png"), (100, 100))
black_knight_image = pygame.transform.scale(pygame.image.load("chess_images/black_chess_knight.png"), (100, 100))
black_pawn_image = pygame.transform.scale(pygame.image.load("chess_images/black_chess_pawn.png"), (100, 100))

chess_board = [
            ["0101", "0011", "0100", "0110", "0111", "0100", "0011", "0101"],
            ["0010", "0010", "0010", "0010", "0010", "0010", "0010", "0010"],
            ["0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000"],
            ["0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000"],
            ["0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000"],
            ["0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000"],
            ["1010", "1010", "1010", "1010", "1010", "1010", "1010", "1010"],
            ["1101", "1011", "1100", "1110", "1111", "1100", "1011", "1101"]
            ]
piece_list = [
["1111", white_king_image],["1110", white_queen_image], ["1101", white_rook_image],["1100", white_bishop_image], 
["1011", white_knight_image],["1010", white_pawn_image], ["0111", black_king_image],["0110", black_queen_image], 
["0101", black_rook_image],["0100", black_bishop_image], ["0011", black_knight_image],["0010", black_pawn_image]
]

def graph():
    for i in range(8):
        for k in range(8):
            square = pygame.Rect(k * 100, i * 100, WIDTH / 8, HEIGHT / 8)
            if (i + k) % 2 == 0:
                pygame.draw.rect(screen, (238,238,210), square)
            else:
                pygame.draw.rect(screen, (118,150,86), square)
def draw_pieces():
    for i in range(8):
        for j in range(8):
            for x in piece_list:
                if chess_board[i][j] == x[0]:
                    screen.blit(x[1], (j*100, i*100))

def straight_between(cord1, cord2):
    horz_dis = abs(cord1[0]-cord2[0])
    vir_dis = abs(cord1[1]-cord2[1])
    if cord1[0]<cord2[0]:    
        for num in range(horz_dis-1):
            if chess_board[cord1[1]+num+1][cord1[0]] != "0000":
                return False
    if cord1[0]>cord2[0]: 
        for num in range(horz_dis-1):
            if chess_board[cord1[1]][cord1[0]-num-1] != "0000":
                return False
    if cord1[1]<cord2[1]:
        for num in range(vir_dis-1):
            if chess_board[cord1[1]+num+1][cord1[0]] != "0000":
                return False
    if cord1[1]>cord2[1]:    
        for num in range(vir_dis-1):
            if chess_board[cord1[1]][cord1[0]-num-1] != "0000":
                return False
    return True
def diagional_between(cord1, cord2):
    dis = abs(cord1[0]-cord2[0])
    if cord1[0]<cord2[0] and cord1[1]<cord2[1]:
        for num in range(dis-1):
            if chess_board[cord1[1]+num+1][cord1[0]+num+1] != "0000":
                return False
    if cord1[0]<cord2[0] and cord1[1]>cord2[1]:
        for num in range(dis-1):
            if chess_board[cord1[1]-num-1][cord1[0]+num+1] != "0000":
                return False
    if cord1[0]>cord2[0] and cord1[1]<cord2[1]:
        for num in range(dis-1):
            if chess_board[cord1[1]+num+1][cord1[0]-num-1] != "0000":
                return False
    if cord1[0]>cord2[0] and cord1[1]>cord2[1]:
        for num in range(dis-1):
            if chess_board[cord1[1]-num-1][cord1[0]-num-1] != "0000":
                return False
    return True

def king(prev, mouse_pos, prev_piece):
    current = [mouse_pos[1]//100, mouse_pos[0]//100]
    for i in range(-1, 2):
        for j in range(-1, 2):       
            if [prev[0]+i, prev[1]+j] == current and (i, j) != (0, 0):
                chess_board[mouse_pos[1]//100][mouse_pos[0]//100] = prev_piece[0]
                screen.blit(prev_piece[1], (mouse_pos[0]//100*100, mouse_pos[1]//100*100))
                return None
  
    chess_board[prev[0]][prev[1]] = prev_piece[0]
    return 1
def queen(prev, mouse_pos, prev_piece):
    current = [mouse_pos[1]//100, mouse_pos[0]//100]
    #straight
    if prev[0] == current[0] or prev[1] == current[1]:
        if straight_between((prev[1], prev[0]), (current[1], current[0])):
            chess_board[mouse_pos[1]//100][mouse_pos[0]//100] = prev_piece[0]
            screen.blit(prev_piece[1], (mouse_pos[0]//100*100, mouse_pos[1]//100*100))
        else:
            chess_board[prev[0]][prev[1]] = prev_piece[0]
            return 1 
    #diagional
    elif prev[0] - prev[1] == current[0] - current[1] or prev[0] + prev[1] == current[0] + current[1]:
        if diagional_between((prev[1], prev[0]), (current[1], current[0])):
            chess_board[mouse_pos[1]//100][mouse_pos[0]//100] = prev_piece[0]
            screen.blit(prev_piece[1], (mouse_pos[0]//100*100, mouse_pos[1]//100*100))
        else:
            chess_board[prev[0]][prev[1]] = prev_piece[0]
            return 1
    #extra stuff
    else:
        chess_board[prev[0]][prev[1]] = prev_piece[0]
        return 1
    if chess_board[current[0]][current[1]] == chess_board[prev[0]][prev[1]]:
        chess_board[prev[0]][prev[1]] = prev_piece[0]
        return 1
def rook(prev, mouse_pos, prev_piece):
    current = [mouse_pos[1]//100, mouse_pos[0]//100]
    if prev[0] == current[0] or prev[1] == current[1]:
        if straight_between((prev[1], prev[0]), (current[1], current[0])):
            chess_board[mouse_pos[1]//100][mouse_pos[0]//100] = prev_piece[0]
            screen.blit(prev_piece[1], (mouse_pos[0]//100*100, mouse_pos[1]//100*100))
        else:
            chess_board[prev[0]][prev[1]] = prev_piece[0]
            return 1
    else:
        chess_board[prev[0]][prev[1]] = prev_piece[0]
        return 1
    if chess_board[current[0]][current[1]] == chess_board[prev[0]][prev[1]]:
        chess_board[prev[0]][prev[1]] = prev_piece[0]
        return 1 
def bishop(prev, mouse_pos, prev_piece):
    current = [mouse_pos[1]//100, mouse_pos[0]//100]
    if prev[0] - prev[1] == current[0] - current[1] or prev[0] + prev[1] == current[0] + current[1]:
        if diagional_between((prev[1], prev[0]), (current[1], current[0])):
            chess_board[mouse_pos[1]//100][mouse_pos[0]//100] = prev_piece[0]
            screen.blit(prev_piece[1], (mouse_pos[0]//100*100, mouse_pos[1]//100*100)) 
        else:
            chess_board[prev[0]][prev[1]] = prev_piece[0]
            return 1
    else:    
        chess_board[prev[0]][prev[1]] = prev_piece[0]
        return 1
    if chess_board[current[0]][current[1]] == chess_board[prev[0]][prev[1]]:
        chess_board[prev[0]][prev[1]] = prev_piece[0]
        return 1 
def knight(prev, mouse_pos, prev_piece):
    current = [mouse_pos[1]//100, mouse_pos[0]//100]
    for a in range(-1, 2, 2):
        for b in range(-2, 3, 4):
            if (prev[0] + a, prev[1] + b) == (current[0], current[1]):
                chess_board[mouse_pos[1]//100][mouse_pos[0]//100] = prev_piece[0]
                screen.blit(prev_piece[1], (mouse_pos[0]//100*100, mouse_pos[1]//100*100)) 
                return None
            elif (prev[0] + b, prev[1] + a) == (current[0], current[1]):
                chess_board[mouse_pos[1]//100][mouse_pos[0]//100] = prev_piece[0]
                screen.blit(prev_piece[1], (mouse_pos[0]//100*100, mouse_pos[1]//100*100)) 
                return None
    chess_board[prev[0]][prev[1]] = prev_piece[0]
    return 1
def pawn(prev, mouse_pos, prev_piece):
    current = [mouse_pos[1]//100, mouse_pos[0]//100]
    if prev_piece[0][0] == "1":
        if chess_board[current[0]][current[1]] == "0000" and [current[0]+1, current[1]] == prev or [current[0]+2, current[1]] == prev and prev[0] == 6:
            chess_board[mouse_pos[1]//100][mouse_pos[0]//100] = prev_piece[0]
            screen.blit(prev_piece[1], (mouse_pos[0]//100*100, mouse_pos[1]//100*100)) 
            return None        
        if chess_board[current[0]][current[1]] != "0000" and ([current[0]+1, current[1]-1] == prev or [current[0]+1, current[1]+1] == prev):
            chess_board[mouse_pos[1]//100][mouse_pos[0]//100] = prev_piece[0]
            screen.blit(prev_piece[1], (mouse_pos[0]//100*100, mouse_pos[1]//100*100)) 
            return None

    if prev_piece[0][0] == "0":
        if chess_board[current[0]][current[1]] == "0000" and [current[0]-1, current[1]] == prev or [current[0]-2, current[1]] == prev and prev[0] == 1:
            chess_board[mouse_pos[1]//100][mouse_pos[0]//100] = prev_piece[0]
            screen.blit(prev_piece[1], (mouse_pos[0]//100*100, mouse_pos[1]//100*100)) 
            return None
        if chess_board[current[0]][current[1]] != "0000" and ([current[0]-1, current[1]+1] == prev or [current[0]-1, current[1]-1] == prev):
            chess_board[mouse_pos[1]//100][mouse_pos[0]//100] = prev_piece[0]
            screen.blit(prev_piece[1], (mouse_pos[0]//100*100, mouse_pos[1]//100*100)) 
            return None


    chess_board[prev[0]][prev[1]] = prev_piece[0]
    return 1

def check(whoose_turn, prev, prev_piece):
    king_info = str(whoose_turn%2) + "111"
    for y in range(8):
        for x in range(8):
            if chess_board[y][x] == king_info:
                king_info = [str(whoose_turn%2) + "111", x, y]
    
    
    

def checkmate(whoose_turn):
    king_info = str(whoose_turn%2) + "111"
    None
    


def main():
    prev = "None"
    whoose_turn = 1
    holding = False
    prev_piece = 1
    while True:
        clock.tick(6)
        graph()
        draw_pieces()
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        if pygame.mouse.get_pressed()[0] == True:    
            for x in piece_list:
                if chess_board[mouse_pos[1]//100][mouse_pos[0]//100] == x[0] and holding == False and int(x[0][0]) == whoose_turn%2:
                    screen.blit(x[1], (mouse_pos[0]-50, mouse_pos[1]-50))
                    #all of var stufff
                    holding, prev_piece = True, x 
                    prev = [mouse_pos[1]//100, mouse_pos[0]//100]
                    chess_board[mouse_pos[1]//100][mouse_pos[0]//100] = "0000"
                    whoose_turn += 1
                elif holding == True:
                    screen.blit(prev_piece[1], (mouse_pos[0]-50, mouse_pos[1]-50))
        
        if pygame.mouse.get_pressed()[0] == False:
            if holding == True:
                check(whoose_turn, prev, prev_piece)
                if prev_piece[0][1:4] == "111":
                    if king(prev, mouse_pos, prev_piece):
                        whoose_turn += 1
                if prev_piece[0][1:4] == "110":
                    if queen(prev, mouse_pos, prev_piece):
                        whoose_turn += 1
                if prev_piece[0][1:4] == "101":
                    if rook(prev, mouse_pos, prev_piece) == 1:
                        whoose_turn += 1
                if prev_piece[0][1:4] == "100":
                    if bishop(prev, mouse_pos, prev_piece) == 1:
                        whoose_turn += 1
                if prev_piece[0][1:4] == "011":
                    if knight(prev, mouse_pos, prev_piece) == 1:
                        whoose_turn += 1  
                if prev_piece[0][1:4] == "010":
                    if pawn(prev, mouse_pos, prev_piece) == 1:
                        whoose_turn +=1
                holding = False
        pygame.display.update()
main()