import re


class Solution:

    def __init__(self):
        reader = open('input.txt')
        entries = reader.read().split("\n\n")
        number_order = entries[0]
        boards = []

        for i in range(1, len(entries)):
            board = []
            for row in entries[i].splitlines():
                numbers = [int(x) for x in re.findall(r"\d+", row)]
                board.append(numbers)

            boards.append(board)

        self.boards = boards
        self.numbers = [int(x) for x in re.findall(r"\d+", number_order)]

    def play_bingo(self, boards, numbers):
        playing_boards = boards.copy()
        winning_row = ['*', '*', '*', '*', '*']
        for n in numbers:
            for pb in playing_boards:
                number_found = False
                winner = False
                for i in range(0, 5):
                    for j in range(0, 5):
                        if pb[i][j] == n:
                            pb[i][j] = '*'
                            number_found = True
                if number_found:
                    for i in range(0, 5):
                        column = [row[i] for row in pb]
                        row = pb[i]
                        if row == winning_row or column == winning_row:
                            return self.find_score(pb, n)

    def find_loser(self, boards, numbers):
        playing_boards = boards.copy()

        winning_row = ['*', '*', '*', '*', '*']
        for n in numbers:
            to_remove = []
            for i in range(0, len(playing_boards)):
                pb = playing_boards[i]
                number_found = False
                for i in range(0, 5):
                    for j in range(0, 5):
                        if pb[j][i] == n:
                            pb[j][i] = '*'
                            number_found = True

                if number_found:
                    board_won = False
                    for i in range(0, 5):
                        column = [row[i] for row in pb]
                        row = pb[i]
                        if row == winning_row or column == winning_row:
                            board_won = True

                    if board_won:
                        to_remove.append(pb)
                        if len(playing_boards) == 1:
                            return self.find_score(pb, n)
            for r in to_remove:
                playing_boards.remove(r)

    def find_score(self, board, number):
        sum = 0
        for row in board:
            for entry in row:
                if entry != "*":
                    sum = sum + int(entry)

        return int(number) * sum

    def part_one(self):
        print(self.find_loser(self.boards, self.numbers))



sol = Solution()
sol.part_one()
