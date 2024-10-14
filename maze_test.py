import unittest
from maze import *

class Test(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 6
        
        #Check if there are 12 squares in 1 row
        m1 = Maze(0,0, 6, 12, 10, 10)
        self.assertEqual(12, len(m1._cells[0]))
        
        #Check if there are 6 rows
        self.assertEqual(6, len(m1._cells))
        
        m2 = Maze(10, 32, 8, 15, 32, 10)
        self.assertEqual(8, len(m2._cells))
        self.assertEqual(15, len(m2._cells[0]))
        self.assertEqual(10, m2._x1)
        self.assertEqual(32, m2._y1)
        
        self.assertNotEqual(len(m1._cells), len(m2._cells))
        self.assertNotEqual(len(m1._cells[0]), len(m2._cells[0]))
        
if __name__ == "__main__":
    unittest.main()