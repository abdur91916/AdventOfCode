import collections

import numpy as np
import re
from typing import NamedTuple


class Cuboid(NamedTuple):
    x_low: int
    x_high: int
    y_low: int
    y_high: int
    z_low: int
    z_high: int
    on: bool


import queue


class Solution:
    cubes_on = set()
    cubes_to_process = queue.Queue()

    def __init__(self, part):
        if part == 1:
            self.part = "one"
        else:
            self.part = "two"
        reader = open('input' + str(part) + '.txt')
        input = reader.read().splitlines()
        for c in input:
            c = c.split(" ")
            on = c[0] == "on"
            coordinates = [re.findall(r"-*\d+", i) for i in c[1].split(",")]
            cube = Cuboid(x_low=int(coordinates[0][0]), x_high=int(coordinates[0][1]),
                          y_low=int(coordinates[1][0]), y_high=int(coordinates[1][1]),
                          z_low=int(coordinates[2][0]), z_high=int(coordinates[2][1]),
                          on=on)
            self.cubes_to_process.put(cube)

    def remove_from_cube(self, cube, cube_to_remove):
        remaining_cubes = []
        cube_remaining = cube
        if cube_remaining.x_low < cube_to_remove.x_low:
            sub_cube = Cuboid(x_low=cube_remaining.x_low, x_high=cube_to_remove.x_low - 1,
                              y_low=cube_remaining.y_low, y_high=cube_remaining.y_high,
                              z_low=cube_remaining.z_low, z_high=cube_remaining.z_high,
                              on=cube_remaining.on)

            remaining_cubes.append(sub_cube)
            cube_remaining = Cuboid(x_low=cube_to_remove.x_low, x_high=cube_remaining.x_high,
                                    y_low=cube_remaining.y_low, y_high=cube_remaining.y_high,
                                    z_low=cube_remaining.z_low, z_high=cube_remaining.z_high,
                                    on=cube_remaining.on)
        if cube_remaining.x_high > cube_to_remove.x_high:
            sub_cube = Cuboid(x_low=cube_to_remove.x_high + 1, x_high=cube_remaining.x_high,
                              y_low=cube_remaining.y_low, y_high=cube_remaining.y_high,
                              z_low=cube_remaining.z_low, z_high=cube_remaining.z_high,
                              on=cube_remaining.on)
            remaining_cubes.append(sub_cube)
            cube_remaining = Cuboid(x_low=cube_remaining.x_low, x_high=cube_to_remove.x_high,
                                    y_low=cube_remaining.y_low, y_high=cube_remaining.y_high,
                                    z_low=cube_remaining.z_low, z_high=cube_remaining.z_high,
                                    on=cube_remaining.on)

        if cube_remaining.y_low < cube_to_remove.y_low:
            sub_cube = Cuboid(x_low=cube_remaining.x_low, x_high=cube_remaining.x_high,
                              y_low=cube_remaining.y_low, y_high=cube_to_remove.y_low - 1,
                              z_low=cube_remaining.z_low, z_high=cube_remaining.z_high,
                              on=cube_remaining.on)
            remaining_cubes.append(sub_cube)
            cube_remaining = Cuboid(x_low=cube_remaining.x_low, x_high=cube_remaining.x_high,
                                    y_low=cube_to_remove.y_low, y_high=cube_remaining.y_high,
                                    z_low=cube_remaining.z_low, z_high=cube_remaining.z_high,
                                    on=cube_remaining.on)
        if cube_remaining.y_high > cube_to_remove.y_high:
            sub_cube = Cuboid(x_low=cube_remaining.x_low, x_high=cube_remaining.x_high,
                              y_low=cube_to_remove.y_high + 1, y_high=cube_remaining.y_high,
                              z_low=cube_remaining.z_low, z_high=cube_remaining.z_high,
                              on=cube_remaining.on)
            remaining_cubes.append(sub_cube)
            cube_remaining = Cuboid(x_low=cube_remaining.x_low, x_high=cube_remaining.x_high,
                                    y_low=cube_remaining.y_low, y_high=cube_to_remove.y_high,
                                    z_low=cube_remaining.z_low, z_high=cube_remaining.z_high,
                                    on=cube_remaining.on)

        if cube_remaining.z_low < cube_to_remove.z_low:
            sub_cube = Cuboid(x_low=cube_remaining.x_low, x_high=cube_remaining.x_high,
                              y_low=cube_remaining.y_low, y_high=cube_remaining.y_high,
                              z_low=cube_remaining.z_low, z_high=cube_to_remove.z_low - 1,
                              on=cube_remaining.on)
            remaining_cubes.append(sub_cube)
            cube_remaining = Cuboid(x_low=cube_remaining.x_low, x_high=cube_remaining.x_high,
                                    y_low=cube_remaining.y_low, y_high=cube_remaining.y_high,
                                    z_low=cube_to_remove.z_low, z_high=cube_remaining.z_high,
                                    on=cube_remaining.on)
        if cube_remaining.z_high > cube_to_remove.z_high:
            sub_cube = Cuboid(x_low=cube_remaining.x_low, x_high=cube_remaining.x_high,
                              y_low=cube_remaining.y_low, y_high=cube_remaining.y_high,
                              z_low=cube_to_remove.z_high + 1, z_high=cube_remaining.z_high,
                              on=cube_remaining.on)
            remaining_cubes.append(sub_cube)
            cube_remaining = Cuboid(x_low=cube_remaining.x_low, x_high=cube_remaining.x_high,
                                    y_low=cube_remaining.y_low, y_high=cube_remaining.y_high,
                                    z_low=cube_remaining.z_low, z_high=cube_to_remove.z_high,
                                    on=cube_remaining.on)

        return remaining_cubes

    def find_overlap(self, old_cube, new_cube):
        overlap, overlap_x = self.overlap_in_range((old_cube.x_low, old_cube.x_high), (new_cube.x_low, new_cube.x_high))
        if not overlap:
            return False, None
        overlap, overlap_y = self.overlap_in_range((old_cube.y_low, old_cube.y_high), (new_cube.y_low, new_cube.y_high))
        if not overlap:
            return False, None
        overlap, overlap_z = self.overlap_in_range((old_cube.z_low, old_cube.z_high), (new_cube.z_low, new_cube.z_high))
        if not overlap:
            return False, None

        return True, Cuboid(x_low=overlap_x[0], x_high=overlap_x[1],
                            y_low=overlap_y[0], y_high=overlap_y[1],
                            z_low=overlap_z[0], z_high=overlap_z[1],
                            on=new_cube.on)

    def overlap_in_range(self, range_1, range_2):
        a_s, a_e = range_1
        b_s, b_e = range_2
        if b_s > a_e or a_s > b_e:
            return False, (0, 0)
        else:
            overlap_s = max(a_s, b_s)
            overlap_e = min(a_e, b_e)
            return True, (overlap_s, overlap_e)

    def store_cube(self, cube):
        no_overlaps = True
        for cube_2 in self.cubes_on:
            does_overlap, overlap_cube = self.find_overlap(cube_2, cube)
            if does_overlap:
                no_overlaps = False
                if not overlap_cube.on:
                    self.cubes_on.remove(cube_2)
                    cubes_to_add = self.remove_from_cube(cube_2, overlap_cube)
                    self.cubes_on.update(cubes_to_add)
                remaining_cubes = self.remove_from_cube(cube, overlap_cube)
                for c in remaining_cubes:
                    self.cubes_to_process.queue.insert(0, c)
                break

        if no_overlaps and cube.on:
            self.cubes_on.add(cube)

    def calculate_size(self, cube):
        return (1 + cube.x_high - cube.x_low) * (1 + cube.y_high - cube.y_low) * (1 + cube.z_high - cube.z_low)

    def answer(self):
        while not self.cubes_to_process.empty():
            self.store_cube(self.cubes_to_process.get())
        size = 0
        for c in self.cubes_on:
            size += self.calculate_size(c)
        print("The answer to Day 21 part " + str(self.part) + " is " + str(size))


sol1 = Solution(1)
sol1.answer()
sol2 = Solution(2)
sol2.answer()
