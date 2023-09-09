import pygame

import math
import pynput

WIDTH, HEIGHT = 800, 800
VALID = "valid"
CAPTURE = "capture"
BLACK_TURN, RED_TURN= 0, 1
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
turn = BLACK_TURN

bk = pygame.transform.scale(pygame.image.load("checkers_pieces/checkers_black_king.png"), (90, 90))
bp = pygame.transform.scale(pygame.image.load("checkers_pieces/checkers_black_piece.png"), (90, 90))
rk = pygame.transform.scale(pygame.image.load("checkers_pieces/checkers_red_king.png"), (90, 90))
rp = pygame.transform.scale(pygame.image.load("checkers_pieces/checkers_red_piece.png"), (90, 90))


board = [
		["", bp, "", bp, "", bp, "", bp],
		[bp, "", bp, "", bp, "", bp, ""],
		["", bp, "", bp, "", bp, "", bp],
		["", "", "", "", "", "", "", ""],
		["", "", "", "", "", "", "", ""],
		[rp, "", rp, "", rp, "", rp, ""],
		["", rp, "", rp, "", rp, "", rp],
		[rp, "", rp, "", rp, "", rp, ""]
		]


#------------------------ Helper Functions ------------------------#

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if len(a_set.intersection(b_set)) > 0:
        return True
    return False  

def is_right_turn():
	if turn == BLACK_TURN:
		return {bp, bk}
	elif turn == RED_TURN:
		return {rp, rk}

#------------------------ Board Functions ------------------------#

def draw_board():
	for i in range(8):
		for k in range(8):
			square = pygame.Rect(k * WIDTH / 8, i * HEIGHT / 8, WIDTH / 8, HEIGHT / 8)
			if (i + k) % 2 == 0:
				pygame.draw.rect(screen, (238,238,210), square)
			else:
				pygame.draw.rect(screen, (118, 150, 86), square)


def draw_pieces():
	for y in range(8):
		for x in range(8):
			if board[y][x] != "":
				screen.blit(board[y][x], (x * 100 + 5, y * 100 + 5))

#------------------------ Piece Movement Functions ------------------------#

def bp_move(xmouse, ymouse, piece_holding, previous_pos):
	if piece_holding != bp:
		return
	if board[ymouse][xmouse] == "":    	# checks if spot is occupied
		for x in range(-1, 2, 2):  		# checks if move is valid for bp
			if (xmouse, ymouse) == (previous_pos[0] + x , previous_pos[1] + 1):
				return VALID
		for x in range(-2, 3, 4):       # for capturing		   # checks if move is valid for bp
			if (xmouse, ymouse) == (previous_pos[0] + x , previous_pos[1] + 2) and \
			board[previous_pos[1] + 1][previous_pos[0] + x // 2] in {rp, rk}:
				return CAPTURE


def rp_move(xmouse, ymouse, piece_holding, previous_pos):
	if piece_holding != rp:
		return
	
	if board[ymouse][xmouse] == "":
		for x in range(-1, 2, 2):
			if (xmouse, ymouse) == (previous_pos[0] + x , previous_pos[1] - 1):
				return VALID
		for x in range(-2, 3, 4):
			if (xmouse, ymouse) == (previous_pos[0] + x , previous_pos[1] - 2) and \
			board[previous_pos[1] - 1][previous_pos[0] + x // 2] in {bp, bk}:
				return CAPTURE

def bk_move(xmouse, ymouse, piece_holding, previous_pos):
	if piece_holding != bk:
		return

	if board[ymouse][xmouse] == "":

		for y in range(-1, 2, 2):	
			for x in range(-1, 2, 2):
				if (xmouse, ymouse) == (previous_pos[0] + x , previous_pos[1] + y):
					return VALID
		for y in range(-2, 3, 4):	
			for x in range(-2, 3, 4):
				if (xmouse, ymouse) == (previous_pos[0] + x , previous_pos[1] + y) and \
				board[previous_pos[1] + y//2][previous_pos[0] + x // 2] in {rp, rk}:
					return CAPTURE

def rk_move(xmouse, ymouse, piece_holding, previous_pos):
	if piece_holding != rk:
		return

	if board[ymouse][xmouse] == "":
		for y in range(-1, 2, 2):	
			for x in range(-1, 2, 2):
				if (xmouse, ymouse) == (previous_pos[0] + x , previous_pos[1] + y):
					return VALID
		for y in range(-2, 3, 4):	
			for x in range(-2, 3, 4):
				if (xmouse, ymouse) == (previous_pos[0] + x , previous_pos[1] + y) and \
				board[previous_pos[1] + y//2][previous_pos[0] + x // 2] in {bp, bk}:
					return CAPTURE

def promotion(xmouse, ymouse, piece_holding):
	if piece_holding == rp and ymouse == 0:
		board[ymouse][xmouse] = rk
		screen.blit(rk, (xmouse * 100 + 5, ymouse * 100 + 5))
	elif piece_holding == bp and ymouse == 7:
		board[ymouse][xmouse] = bk
		screen.blit(bk, (xmouse * 100 + 5, ymouse * 100 + 5))

#------------------------ Turn Functions ------------------------#

def black_move_avalible():
	for y in range(8):
		for x in range(8):
			if board[y][x] == bp and "" in {board[y+1][x+1], board[y+1][x-1]}:	
				return True
	return False

def red_move_avalible():
	for y in range(8):
		for x in range(8):
			if board[y][x] == bp and "" in {board[y-1][x+1], board[y-1][x-1]}:	
				return True
	return False

def black_capature_avalible():
	for y in range(8):
		for x in range(8):
			try:
				if board[y][x] == bp and "" in {board[y+2][x+2], board[y+2][x-2]} and \
				common_member([rp, rk],[board[y+1][x+1], board[y+1][x-1]]):
					return True
			except:
				None
	return False

def red_capature_avalible():
	for y in range(8):
		for x in range(8):
			try:	
				if board[y][x] == bp and "" in {board[y-2][x+2], board[y-2][x-2]} and \
				common_member([rp, rk],[board[y-1][x+1], board[y-1][x-1]]):
					return True
			except:
				return None
	return False


#------------------------ Displays Changes ------------------------#

def display_black_moves(xmouse, ymouse, piece_holding, previous_pos):
	var = [xmouse, ymouse, piece_holding, previous_pos]  #this to make next lines shorter

	if  VALID in {bp_move(*var), bk_move(*var)}:
		board[ymouse][xmouse] = piece_holding
		screen.blit(piece_holding, (xmouse * 100 + 5, ymouse * 100 + 5))
		promotion(xmouse, ymouse, piece_holding)
		global move_type
		move_type = VALID
	elif CAPTURE in {bp_move(*var), bk_move(*var)}:
		board[(ymouse + previous_pos[1]) // 2][(xmouse+previous_pos[0]) // 2] = ""
		board[ymouse][xmouse] = piece_holding
		screen.blit(piece_holding, (xmouse * 100 + 5, ymouse * 100 + 5))
		promotion(xmouse, ymouse, piece_holding)
		move_type = CAPTURE
	else:   # returns to previous_pos
		board[previous_pos[1]][previous_pos[0]] = piece_holding
		screen.blit(piece_holding, (previous_pos[0] * 100 + 5, previous_pos[1] * 100 + 5))
		global turn
		turn = BLACK_TURN

def display_red_moves(xmouse, ymouse, piece_holding, previous_pos):
	var = [xmouse, ymouse, piece_holding, previous_pos]  #this to make next lines shorter

	if  VALID in {rp_move(*var), rk_move(*var)}:
		board[ymouse][xmouse] = piece_holding
		screen.blit(piece_holding, (xmouse * 100 + 5, ymouse * 100 + 5))
		promotion(xmouse, ymouse, piece_holding)
		global move_type
		move_type = VALID
	elif  CAPTURE in {rp_move(*var), rk_move(*var)}:
		board[(ymouse + previous_pos[1]) // 2][(xmouse+previous_pos[0]) // 2] = ""
		board[ymouse][xmouse] = piece_holding
		screen.blit(piece_holding, (xmouse * 100 + 5, ymouse * 100 + 5))
		promotion(xmouse, ymouse, piece_holding)
		move_type = CAPTURE
	else:   # returns to previous_pos
		board[previous_pos[1]][previous_pos[0]] = piece_holding
		screen.blit(piece_holding, (previous_pos[0] * 100 + 5, previous_pos[1] * 100 + 5))
		global turn
		turn = RED_TURN
		
#------------------------ Pygame Mainloop ------------------------#


def main():
	mouse_is_holding = False
	global turn
	while True:
		
		clock.tick(60)
		draw_board()
		draw_pieces()
		# these to make the code shorter.
		mouse_pos = pygame.mouse.get_pos()
		xmouse = mouse_pos[0]//100
		ymouse = mouse_pos[1]//100

		if pygame.mouse.get_pressed()[0] == True: 
			# this is tpo map the piece to the mouse
			if mouse_is_holding == True:
				screen.blit(piece_holding, (mouse_pos[0]-45, mouse_pos[1]-45))

			# this calculates for the first frame of click
			elif board[ymouse][xmouse] != "":
				if board[ymouse][xmouse] in is_right_turn():
					screen.blit(board[ymouse][xmouse], (mouse_pos[0] - 45, mouse_pos[1] - 45))
					piece_holding = board[ymouse][xmouse]
					mouse_is_holding = True
					previous_pos = (xmouse, ymouse)
					board[ymouse][xmouse] = "" 
					
		elif pygame.mouse.get_pressed()[0] == False and mouse_is_holding == True:
			
			if turn == BLACK_TURN: 
				turn = RED_TURN
				print(1)
				display_black_moves(xmouse, ymouse, piece_holding, previous_pos)

				if black_capature_avalible() and move_type == CAPTURE:
					print("hi")
					turn = BLACK_TURN

			elif turn == RED_TURN:
				turn = BLACK_TURN
				print(2)
				display_red_moves(xmouse, ymouse, piece_holding, previous_pos)

				if red_capature_avalible() and move_type == CAPTURE:
					print("red")
					turn = RED_TURN

			mouse_is_holding = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		pygame.display.update()
main()
