import collections

import numpy as np
import re


class Solution:

    def __init__(self):
        reader = open('input.txt')
        input = reader.read().split("\n\n")
        self.enhancement = [c for c in input[0]]
        self.image = np.array([list(x) for x in input[1].splitlines()])


    def enhance(self, image, char):
        padded_image = np.pad(image, ((2, 2), (2, 2)), 'constant', constant_values=char)
        new_image = []
        for i in range(1, len(padded_image)-1):
            row = []
            padded_row = padded_image[i]
            for j in range(1, len(padded_row) -1):
                square = padded_image[i-1:i+2,j-1:j+2]
                line = square.flatten()
                line_string = ''.join(line)
                line_string = line_string.replace("#", '1')
                line_string = line_string.replace(".", '0')
                new_char = self.enhancement[int(line_string, 2)]
                row.append(new_char)
            new_image.append(row)
        return new_image

    def part_one(self):
        new_image = self.enhance(self.image, '.')
        new_image = self.enhance(new_image, '#')
        count = sum([i.count('#') for i in new_image])

        print("The answer to Day 19 part one is " + str(count))

    def part_two(self):
        new_image = self.image.copy()
        for i in range(0, 50):
            if i % 2 == 0:
                char = '.'
            else:
                char = '#'
            new_image = self.enhance(new_image, char)
        count = sum([i.count('#') for i in new_image])

        print("The answer to Day 19 part two is " + str(count))

sol = Solution()
sol.part_one()
sol.part_two()
