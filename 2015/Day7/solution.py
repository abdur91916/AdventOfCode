import re


class Solution:
    key_value1 = {}
    key_value2 = {}

    def __init__(self):
        reader = open('input.txt')
        operations = reader.read().splitlines()
        reader = open('input2.txt')
        operations2 = reader.read().splitlines()
        self.operations = operations
        self.operations2 = operations2


    def resolve_operations(self, operations):
        instruction_copy = operations.copy()
        key_value = {}

        while len(instruction_copy) > 0:
            for x in instruction_copy:
                operation = x.split(" -> ")

                keys_required = re.findall("[a-z]+", operation[0])
                can_resolve = True
                for k in keys_required:
                    if k not in key_value:
                        can_resolve = False

                if can_resolve:
                    instruction_copy.remove(x)
                    value = self.resolve(operation[0], key_value)
                    key = operation[1]
                    key_value[key] = value
        return key_value

    def resolve(self, input, key_values):
        symbols = input.split(" ")
        if len(symbols) == 1:
            return self.resolve_var(symbols[0], key_values)

        if len(symbols) == 2:
            var1 = self.resolve_var(symbols[1], key_values)
            if symbols[0] == "NOT":
                return ~var1
            else:
                print("error")

        if len(symbols) == 3:
            var1 = self.resolve_var(symbols[0], key_values)
            var2 = self.resolve_var(symbols[2], key_values)
            operator = symbols[1]
            if operator == "AND":
                return var1 & var2
            elif operator == "OR":
                return var1 | var2
            elif operator == "LSHIFT":
                return var1 << var2
            elif operator == "RSHIFT":
                return var1 >> var2
            else:
                print("error")




        return 1

    def resolve_var(self, var, key_values):
        if var.isnumeric():
            return int(var)
        else:
            return key_values[var]

    def part_one(self):
        self.key_value1 = self.resolve_operations(self.operations)
        print("The answer to Day 7 part one is " + str(self.key_value1['a']))

    def part_two(self):
        self.key_value2 = self.resolve_operations(self.operations2)
        print("The answer to Day 7 part two is " + str(self.key_value2['a']))



sol = Solution()
sol.part_one()
sol.part_two()

