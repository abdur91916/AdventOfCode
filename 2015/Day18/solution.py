import numpy as np
class Solution:


    def __init__(self):
        reader = open('input.txt')
        entries = reader.read().splitlines()
        self.lights = np.array([list(x) for x in entries])
        self.side_length = len(entries)

    def animate(self, lights_old):
        lights = lights_old.copy()
        new_lights = np.full((self.side_length, self.side_length), '*')
        for i in range(0, self.side_length):
            for j in range(0, self.side_length):
                x_low = i - 1 if i > 0 else 0
                y_low = j - 1 if j > 0 else 0
                x_high = i + 1 if i < self.side_length - 1 else self.side_length - 1
                y_high = j + 1 if j < self.side_length - 1 else self.side_length - 1
                current_value = lights[i][j]
                surronding = lights[x_low:x_high+1, y_low:y_high+1]
                on = np.count_nonzero(surronding == '#')
                if current_value == '#':
                    if on == 3 or on == 4:
                        new_lights[i][j] = '#'
                elif on == 3:
                    new_lights[i][j] = '#'
        return new_lights


    def stuck_lights(self, lights):
        x_high = self.side_length - 1
        y_high = self.side_length - 1
        lights[0][0] = '#'
        lights[0][y_high] = '#'
        lights[x_high][0] = '#'
        lights[x_high][y_high] = '#'
        return lights










    def part_one(self):
        lights = self.lights
        for i in range(0, 100):
            lights = self.animate(lights)
        print("The answer to Day 18 part one is " + str(np.count_nonzero(lights == '#')))


    def part_two(self):
        lights = self.lights
        for i in range(0, 100):
            lights = self.animate(lights)
            lights = self.stuck_lights(lights)
            # print(lights)
        print("The answer to Day 18 part two is " + str(np.count_nonzero(lights == '#')))


sol = Solution()
sol.part_two()
sol.part_one()

