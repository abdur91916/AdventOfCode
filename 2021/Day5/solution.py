import re
import numpy as np

class Solution:


    def __init__(self):
        self.map = np.zeros((1000, 1000))
        reader = open('input.txt')
        lines = reader.read().splitlines()
        line_vecotos = []
        for line in lines:
            numbers_in_vector = [int(x) for x in re.findall(r"\d+", line)]
            x1, y1 = numbers_in_vector[0], numbers_in_vector[1]
            x2, y2 = numbers_in_vector[2], numbers_in_vector[3]
            vector = [(x1,y1), (x2,y2)]
            line_vecotos.append(vector)

        self.line_vecotos = line_vecotos


    def populate_map_with_straight_lines(self):
        for l in self.line_vecotos:
            x1, y1 = l[0]
            x2, y2 = l[1]

            if x1 == x2:
                if y1 > y2:
                    y1, y2 = y2, y1
                for y in range(y1, y2+1):
                    self.map[x1][y] = self.map[x1][y] + 1
            elif y1 == y2:
                if x1 > x2:
                    x1, x2 = x2, x1
                for x in range(x1, x2+1):
                    self.map[x][y1] = self.map[x][y1] + 1


    def populate_map_with_horiz_lines(self):
        for l in self.line_vecotos:
            x1, y1 = l[0]
            x2, y2 = l[1]

            if x1 != x2 and y1 != y2:
                x_step = 1
                y_step = 1
                current_x = x1
                current_y = y1

                if x1 > x2:
                    x_step = -1
                if y1 > y2:
                    y_step = -1
                self.map[current_x][current_y] = self.map[current_x][current_y] + 1
                while current_x != x2 and current_y != y2:
                    current_x = current_x + x_step
                    current_y = current_y + y_step
                    self.map[current_x][current_y] = self.map[current_x][current_y] + 1

    def part_one(self):
        self.populate_map_with_straight_lines()
        sum = (np.asarray(self.map) > 1).sum()
        print("The answer to Day 5 part one is " + str(sum))


    def part_two(self):
        self.populate_map_with_horiz_lines()
        sum = (np.asarray(self.map) > 1).sum()
        print("The answer to Day 14 part two is " + str(sum))


sol = Solution()
sol.part_one()
sol.part_two()
