import hashlib

class Solution:

    def __init__(self):
        self.start = 'uqwqemis'

    def is_valid(self, hash, number_of_zeros):
        return hash[0:number_of_zeros] == "0" * number_of_zeros

    def find_hash(self, input):
        return hashlib.md5(input.encode()).hexdigest()


    def find_password(self, seed, positional):
        password = '        '
        chars_found = 0
        current_int = 0
        chars_to_find = ['0', '1', '2', '3', '4', '5', '6', '7']
        while chars_found < 8:
            hash = self.find_hash(seed + str(current_int))
            if self.is_valid(hash, 5):
                if positional:
                    if hash[5] in chars_to_find:
                        chars_to_find.remove(hash[5])
                        position = int(hash[5])
                        password = password[:position] + hash[6] + password[position+1:]
                        chars_found = chars_found + 1
                else:
                    password = password.replace(' ', hash[5], 1)
                    chars_found += + 1
            current_int += 1
        return password




    def part_one(self):
        password = self.find_password(self.start, False)

        print("The answer to Day 5 part one is " + password)

    def part_two(self):
        password = self.find_password(self.start, True)

        print("The answer to Day 5 part two is " + password)



sol = Solution()
sol.part_two()
sol.part_one()
