import itertools
import random
import re


# 1
# def max_piece(piece):
#     return piece[0] + piece[1]
#
#
# full_set = [list(n) for n in itertools.combinations_with_replacement(range(7), 2)]
#
# random.shuffle(full_set)
# stock_pieces = full_set[:14]
# player_pieces = full_set[14:21]
# comp_pieces = full_set[21:]
#
# player_pieces.sort(key=max_piece, reverse=True)
# comp_pieces.sort(key=max_piece, reverse=True)
#
# max_player = player_pieces[0]
# max_comp = comp_pieces[0]
#
# domino_snake =[]
# if max_comp[0] + max_comp[1] > max_player[0] + max_player[1]:
#     domino_snake.append(comp_pieces.pop(0))
#     status = "player"
# else:
#     domino_snake.append(player_pieces.pop(0))
#     status = "computer"
#
# print(f"""Stock pieces: {stock_pieces}
# Computer pieces: {comp_pieces}
# player pieces: {player_pieces}
# Domino snake: {domino_snake}
# Status: {status}""")


# 2
# def max_piece(piece):
#     return piece[0] + piece[1]
#
#
# class Domino:
#     def __init__(self):
#         self.full_set = []
#         self.stock_pieces = []
#         self.player_pieces = []
#         self.comp_pieces = []
#         self.domino_snake = []
#         self.status = ""
#
#     def start_set(self):
#         self.full_set = [list(n) for n in itertools.combinations_with_replacement(range(7), 2)]
#
#         random.shuffle(self.full_set)
#         self.stock_pieces = self.full_set[:14]
#         self.player_pieces = self.full_set[14:21]
#         self.comp_pieces = self.full_set[21:]
#
#         self.player_pieces.sort(key=max_piece, reverse=True)
#         self.comp_pieces.sort(key=max_piece, reverse=True)
#
#         max_player = self.player_pieces[0]
#         max_comp = self.comp_pieces[0]
#
#         if max_comp[0] + max_comp[1] > max_player[0] + max_player[1]:
#             self.domino_snake.append(self.comp_pieces.pop(0))
#             self.status = "player"
#         else:
#             self.domino_snake.append(self.player_pieces.pop(0))
#             self.status = "computer"
#
#     def state(self):
#         print(f"""Stock size: {len(self.stock_pieces)}
# Computer pieces: {len(self.comp_pieces)}\n
# {self.domino_snake}\n
# Your pieces:""")
#         for i, n in enumerate(self.player_pieces):
#             print(f"{i+1}:{n}")
#         if self.status == "player":
#             print("\nStatus: It's your turn to make a move. Enter your command.")
#         else:
#             print("\nStatus: Computer is about to make a move. Press Enter to continue...")
#
#
# domino = Domino()
# domino.start_set()
# print("=" * 70)
# domino.state()

# 3
# def max_piece(piece):
#     return piece[0] + piece[1]
#
#
# class Domino:
#     def __init__(self):
#         self.full_set = []
#         self.stock_pieces = []
#         self.player_pieces = []
#         self.comp_pieces = []
#         self.domino_snake = []
#         self.status = ""
#         self.end_game = False
#
#     def start_set(self):
#         self.full_set = [list(n) for n in itertools.combinations_with_replacement(range(7), 2)]
#
#         random.shuffle(self.full_set)
#         self.stock_pieces = self.full_set[:14]
#         self.player_pieces = self.full_set[14:21]
#         self.comp_pieces = self.full_set[21:]
#
#         self.player_pieces.sort(key=max_piece, reverse=True)
#         self.comp_pieces.sort(key=max_piece, reverse=True)
#
#         max_player = self.player_pieces[0]
#         max_comp = self.comp_pieces[0]
#
#         if max_comp[0] + max_comp[1] > max_player[0] + max_player[1]:
#             self.domino_snake.append(self.comp_pieces.pop(0))
#             self.status = "player"
#         else:
#             self.domino_snake.append(self.player_pieces.pop(0))
#             self.status = "computer"
#
#     def state(self):
#         print("=" * 70)
#         print(f"""Stock size: {len(self.stock_pieces)}
# Computer pieces: {len(self.comp_pieces)}\n""")
#         if len(self.domino_snake) <= 6:
#             print(*self.domino_snake, sep="")
#         else:
#             print(*self.domino_snake[:3], sep="", end="")
#             print("...", sep="", end="")
#             print(*self.domino_snake[-3:], sep="")
#         print("\nYour pieces:")
#         for i, n in enumerate(self.player_pieces):
#             print(f"{i+1}:{n}")
#         if self.end_game and self.status == "player":
#             print("Status: The game is over. You won!")
#             exit()
#         elif self.end_game and self.status == "computer":
#             print("Status: The game is over. The computer won!")
#             exit()
#         elif self.end_game and self.status == "draw":
#             print("Status: The game is over. It's a draw!")
#             exit()
#         elif self.status == "player":
#             print("\nStatus: It's your turn to make a move. Enter your command.")
#             self.player_move()
#         else:
#             print("\n: Computer is about to make a move. Press Enter to continue...")
#             self.comp_move()
#
#     def player_move(self):
#         move = input()
#         if move == "0":
#             remain = len(self.stock_pieces)
#             if remain > 0:
#                 self.player_pieces.append(self.stock_pieces.pop(random.randrange(remain)))
#                 self.status = "computer"
#             else:
#                 print("There are no pieces in stock. Choose from your pieces")
#                 self.player_move()
#         elif re.match(r"-?\d", move) and abs(int(move)) <= len(self.player_pieces):
#             index = abs(int(move)) - 1
#             if move[0] == "-":
#                 self.domino_snake.insert(0, self.player_pieces.pop(index))
#             else:
#                 self.domino_snake.append(self.player_pieces.pop(index))
#             if len(self.player_pieces) == 0:
#                 self.end_game = True
#             elif self.sum_same() == 8:
#                 self.status = "draw"
#                 self.end_game = True
#             else:
#                 self.status = "computer"
#         else:
#             print("Invalid input. Please try again.")
#             self.player_move()
#
#     def comp_move(self):
#         _enter = input()
#         index = random.randrange(len(self.comp_pieces))
#         side = random.choice("-+")
#         if side == "-":
#             self.domino_snake.insert(0, self.comp_pieces.pop(index))
#         else:
#             self.domino_snake.append(self.comp_pieces.pop(index))
#         if len(self.comp_pieces) == 0:
#             self.end_game = True
#         elif self.sum_same():
#             self.status = "draw"
#             self.end_game = True
#         else:
#             self.status = "player"
#
#     def sum_same(self):
#         sums = 0
#         if self.domino_snake[0][0] == self.domino_snake[-1][1]:
#             value = self.domino_snake[0][0]
#             sums = len([1 for item in self.domino_snake if item[0] == value or item[1] == value])
#         if sums == 8:
#             return True
#         else:
#             return False
#
#
# domino = Domino()
# domino.start_set()
# while 1:
#     domino.state()

# 4

# def max_piece(piece):
#     return piece[0] + piece[1]
#
#
# class Domino:
#     def __init__(self):
#         self.full_set = []
#         self.stock_pieces = []
#         self.player_pieces = []
#         self.comp_pieces = []
#         self.domino_snake = []
#         self.status = ""
#         self.end_game = False
#
#     def start_set(self):
#         self.full_set = [list(n) for n in itertools.combinations_with_replacement(range(7), 2)]
#
#         random.shuffle(self.full_set)
#         self.stock_pieces = self.full_set[:14]
#         self.player_pieces = self.full_set[14:21]
#         self.comp_pieces = self.full_set[21:]
#
#         self.player_pieces.sort(key=max_piece, reverse=True)
#         self.comp_pieces.sort(key=max_piece, reverse=True)
#
#         max_player = self.player_pieces[0]
#         max_comp = self.comp_pieces[0]
#
#         if max_comp[0] + max_comp[1] > max_player[0] + max_player[1]:
#             self.domino_snake.append(self.comp_pieces.pop(0))
#             self.status = "player"
#         else:
#             self.domino_snake.append(self.player_pieces.pop(0))
#             self.status = "computer"
#
#     def state(self):
#         print("=" * 70)
#         print(f"""Stock size: {len(self.stock_pieces)}
# Computer pieces: {len(self.comp_pieces)}\n""")
#         if len(self.domino_snake) <= 6:
#             print(*self.domino_snake, sep="")
#         else:
#             print(*self.domino_snake[:3], sep="", end="")
#             print("...", sep="", end="")
#             print(*self.domino_snake[-3:], sep="")
#         print("\nYour pieces:")
#         for i, n in enumerate(self.player_pieces, 1):
#             print(f"{i}:{n}")
#         if self.end_game and self.status == "player":
#             print("Status: The game is over. You won!")
#             exit()
#         elif self.end_game and self.status == "computer":
#             print("Status: The game is over. The computer won!")
#             exit()
#         elif self.end_game and self.status == "draw":
#             print("Status: The game is over. It's a draw!")
#             exit()
#         elif self.status == "player":
#             print("\nStatus: It's your turn to make a move. Enter your command.")
#             self.player_move()
#         else:
#             print("\nStatus: Computer is about to make a move. Press Enter to continue...")
#             input()
#             self.comp_move()
#
#     def player_move(self):
#         move = input()
#         if move == "0":
#             remain = len(self.stock_pieces)
#             if remain > 0:
#                 self.player_pieces.append(self.stock_pieces.pop(random.randrange(remain)))
#                 self.status = "computer"
#             else:
#                 print("There are no pieces in stock. Choose from your pieces")
#                 self.player_move()
#         elif re.match(r"-?\d", move) and abs(int(move)) <= len(self.player_pieces):
#             index = abs(int(move)) - 1
#             if move[0] == "-" and self.legal_move(self.player_pieces[index], "left"):
#                 if self.orientation(self.player_pieces[index], "left"):
#                     self.domino_snake.insert(0, self.player_pieces.pop(index))
#                 else:
#                     self.player_pieces[index].reverse()
#                     self.domino_snake.insert(0, self.player_pieces.pop(index))
#             elif self.legal_move(self.player_pieces[index], "right"):
#                 if self.orientation(self.player_pieces[index], "right"):
#                     self.domino_snake.append(self.player_pieces.pop(index))
#                 else:
#                     self.player_pieces[index].reverse()
#                     self.domino_snake.append(self.player_pieces.pop(index))
#             else:
#                 print("Illegal move. Please try again.")
#                 self.player_move()
#
#             if len(self.player_pieces) == 0:
#                 self.end_game = True
#             elif self.sum_same() == 8:
#                 self.status = "draw"
#                 self.end_game = True
#             else:
#                 self.status = "computer"
#         else:
#             print("Invalid input. Please try again.")
#             self.player_move()
#
#     def comp_move(self):
#         index = random.randrange(len(self.comp_pieces))
#         side = random.choice("-+")
#         if index == 0:
#             remain = len(self.stock_pieces)
#             if remain > 0:
#                 self.comp_pieces.append(self.stock_pieces.pop(random.randrange(remain)))
#                 self.status = "player"
#             else:
#                 self.comp_move()
#         else:
#             if side == "-" and self.legal_move(self.comp_pieces[index], "left"):
#                 if self.orientation(self.comp_pieces[index], "left"):
#                     self.domino_snake.insert(0, self.comp_pieces.pop(index))
#                 else:
#                     self.comp_pieces[index].reverse()
#                     self.domino_snake.insert(0, self.comp_pieces.pop(index))
#             elif self.legal_move(self.comp_pieces[index], "right"):
#                 if self.orientation(self.comp_pieces[index], "right"):
#                     self.domino_snake.append(self.comp_pieces.pop(index))
#                 else:
#                     self.comp_pieces[index].reverse()
#                     self.domino_snake.append(self.comp_pieces.pop(index))
#             else:
#                 self.comp_move()
#
#             if len(self.comp_pieces) == 0:
#                 self.end_game = True
#             elif self.sum_same():
#                 self.status = "draw"
#                 self.end_game = True
#             else:
#                 self.status = "player"
#
#     def sum_same(self):
#         sums = 0
#         if self.domino_snake[0][0] == self.domino_snake[-1][1]:
#             value = self.domino_snake[0][0]
#             sums = len([1 for item in self.domino_snake if item[0] == value or item[1] == value])
#         if sums == 8:
#             return True
#         else:
#             return False
#
#     def legal_move(self, piece, side):
#         if side == "left" and self.domino_snake[0][0] in piece or side == "right" and self.domino_snake[-1][1] in piece:
#             return True
#         else:
#             return False
#
#     def orientation(self, piece, side):
#         if side == "left" and piece[1] == self.domino_snake[0][0] or side == "right" and piece[0] == self.domino_snake[-1][1]:
#             return True
#         else:
#             return False
#
#
# domino = Domino()
# domino.start_set()
# while 1:
#     domino.state()

# 5

def max_piece(piece):
    return piece[0] + piece[1]


class Domino:
    def __init__(self):
        self.full_set = []
        self.stock_pieces = []
        self.player_pieces = []
        self.comp_pieces = []
        self.domino_snake = []
        self.status = ""
        self.end_game = False
        self.count = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}

    def start_set(self):
        self.full_set = [list(n) for n in itertools.combinations_with_replacement(range(7), 2)]

        random.shuffle(self.full_set)
        self.stock_pieces = self.full_set[:14]
        self.player_pieces = self.full_set[14:21]
        self.comp_pieces = self.full_set[21:]

        self.player_pieces.sort(key=max_piece, reverse=True)
        self.comp_pieces.sort(key=max_piece, reverse=True)

        max_player = self.player_pieces[0]
        max_comp = self.comp_pieces[0]

        if max_comp[0] + max_comp[1] > max_player[0] + max_player[1]:
            self.domino_snake.append(self.comp_pieces.pop(0))
            self.status = "player"
        else:
            self.domino_snake.append(self.player_pieces.pop(0))
            self.status = "computer"

    def state(self):
        print("=" * 70)
        print(f"""Stock size: {len(self.stock_pieces)}
Computer pieces: {len(self.comp_pieces)}\n""")
        if len(self.domino_snake) <= 6:
            print(*self.domino_snake, sep="")
        else:
            print(*self.domino_snake[:3], sep="", end="")
            print("...", sep="", end="")
            print(*self.domino_snake[-3:], sep="")
        print("\nYour pieces:")
        for i, n in enumerate(self.player_pieces, 1):
            print(f"{i}:{n}")
        if self.end_game and self.status == "player":
            print("Status: The game is over. You won!")
            exit()
        elif self.end_game and self.status == "computer":
            print("Status: The game is over. The computer won!")
            exit()
        elif self.end_game and self.status == "draw":
            print("Status: The game is over. It's a draw!")
            exit()
        elif self.status == "player":
            print("\nStatus: It's your turn to make a move. Enter your command.")
            self.player_move()
        else:
            print("\nStatus: Computer is about to make a move. Press Enter to continue...")
            input()
            self.comp_move()

    def player_move(self):
        move = input()
        if move == "0":
            remain = len(self.stock_pieces)
            if remain > 0:
                self.player_pieces.append(self.stock_pieces.pop(random.randrange(remain)))
                self.status = "computer"
            else:
                self.status = "computer"
        elif re.match(r"-?\d", move) and abs(int(move)) <= len(self.player_pieces):
            index = abs(int(move)) - 1
            if move[0] == "-" and self.legal_move(self.player_pieces[index], "left"):
                if self.orientation(self.player_pieces[index], "left"):
                    self.domino_snake.insert(0, self.player_pieces.pop(index))
                else:
                    self.player_pieces[index].reverse()
                    self.domino_snake.insert(0, self.player_pieces.pop(index))
            elif self.legal_move(self.player_pieces[index], "right"):
                if self.orientation(self.player_pieces[index], "right"):
                    self.domino_snake.append(self.player_pieces.pop(index))
                else:
                    self.player_pieces[index].reverse()
                    self.domino_snake.append(self.player_pieces.pop(index))
            else:
                print("Illegal move. Please try again.")
                self.player_move()

            if len(self.player_pieces) == 0:
                self.end_game = True
            elif self.sum_same():
                self.status = "draw"
                self.end_game = True
            else:
                self.status = "computer"
        else:
            print("Invalid input. Please try again.")
            self.player_move()

    def comp_move(self):
        # each domino in computer hand receives a score equal to the sum of appearances of each of its numbers in its hand, and in the snake
        self.count_numbers(self.domino_snake, self.comp_pieces)
        self.comp_pieces.sort(key=self.count_score, reverse=True)
        move_done = False
        # trying each piece for both sides
        for i, piece in enumerate(self.comp_pieces):
            if self.legal_move(piece, "left"):
                if self.orientation(piece, "left"):
                    self.domino_snake.insert(0, self.comp_pieces.pop(i))
                    move_done = True
                    break
                else:
                    self.comp_pieces[i].reverse()
                    self.domino_snake.insert(0, self.comp_pieces.pop(i))
                    move_done = True
                    break
            elif self.legal_move(piece, "right"):
                if self.orientation(piece, "right"):
                    self.domino_snake.append(self.comp_pieces.pop(i))
                    move_done = True
                    break
                else:
                    self.comp_pieces[i].reverse()
                    self.domino_snake.append(self.comp_pieces.pop(i))
                    move_done = True
                    break

        if move_done:
            if len(self.comp_pieces) == 0:
                self.end_game = True
            elif self.sum_same():
                self.status = "draw"
                self.end_game = True
            else:
                self.status = "player"
        # if no piece is playable computer skips a turn by taking a piece from stock
        else:
            remain = len(self.stock_pieces)
            if remain > 0:
                self.comp_pieces.append(self.stock_pieces.pop(random.randrange(remain)))
                self.status = "player"
            else:
                self.status = "player"

    def sum_same(self):
        sums = 0
        if self.domino_snake[0][0] == self.domino_snake[-1][1]:
            value = self.domino_snake[0][0]
            for i in itertools.chain(*self.domino_snake):
                if i == value:
                    sums += 1
        if sums == 8:
            return True
        else:
            return False

    def legal_move(self, piece, side):
        if side == "left" and self.domino_snake[0][0] in piece or side == "right" and self.domino_snake[-1][1] in piece:
            return True
        else:
            return False

    def orientation(self, piece, side):
        if side == "left" and piece[1] == self.domino_snake[0][0] or side == "right" and piece[0] == self.domino_snake[-1][1]:
            return True
        else:
            return False

    def count_numbers(self, domino_snake, comp_pieces):
        for piece in itertools.chain(comp_pieces, domino_snake):
            for i in piece:
                if i == 0:
                    self.count["0"] += 1
                elif i == 1:
                    self.count["1"] += 1
                elif i == 2:
                    self.count["2"] += 1
                elif i == 3:
                    self.count["3"] += 1
                elif i == 4:
                    self.count["4"] += 1
                elif i == 5:
                    self.count["5"] += 1
                elif i == 6:
                    self.count["6"] += 1

    def count_score(self, piece):
        score = 0
        for i in piece:
            for key, value in self.count.items():
                if i == int(key):
                    score += value
        return score


domino = Domino()
domino.start_set()
while 1:
    domino.state()
