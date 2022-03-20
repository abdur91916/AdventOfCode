import re

import numpy as np

class Solution:


    def __init__(self):
        reader = open('input.txt')
        self.instructrions = reader.read().splitlines()
        self.display = np.zeros((6,50))

    def parse_instructions(self, instructions):
        for i in instructions:
            params = [int(x) for x in re.findall(r'\d+', i)]
            if 'rect' in i:
                length = params[0]
                height = params[1]
                self.display[0:height, 0:length] = 1
            elif 'rotate row' in i:
                row_number = params[0]
                amount = params[1]
                self.display[row_number] = np.roll(self.display[row_number], amount)

            elif 'rotate column' in i:
                col_number = params[0]
                amount = params[1]
                self.display[:,col_number] = np.roll(self.display[:,col_number], amount)


    def print_display(self, display):
        string_display = np.char.mod('%d', display)
        string_display[string_display=="1"] = "#"
        string_display[string_display=="0"] = " "
        character = ''
        char_array = string_display
        for row in char_array:
            character = character + ''.join(row) + '\n'

        print(character)



    def part_one(self):
        self.parse_instructions(self.instructrions)
        count = np.count_nonzero(self.display)

        print("The answer to Day 8 part one is " + str(count))

    def part_two(self):
        self.print_display(self.display)





sol = Solution()
sol.part_one()
sol.part_two()
