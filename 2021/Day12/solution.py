import numpy as np

class Solution:




    def __init__(self):
        reader = open('input.txt')
        input = reader.read().splitlines()
        self.paths = {}
        self.sols = set()
        for i in input:
            caves = i.split("-")
            cave1 = caves[0]
            cave2 = caves[1]
            if cave1 not in self.paths:
                self.paths[cave1] = []
            if cave2 not in self.paths:
                self.paths[cave2] = []

            self.paths[cave1].append(cave2)
            self.paths[cave2].append(cave1)


    def visit_caves(self, caves_visited_so_far, can_visit_cave_func):

        current_cave = caves_visited_so_far[-1]
        for c in self.paths[current_cave]:
            caves_visited = caves_visited_so_far.copy()
            if c == 'end':
                caves_visited.append(c)
                visit_string = ""
                for cave_visited in caves_visited:
                    visit_string = visit_string + cave_visited + ", "
                self.sols.add(visit_string)
            elif can_visit_cave_func(caves_visited, c):
                caves_visited.append(c)
                self.visit_caves(caves_visited, can_visit_cave_func)

    def can_visit_cave(self, caves_visited, cave):
        return cave not in caves_visited or cave.isupper() and cave != 'start'

    def can_visit_cave_part2(self, caves_visited, cave):
        if cave not in caves_visited:
            return True
        if cave.isupper():
            return True
        if cave.islower() and cave != 'start':
            lower_caves = [c for c in caves_visited if c.islower()]
            contains_duplicates = any(lower_caves.count(c) > 1 for c in lower_caves)
            return not contains_duplicates
        return False


    def part_one(self):
        self.visit_caves(['start'], self.can_visit_cave)

        print("The answer to Day 11 part one is " + str(len(self.sols)))

    def part_two(self):
        self.visit_caves(['start'], self.can_visit_cave_part2)

        print("The answer to Day 11 part one is " + str(len(self.sols)))



sol = Solution()
sol.part_one()
sol.part_two()



