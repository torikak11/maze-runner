from window import Window
from line import Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(5, 5, 18, 18, 40, 40, win)
    solvable = maze.solve()
    if solvable:
        print("maze solvable!")
    else:
        print("maze not solvable")
    win.wait_for_close()

main()