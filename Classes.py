class Queen():
    def __init__(self,position,colour,enemy_pieces,has_moved=False):
        self.has_moved = has_moved
        self.position = position
        self.colour = colour
        self.enemy_pieces = enemy_pieces
    
    def validate_move(self,NewPos):
        # Bishop movement
        if abs(ord(NewPos[0]) - ord(self.position[0])) == abs(int(NewPos[1]) - int(self.position[1])) and NewPos != self.position:
            return True
        # Rook movement
        elif (NewPos[0] == self.position[0] or NewPos[1] == self.position[1]) and NewPos != self.position:
            return True
        return False
    
    def move(self,NewPos):
        if self.validate_move(NewPos):
            self.position = NewPos

class King(Queen):
    def is_in_check(self):
        for piece in self.enemy_pieces:
            if piece.validate_move(self.position):
                return True

#TODO - EVALUATE THIS LOGIC
    def validate_move(self, NewPos):
        if abs(ord(NewPos[0]) - ord(self.position[0])) == 1 or abs(int(NewPos[1]) - int(self.position[1])) == 1:
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