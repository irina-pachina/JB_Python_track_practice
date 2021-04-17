
import itertools
import random
import re


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

    def max_piece(self, piece):
        return piece[0] + piece[1]

    def start_set(self):
        # 28 unique dominoes with integer numbers that can range from 0 to 6
        self.full_set = [list(n) for n in itertools.combinations_with_replacement(range(7), 2)]
        # each player gets 7 pieces and the rest 14 is in stock
        random.shuffle(self.full_set)
        self.stock_pieces = self.full_set[:14]
        self.player_pieces = self.full_set[14:21]
        self.comp_pieces = self.full_set[21:]
        # player that have the highest domino domino starts a snake, i.e. max sum of numbers on a piece
        self.player_pieces.sort(key=self.max_piece, reverse=True)
        self.comp_pieces.sort(key=self.max_piece, reverse=True)

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
        # if snake is too long preview with 3 outer pieces is printed
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
        # "0" is to take a piece from the stock if it's not empty or skip a turn
        if move == "0":
            remain = len(self.stock_pieces)
            if remain > 0:
                self.player_pieces.append(self.stock_pieces.pop(random.randrange(remain)))
                self.status = "computer"
            else:
                self.status = "computer"
        # player enters piece number from their hand and side "-" if they want to add to the head, i.e. "2", "-6"
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

    # "draw" state is archived when the numbers on the ends of the snake are identical and appear within the snake 8 times
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

    # to check if piece can be added to preferred side
    def legal_move(self, piece, side):
        if side == "left" and self.domino_snake[0][0] in piece or side == "right" and self.domino_snake[-1][1] in piece:
            return True
        else:
            return False

    # to check if piece can be added as it is or needs a reverse
    def orientation(self, piece, side):
        if side == "left" and piece[1] == self.domino_snake[0][0] or side == "right" and piece[0] == self.domino_snake[-1][1]:
            return True
        else:
            return False

    # count the number of 0's, 1's, 2's, etc., in player's hand, and in the snake
    def count_numbers(self, domino_snake, hand):
        for piece in itertools.chain(hand, domino_snake):
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

    # to sort pieces in hand by the sum of appearances of each of its numbers
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
