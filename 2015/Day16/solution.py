import re
class Solution:
    sue = {}
    clues = {}
    clues2 = {}


    def __init__(self):
        reader = open('input.txt')
        entries = reader.read().splitlines()
        for i in range(0, len(entries)):

            sue_info = {}
            info_array = re.findall(r"\w+: \d+", entries[i])
            for info in info_array:
                attribute = re.search(r"\w+", info).group()
                value = re.search(r"\d+", info).group()
                sue_info[attribute] = int(value)
            self.sue["sue " + str(i+1)] = sue_info

        self.clues2 = self.add_clues("clues2.txt")
        self.clues = self.add_clues("clues.txt")


    def add_clues(self, clue_file):
        reader = open(clue_file)
        clues = reader.read().splitlines()
        clue_array = {}
        for c in clues:
            symbol = "="
            if ">" in c:
                symbol = ">"
            elif "<" in c:
                symbol = "<"
            clue_info = re.search(r"\w+", c).group()
            value = re.search(r"\d+", c).group()
            clue_array[clue_info] = (symbol, int(value))
        return clue_array


    def cross_ref(self, people, clues):
        valid_people = []
        for i in people:
            valid = True
            person = people[i]
            for c in clues:
                if c in person:
                    symbol, clue_value = clues[c]
                    person_value = person[c]
                    if not self.evaluate(person_value, symbol, clue_value):
                        valid = False
            if valid:
                valid_people.append(i)
        return valid_people

    def evaluate(self, value, operator, target):
        if operator == "<":
            return value < target
        elif operator == ">":
            return value > target
        else:
            return value == target




    def part_one(self):
        person = self.cross_ref(self.sue, self.clues)
        print("The answer to Day 16 part one is " + str(person))

    def part_two(self):
        person = self.cross_ref(self.sue, self.clues2)
        print("The answer to Day 16 part two is " + str(person))

sol = Solution()
sol.part_one()
sol.part_two()

