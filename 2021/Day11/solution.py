import numpy as np

class Solution:



    def __init__(self):
        reader = open('input.txt')
        input = reader.read().splitlines()
        self.octopus = []
        for i in input:
            self.octopus.append([int(x) for x in i])
        self.octopus = np.array(self.octopus)
        self.grid_size = len(self.octopus)

    def add_ones(self, octopus):
        return octopus + 1

    def flash(self, octopus, i, j):
        octopus[i][j] = 0
        i_min = i - 1 if i > 0 else 0
        j_min = j - 1 if j > 0 else 0
        i_max = i + 1 if i < self.grid_size - 1 else self.grid_size - 1
        j_max = j + 1 if j < self.grid_size - 1 else self.grid_size - 1

        for x in range(i_min, i_max + 1):
            for y in range(j_min, j_max + 1):
                if octopus[x][y] != 0:
                    octopus[x][y] = octopus[x][y] + 1

        return octopus


    def step(self, octopus):
        octopus = self.add_ones(octopus)
        found_new_flash = True
        flash_count = 0
        while found_new_flash:
            found_new_flash = False
            for i in range(0, self.grid_size):
                for j in range(0, self.grid_size):
                    brightness = octopus[i][j]
                    if brightness > 9:
                        found_new_flash = True
                        flash_count += 1
                        octopus = self.flash(octopus, i, j)
        return octopus, flash_count

    def step_n_times(self, octopus, n):
        flashes = 0
        for i in range(0, n):
            octopus, new_flashes = self.step(octopus)
            flashes = flashes + new_flashes
        return octopus, flashes

    def find_simultaneous_flash(self, octopus):
        step = 1
        number_of_octopus = self.grid_size * self.grid_size
        while True:
            octopus, new_flashes = self.step(octopus)
            if new_flashes == number_of_octopus:
                return step
            step += 1


    def part_one(self):
        octopus = self.octopus.copy()
        octopus, flashes = self.step_n_times(octopus, 100)

        print("The answer to Day 11 part one is " + str(flashes))

    def part_two(self):
        octopus = self.octopus.copy()
        step = self.find_simultaneous_flash(octopus)

        print("The answer to Day 11 part two is " + str(step))


sol = Solution()
sol.part_one()
sol.part_two()


