import pygame
pygame.init()
from chess_class import Chess_Piece
from chess_class import white_piece_info, black_piece_info

white_king = Chess_Piece("white", "king", 3, 0)
white_queen = Chess_Piece("white", "queen", 4, 0)
white_knight1 = Chess_Piece("white", "knight1", 1, 0)
white_knight2 = Chess_Piece("white", "knight2", 6, 0)
white_bishop1 = Chess_Piece("white", "bishop1", 2, 0)
white_bishop2 = Chess_Piece("white", "bishop2", 5, 0)
white_rook1 = Chess_Piece("white", "rook1", 0, 0)
white_rook2 = Chess_Piece("white", "rook2", 7, 0)
#
white_pawn1 = Chess_Piece("white", "pawn1", 0, 1)
white_pawn2 = Chess_Piece("white", "pawn2", 1, 1)
white_pawn3 = Chess_Piece("white", "pawn3", 2, 1)
white_pawn4 = Chess_Piece("white", "pawn4", 3, 1)
white_pawn5 = Chess_Piece("white", "pawn5", 4, 1)
white_pawn6 = Chess_Piece("white", "pawn6", 5, 1)
white_pawn7 = Chess_Piece("white", "pawn7", 6, 1)
white_pawn8 = Chess_Piece("white", "pawn8", 7, 1)


black_king = Chess_Piece("black", "king", 3, 7)
black_queen = Chess_Piece("black", "queen", 4, 7)
black_knight1 = Chess_Piece("black", "knight1", 1, 7)
black_knight2 = Chess_Piece("black", "knight2", 6, 7)
black_bishop1 = Chess_Piece("black", "bishop1", 2, 7)
black_bishop2 = Chess_Piece("black", "bishop2", 5, 7)
black_rook1 = Chess_Piece("black", "rook1", 0, 7)
black_rook2 = Chess_Piece("black", "rook2", 7, 7)
#
black_pawn1 = Chess_Piece("black", "pawn1", 0, 6)
black_pawn2 = Chess_Piece("black", "pawn2", 1, 6)
black_pawn3 = Chess_Piece("black", "pawn3", 2, 6)
black_pawn4 = Chess_Piece("black", "pawn4", 3, 6)
black_pawn5 = Chess_Piece("black", "pawn5", 4, 6)
black_pawn6 = Chess_Piece("black", "pawn6", 5, 6)
black_pawn7 = Chess_Piece("black", "pawn7", 6, 6)
black_pawn8 = Chess_Piece("black", "pawn8", 7, 6)


white_king_image = pygame.transform.scale(pygame.image.load("chess_images/white_chess_king.png"), (100, 100))
white_queen_image = pygame.transform.scale(pygame.image.load("chess_images/white_chess_queen.png"), (100, 100))
white_knight_image = pygame.transform.scale(pygame.image.load("chess_images/white_chess_knight.png"), (100, 100))
white_bishop_image = pygame.transform.scale(pygame.image.load("chess_images/white_chess_bishop.png"), (100, 100))
white_rook_image = pygame.transform.scale(pygame.image.load("chess_images/white_chess_rook.png"), (100, 100))
white_pawn_image = pygame.transform.scale(pygame.image.load("chess_images/white_chess_pawn.png"), (100, 100))

black_king_image = pygame.transform.scale(pygame.image.load("chess_images/black_chess_king.png"), (100, 100))
black_queen_image = pygame.transform.scale(pygame.image.load("chess_images/black_chess_queen.png"), (100, 100))
black_knight_image = pygame.transform.scale(pygame.image.load("chess_images/black_chess_knight.png"), (100, 100))
black_bishop_image = pygame.transform.scale(pygame.image.load("chess_images/black_chess_bishop.png"), (100, 100))
black_rook_image = pygame.transform.scale(pygame.image.load("chess_images/black_chess_rook.png"), (100, 100))
black_pawn_image = pygame.transform.scale(pygame.image.load("chess_images/black_chess_pawn.png"), (100, 100))

clock = pygame.time.Clock()

chess_piece_list = [white_king, white_queen, white_knight1, white_knight2, white_bishop1, white_bishop2, white_rook1, white_rook2, white_pawn1, white_pawn2, white_pawn3, white_pawn4, white_pawn5, white_pawn6, white_pawn7, white_pawn8,
black_king, black_queen, black_knight1, black_knight2, black_bishop1, black_bishop2, black_rook1, black_rook2, black_pawn1, black_pawn2, black_pawn3, black_pawn4, black_pawn5, black_pawn6, black_pawn7, black_pawn8]

chess_image_list = [white_king_image, white_queen_image, white_knight_image, white_knight_image, white_bishop_image, white_bishop_image, white_rook_image, white_rook_image, white_pawn_image, white_pawn_image, white_pawn_image, white_pawn_image, white_pawn_image, white_pawn_image, white_pawn_image, white_pawn_image,
black_king_image, black_queen_image, black_knight_image, black_knight_image, black_bishop_image, black_bishop_image, black_rook_image, black_rook_image, black_pawn_image, black_pawn_image, black_pawn_image, black_pawn_image, black_pawn_image, black_pawn_image, black_pawn_image, black_pawn_image]

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def graph():
    for i in range(8):
        for k in range(8):
            square = pygame.Rect(k * 100, i * 100, WIDTH / 8, HEIGHT / 8)
            if (i + k) % 2 == 0:
                pygame.draw.rect(screen, (238,238,210), square)
            else:
                pygame.draw.rect(screen, (118,150,86), square)
def draw_pieces():
    screen.blit(white_king_image, (white_king.x, white_king.y))
    screen.blit(white_queen_image, (white_queen.x, white_queen.y))
    screen.blit(white_knight_image, (white_knight1.x, white_knight1.y))
    screen.blit(white_knight_image, (white_knight2.x, white_knight2.y))
    screen.blit(white_bishop_image, (white_bishop1.x, white_bishop1.y))    
    screen.blit(white_bishop_image, (white_bishop2.x, white_bishop2.y))
    screen.blit(white_rook_image, (white_rook1.x, white_rook1.y))
    screen.blit(white_rook_image, (white_rook2.x, white_rook2.y))

    screen.blit(white_pawn_image, (white_pawn1.x, white_pawn1.y))
    screen.blit(white_pawn_image, (white_pawn2.x, white_pawn2.y))
    screen.blit(white_pawn_image, (white_pawn3.x, white_pawn3.y))
    screen.blit(white_pawn_image, (white_pawn4.x, white_pawn4.y))
    screen.blit(white_pawn_image, (white_pawn5.x, white_pawn5.y))
    screen.blit(white_pawn_image, (white_pawn6.x, white_pawn6.y))
    screen.blit(white_pawn_image, (white_pawn7.x, white_pawn7.y))
    screen.blit(white_pawn_image, (white_pawn8.x, white_pawn8.y))
    
    screen.blit(black_king_image, (black_king.x, black_king.y))
    screen.blit(black_queen_image, (black_queen.x, black_queen.y))
    screen.blit(black_knight_image, (black_knight1.x, black_knight1.y))
    screen.blit(black_knight_image, (black_knight2.x, black_knight2.y))
    screen.blit(black_bishop_image, (black_bishop1.x, black_bishop1.y))    
    screen.blit(black_bishop_image, (black_bishop2.x, black_bishop2.y))
    screen.blit(black_rook_image, (black_rook1.x, black_rook1.y))
    screen.blit(black_rook_image, (black_rook2.x, black_rook2.y))

    screen.blit(black_pawn_image, (black_pawn1.x, black_pawn1.y))
    screen.blit(black_pawn_image, (black_pawn2.x, black_pawn2.y))
    screen.blit(black_pawn_image, (black_pawn3.x, black_pawn3.y))
    screen.blit(black_pawn_image, (black_pawn4.x, black_pawn4.y))
    screen.blit(black_pawn_image, (black_pawn5.x, black_pawn5.y))
    screen.blit(black_pawn_image, (black_pawn6.x, black_pawn6.y))
    screen.blit(black_pawn_image, (black_pawn7.x, black_pawn7.y))
    screen.blit(black_pawn_image, (black_pawn8.x, black_pawn8.y))


def main():
    current_cords=(900, 900)
    piece_clicked_on = None
    holding_piece = False
    mouse_up_runs = True
    new_piece = True
    num = 0
    origin_cords = (900, 900)
    
    graph()
    draw_pieces()
    pygame.display.update()
    
    while True:
        clock.tick(60)
        mouse_pos = pygame.mouse.get_pos()  
        color = white_king.cord_to_type(mouse_pos[0] // 100 * 100, mouse_pos[1] // 100 * 100)[0]
        type = white_king.cord_to_type(mouse_pos[0] // 100 * 100, mouse_pos[1] // 100 * 100)[1]
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if pygame.mouse.get_pressed()[0]:            
            mouse_up_runs = True
            
            #goes though list to find the piece
            for piece in chess_piece_list:
                if piece.color == color and piece.type == type:
                    if holding_piece == True:
                        num = chess_piece_list.index(piece)
                        holding_piece = False
            
            if num != None: #makes sure no error
                piece_clicked_on = chess_piece_list[num] 
                current_cords = (piece_clicked_on.x+50, piece_clicked_on.y+50)
                #to make origin cords
                if new_piece:    
                    new_piece = False

                    if piece_clicked_on.color == "white":
                        origin_cords = (white_piece_info[num][1], white_piece_info[num][2])
                    if piece_clicked_on.color == "black":
                        origin_cords = (black_piece_info[num-16][1], black_piece_info[num-16][2])
                    
                
                #folow mouse command
                piece_clicked_on.move_to(mouse_pos[0] - 50, mouse_pos[1] - 50)

                graph()
                draw_pieces()
                screen.blit(chess_image_list[chess_piece_list.index(piece_clicked_on)], (piece_clicked_on.x, piece_clicked_on.y))
                pygame.display.update()


        if pygame.mouse.get_pressed()[0] == False and mouse_up_runs:
            #bools to make things restet and run once
            new_piece = True
            holding_piece = True
            mouse_up_runs = False
            num = None
            
            for piece in chess_piece_list:
                piece.move_to((piece.x + 50) // 100 * 100, (piece.y + 50) // 100 * 100)

            if piece_clicked_on != None:
                if piece_clicked_on.type == "king":
                    piece_clicked_on.king_move(origin_cords, current_cords)
                elif piece_clicked_on.type[:4] == "rook":
                    piece_clicked_on.rook_move(origin_cords, current_cords)
                elif piece_clicked_on.type[:6] == "bishop":
                    piece_clicked_on.bishop_move(origin_cords, current_cords)
                elif piece_clicked_on.type == "queen":
                    piece_clicked_on.queen_move(origin_cords, current_cords)
                elif piece_clicked_on.type[:6] == "knight":
                    piece_clicked_on.knight_move(origin_cords, current_cords)
                elif piece_clicked_on.type[:4] == "pawn":
                    piece_clicked_on.pawn_move(origin_cords, current_cords)

            for piece in chess_piece_list:    
                if piece_clicked_on != None and piece.x == piece_clicked_on.x and piece.y == piece_clicked_on.y and piece != piece_clicked_on:
                    if piece_clicked_on.color != piece.color:
                        piece.capture()
                    if piece_clicked_on.color == piece.color:
                        piece_clicked_on.move_to(origin_cords[0], origin_cords[1])
            graph()
            draw_pieces()
            pygame.display.update()
        
        
        

main()