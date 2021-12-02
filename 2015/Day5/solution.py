import re


class Solution:
    bad_list = ["ab", "cd", "pq", "xy"]
    vowels = ["a", "e", "i", "o", "u"]

    def __init__(self):
        reader = open('input.txt')
        strings = reader.read().splitlines()
        self.strings = strings

    def is_nice(self, string):
        vowel_count = 0
        two_in_a_row = False
        length = len(string)

        if string[0] in self.vowels:
            vowel_count = vowel_count + 1
        for i in range(1, length):
            current_char = string[i]
            previous_char = string[i - 1]

            if current_char in self.vowels:
                vowel_count = vowel_count + 1

            if current_char == previous_char:
                two_in_a_row = True

            if previous_char + current_char in self.bad_list:
                return False

        return two_in_a_row and vowel_count > 2

    def is_nice_two(self, string):
        seperated_char = False
        double_match = False
        length = len(string)

        for i in range(2, length):
            first = string[i - 2]
            second = string[i - 1]
            third = string[i]

            sub_string_one = string[0:i - 2]
            sub_string_two = string[i:length]
            if not double_match and (
                    re.search(first + second, sub_string_one) or re.search(first + second, sub_string_two)):
                double_match = True

            if not seperated_char and first == third:
                seperated_char = True

            if seperated_char and double_match:
                return True

        return seperated_char and double_match

    def partOne(self):
        good_string_count = 0
        for x in self.strings:
            if self.is_nice(x):
                good_string_count = good_string_count + 1
        print("The answer to Day 1 part one is " + str(good_string_count))

    def part_two(self):
        good_string_count = 0
        for x in self.strings:
            if self.is_nice_two(x):
                good_string_count = good_string_count + 1
        print("The answer to Day 1 part two is " + str(good_string_count))


sol = Solution()
sol.partOne()
sol.part_two()
