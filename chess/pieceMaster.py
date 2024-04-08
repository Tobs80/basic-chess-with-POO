class PieceMaster():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = 'black' if  color=='b' else 'white'
        self.letter = ''
        self.eaten = False
        self.mov_dir =1 if self.color=='black' else -1

    def assign_letter(self, letter):
        pass

    def validate_movement(self, new_x, new_y,  board):
        #vertical validation
        step_x = 1 if new_y > self.y else -1# (0 if new_y == self.y else -1)
        step_y = 1 if new_x > self.x else -1#(0 if new_x == self.x else -1)
        if new_x==self.x:
            for y in range(self.y+step_x, new_y, step_x):
                if board[y][self.x].piece:
                    return False
        #horitzontal       
        elif new_y==self.y:
            
            for x in range(self.x+step_y, new_x, step_y):
                if board[self.y][x].piece:
                    return False
                
        step_x = 1 if new_y > self.y else (0 if new_y == self.y else -1)
        step_y = 1 if new_x > self.x else (0 if new_x == self.x else -1)     
        x, y = self.x + step_y, self.y + step_x
        while x != new_x and y != new_y:
            if board[y][x].piece:
                return False
            x += step_y
            y += step_x
        
                
        return True
                
    def get_coords(self):
        return self.x, self.y

    def __repr__(self):
        return self.letter


    

    def retire(self):
        pass
