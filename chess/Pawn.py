from pieceMaster import PieceMaster
from queen import Queen
class Pawn(PieceMaster):
    
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = 'pawn'
        self.moved = False
    
        
    def eat(self, x, y, board):
        
        if  (self.x+1==x or x ==self.x-1) and y==self.y+1*self.mov_dir:
            if self.validate_movement:
                self.x =x
                self.y+=1*self.mov_dir
            return self.x, self.y      
        return -1,-1

    def move(self,x, y, board):
        
        if self.x ==x and y == self.y+1*self.mov_dir:
            if self.validate_movement:
                self.y+=self.mov_dir
                self.moved = True
                return self.x, self.y
        elif not self.moved:
            if  (self.x==x) and y==self.y+2*self.mov_dir:
                self.y+=2*self.mov_dir
                self.moved = True
                return self.x, self.y
        
        return -1,-1

    def Check_Promotion(self, board):
        if self.color == 'black' and self.y==2:
            print('promotion')
            board[self.y][self.x].set_piece(Queen(self.x, self.y, 'b'))

        if self.color=='white' and self.y ==5:
            print('promotion')
            board[self.y][self.x].set_piece(Queen(self.x, self.y, 'w'))


