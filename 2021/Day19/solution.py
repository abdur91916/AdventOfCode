import collections

import numpy as np
import re


class Solution:
    scanner_rotations = {}
    rotations_matricies = {}
    scanners = []
    scanner_positons = {}
    pairs_checked = []

    def __init__(self):
        self.find_rotation_matricies()
        reader = open('input.txt')
        input = reader.read().split("\n\n")
        input = [i.splitlines()[1:] for i in input]
        for scanner in input:
            current_scanner = []
            for beacon in scanner:
                position = beacon.split(",")
                position = np.array([int(p) for p in position])
                current_scanner.append(position)
            self.scanners.append(current_scanner)

    def find_rotation_matricies(self):
        i = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        x = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
        y = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
        z = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])

        self.rotations_matricies[0] = i
        self.rotations_matricies[1] = x
        self.rotations_matricies[2] = y
        self.rotations_matricies[3] = z
        self.rotations_matricies[4] = np.dot(x, x)
        self.rotations_matricies[5] = np.dot(x, y)
        self.rotations_matricies[6] = np.dot(x, z)
        self.rotations_matricies[7] = np.dot(y, x)
        self.rotations_matricies[8] = np.dot(y, y)
        self.rotations_matricies[9] = np.dot(z, y)
        self.rotations_matricies[10] = np.dot(z, z)
        self.rotations_matricies[11] = np.dot(np.dot(x, x), x)
        self.rotations_matricies[12] = np.dot(np.dot(x, x), y)
        self.rotations_matricies[13] = np.dot(np.dot(x, x), z)
        self.rotations_matricies[14] = np.dot(np.dot(x, y), x)
        self.rotations_matricies[15] = np.dot(np.dot(x, y), y)
        self.rotations_matricies[16] = np.dot(np.dot(x, z), z)
        self.rotations_matricies[17] = np.dot(np.dot(y, x), x)
        self.rotations_matricies[18] = np.dot(np.dot(y, y), y)
        self.rotations_matricies[19] = np.dot(np.dot(z, z), z)
        self.rotations_matricies[20] = np.dot(np.dot(np.dot(x, x), x), y)
        self.rotations_matricies[21] = np.dot(np.dot(np.dot(x, x), y), x)
        self.rotations_matricies[22] = np.dot(np.dot(np.dot(x, y), x), x)
        self.rotations_matricies[23] = np.dot(np.dot(np.dot(x, y), y), y)

    def find_positions(self):
        found_scanners = [0]
        unfound_scanners = list(range(1, len(self.scanners)))
        self.scanner_positons[0] = [0, 0, 0]
        self.scanner_rotations[0] = 0
        while len(unfound_scanners) != 0:
            current_unfound_i = 0
            while current_unfound_i < len(unfound_scanners):
                current_unfound = unfound_scanners[current_unfound_i]
                for i in found_scanners:
                    if not (current_unfound, i) in self.pairs_checked:
                        self.pairs_checked.append((current_unfound, i))
                        overlap, position, rotation = self.find_overlap(i, current_unfound)
                        if overlap:
                            found_scanners.append(current_unfound)
                            unfound_scanners.remove(current_unfound)
                            offset = position
                            self.scanner_positons[current_unfound] = offset

                            self.scanners[current_unfound] = [self.rotate(i, rotation) for i in
                                                              self.scanners[current_unfound]]
                            self.scanners[current_unfound] = [np.subtract(i, offset) for i in
                                                              self.scanners[current_unfound]]
                            current_unfound_i -= 1
                            print(unfound_scanners)
                            break
                current_unfound_i += 1

    def rotate(self, vector, rotation):
        return np.dot(self.rotations_matricies[rotation], vector)

    def find_overlap(self, scanner_1, scanner_2):
        for r in range(0, 24):
            positions_1 = self.scanners[scanner_1]
            positions_2 = self.scanners[scanner_2].copy()
            positions_2 = [self.rotate(i, r) for i in positions_2]
            for position_index in range(0, len(positions_2)):
                for fixed_point in positions_1:
                    offset = np.subtract(positions_2[position_index], fixed_point)
                    new_positions = [np.subtract(i, offset) for i in positions_2]
                    aset = set([tuple(x) for x in positions_1])
                    bset = set([tuple(x) for x in new_positions])
                    intersetion = np.array([x for x in aset & bset])
                    if len(intersetion) >= 12:
                        return True, offset, r
        return False, None, None


    def find_all(self):
        all_beacons = set()
        for s in self.scanners:
            for b in s:
                all_beacons.add(tuple(b))
        return list(all_beacons)

    def find_largest_distance(self):
        largest_dist = 0
        for i in range(0, len(self.scanners)):
            for j in range(i, len(self.scanners)):
                position_1 = self.scanner_positons[i]
                position_2 = self.scanner_positons[j]
                dist = np.subtract(position_1, position_2)
                dist = [abs(x) for x in dist]
                dist = sum(dist)
                if dist > largest_dist:
                    largest_dist = dist
        return largest_dist


    def part_one(self):
        self.find_positions()
        all_beacons = self.find_all()

        print("The answer to Day 19 part one is " + str(len(all_beacons)))

    def part_two(self):
        dist = self.find_largest_distance()

        print("The answer to Day 19 part two is " + str(dist))

sol = Solution()
sol.part_one()
sol.part_two()
