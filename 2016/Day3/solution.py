import re


class Solution:
    def __init__(self):
        reader = open('input.txt')
        triangles = reader.read().splitlines()
        triangles = [t.split() for t in triangles]
        self.triangles = []
        self.valid = []
        for t in triangles:
            self.triangles.append([int(x) for x in t])
        print()

    def find_valid_triangles(self, triangles):
        valid = []
        for t in triangles:
            x = t[0]
            y = t[1]
            z = t[2]
            if x > 0 and y > 0 and z > 0:
                total = x + y + z
                biggest = max(t)
                if total - biggest > biggest:
                    valid.append(t)
        return valid

    def find_vertical_triangles(self, triangles):
        new_triangles = []
        for i in range(0, len(triangles)-2, 3):
            row_1 = triangles[i]
            row_2 = triangles[i+1]
            row_3 = triangles[i+2]
            new_triangles.append([row_1[0], row_2[0], row_3[0]])
            new_triangles.append([row_1[1], row_2[1], row_3[1]])
            new_triangles.append([row_1[2], row_2[2], row_3[2]])

        return new_triangles



    def part_one(self):
        valid = self.find_valid_triangles(self.triangles)

        print("The answer to Day 3 part one is " + str(len(valid)))

    def part_two(self):
        triangles = self.find_vertical_triangles(self.triangles)
        valid = self.find_valid_triangles(triangles)
        print("The answer to Day 3 part two is " + str(len(valid)))


sol = Solution()
sol.part_one()
sol.part_two()
