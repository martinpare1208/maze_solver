import random
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
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        else:
            self._seed = 0
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        
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
    
        
    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell._visited = True
        
        while True:
            to_visit = []
            
        
            #Check above
            if i > 0 and self._cells[i - 1][j]._visited == False:
                to_visit.append((i - 1, j))
        
            #Check under
            if i < self._num_rows - 1 and self._cells[i + 1][j]._visited == False:
                to_visit.append((i + 1, j))

            #Check left
            if j > 0 and self._cells[i][j - 1]._visited == False:
                to_visit.append((i, j - 1))
        
            #Check right
            if j < self._num_cols - 1 and self._cells[i][j + 1]._visited == False:
                to_visit.append((i, j + 1))
        
            if not to_visit:
                return
            
            #random neighbor to choose
            direction_index = random.randrange(len(to_visit))
            next_index = to_visit[direction_index]
            
            #if no more neighbors
            if len(to_visit) == 0:
                self._draw_cell(i,j)
                return 
            
            #Remove wall between current cell and next cell
            
            #check above
            if next_index[0] == i - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i - 1][j].has_bottom_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i - 1, j)
            
            #check below
            if next_index[0] == i + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i + 1][j].has_top_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i + 1, j)
            
            #check right
            if next_index[1] == j + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i][j+1].has_left_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i, j + 1)
                
            #check left
            if next_index[1] == j - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i][j-1].has_right_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i, j - 1)
                
            self._break_walls_r(next_index[0], next_index[1])
            
    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell._visited = False
        return
    def solve(self):
        solved = self._solve_r(0,0)
        if solved:
            return True
        return False
        
    def _solve_r(self, i, j):
        # List of (row_offset, col_offset) for each direction
        self._animate()
        self._cells[i][j]._visited = True
        if i == self._num_rows - 1 and j == self._num_cols - 1:
            return True
        
        for n in range(3):
            
            #Check above
            if i > 0 and self._cells[i - 1][j] and self._cells[i-1][j]._visited == False and self._cells[i-1][j].has_bottom_wall == False and self._cells[i][j].has_top_wall == False:
                self._cells[i][j].draw_move(self._cells[i-1][j])
                if self._solve_r(i - 1, j):
                    return True
                self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)
                
            #Check below
            if i < self._num_rows - 1 and self._cells[i + 1][j] and self._cells[i + 1][j]._visited == False and self._cells[i+1][j].has_top_wall == False and self._cells[i][j].has_bottom_wall == False:
                self._cells[i][j].draw_move(self._cells[i+1][j])
                if self._solve_r(i + 1, j):
                    return True
                self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
                
            #Check right
            if j < self._num_cols - 1 and self._cells[i][j + 1] and self._cells[i][j + 1]._visited == False and self._cells[i][j + 1].has_left_wall == False and self._cells[i][j].has_right_wall == False:
                self._cells[i][j].draw_move(self._cells[i][j+1])
                if self._solve_r(i, j + 1):
                    return True
                self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)
            #Check left
            if  j > 0 and self._cells[i][j - 1] and self._cells[i][j - 1]._visited == False and self._cells[i][j - 1].has_right_wall == False and self._cells[i][j].has_left_wall == False:
                self._cells[i][j].draw_move(self._cells[i][j-1])
                if self._solve_r(i, j - 1):
                    return True
                self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)
        return False
    
    def _bfs_solve(self, i, j):
        to_visit = []
        to_visit.append((i, j))
        self._cells[i][j]._visited = True
        hashmap = {
            (i, j): None
        }
        while to_visit:
            self._animate()
            square = to_visit.pop(0)
            i = square[0]
            j = square[1]
            self._cells[square[0]][square[1]]._visited = True
            
            #explore all possible neighbors
            
            #Check above
            if i > 0 and self._cells[i - 1][j] and self._cells[i-1][j]._visited == False and self._cells[i-1][j].has_bottom_wall == False and self._cells[i][j].has_top_wall == False:
               if self._bfs_check_goal(i-1, j):
                   self._cells[i][j].draw_move(self._cells[i - 1][j])
                   to_visit.append((i - 1, j))
                   hashmap[(i - 1, j)] = i, j
                   self._bfs_get_path(hashmap, (i - 1, j))
                   return
               hashmap[(i - 1, j)] = i, j
               to_visit.append((i - 1, j))
               print(to_visit)
               self._cells[i][j].draw_move(self._cells[i - 1][j])
               
            #Check below
            if i < self._num_rows - 1 and self._cells[i + 1][j] and self._cells[i + 1][j]._visited == False and self._cells[i+1][j].has_top_wall == False and self._cells[i][j].has_bottom_wall == False:
                if self._bfs_check_goal(i+1, j):
                   self._cells[i][j].draw_move(self._cells[i + 1][j])
                   to_visit.append((i+1, j))
                   hashmap[(i + 1, j)] = i, j
                   self._bfs_get_path(hashmap, (i + 1, j))
                   return
                hashmap[(i + 1, j)] = i, j
                to_visit.append((i+1, j))
                print(to_visit)
                self._cells[i][j].draw_move(self._cells[i + 1][j])

                
            #Check right
            if j < self._num_cols - 1 and self._cells[i][j + 1] and self._cells[i][j + 1]._visited == False and self._cells[i][j + 1].has_left_wall == False and self._cells[i][j].has_right_wall == False:
                if self._bfs_check_goal(i, j + 1):
                   self._cells[i][j].draw_move(self._cells[i][j + 1])
                   to_visit.append((i, j + 1))
                   hashmap[(i, j + 1)] = i, j
                   self._bfs_get_path(hashmap, (i, j + 1))
                   return
                hashmap[(i, j + 1)] = i, j
                to_visit.append((i, j + 1))
                print(to_visit)
                self._cells[i][j].draw_move(self._cells[i][j+1])

                
            #Check left
            if j > 0 and self._cells[i][j - 1] and self._cells[i][j - 1]._visited == False and self._cells[i][j - 1].has_right_wall == False and self._cells[i][j].has_left_wall == False:
                if self._bfs_check_goal(i, j-1):
                   self._cells[i][j].draw_move(self._cells[i][j - 1])
                   to_visit.append((i, j - 1))
                   hashmap[(i, j - 1)] = i, j
                   self._bfs_get_path(hashmap, (i, j - 1))
                   return
                hashmap[(i, j - 1)] = i, j
                to_visit.append((i, j - 1))
                print(to_visit)
                self._cells[i][j].draw_move(self._cells[i][j - 1])
            

    def _bfs_check_goal(self, i, j):
        if i == self._num_rows - 1 and j == self._num_cols - 1:
            return True
            
    def _bfs_get_path(self, map, current_coord):
        path = []
        while current_coord is not None:
            path_to_add = []
            path_to_add.append(current_coord)
            current_coord = map[current_coord]
            path_to_add.append(current_coord)
            path.append(path_to_add)
        for each_path in path:
            print(each_path)
            if each_path[1] is not None:
                self._cells[each_path[0][0]][each_path[0][1]].draw_move(self._cells[each_path[1][0]][each_path[1][1]], undo=True)
            else:
                return
        return
        

