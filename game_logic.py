# game_logic.py

import random


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


def return_random_point_to_move(board, color):
    not_found = True
    point_list = ["00","03","06","11","13","15","22","23","24",\
                "30","31","32","34","35","36","42","43","44",\
                "51","53","55","60","63","66"]
    while not_found and point_list:
        random_string = random.choice(point_list)
        random_point = getattr(board, 'point_' + random_string)
        if random_point.cget("bg") == color:
            neighbors = get_neighbors(board, random_point.x, random_point.y)
            possible_to_move = False
            for neighbor in neighbors:
                if neighbor.cget("bg") == "brown":
                    possible_to_move = True
            if possible_to_move:
                not_found = False
            else:
                point_list.remove(random_string)
        else:
            point_list.remove(random_string)
    if point_list:
        return random_point
    else:
        return None


def look_for_cpu_mill(board, x, y):
    # check if mill
    if check_if_mill(board,x,y):
        # search for human piece
        second_random_point = return_random_point_without_mill(board, board.human_is)
        if second_random_point:
            second_random_point.configure(bg="brown")
            board.human_pieces_board = board.human_pieces_board - 1
        else:
            second_random_point = return_random_point(board, board.human_is)
            second_random_point.configure(bg="brown")
            board.human_pieces_board = board.human_pieces_board - 1


def button_clicked(board, x, y):
    board.info2.configure(text="")
    print("Button:", x, y, "clicked!")
    clicked_point = getattr(board, 'point_' + str(x) + str(y))

    # remove piece
    if board.remove_piece:
        if clicked_point.cget("bg") == board.cpu_is:
            can_be_removed = True
            if check_if_mill(board, x, y):
                one_point = return_random_point_without_mill(board, board.cpu_is)
                if one_point:
                    board.info2.configure(text="Stein nicht möglich!")
                    can_be_removed = False
            if can_be_removed:
                clicked_point.configure(bg="brown")
                board.cpu_pieces_board = board.cpu_pieces_board - 1
                board.remove_piece = False
                if not (board.cpu_pieces_board < 3 and board.cpu_pieces_set == 9):
                    computers_turn(board)
        else:
            board.info2.configure(text="Falscher Stein!")
    # set new piece
    elif board.human_pieces_set < 9:
        if clicked_point.cget("bg") == "brown":
            clicked_point.configure(bg=board.human_is)
            board.human_pieces_set = board.human_pieces_set + 1
            board.human_pieces_board = board.human_pieces_board + 1
            if check_if_mill(board, x, y):
                board.remove_piece = True
            else:
                computers_turn(board)
        else:
            board.info2.configure(text="Stein kann hier nicht platziert werden!")
    # select position to move
    elif board.move_piece:
        good_move = False
        neighbors = get_neighbors(board, board.moved_x, board.moved_y)
        for neighbor in neighbors:
            if neighbor is clicked_point and clicked_point.cget("bg") == "brown":
                good_move = True
        if good_move:
            board.move_piece = False
            clicked_point.configure(bg=board.human_is)
            old_point = getattr(board, 'point_' + str(board.moved_x) + str(board.moved_y))
            old_point.configure(bg="brown")
            if check_if_mill(board, x, y):
                board.remove_piece = True
            else:
                computers_turn(board)
        else:
            board.info2.configure(text="Stein kann hier nicht platziert werden!")
    # select position to jump
    elif board.jump_piece:
        if clicked_point.cget("bg") == "brown":
            board.jump_piece = False
            clicked_point.configure(bg=board.human_is)
            old_point = getattr(board, 'point_' + str(board.moved_x) + str(board.moved_y))
            old_point.configure(bg="brown")
            if check_if_mill(board, x, y):
                board.remove_piece = True
            else:
                computers_turn(board)
        else:
            board.info2.configure(text="Stein kann hier nicht platziert werden!")
    # select piece to move
    elif board.human_pieces_board > 3 and board.cpu_pieces_board >= 3 and board.win == 0:
        if clicked_point.cget("bg") == board.human_is:
            neighbors = get_neighbors(board, x, y)
            possible_to_move = False
            for neighbor in neighbors:
                if neighbor.cget("bg") == "brown":
                    possible_to_move = True
            if possible_to_move:
                board.moved_x = x
                board.moved_y = y
                clicked_point.configure(bg="blue")
                board.move_piece = True
            else:
                board.info2.configure(text="Stein kann nicht verschoben werden!")
        else:
            board.info2.configure(text="Bitte eigenen Stein auswählen!")
    # select piece to jump
    elif board.human_pieces_board == 3 and board.cpu_pieces_board >= 3 and board.win == 0:
        if clicked_point.cget("bg") == board.human_is:
            board.moved_x = x
            board.moved_y = y
            clicked_point.configure(bg="blue")
            board.jump_piece = True
        else:
            board.info2.configure(text="Bitte eigenen Stein auswählen!")
    # game finished
    else:
        board.info2.configure(text="Bitte neues Spiel starten!")

    # show info1
    if board.win == 1:
        board.info1.configure(text="Du hast gewonnen! CPU ist bewegungsunfähig!")
    elif board.win == 2:
        board.info1.configure(text="Du hast verloren! Spieler ist bewegungsunfähig!")
    elif board.remove_piece:
        board.info1.configure(text="Mühle! Bitte Stein entfernen!")
    elif board.human_pieces_set < 9:
        board.info1.configure(text="Bitte Stein setzen!")
    elif board.human_pieces_board > 3 and board.cpu_pieces_board >= 3:
        board.info1.configure(text="Bitte Stein schieben!")
    elif board.human_pieces_board == 3 and board.cpu_pieces_board >= 3:
        board.info1.configure(text="Bitte mit Stein springen!")
    elif board.human_pieces_board < 3:
        board.info1.configure(text="Du hast verloren! Spieler hat nur noch zwei Steine!")
    elif board.cpu_pieces_board < 3:
        board.info1.configure(text="Du hast gewonnen! CPU hat nur noch zwei Steine!")


def computers_turn(board):
    print("Computers Turn")

    # set cpu piece
    if board.cpu_pieces_set < 9:
        # Search empty point
        random_point = return_random_point(board, "brown")
        random_point.configure(bg=board.cpu_is)
        board.cpu_pieces_board = board.cpu_pieces_board + 1
        board.cpu_pieces_set = board.cpu_pieces_set + 1
        look_for_cpu_mill(board, random_point.x, random_point.y)
    else:
        # move cpu piece
        if board.cpu_pieces_board > 3:
            random_point = return_random_point_to_move(board, board.cpu_is)
            if random_point:
                neighbors = get_neighbors(board, random_point.x, random_point.y)
                for neighbor in neighbors:
                    if neighbor.cget("bg") == "brown":
                        random_point.configure(bg="brown")
                        neighbor.configure(bg=board.cpu_is)
                        break
                look_for_cpu_mill(board, neighbor.x, neighbor.y)
            else:
                board.info1.configure(text="Du hast gewonnen! Die CPU ist bewegungsunfähig!")
                board.win = 1
        # jump cpu piece
        else:
            first_point = return_random_point(board, board.cpu_is)
            second_point = return_random_point(board, "brown")
            first_point.configure(bg="brown")
            second_point.configure(bg=board.cpu_is)
            look_for_cpu_mill(board, second_point.x, second_point.y)

    # check if human can move
    if board.human_pieces_set == 9:
        human_point = return_random_point_to_move(board, board.human_is)
        if human_point is None:
            board.info1.configure(text="Du hast verloren! Der Spieler ist bewegungsunfähig!")
            board.win = 2
