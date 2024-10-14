from cell import Cell
from window import *
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        
    def _create_cells(self):
        for i in range(self._num_rows):
            row_to_add = []
            for j in range(self._num_cols):
                cell_to_add = Cell(self._win)
                row_to_add.append(cell_to_add)
            self._cells.append(row_to_add)
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)
                
    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell.draw(x1=(j * self._cell_size_x) + self._x1, 
                  y1=(i * self._cell_size_y) + self._y1, 
                  x2=(j * self._cell_size_x) + self._cell_size_x + self._x1, 
                  y2=(i * self._cell_size_y) + self._cell_size_y + self._y1)
        self._animate()
        
    def _animate(self):
        if self._win is None:
            return   
        self._win.redraw()
        time.sleep(0.05)
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._cells[-1][-1].has_right_wall = False
        self._draw_cell(0,0)
        self._draw_cell(len(self._cells)-1, len(self._cells[0])-1)  
        
        
    