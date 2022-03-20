import re

class Solution:
    height_map = []


    def __init__(self):
        reader = open('input.txt')
        input = reader.read().splitlines()
        for i in input:
            self.height_map.append([int(x) for x in i])
        self.grid_height = len(input)
        self.grid_width = len(self.height_map[0])


    def find_low_points(self):
        low_points =[]
        low_coordinates = []
        for i in range(0, self.grid_height):
            for j in range(0, self.grid_width):
                current = self.height_map[i][j]
                points = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                adjacent_values = []
                for x, y in points:
                    if x in range(0, self.grid_height) and y in range(0, self.grid_width):
                        adjacent_values.append(self.height_map[x][y])
                if current < min(adjacent_values):
                    low_points.append(current)
                    low_coordinates.append((i, j))
        risk = sum(low_points) + len(low_points)
        return risk, low_coordinates

    def find_basin_size(self, basin):
        unresolved_points = basin.copy()
        resolved = set()

        while len(unresolved_points) != 0:
            i, j = unresolved_points.pop()
            resolved.add((i, j))
            points = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for x, y in points:
                if x in range(0, self.grid_height) and y in range(0, self.grid_width):
                    value = self.height_map[x][y]
                    if value != 9 and (x, y) not in resolved:
                        unresolved_points.add((x, y))
                        basin.add((x, y))
        return len(basin)






    def part_one(self):
        risk, low_coordinates = self.find_low_points()

        print("The answer to Day 8 part one is " + str(risk))

    def part_two(self):
        risk, low_coordinates = self.find_low_points()
        basin_sizes = [self.find_basin_size({(x, y)}) for x, y in low_coordinates]
        b = sorted(basin_sizes)
        first = b[-1]
        second = b[-2]
        third = b[-3]


        print("The answer to Day 6 part one is " + str(first*second*third))


sol = Solution()
sol.part_one()
sol.part_two()