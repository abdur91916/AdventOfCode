import re


class Solution:

    def __init__(self):
        self.old_pass = "hepxcrrq"

    def roll_over(self, password, position):
        new_char = chr(ord(password[position]) + 1)
        password = self.replace_in_string(password, new_char, position)
        for i in range(position+1, len(password)):
            password = self.replace_in_string(password, "a", i)
        return password

    def increment(self, password, position):
        char_to_increment = password[position]

        if char_to_increment == "z":
            next_char = "a"
            password = self.replace_in_string(password, next_char, position)
            password = self.increment(password, position - 1)
        else:
            next_char = chr(ord(char_to_increment) + 1)
            password = self.replace_in_string(password, next_char, position)
        return password

    def skip_invalid(self, password):
        length = len(password)
        new_pass = ""
        for i in range(0, length):
            current_letter = password[i]
            if current_letter == "i" or current_letter == "o" or current_letter == "l":
                return self.roll_over(password, i)
        return password

    def is_valid_1(self, password):
        no_illegal_letters = not ("i" in password or "o" in password or "l" in password)
        consecutive_letters = False
        double_letters_count = 0

        for i in range(2, len(password)):
            first = password[i - 2]
            second = password[i - 1]
            third = password[i]
            if ord(first) + 1 == ord(second) and ord(first) + 2 == ord(third):
                consecutive_letters = True

        i = 0
        while i < (len(password) - 1):
            if password[i] == password[i + 1]:
                i = i + 2
                double_letters_count = double_letters_count + 1
            else:
                i = i + 1

        return no_illegal_letters and consecutive_letters and double_letters_count >= 2

    def replace_in_string(self, string, new_letter, position):
        new_string = string[0:position] + new_letter + string[position + 1:len(string)]
        return new_string

    def find_next_pass(self, old_pass):
        next_password = old_pass
        next_password = self.increment(next_password, 7)
        next_password = self.skip_invalid(next_password)
        while not self.is_valid_1(next_password):
            next_password = self.increment(next_password, 7)
            next_password = self.skip_invalid(next_password)
        return next_password

    def part_one(self):
        next_password = self.find_next_pass(self.old_pass)
        print("The answer to Day 10 part one is " + str(next_password))

    def part_two(self):
        next_password = self.find_next_pass(self.old_pass)
        next_password = self.find_next_pass(next_password)
        print("The answer to Day 10 part two is " + str(next_password))


sol = Solution()
sol.part_one()
sol.part_two()
