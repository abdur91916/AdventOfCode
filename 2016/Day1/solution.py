import re
class Solution:
    def __init__(self):
        reader = open('input.txt')
        instructions = reader.read().split(', ')
        self.instructions = instructions

    def move(self, instructions, want_hq):
        visited = []
        found_hq = False
        hq_x = 0
        hq_y = 0

        position_x = 0
        position_y = 0
        current_rotation_x = 0
        current_rotation_y = 1
        for i in instructions:
            rotate = i[0]
            distance = int(re.search(r"\d+", i).group())
            if rotate == "R":
                current_rotation_x, current_rotation_y = self.rotate_right(current_rotation_x, current_rotation_y)
            elif rotate == "L":
                current_rotation_x, current_rotation_y = self.rotate_left(current_rotation_x, current_rotation_y)

            for d in range(0, distance):
                position_x = position_x + current_rotation_x
                position_y = position_y + current_rotation_y
                if (position_x, position_y) not in visited:
                    visited.append((position_x, position_y))
                elif not found_hq:
                    hq_x = position_x
                    hq_y = position_y
                    found_hq = True
                    if want_hq:
                        return hq_x, hq_y

        return position_x, position_y



    def rotate_right(self, x, y):
        if x == 0:
            x = y
            y = 0
        elif y == 0:
            y = -x
            x = 0
        return x, y

    def rotate_left(self, x, y):
        if x == 0:
            x = -y
            y = 0
        elif y == 0:
            y = x
            x = 0
        return x, y


    def part_one(self):
        x, y = self.move(self.instructions, False)
        distance = abs(x) + abs(y)
        print("The answer to Day 1 part one is " + str(distance))


    def part_two(self):
        x, y = self.move(self.instructions, True)
        distance = abs(x) + abs(y)
        print("The answer to Day 1 part one is " + str(distance))



sol = Solution()
sol.part_one()
sol.part_two()
