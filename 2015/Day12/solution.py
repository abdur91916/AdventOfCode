import re
import json


class Solution:
    all_ints = []
    negative_ints = []

    def __init__(self):
        reader = open('input.txt')
        self.input = reader.read()
        self.all_ints = self.find_all_numbers(self.input)
        self.negative_ints = self.find_negative_numbers(self.input)

    def find_all_numbers(self, input):
        all_ints = re.findall(r"\d+", input)
        return [int(x) for x in all_ints]

    def find_negative_numbers(self, input):
        negative_ints = re.findall(r"-\d+", input)
        return [int(x) for x in negative_ints]

    def remove_object(self, obj):
        for key in obj:
            value = obj[key]
            if value == "red":
                return True
        return False

    def remove_red_objects(self, parent, key):
        value = parent[key]
        if type(value) is dict:
            if self.remove_object(value):
                parent[key] = {}
            else:
                for key in value:
                    self.remove_red_objects(value, key)

        elif type(value) is list:
            for i in range(0, len(value)):
                self.remove_red_objects(value,i)



    def part_one(self):
        all_numbs_value = sum(self.all_ints)
        negative_sum = sum(self.negative_ints)
        total = all_numbs_value + 2 * negative_sum

        print("The answer to Day 12 part one is " + str(total))

    def part_two(self):
        json_obj = json.loads(self.input)
        for key in json_obj:
            value = json_obj[key]
            if type(value) is dict or type(value) is list:
                self.remove_red_objects(json_obj, key)

        new_input = json.dumps(json_obj)

        all_ints = self.find_all_numbers(new_input)
        negative_ints = self.find_negative_numbers(new_input)

        abs_sum = sum(all_ints)
        negative_sum = sum(negative_ints)
        total = abs_sum + 2 * negative_sum

        print("The answer to Day 12 part two is " + str(total))


sol = Solution()
sol.part_one()
sol.part_two()
