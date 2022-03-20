import re
import numpy


class Solution:
    def __init__(self):
        self.starting = 20151125


    def find_triangular(self, n):
        return (n * (n+1)) // 2


    def find_index(self, x, y):
        return self.find_triangular(y) + (self.find_triangular(y-1 + x-1) - self.find_triangular(y-1)) - 1

    def find_value(self, x, y):
        index = self.find_index(x, y)
        multiplier = 252533
        current_multiplier = 1
        modulo = 33554393
        for i in range(0, index):
            current_multiplier = (current_multiplier * multiplier) % modulo

        return (self.starting * current_multiplier) % modulo

    def part_one(self):
        answer = self.find_value(2978, 3083)
        print("The answer to Day 24 part one is " + str(answer))



sol = Solution()
sol.part_one()
