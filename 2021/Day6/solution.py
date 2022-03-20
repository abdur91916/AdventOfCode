import re

class Solution:

    fish_count = {}

    def __init__(self):
        reader = open('input.txt')
        lines = reader.read()
        fishes = re.findall(r"\d+", lines)
        for i in range(0, 9):
            self.fish_count[i] = 0

        for fish in fishes:
            self.fish_count[int(fish)] = self.fish_count[int(fish)] + 1

    def pass_day(self, fish_count):
        new_fish = fish_count[0]
        new_total = sum(fish_count.values()) + new_fish

        for i in range(1, 9):
            fish_count[i-1] = fish_count[i]
        fish_count[6] = fish_count[6] + new_fish
        fish_count[8] = new_fish

        return new_total




    def part_one(self):
        total = 0
        fishes = self.fish_count.copy()
        for i in range(0, 80):
            total = self.pass_day(fishes)

        print("The answer to Day 6 part one is " + str(total))

    def part_two(self):
        total = 0
        fishes = self.fish_count.copy()
        for i in range(0, 256):
            total = self.pass_day(fishes)

        print("The answer to Day 6 part two is " + str(total))
    #
    #
    # def part_two(self):
    #     self.populate_map_with_horiz_lines()
    #     sum = (np.asarray(self.map) > 1).sum()
    #     print("The answer to Day 14 part two is " + str(sum))


sol = Solution()
sol.part_one()
sol.part_two()
