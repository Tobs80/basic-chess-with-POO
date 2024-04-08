from pieceMaster import PieceMaster

class Knight(PieceMaster):
    
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'knight'
    
        
    def eat(self, new_x, new_y, board):
        delta_x = abs(new_x - self.x)
        delta_y = abs(new_y - self.y)
        if (delta_x == 1 and delta_y == 2) or (delta_x == 2 and delta_y == 1):
                self.x = new_x
                self.y = new_y
                return self.x, self.y
        else:
            return -1,-1

    def move(self, new_x, new_y, board):
        delta_x = abs(new_x - self.x)
        delta_y = abs(new_y - self.y)
        if (delta_x == 1 and delta_y == 2) or (delta_x == 2 and delta_y == 1):
            if self.validate_movement(new_x,new_y,board):
                self.x = new_x
                self.y = new_y
                return self.x, self.y
        
        return -1,-1

   
    

