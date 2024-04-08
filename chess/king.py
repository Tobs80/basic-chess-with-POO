from pieceMaster import PieceMaster

class King(PieceMaster):
    
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'king'
    
        
    def eat(self, new_x, new_y, board):
        if abs(new_x - self.x) <= 1 and abs(new_y - self.y) <= 1:
            if self.validate_movement(new_x,new_y, board):
                self.x = new_x
                self.y = new_y
                return self.x, self.y
        
        return -1,-1

    def move(self, new_x, new_y, board):
        if abs(new_x - self.x) <= 1 and abs(new_y - self.y) <= 1:
            if self.validate_movement(new_x,new_y,board):
                self.x = new_x
                self.y = new_y
                return self.x, self.y
        
        return -1,-1

   
    

