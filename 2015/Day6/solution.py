import numpy
import re


class Solution:
    lights = numpy.zeros((1000, 1000))

    def __init__(self):
        reader = open('input.txt')
        instructions = reader.read().splitlines()
        self.instructions = instructions

    def part_one(self):
        number_of_instructions = len(self.instructions)
        for i in range(0, number_of_instructions):
            instruction = self.instructions[i]
            coordinates = re.findall("\d+,\d+", instruction)
            lower = coordinates[0].split(",")
            higher = coordinates[1].split(",")

            lower_x = int(lower[0])
            lower_y = int(lower[1])
            higher_x = int(higher[0])
            higher_y = int(higher[1])

            if "turn on" in instruction:
                for x in range(lower_x, higher_x+1):
                    for y in range(lower_y, higher_y+1):
                        self.lights[x][y] = 1
            elif "turn off" in instruction:
                for x in range(lower_x, higher_x+1):
                    for y in range(lower_y, higher_y+1):
                        self.lights[x][y] = 0
            elif "toggle" in instruction:
                for x in range(lower_x, higher_x+1):
                    for y in range(lower_y, higher_y+1):
                        self.lights[x][y] = 1 - self.lights[x][y]

            else:
                print("cannot parse " + instruction)
        print("The answer to Day 6 part one is " + str(numpy.count_nonzero(self.lights)))



    def part_two(self):
        number_of_instructions = len(self.instructions)
        for i in range(0, number_of_instructions):
            instruction = self.instructions[i]
            coordinates = re.findall("\d+,\d+", instruction)
            lower = coordinates[0].split(",")
            higher = coordinates[1].split(",")

            lower_x = int(lower[0])
            lower_y = int(lower[1])
            higher_x = int(higher[0])
            higher_y = int(higher[1])

            if "turn on" in instruction:
                for x in range(lower_x, higher_x+1):
                    for y in range(lower_y, higher_y+1):
                        self.lights[x][y] = self.lights[x][y] + 1
            elif "turn off" in instruction:
                for x in range(lower_x, higher_x+1):
                    for y in range(lower_y, higher_y+1):
                        if not self.lights[x][y] == 0:
                          self.lights[x][y] = self.lights[x][y] - 1
            elif "toggle" in instruction:
                for x in range(lower_x, higher_x+1):
                    for y in range(lower_y, higher_y+1):
                        self.lights[x][y] = self.lights[x][y] + 2

            else:
                print("cannot parse " + instruction)
        print("The answer to Day 6 part one is " + str(numpy.sum(self.lights)))

sol = Solution()
sol.part_one()
sol.part_two()
