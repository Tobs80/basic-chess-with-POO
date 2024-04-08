from tkinter import Button, PhotoImage
from  PIL import Image, ImageTk
import pathlib
Dir = str(pathlib.Path(__file__).parent.resolve())
class Tbutton(Button):
    board = []
    selected_piece = None
    eaten = []
    color_turn = 'white'
    def __init__(self, master=None, cnf={}, row=None, col=None, side_size = 0, callback=None,  **kwargs):
        super().__init__(master, cnf, width = side_size, height=side_size, command = self._on_click, justify='center',  **kwargs)
        self.row = row
        self.col = col
        self.callback = callback
        self.piece = None
        self.place(x = self.row*side_size, y = self.col*side_size)
        #self["state"] = "disabled"


    def check_piece(self):
        if self.piece:
            self["state"] = "normal"
            self.piece.color
            self.image = PhotoImage(file =Dir+f'\\images\\{self.piece.color}\\{self.piece.name}.png').subsample(10,10)
            
            self["image"] = self.image
            
        else:
            #self["state"] = "disabled"
            self["image"] = ''
    
    def change_turn(self):
        if Tbutton.color_turn=='black':
            Tbutton.color_turn='white'
        elif Tbutton.color_turn=='white':
            Tbutton.color_turn='black'

    def set_piece(self, piece):
        self.piece = piece
        self.check_piece()
    
    def clear_piece(self,old_y, old_x, inverse_color=False):
        Tbutton.board[old_y][old_x].piece= None
        self.clear_bg(old_y, old_x)
        #self.piece = None
    
    def clear_bg(self,old_y, old_x, inverse_color=False):
        old_color = '#C19770' if (old_x + old_y)%2==int(inverse_color) else '#faf0dc'
        Tbutton.board[old_y][old_x]['bg']= old_color
        Tbutton.board[old_y][old_x]['fg'] = 'black'

    def get_coords(self):
        return self.row, self.col
    
    

    def _on_click(self):
        #print(type(self))

        if self.piece and self.piece.color == Tbutton.color_turn:
            if not Tbutton.selected_piece  :
                Tbutton.selected_piece = self.piece
                Tbutton.board[self.piece.y][self.piece.x]['bg']='#c1e2be'
                return
            else:
                if self.piece.color == Tbutton.selected_piece.color:
                    self.clear_bg(Tbutton.selected_piece.y, Tbutton.selected_piece.x)
                    Tbutton.selected_piece = self.piece
                    Tbutton.board[self.piece.y][self.piece.x]['bg']='#c1e2be' 
                return

        if Tbutton.selected_piece :
            old_x = Tbutton.selected_piece.x
            old_y = Tbutton.selected_piece.y
            if self.piece:
                Tbutton.eaten.append(self.piece.name)
                new_x, new_y = Tbutton.selected_piece.eat(self.row, self.col, Tbutton.board)
                #print('comida')
            else:
                new_x,new_y = Tbutton.selected_piece.move(self.row, self.col, Tbutton.board)
                #print('movida')
            if new_x!=-1:
                #Tbutton.board[old_y][old_x].clear_piece(inverse_color=inverse_color)
                self.clear_piece(old_y,old_x)
                Tbutton.board[new_y][new_x].set_piece(Tbutton.selected_piece)
                Tbutton.selected_piece = None
                self.change_turn()
                self.callback(old_x, old_y, new_x, new_y )

        


