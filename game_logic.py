# game_logic.py

import random

remove_piece = False
move_piece = False
moved_x = 0
moved_y = 0

def get_neighbors(board, x, y):
    selected_point = getattr(board, 'point_' + str(x) + str(y))
    pointleft, pointmiddle, pointright = get_horizontal_line(board, x, y)
    pointup, pointcenter, pointbottom = get_vertical_line(board, x, y)
    if selected_point is not pointcenter:
        if selected_point is not pointmiddle:
            return [pointmiddle, pointcenter]
        else:
            return [pointleft, pointright, pointcenter]
    else:
        if selected_point is not pointmiddle:
            return [pointmiddle, pointup, pointbottom]
        else:
            return [pointleft, pointright, pointup, pointbottom]


def get_horizontal_line(board, x, y):
    if x == 0:
        return (board.point_00, board.point_03, board.point_06)
    elif x == 1:
        return (board.point_11, board.point_13, board.point_15)
    elif x == 2:
        return (board.point_22, board.point_23, board.point_24)
    elif x == 3:
        if y <=2:
            return (board.point_30, board.point_31, board.point_32)
        elif y >= 4:
            return (board.point_34, board.point_35, board.point_36)
    elif x == 4:
        return (board.point_42, board.point_43, board.point_44)
    elif x == 5:
        return (board.point_51, board.point_53, board.point_55)
    elif x == 6:    
        return (board.point_60, board.point_63, board.point_66)


def get_vertical_line(board, x, y):
    if y == 0:
        return (board.point_00, board.point_30, board.point_60)
    elif y == 1:
        return (board.point_11, board.point_31, board.point_51)
    elif y == 2:
        return (board.point_22, board.point_32, board.point_42)
    elif y == 3:
        if x <=2:
            return (board.point_03, board.point_13, board.point_23)
        elif x >= 4:
            return (board.point_43, board.point_53, board.point_63)
    elif y == 4:
        return (board.point_24, board.point_34, board.point_44)
    elif y == 5:
        return (board.point_15, board.point_35, board.point_55)
    elif y == 6:    
        return (board.point_06, board.point_36, board.point_66)


def check_if_mill(board, x, y):
    chosen_point = getattr(board, 'point_' + str(x) + str(y))
    color = chosen_point.cget("bg")
    if color == "brown":
        return False

    # check for horizontal line
    pointleft, pointmiddle, pointright = get_horizontal_line(board, x, y)
    if pointleft.cget("bg") == color and pointmiddle.cget("bg") == color and pointright.cget("bg") == color:
        return True
    
    # check for vertical line
    pointup, pointcenter, pointbottom = get_vertical_line(board, x, y)
    if pointup.cget("bg") == color and pointcenter.cget("bg") == color and pointbottom.cget("bg") == color:
        return True

    return False


def button_clicked(board, x, y):
    global remove_piece
    global move_piece
    global moved_x
    global moved_y
    board.info2.configure(text="")
    print("Button:", x, y, "clicked!")
    clicked_point = getattr(board, 'point_' + str(x) + str(y))

    # remove piece
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
    # set new piece
    elif board.white_pieces_set < 9:
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
    # select position to move
    elif move_piece:
        neighbors = get_neighbors(board, moved_x, moved_y)
        for neighbor in neighbors:
            if neighbor is clicked_point and clicked_point.cget("bg") == "brown":
                good_move = True
        if good_move:
            move_piece = False
            clicked_point.configure(bg="white")
            old_point = getattr(board, 'point_' + str(moved_x) + str(moved_y))
            old_point.configure(bg="brown")
            if check_if_mill(board, x, y):
                board.info1.configure(text="Mühle! Bitte Stein entfernen!")
                remove_piece = True
            else:
                computers_turn(board)
        else:
            board.info2.configure(text="Stein kann hier nicht platziert werden!")
    # select piece to move
    else:
        if clicked_point.cget("bg") == "white":
            neighbors = get_neighbors(board, x, y)
            possible_to_move = False
            for neighbor in neighbors:
                if neighbor.cget("bg") == "brown":
                    possible_to_move = True
            if possible_to_move:
                moved_x = x
                moved_y = y
                clicked_point.configure(bg="blue")
                move_piece = True
            else:
                board.info2.configure(text="Stein kann nicht verschoben werden!")
        else:
            board.info2.configure(text="Bitte weißen Stein auswählen!")


def return_random_point(board, color):
    not_found = True
    point_list = ["00","03","06","11","13","15","22","23","24",\
                "30","31","32","34","35","36","42","43","44",\
                "51","53","55","60","63","66"]
    while not_found and point_list:
        random_string = random.choice(point_list)
        random_point = getattr(board, 'point_' + random_string)
        if random_point.cget("bg") == color:
            not_found = False
        else:
            point_list.remove(random_string)
    if point_list:
        return random_point
    else:
        return None


def return_random_point_without_mill(board, color):
    not_found = True
    point_list = ["00","03","06","11","13","15","22","23","24",\
                "30","31","32","34","35","36","42","43","44",\
                "51","53","55","60","63","66"]
    while not_found and point_list:
        random_string = random.choice(point_list)
        random_point = getattr(board, 'point_' + random_string)
        if random_point.cget("bg") == color and not check_if_mill(board,int(random_string[0]),int(random_string[1])):
            not_found = False
        else:
            point_list.remove(random_string)
    if point_list:
        return random_point
    else:
        return None


def computers_turn(board):
    print("Computers Turn")
    point_list = ["00","03","06","11","13","15","22","23","24",\
                "30","31","32","34","35","36","42","43","44",\
                "51","53","55","60","63","66"]

    if board.black_pieces_set < 9:
        # Search empty point
        random_point = return_random_point(board, "brown")
        random_point.configure(bg="black")
        board.black_pieces_board = board.black_pieces_board + 1
        board.black_pieces_set = board.black_pieces_set + 1
        # check if mill
        if check_if_mill(board,random_point.x,random_point.y):
            # search for white
            second_random_point = return_random_point_without_mill(board, "white")
            if second_random_point:
                second_random_point.configure(bg="brown")
                board.white_pieces_board = board.white_pieces_board - 1
    else:
        pass


