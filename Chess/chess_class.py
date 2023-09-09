import pygame
white_piece_info = [["king", 3, 0], ["queen", 4, 0], ["knight1", 1, 0], ["knight2", 6, 0], ["bishop1", 2, 0], ["bishop2", 5, 0], ["rook1", 0, 0], ["rook2", 7, 0],
["pawn1", 0, 1], ["pawn2", 1, 1], ["pawn3", 2, 1], ["pawn4", 3, 1], ["pawn5", 4, 1], ["pawn6", 5, 1], ["pawn7", 6, 1], ["pawn8", 7, 1]]

black_piece_info = [["king", 3, 7], ["queen", 4, 7], ["knight1", 1, 7], ["knight2", 6, 7], ["bishop1", 2, 7], ["bishop2", 5, 7], ["rook1", 0, 7], ["rook2", 7, 7],
["pawn1", 0, 6], ["pawn2", 1, 6], ["pawn3", 2, 6], ["pawn4", 3, 6], ["pawn5", 4, 6], ["pawn6", 5, 6], ["pawn7", 6, 6], ["pawn8", 7, 1]]


class Chess_Piece:
    def __init__(self, color, type, i, j):
        #i and j represents x and y, but i use a diffrent x and y later, thus, i, j
        self.color = color
        self.type = type
        self.x, self.y = i*100, j*100

    
    def cord_to_type(self, x, y):
        for item in white_piece_info:
            if item[1]==x and item[2]==y:
                return ("white", item[0])
        for item in black_piece_info:
            if item[1]==x and item[2]==y:
                return ("black", item[0])
        return (None, None)

    
    def type_to_cord(self, color, type):
        if color == "black":
            for item in black_piece_info:
                if item[0]==type:
                    return (item[1], item[2])        
        if color == "white": 
            for item in white_piece_info:
                if item[0]==type:
                    return (item[1], item[2])
        return (None, None)

    
    def move_to(self, x, y): 
        self.x, self.y = x, y
        if self.color == "white":     
            for item in white_piece_info:
                if item[0] == self.type:
                    item[1], item[2] = x, y
        if self.color == "black":
            for item in black_piece_info:
                if item[0] == self.type:
                    item[1], item[2] = x, y  
        return self
    
    
    def move_by(self, x, y):
        self.x += x*100
        self.y += y*100
        if self.color == "white":     
            for item in white_piece_info:
                if item[0] == self.type:
                    item[1], item[2] = x*100, y*100
        if self.color == "black":
            for item in black_piece_info:
                if item[0] == self.type:
                    item[1], item[2] = x*100, y*100
        return self
   
    


    
    def capture(self):
        self.move_to(1000, 1000)
    
    
    def king_move(self, origin_cords, current_cords):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (origin_cords[0]//100+i, origin_cords[1]//100+j) == (current_cords[0]//100, current_cords[1]//100):
                    return None
        self.move_to(origin_cords[0], origin_cords[1])
                

    def rook_move(self, origin_cords, current_cords):
        if origin_cords[0]//100 == current_cords[0]//100 or origin_cords[1]//100 == current_cords[1]//100:
            print(0)
            for n in range(origin_cords[0]//100+1, current_cords[0]//100):
                print(1)
                if self.cord_to_type(n*100, origin_cords[1]) != (None, None):
                    self.move_to(origin_cords[0], origin_cords[1])
                    return None
            
            
            for n in range(origin_cords[0]//100+1, current_cords[0]//100):
                print(1)
                if self.cord_to_type(n*100, origin_cords[1]) != (None, None):
                    self.move_to(origin_cords[0], origin_cords[1])
                    return None
        self.move_to(origin_cords[0], origin_cords[1])
    
    
    def bishop_move(self, origin_cords, current_cords):
        if origin_cords[0]//100 - origin_cords[1]//100 == current_cords[0]//100 - current_cords[1]//100:
            return None
        if origin_cords[0]//100 + origin_cords[1]//100 == current_cords[0]//100 + current_cords[1]//100:
            return None
        self.move_to(origin_cords[0], origin_cords[1])
    

    def queen_move(self, origin_cords, current_cords):
        import pygame
white_piece_info = [["king", 3, 0], ["queen", 4, 0], ["knight1", 1, 0], ["knight2", 6, 0], ["bishop1", 2, 0], ["bishop2", 5, 0], ["rook1", 0, 0], ["rook2", 7, 0],
["pawn1", 0, 1], ["pawn2", 1, 1], ["pawn3", 2, 1], ["pawn4", 3, 1], ["pawn5", 4, 1], ["pawn6", 5, 1], ["pawn7", 6, 1], ["pawn8", 7, 1]]

black_piece_info = [["king", 3, 7], ["queen", 4, 7], ["knight1", 1, 7], ["knight2", 6, 7], ["bishop1", 2, 7], ["bishop2", 5, 7], ["rook1", 0, 7], ["rook2", 7, 7],
["pawn1", 0, 6], ["pawn2", 1, 6], ["pawn3", 2, 6], ["pawn4", 3, 6], ["pawn5", 4, 6], ["pawn6", 5, 6], ["pawn7", 6, 6], ["pawn8", 7, 1]]


class Chess_Piece:
    def __init__(self, color, type, i, j):
        #i and j represents x and y, but i use a diffrent x and y later, thus, i, j
        self.color = color
        self.type = type
        self.x, self.y = i*100, j*100

    
    def cord_to_type(self, x, y):
        for item in white_piece_info:
            if item[1]==x and item[2]==y:
                return ("white", item[0])
        for item in black_piece_info:
            if item[1]==x and item[2]==y:
                return ("black", item[0])
        return (None, None)

    
    def type_to_cord(self, color, type):
        if color == "black":
            for item in black_piece_info:
                if item[0]==type:
                    return (item[1], item[2])        
        if color == "white": 
            for item in white_piece_info:
                if item[0]==type:
                    return (item[1], item[2])
        return (None, None)

    
    def move_to(self, x, y): 
        self.x, self.y = x, y
        if self.color == "white":     
            for item in white_piece_info:
                if item[0] == self.type:
                    item[1], item[2] = x, y
        if self.color == "black":
            for item in black_piece_info:
                if item[0] == self.type:
                    item[1], item[2] = x, y  
        return self
    
    
    def move_by(self, x, y):
        self.x += x*100
        self.y += y*100
        if self.color == "white":     
            for item in white_piece_info:
                if item[0] == self.type:
                    item[1], item[2] = x*100, y*100
        if self.color == "black":
            for item in black_piece_info:
                if item[0] == self.type:
                    item[1], item[2] = x*100, y*100
        return self
   
    


    
    def capture(self):
        self.move_to(1000, 1000)
    
    
    def king_move(self, origin_cords, current_cords):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (origin_cords[0]//100+i, origin_cords[1]//100+j) == (current_cords[0]//100, current_cords[1]//100):
                    return None
        self.move_to(origin_cords[0], origin_cords[1])
                

    def rook_move(self, origin_cords, current_cords):
        if origin_cords[0]//100 == current_cords[0]//100 or origin_cords[1]//100 == current_cords[1]//100:
            print(0)
            for n in range(origin_cords[0]//100+1, current_cords[0]//100):
                print(1)
                if self.cord_to_type(n*100, origin_cords[1]) != (None, None):
                    self.move_to(origin_cords[0], origin_cords[1])
                    return None
            
            
            for n in range(origin_cords[0]//100+1, current_cords[0]//100):
                print(1)
                if self.cord_to_type(n*100, origin_cords[1]) != (None, None):
                    self.move_to(origin_cords[0], origin_cords[1])
                    return None
        self.move_to(origin_cords[0], origin_cords[1])
    
    
    def bishop_move(self, origin_cords, current_cords):
        if origin_cords[0]//100 - origin_cords[1]//100 == current_cords[0]//100 - current_cords[1]//100:
            return None
        if origin_cords[0]//100 + origin_cords[1]//100 == current_cords[0]//100 + current_cords[1]//100:
            return None
        self.move_to(origin_cords[0], origin_cords[1])
    

    def queen_move(self, origin_cords, current_cords):
        if origin_cords[0]//100 == current_cords[0]//100 or origin_cords[1]//100 == current_cords[1]//100:
            return None
        elif origin_cords[0]//100 - origin_cords[1]//100 == current_cords[0]//100 - current_cords[1]//100:
            return None
        elif origin_cords[0]//100 + origin_cords[1]//100 == current_cords[0]//100 + current_cords[1]//100:
            return None
        self.move_to(origin_cords[0], origin_cords[1])


    def knight_move(self, origin_cords, current_cords):
        for a in range(-1, 2, 2):
            for b in range(-2, 3, 4):
                print(a, b)
                if (origin_cords[0]//100 + a, origin_cords[1]//100 + b) == (current_cords[0]//100, current_cords[1]//100):
                    return None
                elif (origin_cords[0]//100 + b, origin_cords[1]//100 + a) == (current_cords[0]//100, current_cords[1]//100):
                    return None
        self.move_to(origin_cords[0], origin_cords[1])
    
    








    def pawn_move(self, origin_cords, current_cords):
        if self.color == "white":
            if (origin_cords[0]//100 + 1, origin_cords[1]//100 + 1) == (current_cords[0]//100, current_cords[1]//100):
                for piece in black_piece_info:
                    if piece[1]//100 == self.x//100 and piece[2]//100 == self.y//100:
                        return None
            if (origin_cords[0]//100 - 1, origin_cords[1]//100 + 1) == (current_cords[0]//100, current_cords[1]//100):
                for piece in black_piece_info:
                    if piece[1]//100 == self.x//100 and piece[2]//100 == self.y//100:
                        return None
            if (origin_cords[0]//100, origin_cords[1]//100 - 1) == (current_cords[0]//100, current_cords[1]//100):
                self.move_to(origin_cords[0], origin_cords[1])
                return None
            if origin_cords[1]//100 == 1:
                if current_cords[1]//100 - origin_cords[1]//100 == 2:
                    if current_cords[0]//100 == origin_cords[0]//100:    
                        return None
            if current_cords[1]//100 - origin_cords[1]//100 == 1:
                if current_cords[0]//100 == origin_cords[0]//100:    
                    return None
        if self.color == "black":
            if (origin_cords[0]//100 + 1, origin_cords[1]//100 - 1) == (current_cords[0]//100, current_cords[1]//100):
                for piece in white_piece_info:
                    if piece[1]//100 == self.x//100 and piece[2]//100 == self.y//100:
                        return None
            if (origin_cords[0]//100 - 1, origin_cords[1]//100 - 1) == (current_cords[0]//100, current_cords[1]//100):
                for piece in white_piece_info:
                    if piece[1]//100 == self.x//100 and piece[2]//100 == self.y//100:
                        return None        
            if (origin_cords[0]//100, origin_cords[1]//100 + 1) == (current_cords[0]//100, current_cords[1]//100):
                self.move_to(origin_cords[0], origin_cords[1])
                return None
            if origin_cords[1]//100 == 6:
                if current_cords[1]//100 - origin_cords[1]//100 == -2:
                    if current_cords[0]//100 == origin_cords[0]//100:
                        return None
            if current_cords[1]//100 - origin_cords[1]//100 == -1:
                if current_cords[0]//100 == origin_cords[0]//100:    
                    return None
        self.move_to(origin_cords[0], origin_cords[1])

def straight_between(cord1, cord2):
    horz_dis = abs(cord1[0]-cord2[0])
    vir_dis = abs(cord1[1]-cord2[1])
    if cord1<cord2:    
        for num in range(horz_dis-1):
            print(cord1[0]+num, cord1[1])
        for num in range(vir_dis-1):
            print(cord1[0], cord1[1]+num)    
    if cord2<cord1:
        for num in range(vir_dis-1):
            print(cord2[0]+num, cord2[1])
        for num in range(vir_dis-1):
            print(cord2[0], cord2[1]+num)
    
