# start_game.py

import draw_playboard as draw

window = draw.generate_window()
draw.globalwindow = window
board = draw.playboard()
draw.draw_buttons(board, window)

print("Program finished")