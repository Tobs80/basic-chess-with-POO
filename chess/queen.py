from pieceMaster import PieceMaster

class Queen(PieceMaster):
    
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'queen'

    
        
    def eat(self, new_x, new_y, board):
        if new_x == self.x or new_y == self.y or abs(new_x - self.x) == abs(new_y - self.y):
            if self.validate_movement(new_x,new_y, board):
                self.x = new_x
                self.y = new_y
                return self.x, self.y
        
        return -1,-1

    def move(self, new_x, new_y, board):
        if new_x == self.x or new_y == self.y or abs(new_x - self.x) == abs(new_y - self.y):
            if self.validate_movement(new_x,new_y,board):
                self.x = new_x
                self.y = new_y
                return self.x, self.y
        
        return -1,-1

   
    

