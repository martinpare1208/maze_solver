from window import *
from cell import *
from maze import *


def main():
    # cell_test = Cell(True, True, True, True, 0, 100, 0, 100, win=win)
    # cell_test.draw()
    
    # c1 = Cell(win)
    # c1.has_right_wall = False
    # c1.draw(50, 50, 100, 100)

    # c2 = Cell(win)
    # c2.has_left_wall = False
    # c2.has_bottom_wall = False
    # c2.draw(100, 50, 150, 100)

    # c1.draw_move(c2)

    # c3 = Cell(win)
    # c3.has_top_wall = False
    # c3.has_right_wall = False
    # c3.draw(100, 100, 150, 150)

    # c2.draw_move(c3)

    # c4 = Cell(win)
    # c4.has_left_wall = False
    # c4.draw(150, 100, 200, 150)

    # c3.draw_move(c4, True)
    num_rows = 5
    num_cols = 5
    offset = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * offset) / num_cols
    cell_size_y = (screen_y - 2 * offset) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(offset, offset, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze._break_entrance_and_exit()
    win.wait_for_close()


main()