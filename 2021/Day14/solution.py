import numpy as np
import re

class Solution:

    def __init__(self):
        reader = open('input.txt')
        input = reader.read()
        input = input.split("\n\n")
        self.start = input[0]
        rules = input[1].splitlines()
        self.word_map = {}

        for r in rules:
            rule = r.split(" -> ")
            self.word_map[rule[0]] = rule[1]

    def polymerize_2(self, word, times):
        pair_freq = {}
        letter_freq = {}
        for c in word:
            if c not in letter_freq:
                letter_freq[c] = 0
            letter_freq[c] += 1

        for i in range(0, len(word) - 1):
            pair = word[i:i+2]
            if pair not in pair_freq:
                pair_freq[pair] = 0
            pair_freq[pair] += 1

        for i in range(0, times):
            new_pair_freq = {}
            for pair in pair_freq:
                count = pair_freq[pair]
                first = pair[0]
                second = pair[1]
                middle = self.word_map[first+second]
                if middle not in letter_freq:
                    letter_freq[middle] = 0

                if first+middle not in new_pair_freq:
                    new_pair_freq[first+middle] = 0

                if middle+second not in new_pair_freq:
                    new_pair_freq[middle+second] = 0

                letter_freq[middle] += count
                new_pair_freq[first+middle] += count
                new_pair_freq[middle+second] += count
            pair_freq = new_pair_freq

        return letter_freq


    def find_score(self, letter_freq):
        key_max = max(letter_freq.keys(), key=(lambda k: letter_freq[k]))
        key_min = min(letter_freq.keys(), key=(lambda k: letter_freq[k]))

        return letter_freq[key_max] - letter_freq[key_min]

    def part_one(self):
        letter_freq = self.polymerize_2(self.start, 10)
        score = self.find_score(letter_freq)

        print("The answer to Day 14 part one is " + str(score))

    def part_two(self):
        letter_freq = self.polymerize_2(self.start, 40)
        score = self.find_score(letter_freq)

        print("The answer to Day 14 part two is " + str(score))

sol = Solution()
sol.part_one()
sol.part_two()
