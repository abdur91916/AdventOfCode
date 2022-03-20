import numpy as np
import re

class Solution:

    def __init__(self):
        reader = open('input.txt')
        input = reader.read()
        input = input.split("\n\n")
        dots_input = input[0].splitlines()
        self.folds = input[1].splitlines()
        dots = []
        max_x = 0
        max_y = 0

        for d in dots_input:
            xy = d.split(',')
            x, y = int(xy[0]), int(xy[1])
            dots.append((x, y))

            max_x = x if x > max_x else max_x
            max_y = y if y > max_y else max_y

        self.paper = np.full((max_y+1, max_x+1), False)

        for x,y in dots:
            self.paper[y][x] = True


    def fold(self, paper, folds):
        for fold in folds:
            point = int(re.search(r'\d+', fold).group())
            array1 = []
            array2 = []
            height, length = paper.shape
            empty = np.full(paper.shape, False)
            if 'y=' in fold:
                array1 = paper[:point, :]
                array2 = paper[point+1:, :]
                array_2_size = len(array2)
                array2 = np.pad(array2, ((0, point-array_2_size), (0, 0)))
                array2 = np.flipud(array2)
            else:
                array1 = paper[:, :point]
                array2 = paper[:, point + 1:]
                array_2_size = len(array2[0])
                array2 = np.pad(paper[:, point + 1:], ((0,0), (0,point-array_2_size )))
                array2 = np.fliplr(array2)
            paper = array1 | array2

        return paper

    def map(self, x):
        return '#' if x else ' '



    def part_one(self):
        paper = self.fold(self.paper.copy(), [self.folds[0]])
        dots = np.count_nonzero(paper)

        print("The answer to Day 13 part one is " + str(dots))

    def part_two(self):
        paper = self.fold(self.paper.copy(), self.folds)
        dots = np.count_nonzero(paper)
        vfunc = np.vectorize(self.map)
        self.print_paper(vfunc(paper))

        print("The answer to Day 13 part twos is " + str(dots))

    def print_paper(self, paper):
        for row in paper:
            row_str = ""
            for entry in row:
                row_str += entry
            print(row_str)

sol = Solution()
sol.part_one()
sol.part_two()
