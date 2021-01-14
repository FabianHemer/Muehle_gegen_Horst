import time
import os
import shutil

stones = [(0,0,"white"),(2,3,"black"),(6,6,"black")]

def start_yolo5 (threadName, board):
    global stones
    point_list = ["00","03","06","11","13","15","22","23","24",\
                "30","31","32","34","35","36","42","43","44",\
                "51","53","55","60","63","66"]
    while(True):
        time.sleep(5)
        print("yolo5 runs")
        changedstones = []
        equalstones = []

        for point in point_list:
            boardpoint = getattr(board, 'point_' + point)
            found = False
            for stone in stones:
                if boardpoint.x == stone[0]:
                    if boardpoint.y == stone[1]:
                        found = True
                        if boardpoint.cget("bg") == stone[2]:
                            equalstones.append(boardpoint)
                        else:
                            changedstones.append(boardpoint)

            if not found and boardpoint.cget("bg") != "brown":
                changedstones.append(boardpoint)
            if not found and boardpoint.cget("bg") == "brown":
                equalstones.append(boardpoint)
        print("Equal:", equalstones)
        print("Changed:", changedstones)
        

def load_board(board):
    global stones


def parse_yolo_to_points():
    #pathToRun = '/Users/fh/FH/Semester 6/Semesterprojekt 2/YOLOv5_Test/runs/detect/exp'
    #pathToLabelFile = pathToRun + '/labels/screenshot.txt'
    pathToLabelFile = 'C:/00Data/HFU/Semester6/Semesterprojekt/screenshot.txt'
    labelsFile = open(pathToLabelFile, 'r')
    myList = list()
    result = list()

    for line in labelsFile:
        lineSubStrings = line.split()
        myList.append((lineSubStrings[0], lineSubStrings[1], lineSubStrings[2]))

    for i in myList:
        myX = float(i[1])
        myY = float(i[2])
        myClass = "white"
        if i[0] == 0:
            myClass = "black"

        if 0.26 < myX < 0.33 and 0.86 < myY < 1:
            result.append((0, 0, myClass))
        elif 0.45 < myX < 0.52 and 0.86 < myY < 1:
            result.append((0, 3, myClass))
        elif 0.66 < myX < 0.75 and 0.86 < myY < 1:
            result.append((0, 6, myClass))
        
        elif 0.33 < myX < 0.39 and 0.75 < myY < 0.85:
            result.append((1, 1, myClass))
        elif 0.45 < myX < 0.52 and 0.75 < myY < 0.85:
            result.append((1, 3, myClass))
        elif 0.58 < myX < 0.66 and 0.75 < myY < 0.85:
            result.append((1, 5, myClass))

        elif 0.39 < myX < 0.45 and 0.60 < myY < 0.75:
            result.append((2, 2, myClass))
        elif 0.45 < myX < 0.52 and 0.60 < myY < 0.75:
            result.append((2, 3, myClass))
        elif 0.52 < myX < 0.58 and 0.60 < myY < 0.75:
            result.append((2, 4, myClass))

        elif 0.26 < myX < 0.33 and 0.45 < myY < 0.60:
            result.append((3, 0, myClass))
        elif 0.33 < myX < 0.39 and 0.45 < myY < 0.60:
            result.append((3, 1, myClass))
        elif 0.39 < myX < 0.45 and 0.45 < myY < 0.60:
            result.append((3, 2, myClass))
        elif 0.52 < myX < 0.58 and 0.45 < myY < 0.60:
            result.append((3, 4, myClass))
        elif 0.58 < myX < 0.66 and 0.45 < myY < 0.60:
            result.append((3, 5, myClass))
        elif 0.66 < myX < 0.75 and 0.45 < myY < 0.60:
            result.append((3, 6, myClass))

        elif 0.39 < myX < 0.45 and 0.30 < myY < 0.45:
            result.append((4, 2, myClass))
        elif 0.45 < myX < 0.52 and 0.30 < myY < 0.45:
            result.append((4, 3, myClass))
        elif 0.52 < myX < 0.58 and 0.30 < myY < 0.45:
            result.append((4, 4, myClass))
        
        elif 0.33 < myX < 0.39 and 0.15 < myY < 0.30:
            result.append((5, 1, myClass))
        elif 0.45 < myX < 0.52 and 0.15 < myY < 0.30:
            result.append((5, 3, myClass))
        elif 0.58 < myX < 0.66 and 0.15 < myY < 0.30:
            result.append((5, 5, myClass))

        elif 0.26 < myX < 0.33 and 0.00 < myY < 0.15:
            result.append((6, 0, myClass))
        elif 0.45 < myX < 0.52 and 0.00 < myY < 0.15:
            result.append((6, 3, myClass))
        elif 0.66 < myX < 0.75 and 0.00 < myY < 0.15:
            result.append((6, 6, myClass))

    labelsFile.close()
    shutil.rmtree(pathToRun, ignore_errors=True)