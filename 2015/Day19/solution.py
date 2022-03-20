import re
class Solution:
    must_replace = {'SiAl'}
    symbols = 0


    def __init__(self):
        reader = open('input.txt')
        entries = reader.read()
        replacements = re.findall(r"\w+ => \w+", entries)
        entries = entries.splitlines()
        self.string = entries[-1]
        self.mappings = {}
        self.reverse_map = {}
        self.symbols = len(re.findall(r'[A-Z]',self.string))
        for r in replacements:
            word_map = r.split(" => ")
            if not word_map[0] in self.mappings:
                self.mappings[word_map[0]] = []
            self.mappings[word_map[0]].append(word_map[1])
            if not word_map[1] in self.reverse_map:
                self.reverse_map[word_map[1]] = []
            self.reverse_map[word_map[1]].append(word_map[0])

    def find_possible_changes(self, word, mappings):
        new_words = set()
        for c in mappings:
            if c in word:
                for value in mappings[c]:
                    occurrences = re.findall(c, word)
                    for i in range(0, len(occurrences)):
                        new_word = word.replace(c, "*", i+1)
                        new_word = new_word.replace("*", c, i)
                        new_word = new_word.replace("*", value)
                        new_words.add(new_word)
        return new_words


    def part_one(self):
        words = self.find_possible_changes(self.string, self.mappings)
        print("The answer to Day 18 part one is " + str(len(words)))


    def part_two(self):
        steps = self.count_steps(self.string)
        print("The answer to Day 18 part one is " + str(steps))



    # Ar always adds 2 extra elems to a string as does Y, neither can change
    def count_steps(self, word):
        desired_symbols = self.symbols
        number_of_ys = len(re.findall(r"Y", word))
        number_of_Ars = len(re.findall(r"Ar", word))
        desired_symbols = desired_symbols - 2 * number_of_Ars - 2 * number_of_ys
        steps = desired_symbols - 1

        return steps



sol = Solution()
sol.part_one()
sol.part_two()

