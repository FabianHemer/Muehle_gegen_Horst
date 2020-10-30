# game_logic.py

import random

remove_piece = False

def check_if_mill(board, x, y):
    chosen_point = getattr(board, 'point_' + str(x) + str(y))
    color = chosen_point.cget("bg")
    if color == "brown":
        return False

    # check for horizontal line
    if x == 0:
        if board.point_00.cget("bg") == color and board.point_03.cget("bg") == color and board.point_06.cget("bg") == color:
            return True
    elif x == 1:
        if board.point_11.cget("bg") == color and board.point_13.cget("bg") == color and board.point_15.cget("bg") == color:
            return True
    elif x == 2:
        if board.point_22.cget("bg") == color and board.point_23.cget("bg") == color and board.point_24.cget("bg") == color:
            return True
    elif x == 3:
        if y <=2:
            if board.point_30.cget("bg") == color and board.point_31.cget("bg") == color and board.point_32.cget("bg") == color:
                return True
        elif y >= 4:
            if board.point_34.cget("bg") == color and board.point_35.cget("bg") == color and board.point_36.cget("bg") == color:
                return True
    elif x == 4:
        if board.point_42.cget("bg") == color and board.point_43.cget("bg") == color and board.point_44.cget("bg") == color:
            return True
    elif x == 5:
        if board.point_51.cget("bg") == color and board.point_53.cget("bg") == color and board.point_55.cget("bg") == color:
            return True
    elif x == 6:    
        if board.point_60.cget("bg") == color and board.point_63.cget("bg") == color and board.point_66.cget("bg") == color:
            return True
    
    # check for vertical line
    if y == 0:
        if board.point_00.cget("bg") == color and board.point_30.cget("bg") == color and board.point_60.cget("bg") == color:
            return True
    elif y == 1:
        if board.point_11.cget("bg") == color and board.point_31.cget("bg") == color and board.point_51.cget("bg") == color:
            return True
    elif y == 2:
        if board.point_22.cget("bg") == color and board.point_32.cget("bg") == color and board.point_42.cget("bg") == color:
            return True
    elif y == 3:
        if x <=2:
            if board.point_03.cget("bg") == color and board.point_13.cget("bg") == color and board.point_23.cget("bg") == color:
                return True
        elif x >= 4:
            if board.point_43.cget("bg") == color and board.point_53.cget("bg") == color and board.point_63.cget("bg") == color:
                return True
    elif y == 4:
        if board.point_24.cget("bg") == color and board.point_34.cget("bg") == color and board.point_44.cget("bg") == color:
            return True
    elif y == 5:
        if board.point_15.cget("bg") == color and board.point_35.cget("bg") == color and board.point_55.cget("bg") == color:
            return True
    elif y == 6:    
        if board.point_06.cget("bg") == color and board.point_36.cget("bg") == color and board.point_66.cget("bg") == color:
            return True

    return False


def button_clicked(board, x, y):
    global remove_piece
    board.info2.configure(text="")
    print("Button:", x, y, "clicked!")
    clicked_point = getattr(board, 'point_' + str(x) + str(y))

    if remove_piece:
        if clicked_point.cget("bg") == "black":
            if check_if_mill(board, x, y):
                board.info2.configure(text="Stein nicht möglich!")
            else:
                clicked_point.configure(bg="brown")
                board.black_pieces_board = board.black_pieces_board - 1
                remove_piece = False
                board.info1.configure(text="Bitte Stein setzen!")
                if board.black_pieces_board < 3 and board.black_pieces_set == 9:
                    print("Mensch gewonnen")
                computers_turn(board)
        else:
            board.info2.configure(text="Falscher Stein!")

    elif board.white_pieces_set < 9:
        # Setzphase
        if clicked_point.cget("bg") == "brown":
            clicked_point.configure(bg="white")
            board.white_pieces_set = board.white_pieces_set + 1
            board.white_pieces_board = board.white_pieces_board + 1
            if check_if_mill(board, x, y):
                board.info1.configure(text="Mühle! Bitte Stein entfernen!")
                remove_piece = True
            else:
                computers_turn(board)
        else:
            board.info2.configure(text="Zug nicht möglich!")
    else:
        pass



def computers_turn(board):
    print("Computers Turn")
    point_list = ["00","03","06","11","13","15","22","23","24",\
                "30","31","32","34","35","36","42","43","44",\
                "51","53","55","60","63","66"]

    if board.black_pieces_set < 9:
        # Search empty point
        brown_not_found = True
        white_not_found = True
        while brown_not_found:
            random_string = random.choice(point_list)
            random_point = getattr(board, 'point_' + random_string)
            if random_point.cget("bg") == "brown":
                brown_not_found = False
        random_point.configure(bg="black")
        board.black_pieces_board = board.black_pieces_board + 1
        board.black_pieces_set = board.black_pieces_set + 1
        # check if mill
        if check_if_mill(board,int(random_string[0]),int(random_string[1])):
            # search for white
            while white_not_found:
                second_random_string = random.choice(point_list)
                second_random_point = getattr(board, 'point_' + second_random_string)
                if second_random_point.cget("bg") == "white":
                    # check if white is in mill
                    if not check_if_mill(board,int(second_random_string[0]),int(second_random_string[1])):
                        second_random_point.configure(bg="brown")
                        board.white_pieces_board = board.white_pieces_board - 1
                        white_not_found = False
    else:
        pass


