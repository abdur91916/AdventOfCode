import re


class Solution:

    def __init__(self):
        reader = open('input.txt')
        strings = reader.read()

        self.strings = strings

    def replace_specials(self):
        strings_new = self.strings
        strings_new = strings_new.replace('\\\\', "*")
        strings_new = strings_new.replace('\\\"', "&")
        strings_new = re.sub(r"\\x..","$", strings_new)
        strings_new = strings_new.replace("\"", "")
        strings_new = strings_new.replace('*', "\\")
        strings_new = strings_new.replace('&', "\"")
        return strings_new

    def encode(self):
        strings_new = self.strings
        strings_new = strings_new.replace('\\\\', "*")
        strings_new = strings_new.replace('\\\"', "&")

        strings_new = strings_new.replace("\"", "!!!")
        strings_new = strings_new.replace('&', "\\\"")
        strings_new = strings_new.replace('*', "\\\\")
        strings_new = strings_new.replace("\\" , "\\\\")
        strings_new = strings_new.replace("\"", "\\\"")

        return strings_new

    def part_one(self):
        string_in_full = self.strings
        chars_only = self.replace_specials()
        answer = len(string_in_full) - len(chars_only)
        print("The answer to Day 8 part one is " + str(answer))


    def part_two(self):
        encoded = self.encode()
        string_in_full = self.strings
        answer = len(encoded) - len(string_in_full)
        print("The answer to Day 8 part two is " + str(answer))



sol = Solution()
sol.part_one()
sol.part_two()



