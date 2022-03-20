import numpy
from statistics import mode
from collections import Counter

class Solution:

    def __init__(self):
        reader = open('input.txt')
        signals = reader.read().splitlines()
        signal_array = []
        for signal in signals:
            signal_array.append([s for s in signal])
        self.signals = numpy.array(signal_array)
        self.word_length = len(signal_array[0])

    def error_correct(self, signals, length):
        word = ''
        for i in range(0, length):
            chars = signals[:,i]
            char, count = Counter(chars).most_common()[1]
            word = word + char
        return word


    def error_correct_2(self, signals, length):
        word = ''
        for i in range(0, length):
            chars = signals[:,i]
            char, count = Counter(chars).most_common()[-1]
            word = word + char
        return word

    def part_one(self):
        word = self.error_correct(self.signals, self.word_length)

        print("The answer to Day 6 part one is " + word)

    def part_two(self):
        word = self.error_correct_2(self.signals, self.word_length)

        print("The answer to Day 6 part two is " + word)


sol = Solution()
sol.part_one()
sol.part_two()
