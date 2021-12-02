class Solution:
    def __init__(self):
        reader = open('input.txt')
        instructions = reader.read()
        self.instructions = instructions

    def partOne(self):
        floor = 0
        for x in self.instructions:
            if x == "(":
                floor = floor + 1
            elif x == ")":
                floor = floor - 1
            else:
                print("error cannot parse " + x)
        print("The answer to Day 1 part one is " + str(floor))

    def partTwo(self):
        numberOfChars = len(self.instructions)
        floor = 0
        for i in range(numberOfChars):
            instruction = self.instructions[i]
            if instruction == "(":
                floor = floor + 1
            elif instruction == ")":
                floor = floor - 1
            else:
                print("error cannot parse " + instruction)

            if floor == -1:
                print("The answer to Day 1 part two is " + str(i + 1))
                break


sol = Solution()
sol.partOne()
sol.partTwo()
