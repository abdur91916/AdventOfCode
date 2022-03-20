from copy import copy, deepcopy


class Solution:
    steps = []
    sols = []

    def __init__(self):
        reader = open('input.txt')
        inp = reader.read().splitlines()
        self.input = [list(i) for i in inp]


    def move(self, critters):
        new_map = deepcopy(critters)
        for i in range(0,len(critters)):
            for j in range(0, len(critters[i])):
                if critters[i][j] == '>':
                    new_j = (j+1) % len(critters[i])
                    if critters[i][new_j] == '.':
                        new_map[i][new_j] = '>'
                        new_map[i][j] = '.'
        critters = deepcopy(new_map)

        for i in range(0, len(critters)):
            for j in range(0, len(critters[i])):
                    if critters[i][j] == 'v':
                        new_i = (i + 1) % len(critters)
                        if critters[new_i][j] == '.':
                            new_map[new_i][j] = 'v'
                            new_map[i][j] = '.'



        return new_map

    def turns_till_still(self):
        has_moved = True
        steps = 1
        crits = self.input
        while has_moved:
            new_crits = self.move(crits)
            if new_crits == crits:
                has_moved = False
            else:
                steps += 1
            crits = new_crits
            print(steps)
        return steps



    def part_one(self):
        moves = self.turns_till_still()


        print("The answer to Day 25 part one is " + str(moves))

    def part_two(self):


        print("The answer to Day 24 part two is " + str(min(self.sols)))


sol = Solution()
sol.part_one()
# sol.part_two()
