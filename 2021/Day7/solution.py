import re

class Solution:


    def __init__(self):
        reader = open('input.txt')
        input = reader.read()
        self.crabs = [int(x) for x in re.findall(r"\d+", input)]
        self.max = max(self.crabs)
        self.min = min(self.crabs)


    def find_min_distance(self, increase_per_step):
        location = -1
        min_fuel = -1
        for i in range(self.min, self.max+1):
            distance_array = [self.fuel_cost(i, x, increase_per_step) for x in self.crabs]
            fuel = sum(distance_array)
            if min_fuel == -1 or fuel < min_fuel:
                location = i
                min_fuel = fuel
        return location, min_fuel

    def fuel_cost(self, start, end, increase_per_step):
        difference = abs(start - end)
        if increase_per_step == 0:
            return difference
        elif increase_per_step == 1:
            return (difference * (difference + 1)) / 2
        else:
            print("not yet implemented")


    def part_one(self):
        location, fuel = self.find_min_distance(0)

        print("The answer to Day 6 part one is " + str(fuel))

    def part_two(self):
        location, fuel = self.find_min_distance(1)

        print("The answer to Day 6 part one is " + str(fuel))


sol = Solution()
sol.part_one()
sol.part_two()

