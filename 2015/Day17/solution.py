class Solution:
    solutions = []
    number_of_conts_per_solution = {}
    buckets = []

    def __init__(self):
        reader = open('input.txt')
        entries = reader.read().splitlines()
        self.buckets = [int(x) for x in entries]

    def find_all_sols(self, partial_sol, target, current_index):
        if current_index < len(self.buckets):
            current_total = self.find_total(partial_sol)
            partial_sol_with_bucket = partial_sol.copy()
            partial_sol_with_bucket.append(current_index)
            current_total_with_bucket = current_total + self.buckets[current_index]
            if current_total_with_bucket <= target:
                if current_total_with_bucket == target:
                    self.solutions.append(partial_sol_with_bucket)
                else:
                    self.find_all_sols(partial_sol_with_bucket, target, current_index+1)
            self.find_all_sols(partial_sol, target, current_index+1)

    def find_total(self, bucket_indexes):
        total = 0
        for i in bucket_indexes:
            total = total + self.buckets[i]
        return total

    def find_number_of_containers_per_solution(self):
        for i in self.solutions:
            number_of_containers = len(i)
            if not number_of_containers in self.number_of_conts_per_solution:
                self.number_of_conts_per_solution[number_of_containers] = []
            self.number_of_conts_per_solution[number_of_containers].append(i)


    def part_one(self):
        self.find_all_sols([], 150, 0)
        print("The answer to Day 17 part one is " + str(len(self.solutions)))

    def part_two(self):
        self.find_number_of_containers_per_solution()
        different_number_of_containers = self.number_of_conts_per_solution.keys()
        min_number_of_conts = min(different_number_of_containers)
        solutions_with_min = self.number_of_conts_per_solution[min_number_of_conts]
        print("The answer to Day 17 part two is " + str(len(solutions_with_min)))


sol = Solution()
sol.part_one()
sol.part_two()

