import math
import re


class Solution:

    def __init__(self):
        reader = open('input.txt')
        input = reader.read().splitlines()
        self.input = [eval(i) for i in input]
        self.depth_dict = []
        for i in input:
            depth = 0
            depths = []
            for c in i:
                if c == '[':
                    depth += 1
                elif c == ']':
                    depth -= 1
                elif re.match(r"\d", c):
                    depths.append((int(c), depth))
            self.depth_dict.append(depths)

    def split(self, number_array):
        for i in range(0, len(number_array)):
            val, depth = number_array[i]
            if val >= 10:
                number_array[i] = (math.floor(val / 2), depth+1)
                number_array.insert(i+1, (math.ceil(val / 2), depth+1) )
                return True

    def explode(self, number_array):
        for i in range(0, len(number_array)):
            value, depth = number_array[i]
            if depth >= 5:
                next_value, next_depth = number_array[i + 1]
                if next_depth == depth:
                    if i != 0:
                        left_number, left_depth = number_array[i - 1]
                        number_array[i - 1] = (left_number + value, left_depth)
                    if i + 1 < len(number_array) - 1:
                        right_number, right_depth = number_array[i + 2]
                        number_array[i + 2] = (right_number + next_value, right_depth)
                    number_array[i] = (0, depth - 1)
                    del number_array[i + 1]
                return True
        return False

    def reduce(self, number_array):
        if self.explode(number_array):
            return True
        if self.split(number_array):
            return True
        return False

    def sum(self, number_array, number_array2):
        new_sum = number_array + number_array2
        for i in range(0, len(new_sum)):
            val, depth = new_sum[i]
            new_sum[i] = (val, depth+1)
        return new_sum

    def find_total(self, numbers):
        for n in numbers:
            can_reduce = self.reduce(n)
            while can_reduce:
                can_reduce = self.reduce(n)
        sum = numbers[0]
        for i in range(1, len(numbers)):
            sum = self.sum(sum, numbers[i])
            can_reduce = self.reduce(sum)
            while can_reduce:
                can_reduce = self.reduce(sum)
        number_array = self.construct_list(sum)
        return self.find_magnitude(number_array)

    def construct_list(self, number):
        i = 0
        while(len(number) != 1):
            val, depth = number[i]
            next_val, next_depth = number[i+1]
            if depth == next_depth:
                number[i] = ([val, next_val], depth -1)
                del number[i+1]
                i = 0
            else:
                i = (i+1) % (len(number) -1)
        number_list, x = number[0]
        return number_list

    def find_magnitude(self, number_array):
        magnitude = 0
        if isinstance(number_array[0], int):
            magnitude += 3 * number_array[0]
        else:
            magnitude += 3 * self.find_magnitude(number_array[0])
        if isinstance(number_array[1], int):
            magnitude += 2 * number_array[1]
        else:
            magnitude += 2 * self.find_magnitude(number_array[1])
        return magnitude

    def find_largest_two(self, numbers):
        largest_mag = 0
        for i in range(0, len(numbers)):
            for j in range(0, len(numbers)):
                if i != j:
                    mag = self.find_total([numbers[i], numbers[j]])
                    if mag > largest_mag:
                        largest_mag = mag
        return largest_mag

    def part_one(self):
        magnitude = self.find_total(self.depth_dict)
        print("The answer to Day 18 part one is " + str(magnitude))

    def part_two(self):
        largest = self.find_largest_two(self.depth_dict)
        print("The answer to Day 18 part two is " + str(largest))


sol = Solution()
sol.part_one()
sol.part_two()

