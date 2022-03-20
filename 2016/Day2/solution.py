import re


class Solution:
    def __init__(self):
        reader = open('input.txt')
        instructions = reader.read().splitlines()
        self.instructions = instructions
        self.key_pad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.key_pad_2 = [['', '', '1', '', ''], ['', '2', '3', '4', ''], ['5', '6', '7', '8', '9'],
                          ['', 'A', 'B', 'C', ''], ['', '', 'D', '', '']]

    def find_code(self, key_pad, start_x, start_y):
        key = ''
        x = start_x
        y = start_y
        for i in self.instructions:
            for move in i:
                if move == "L":
                    x = x - 1 if self.is_valid(x-1, y, key_pad) else x
                elif move == "R":
                    x = x + 1 if self.is_valid(x+1, y, key_pad) else x
                elif move == "D":
                    y = y + 1 if self.is_valid(x, y+1, key_pad) else y
                elif move == "U":
                    y = y - 1 if self.is_valid(x, y-1, key_pad) else y
            button = key_pad[y][x]
            key = key + button
        return key

    def is_valid(self, x, y, key_pad):
        if x not in range(0, len(key_pad)) or y not in range(0, len(key_pad)):
            return False
        if key_pad[y][x] == '':
            return False
        return True

    def part_one(self):
        code = self.find_code(self.key_pad, 1, 1)

        print("The answer to Day 2 part one is " + code)

    def part_two(self):
        code = self.find_code(self.key_pad_2, 0, 2)
        print("The answer to Day 1 part two is " + code)


sol = Solution()
sol.part_one()
sol.part_two()
