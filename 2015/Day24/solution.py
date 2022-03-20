import re
import numpy


class Solution:


    def __init__(self):
        reader = open('input.txt')
        self.parcels = [int(x) for x in reader.read().splitlines()]


    def split_into_piles(self, parcels, piles):
        smallest_pile_size = 100
        qe = 0
        smallest=[]

        total = sum(parcels)
        group_weight = total // piles
        piles = self.find_piles(0, group_weight, parcels, [])
        for p in piles:
            if len(p) < smallest_pile_size:
                smallest_pile_size = len(p)
                qe = self.find_qe(p)
                smallest = p
            elif len(p) == smallest_pile_size:
                current_qe = self.find_qe(p)
                if current_qe < qe:
                    qe = current_qe
                    smallest = p
        return qe


    def find_qe(self, numbers):
        mult = 1
        for n in numbers:
            mult = mult * n
        return mult


    def find_piles(self, current_size, desired_size, parcels, parcels_in_group):
        piles = []

        for i in range(len(parcels), 0, -1):
            parcel = parcels[i-1]
            parcels_in_new_group = parcels_in_group.copy()
            parcels_in_new_group.append(parcel)
            parcels_remaining = parcels[0:i-1]
            new_size = current_size + parcel
            if new_size == desired_size:
                piles.append(parcels_in_new_group)
            elif new_size < desired_size:
                piles.extend(self.find_piles(new_size, desired_size, parcels_remaining, parcels_in_new_group))
        return piles





    def part_one(self):
        answer = self.split_into_piles(self.parcels, 3)
        print("The answer to Day 24 part one is " + str(answer))


    def part_two(self):
        answer = self.split_into_piles(self.parcels, 4)
        print("The answer to Day 24 part one is " + str(answer))


sol = Solution()
sol.part_one()
sol.part_two()
