# start_game.py

import draw_playboard as draw
import yolo5
import threading


window = draw.generate_window()
draw.globalwindow = window
board = draw.playboard()
threading._start_new_thread(yolo5.start_yolo5, ("yolo5", board))
draw.draw_buttons(board, window)


print("Program finished")