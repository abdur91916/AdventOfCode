import hashlib


class Solution:

    def __init__(self):
        self.secret_key = "bgvyzdsv"

    def is_valid(self, input, number_of_zeros):
        test_string = self.secret_key + str(input)
        result = hashlib.md5(test_string.encode()).hexdigest()
        return result[0:number_of_zeros] == "0" * number_of_zeros

    def part_one(self):
        answer = 0
        while not self.is_valid(answer, 5):
            answer = answer + 1
        print("The answer to Day 1 part one is " + str(answer))
        return answer

    def part_two(self, start_number):
        answer = start_number
        while not self.is_valid(answer, 6):
            answer = answer + 1

        print("The answer to Day 1 part two is " + str(answer))
        return answer


sol = Solution()
answer_part_one = sol.part_one()
sol.part_two(answer_part_one)
