import re
import math


class Solution:


    def __init__(self):
        reader = open('input.txt')
        self.instructions = reader.read().splitlines()
        self.number_instructions = len(self.instructions)

    def follow_instructions(self, register, current_instruction):
        while current_instruction < self.number_instructions:
            current = self.instructions[current_instruction]
            current = current.split()
            command = current[0]
            if command == 'hlf':
                variable = current[1]
                register[variable] = register[variable] // 2
                current_instruction = current_instruction + 1
            elif command == 'tpl':
                variable = current[1]
                register[variable] = register[variable] * 3
                current_instruction = current_instruction + 1
            elif command == 'inc':
                variable = current[1]
                register[variable] = register[variable] + 1
                current_instruction = current_instruction + 1
            elif command == 'jmp':
                amount = int(re.search('-*\d+', current[1]).group())
                current_instruction = current_instruction + amount
            elif command == 'jie':
                variable = re.search('\w+', current[1]).group()
                amount = int(re.search('\d+', current[2]).group())
                if register[variable] % 2 == 0:
                    current_instruction = current_instruction + amount
                else:
                    current_instruction = current_instruction + 1
            elif command == 'jio':
                variable = re.search('\w+', current[1]).group()
                amount = int(re.search('\d+', current[2]).group())
                if register[variable]  == 1:
                    current_instruction = current_instruction + amount
                else:
                    current_instruction = current_instruction + 1
            else:
                print(command)








    def part_one(self):
        register = {'a':0, 'b':0}
        self.follow_instructions(register, 0)
        print("The answer to Day 21 part one is " + str(register['b']))


    def part_two(self):
        register = {'a': 1, 'b': 0}
        self.follow_instructions(register, 0)
        print("The answer to Day 21 part one is " + str(register['b']))


sol = Solution()
sol.part_one()
sol.part_two()


