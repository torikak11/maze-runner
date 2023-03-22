from window import Window
from line import Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    cell = Cell(True, False, True, True, 2, 2, 102, 102, win)
    cell2 = Cell(False, True, True, True, 102, 2, 204, 102, win)
    cell.draw("purple")
    cell2.draw("green")
    cell.draw_move(cell2)
    win.wait_for_close()

main()