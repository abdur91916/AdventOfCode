import re

class Solution:
    openers = ['(', '[', '<', '{']
    closers = [')', ']', '>', '}']
    valid = []
    incomplete = {}


    def __init__(self):
        reader = open('input.txt')
        self.input = reader.read().splitlines()

    def is_corrupt(self, line):
        expected_closing_order = []
        for c in line:
            if c in self.openers:
                closer = ''
                if c == '(':
                    closer = ')'
                elif c == '<':
                    closer = '>'
                elif c == '{':
                    closer = '}'
                elif c == '[':
                    closer = ']'
                expected_closing_order.insert(0, closer)
            elif c in self.closers:
                expected_closer = expected_closing_order.pop(0)
                if not c == expected_closer:
                    return True, c
            else:
                print(line)
                return True, c
        if len(expected_closing_order) == 0:
            self.valid.append(line)
        else:
            self.incomplete[line] = expected_closing_order
        return False, ''

    def find_corrupt_score(self, lines):
        corrupt_char_count = {c:0 for c in self.closers}
        for l in lines:
            is_corrupt, invalid_char = self.is_corrupt(l)
            if is_corrupt:
                corrupt_char_count[invalid_char] = corrupt_char_count[invalid_char] + 1

        score = 0
        for c in corrupt_char_count:
            count = corrupt_char_count[c]
            if c == ')':
                score = score + 3 * count
            elif c == '>':
                score = score + 25137 * count
            elif c == '}':
                score = score + 1197 * count
            elif c == ']':
                score = score + 57 * count

        return score

    def find_incomplete_score(self, lines):
        scores = []
        for completion in lines.values():
            current_score = 0
            for c in completion:
                current_score = current_score * 5
                if c == ')':
                    current_score = current_score + 1
                elif c == '>':
                    current_score = current_score + 4
                elif c == '}':
                    current_score = current_score + 3
                elif c == ']':
                    current_score = current_score + 2
            scores.append(current_score)
        scores = sorted(scores)
        winner = len(scores) // 2
        return scores[winner]


    def part_one(self):
        score = self.find_corrupt_score(self.input)

        print("The answer to Day 10 part one is " + str(score))

    def part_two(self):
        score = self.find_incomplete_score(self.incomplete)

        print("The answer to Day 10 part two is " + str(score))


sol = Solution()
sol.part_one()
sol.part_two()

