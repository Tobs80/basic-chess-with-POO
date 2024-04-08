import numpy as np
import tkinter as tk
from Tbutton import Tbutton
from Pawn import Pawn
from tower import Tower
from bishop import Bishop
from knight import Knight
from queen import Queen
from king import King
import time
SIZE_SIDE = 80
class main(tk.Tk):
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = SIZE_SIDE * 8
        self.width = SIZE_SIDE * 8
        #screen_width = self.winfo_screenmmwidth()
        #screen_height = self.winfo_screenmmheight()
        #print(screen_width,screen_height)
        self.x_offset = 0#(screen_width - self.width) // 2
        self.y_offset = 0#(screen_height - self.height) // 2
        self.geometry (f"{self.width}x{self.height}+{self.x_offset}+{self.y_offset}") 
        self.resizable(False,False)
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill="both", expand=1)        
        self.board = [[0 for j in range(8)] for i in range(8)]
        self.init_tiles()
        self.init_pieces()
        self.turn = 'white'
        Tbutton.board = self.board

    def reset(self):
        self.init_tiles()
        self.init_pieces()
        self.turn = 'white'
        Tbutton.board = self.board
        self.top.destroy()
        Tbutton.eaten=[]

    def init_tiles(self):
        for col in range(8):
            for row in range(8):
                self.board[col][row]= '-'
                if (col+row)%2 == 0:
                    self.board[col][row] = Tbutton(self.canvas, side_size= SIZE_SIDE, bg='#C19770', col=col, row=row, callback=self.on_tbutton_click)
                else:
                    self.board[col][row] = Tbutton(self.canvas, side_size = SIZE_SIDE, bg='#faf0dc', col=col, row=row, callback=self.on_tbutton_click)
                
            
    def init_pawns(self):
        for col in range(8):
            #self.P1 = Pawn(1,col,'b')
            self.board[1][col].set_piece( Pawn(col, 1, 'b'))
            self.board[6][col].set_piece( Pawn(col, 6, 'w'))

            
    def init_towers(self):
        self.board[0][0].set_piece( Tower(0, 0, 'b'))
        self.board[0][7].set_piece( Tower(7, 0, 'b'))
        self.board[7][0].set_piece( Tower(0, 7, 'w'))
        self.board[7][7].set_piece( Tower(7, 7, 'w'))

    def init_bishops(self):
        self.board[0][2].set_piece( Bishop(2, 0, 'b'))
        self.board[0][5].set_piece( Bishop(5, 0, 'b'))
        self.board[7][2].set_piece( Bishop(2, 7, 'w'))
        self.board[7][5].set_piece( Bishop(5, 7, 'w'))

    def init_knights(self):
        self.board[0][1].set_piece( Knight(1, 0, 'b'))
        self.board[0][6].set_piece( Knight(6, 0, 'b'))
        self.board[7][1].set_piece( Knight(1, 7, 'w'))
        self.board[7][6].set_piece( Knight(6, 7, 'w'))

    def init_queens(self):
        self.board[0][4].set_piece( Queen(4, 0, 'b'))
        self.board[7][4].set_piece( Queen(4, 7, 'w'))
    
    def init_kings(self):
        #Tbutton.kings[0] = 
        #Tbutton.kings[1] = 
        self.board[0][3].set_piece(King(3, 0, 'b'))
        self.board[7][3].set_piece(King(3, 7, 'w'))

    def init_pieces(self):
        self.init_pawns()
        self.init_towers()
        self.init_bishops()
        self.init_knights()
        self.init_queens()
        self.init_kings()

    def clear_piece(self,old_y, old_x, inverse_color=False):
        self.board[old_y][old_x].piece= None
        self.clear_bg(old_y, old_x)
    
    def check_pawn_promotion(self, row, col):
        check_piece = self.board[row][col].piece
        if check_piece.name == 'pawn' and (check_piece.y==0 or check_piece.y==7):
            color = check_piece.color[0]
            self.board[row][col].set_piece(Queen(col, row, color))

    def check_king_alive(self):
        if 'king' in Tbutton.eaten:
            self.top = tk.Toplevel(self)
            TOPWIDTH = 200
            TOPHEIGHT = 150
            top_x_offset = self.winfo_x() + (self.width - TOPWIDTH) //2 + self.x_offset
            top_y_offset = self.winfo_y() + (self.height - TOPHEIGHT) //2 + self.y_offset
            self.top.geometry(f"{TOPWIDTH}x{TOPHEIGHT}+{top_x_offset }+{top_y_offset}")
        
            self.top.title("Child")
            self.top.config(bg='white')
            self.top.resizable(False,False)
            self.top.protocol("WM_DELETE_WINDOW", self.reset)
            winner_color = 'Black' if Tbutton.color_turn=='white' else 'White'
            tk.Label(self.top, text= f"{winner_color} wins", font=('arial 25 bold'), bg='white').place(relx=0.5, rely=0.3, anchor='center')
            tk.Button(self.top, text= f"Reiniciar", font=('arial 15 bold'),command=self.reset).place(relx=0.5, rely=0.7, anchor='center')

    def clear_bg(self,old_y, old_x, inverse_color=False):
        old_color = '#C19770' if (old_x + old_y.y)%2!=int(inverse_color) else '#faf0dc'
        self.board[old_y][old_x]['bg']= old_color
        self.board[old_y][old_x]['fg'] = 'black'

    def on_tbutton_click(self,  old_col, old_row,  new_col, new_row):
        
        self.board = Tbutton.board
        self.board[new_row][new_col].check_piece()
        self.check_pawn_promotion(new_row, new_col)
        self.board[old_row][old_col].check_piece()
        self.check_king_alive()
        
     




        
    
if __name__=="__main__":
    cb = main()
    cb.mainloop()
