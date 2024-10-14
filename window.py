from tkinter import Tk, BOTH, Canvas, Button
from line import *
from cell import *
from maze import *

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root_widget = Tk()
        self.__root_widget.title("Maze Solver")
        self.canvas_widget = Canvas(self.__root_widget, bg="white", height=height, width=width)
        self.canvas_widget.pack(fill=BOTH, expand=1)
        self.running = False
        self.draw_button()
        self._maze = None
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close())
        

    def draw_line(self, line, fill_color):
        line.draw(self.canvas_widget, fill_color=fill_color)
    
    def redraw(self):
        self.__root_widget.update_idletasks
        self.__root_widget.update()

    def close(self):
        self.running = False
        
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print('Window closed.')
        
    def draw_button(self):
        button = Button( 
                   text="Click to solve", 
                   command=self.button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)
        button.pack(padx=20, pady=20)

        
    def button_clicked(self):
        self._maze._bfs_solve(0,0)
    