import collections

import numpy as np
import re
from typing import NamedTuple


class Solution:
    steps = []
    sols = []

    def __init__(self):
        reader = open('input.txt')
        inp = reader.read().split("inp w")[1:]
        inp = [i[1:] for i in inp]
        self.input = [i.splitlines() for i in inp]
        # self.input = [i[1:] for i in self.input]
        for i in range(0,14):
            self.steps.append([])
        print()


    def find_combos(self):
        prev_z = {0}
        for i in range(0, len(self.input)):
            current_set = self.input[i]
            new_z = set()
            for n in range(1,10):
                for z in prev_z:
                    map = {'w': n, 'x': 0, 'y': 0, 'z': z}
                    error = False
                    for instruction in current_set:
                        if not self.perform_action(instruction, map):
                            error = True
                            break
                    if not error:
                        self.steps[i].append((z, n, map['z']))
                        new_z.add(map['z'])
            prev_z = new_z


    def find_largest(self):
        current = '9' *14
        while True:
            print(current)
            map = {'w': 0, 'x': 0, 'y': 0, 'z': 1}
            error = False
            for i in range(0, len(self.input)):
                map['w'] = int(current[i])
                current_set = self.input[i]
                for instruction in current_set:
                    if not self.perform_action(instruction, map):
                        error = True
                        break
                if error:
                    break
            if not error and map['z'] == 0:
                return current
            else:
                current = str(int(current) -1)

    def find_all(self, depth, target_z, current_sol):
        possibles = [i for i in self.steps[depth] if i[2] == target_z]
        for start_z, n, next_z in self.steps[depth]:
            if next_z == target_z:
                next_sol = str(n) + current_sol
                if depth == 0:
                    self.sols.append(int(next_sol))
                else:
                    self.find_all(depth-1, start_z, next_sol)




    def perform_action(self, instruction, map):
        op = instruction.split()
        operation = op[0]
        var_1 = op[1]
        val_1 = map[var_1]
        var_2 = op[2]
        important = False
        try:
            val_2 = int(var_2)
            if val_2 < 0:
                important = True
        except ValueError:
            val_2 = map[var_2]

        if operation == 'add':
            map[var_1] = val_1 + val_2
            if important:
                return map[var_1] == map['w']
            return True

        if operation == 'mul':
            map[var_1] = val_1 * val_2
            return True

        if operation == 'div':
            if val_2 == 0:
                return False
            map[var_1] = val_1 // val_2
            return True

        if operation == 'mod':
            if val_2 <= 0 or val_1 < 0:
                return False
            map[var_1] = val_1 % val_2
            return True

        if operation == 'eql':
            map[var_1] = int(val_1 == val_2)
            return True

        print("error")

    def part_one(self):
        self.find_combos()
        self.find_all(13, 0, '')

        print("The answer to Day 24 part one is " + str(max(self.sols)))

    def part_two(self):


        print("The answer to Day 24 part two is " + str(min(self.sols)))


sol = Solution()
sol.part_one()
sol.part_two()
