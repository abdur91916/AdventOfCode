import re

class Solution:



    def __init__(self):
        reader = open('input.txt')
        input = reader.read().splitlines()
        self.input_output = [i.split(' | ') for i in input]

    def count_uniques_in_out(self):
        uniques = 0
        for value in self.input_output:
            output = value[1].split()
            for o in output:
                if len(o) == 2 or len(o) == 3 or len(o) == 4 or len(o) == 7:
                    uniques += 1
        return uniques

    def resolve(self):
        total = 0
        for i in self.input_output:
            output_values = {}
            number_map = {}
            code_map = {}

            input = i[0].split()
            input = [self.alphabetic(x) for x in input]
            output = i[1].split()
            output = [self.alphabetic(x) for x in output]

            for n in input:
                if len(n) == 2:
                    code_map[n] = 1
                    number_map[1] = n
                elif len(n) == 3:
                    code_map[n] = 7
                    number_map[7] = n
                elif len(n) == 4:
                    code_map[n] = 4
                    number_map[4] = n
                elif len(n) == 7:
                    code_map[n] = 8
                    number_map[8] = n

            six_digits = [i for i in input if len(i) == 6]
            five_digits = [i for i in input if len(i) == 5]

            three = self.find_value_containing_substring(number_map[1], five_digits)[0]
            code_map[three] = 3
            number_map[3] = three
            five_digits.remove(three)

            partial_nine = self.find_sum(number_map[4], number_map[7])
            nine = self.find_value_containing_substring(partial_nine, six_digits)[0]
            code_map[nine] = 9
            number_map[9] = nine
            six_digits.remove(nine)

            zero = self.find_value_containing_substring(number_map[1], six_digits)[0]
            code_map[zero] = 0
            number_map[0] = zero
            six_digits.remove(zero)

            six = six_digits[0]
            code_map[six] = 6
            number_map[6] = six
            six_digits.remove(six)

            first_five_digit = five_digits[0]
            sum_value = self.find_sum(first_five_digit, number_map[1])
            if sum_value == nine:
                code_map[first_five_digit] = 5
                number_map[5] = first_five_digit
                five_digits.remove(first_five_digit)
                two = five_digits[0]
                code_map[two] = 2
                number_map[2] = two
            else:
                code_map[first_five_digit] = 2
                number_map[2] = first_five_digit
                five_digits.remove(first_five_digit)
                five = five_digits[0]
                code_map[five] = 5
                number_map[5] = five


            total = total + self.find_sum_output(output,code_map)
        return total


    def find_sum_output(self, strings, map):
        total = ""
        for s in strings:
            total = total + str(map[s])
        return int(total)


    def alphabetic(self, string):
        new_string = ''.join(sorted(string))
        return new_string

    def find_sum(self, string1, string2):
        sum = string1 + string2
        new_number = ''.join(set(sum))
        return self.alphabetic(new_number)

    def find_value_containing_substring(self, substring, strings):
        matches = []
        for s in strings:
            match = True
            for c in substring:
                if c not in s:
                    match = False
            if match:
                matches.append(s)
        return matches



    def part_one(self):
        uniques = self.count_uniques_in_out()

        print("The answer to Day 8 part one is " + str(uniques))

    def part_two(self):
        total = self.resolve()

        print("The answer to Day 6 part one is " + str(total))


sol = Solution()
sol.part_one()
sol.part_two()