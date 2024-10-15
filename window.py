from tkinter import Entry, Label, Tk, BOTH, Canvas, Button, OptionMenu, StringVar
from line import *
from cell import *
from maze import *

class Window:
    def __init__(self, width, height):
        self.options = ['BFS', 'DFS']
        self.width = width
        self.height = height
        self.__root_widget = Tk()
        self.__root_widget.title("Maze Solver")
        self.canvas_widget = Canvas(self.__root_widget, bg="white", height=height, width=width)
        self.canvas_widget.pack(fill=BOTH, expand=1)
        self.running = False
        self.selected_option = StringVar(self.__root_widget)
        self.selected_option.set("Select an Algorithm")
        self.int_rows = StringVar()
        self.int_cols = StringVar()
        self.draw_button()
        self.create_options()
        self.create_int()
        self._maze = None
        self._algorithm = None
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close())
        

    def create_int(self):
        rows = self.int_rows
        cols = self.int_cols
        label1 = Label(self.__root_widget, text="Enter Rows")
        label1.pack(pady=5)
        entry1 = Entry(self.__root_widget, textvariable=rows)
        entry1.pack(pady=5)
        label2 = Label(self.__root_widget, text="Enter Columns")
        label2.pack(pady=5)
        entry2 = Entry(self.__root_widget, textvariable=cols)
        entry2.pack(pady=5)
    
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
        
        button2 = Button(text="Generate Maze", 
                   command=self.generate,
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
        button2.pack(padx=20, pady=20)
    def create_options(self):
        options = OptionMenu(self.__root_widget, self.selected_option, *self.options)
        options.pack(pady=20)
        
    def button_clicked(self):
        if self.selected_option.get() == 'DFS':
            self._maze.solve()
        elif self.selected_option.get() == 'BFS':
            self._maze._bfs_solve(0,0)
            print(self._maze)
    
    def generate(self):
        if self._maze:
            self._maze.reset()
        self.canvas_widget.delete('all')
        num_rows = int(self.int_rows.get())
        num_cols = int(self.int_cols.get())
        offset = 50
        screen_x = 800
        screen_y = 600
        cell_size_x = (screen_x - 2 * offset) / num_cols
        cell_size_y = (screen_y - 2 * offset) / num_rows
        maze = Maze(offset, offset, num_rows, num_cols, cell_size_x, cell_size_y, self, 10)
        self._maze = maze
        
    