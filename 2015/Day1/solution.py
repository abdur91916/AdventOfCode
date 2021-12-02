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


sol = Solution()
sol.partOne()

