import numpy as np
import time

class Solution:

    def __init__(self):
        reader = open('input.txt')
        input = reader.read().splitlines()
        self.grid = []
        for line in input:
            row = []
            for i in line:
                row.append(int(i))
            self.grid.append(row)
        self.size = len(self.grid)
        self.shortest_path = np.full((self.size, self.size), 100*100*9)
        self.shortest_path[0][0] = 0

    def resolve(self):
        places_to_check = {(0, 0): 0}
        while len(places_to_check) != 0:
            i, j = min(places_to_check, key=places_to_check.get)
            del places_to_check[(i, j)]

            if i < self.size - 1:
                danger_total = self.shortest_path[i][j] + self.grid[i + 1][j]
                if danger_total < self.shortest_path[i + 1][j]:
                    self.shortest_path[i + 1][j] = danger_total
                    places_to_check[(i+1, j)] = danger_total

            if j < self.size - 1:
                danger_total = self.shortest_path[i][j] + self.grid[i][j + 1]
                if danger_total < self.shortest_path[i][j + 1]:
                    self.shortest_path[i][j + 1] = danger_total
                    places_to_check[(i, j+1)] = danger_total

            if i > 0:
                danger_total = self.shortest_path[i][j] + self.grid[i - 1][j]
                if danger_total < self.shortest_path[i - 1][j]:
                    self.shortest_path[i - 1][j] = danger_total
                    places_to_check[(i-1, j)] = danger_total

            if j > 0:
                danger_total = self.shortest_path[i][j] + self.grid[i][j - 1]
                if danger_total < self.shortest_path[i][j - 1]:
                    self.shortest_path[i][j - 1] = danger_total
                    places_to_check[(i, j-1)] = danger_total

    def find_full_map(self):
        tile = np.array(self.grid)
        first_row = tile.copy()
        for i in range(0, 4):
            next_tile = (tile.copy() % 9) + 1
            first_row = np.concatenate((first_row, next_tile), axis=1)
            tile = next_tile

        grid = first_row
        row = first_row
        for i in range(0, 4):
            next_row = (row.copy() % 9) + 1
            grid = np.concatenate((grid, next_row), axis=0)
            row = next_row
        self.grid = grid
        self.size = len(self.grid)
        self.shortest_path = np.full((self.size, self.size), 100 * 100 * 9 * 25)
        self.shortest_path[0][0] = 0


    def part_one(self):
        self.resolve()
        print("The answer to Day 15 part one is " + str(self.shortest_path[self.size-1][self.size-1]))

    def part_two(self):
        self.find_full_map()
        self.resolve()
        print("The answer to Day 14 part two is " + str(self.shortest_path[self.size-1][self.size-1]))

sol = Solution()
sol.part_one()
sol.part_two()

