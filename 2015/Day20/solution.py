import math
class Solution:
    house_deliveries = {}
    number_delivered = {}


    def __init__(self):

        self.target = 29000000

    def deliver(self, target, max_deliveries, delivery_per_number):
        house_deliveries = {1: delivery_per_number}
        number_delivered = {1: 1}
        i = 1
        while house_deliveries[i] < target:
            i=i+1
            number_delivered[i] = 0
            elf_total = 0
            divisors = self.find_divisors(i)
            for d in divisors:
                if number_delivered[d] < max_deliveries or max_deliveries == -1:
                    elf_total = elf_total + d
                    number_delivered[d] = number_delivered[d] + 1

            house_deliveries[i] = elf_total * delivery_per_number

        return i

    def find_divisors(self, m):
        sqrt = math.ceil(math.sqrt(m))
        divisors = []

        for i in range(1, sqrt+1):
            if m % i == 0:
                divisors.append(i)
                divisors.append(m/i)
        return divisors




    def part_one(self):
        answer = self.deliver(self.target, -1, 10)
        print("The answer to Day 20 part one is " + str(answer))


    def part_two(self):
        answer = self.deliver(self.target, 50, 11)
        print("The answer to Day 20 part two is " + str(answer))



sol = Solution()
sol.part_two()

sol.part_one()


