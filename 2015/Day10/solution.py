import re


class Solution:

    def __init__(self):
        self.current_string = "3113322113"


    def conways_game(self, times):

        current_string = self.current_string
        for i in range(0, times):
            print(str(i))
            current_number = ""
            current_number_count = 0
            next_string = ""
            for c in current_string:
                if current_number == "":
                    current_number = c
                else:
                    if c != current_number:
                        next_string = next_string + str(current_number_count) + current_number
                        current_number_count = 0
                        current_number = c

                current_number_count = current_number_count + 1
            next_string = next_string + str(current_number_count) + current_number
            current_string = next_string

        return len(current_string)



    def part_one(self):
        answer = self.conways_game(40)
        print("The answer to Day 10 part one is " + str(answer))

    def part_two(self):
        answer = self.conways_game(50)
        print("The answer to Day 10 part two is " + str(answer))






sol = Solution()
sol.part_two()
