OCCUPIED_SPACES = {}

class Queen():
    def __init__(self,position,colour,enemy_pieces,has_moved=False):
        self.has_moved = has_moved
        self.position = position
        self.colour = colour
        self.enemy_pieces = enemy_pieces

    def can_take(self, piece_to_take):
        return True if self.colour != piece_to_take else False
    
    def validate_move(self, NewPos):

        # Bishop movement
        if abs(ord(NewPos[0]) - ord(self.position[0])) == abs(int(NewPos[1]) - int(self.position[1])) and NewPos != self.position:
            return True
        
        # Rook movement
        elif (NewPos[0] == self.position[0] or NewPos[1] == self.position[1]) and NewPos != self.position:
            return True
        
        return False
    
    def move(self, NewPos):

        if check_valid_space(NewPos):

            if self.validate_move(NewPos):
                
                take_piece(NewPos)

                self.position = NewPos

class King(Queen):
    def is_in_check(self):

        for piece in self.enemy_pieces:

            if piece.validate_move(self.position):

                return True

    def validate_move(self, NewPos):

        if abs(ord(NewPos[0]) - ord(self.position[0])) <= 1 and abs(int(NewPos[1]) - int(self.position[1])) <= 1 and NewPos != self.position:
            
            would_be_check = King(NewPos,self.colour,self.enemy_pieces,self.has_moved)
            if would_be_check.is_in_check():

                return False
            
            return True
        
class Bishop(Queen):
    def validate_move(self,NewPos):

        # Bishop movement
        if abs(ord(NewPos[0]) - ord(self.position[0])) == abs(int(NewPos[1]) - int(self.position[1])) and NewPos != self.position:
            return True
        
        # # Rook movement
        # elif (NewPos[0] == self.position[0] or NewPos[1] == self.position[1]) and NewPos != self.position:
        #     return True
        
        return False
    
class Rook(Queen):
    def validate_move(self,NewPos):

        # # Bishop movement
        # if (ord(NewPos[0]) - ord(self.position[0])) == (int(NewPos[1]) - int(self.position[1])) and NewPos != self.position:
        #     return True
        # Rook movement
        if (NewPos[0] == self.position[0] or NewPos[1] == self.position[1]) and NewPos != self.position:

            return True
        
        return False
    
class Pawn(Queen):
    def __init__(self, position, colour, enemy_pieces, has_moved=False):
        super().__init__(position, colour, enemy_pieces, has_moved)

        self.passant = False
    
    def validate_move(self, NewPos):
            
            #advancing
            #double-move on start
            piece_at_newpos = get_piece_at_position(NewPos)
            if piece_at_newpos is None:

                if abs(int(NewPos[1]) - int(self.position[1])) == 2 and NewPos[0]==self.position[0] and not self.has_moved:
                    
                    self.passant = True
                    return True
                
                elif abs(int(NewPos[1]) - int(self.position)) == 1 and NewPos[0]==self.position[0]:
                    return True
                
            #Taking
            else:

                #if the move is diagonally adjacent
                if abs(int(NewPos[1]) - int(self.position)) == 1 and abs(ord(NewPos[0]) - ord(self.position[0])) == 1:
                    
                    #Check en passant
                    if self.colour=='w':
                        potential_pawn = get_piece_at_position(f'{NewPos[0]}{str(int(NewPos[1])-1)}')

                    else:
                        potential_pawn = get_piece_at_position(f'{NewPos[0]}{str(int(NewPos[1])-1)}')

                    if potential_pawn is not None:

                        if potential_pawn.isinstance(Pawn):

                            if potential_pawn.passant == True:

                                return self.can_take(potential_pawn)
                            
                    
                    return self.can_take(potential_pawn)
                
class Knight(Queen):
    def validate_move(self, NewPos):
        #check for abs diff of 2:1 in pos in either rank or file
        #checking difference of 2 files and 1 rank
        if abs(ord(NewPos[0]) - ord(self.position[0])) == 2 and abs(int(NewPos[1]) - int(self.position)) == 1:
            return True
        
        #checking difference of 1 file and 2 ranks
        elif abs(ord(NewPos[0]) - ord(self.position[0])) == 1 and abs(int(NewPos[1]) - int(self.position)) == 2:
            return True
        
        return False

def get_piece_at_position(pos):
    return OCCUPIED_SPACES.get(pos)

def check_valid_space(pos):
    return True if (0 <= ord(pos[0]) - 97 <= 7) and (0 <= int(pos[1]) <= 7) else False

def take_piece(pos):
    OCCUPIED_SPACES.pop(pos, None)

def check_promotions():
    for key in OCCUPIED_SPACES.keys():
        if OCCUPIED_SPACES[key].isinstance(Pawn):
            if key[1] == '1':
                #promote
                pass
            elif key[1] == '8':
                #promote
                pass