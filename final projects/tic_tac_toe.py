# implementation of the game of tic-tac-toe that two players can play from the beginning (with an empty grid)
# through to the end (until there is a draw, or one of the players wins)
# example test inputs = ["1 1", "1 2", "1 3", "2 1", "2 2", "2 3", "3 1"]

def printer(cells):
    print("---------")
    print("|", cells[0], cells[1], cells[2],"|")
    print("|", cells[3], cells[4], cells[5],"|")
    print("|", cells[6], cells[7], cells[8],"|")
    print("---------")


cells = "_________"

printer(cells)

matrix = [[x for x in cells[0:3]], [x for x in cells[3:6]], [x for x in cells[6:9]]]

global coordinates, coordinates_list, i, y


def enter():
    print("Enter the coordinates:")
    global coordinates, coordinates_list, i, y
    coordinates = input()

    coordinates_list = [x for x in coordinates.replace(" ", "") if x.isnumeric()]

    if coordinates_list:
        i = int(coordinates_list[0]) - 1
        y = int(coordinates_list[1]) - 1


# old function to check game state, used on the previous implementation step
# def checker(matrix, cells):
#     counter = 0
#     answer = ""
#     for i in range(3):
#         if matrix[i][0] == matrix[i][1] == matrix[i][2]:
#             answer = matrix[i][0] + " wins"
#             counter += 1
#     for i in range(3):
#         if matrix[0][i] == matrix[1][i] == matrix[2][i]:
#             answer = matrix[0][i] + " wins"
#             counter += 1
#
#     if matrix[1][1] == matrix[2][2] == matrix[0][0]:
#         answer = matrix[1][1] + " wins"
#         counter += 1
#     if matrix[1][1] == matrix[0][2] == matrix[2][0]:
#         answer = matrix[1][1] + " wins"
#         counter += 1
#
#     if abs(cells.count("X") - cells.count("O")) > 1 or counter > 1:
#         answer = "Impossible"
#         print(answer)
#     else:
#         print(answer)
#
#     if answer == "" and "_" not in cells:
#         print("Draw")
#     else:
#         print("Game not finished")


def checker(matrix, cells):
    counter = 0
    answer = ""
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] and matrix[i][0] != "_":
            answer = matrix[i][0] + " wins"
            counter += 1
    for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] and matrix[0][i] != "_":
            answer = matrix[0][i] + " wins"
            counter += 1

    if matrix[1][1] == matrix[2][2] == matrix[0][0] and matrix[1][1] != "_":
        answer = matrix[1][1] + " wins"
        counter += 1
    if matrix[1][1] == matrix[0][2] == matrix[2][0] and matrix[1][1] != "_":
        answer = matrix[1][1] + " wins"
        counter += 1

    if answer == "" and "_" not in cells:
        return "Draw"
    else:
        return answer


enter()
current_player = "X"
while 1:
    if not coordinates.replace(" ", "").isnumeric():
        print("You should enter numbers!")
        enter()
    elif [x for x in coordinates.replace(" ", "") if int(x) > 3]:
        print("Coordinates should be from 1 to 3!")
        enter()
    elif matrix[i][y] != "_":
        print("This cell is occupied! Choose another one!")
        enter()
    else:
        matrix[i][y] = current_player

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

        cells = ''.join([''.join(idx for idx in row) for row in matrix])
        printer(cells)
        if checker(matrix, cells) in ["X wins", "O wins", "Draw"]:
            print(checker(matrix, cells))
            break
        else:
            enter()
