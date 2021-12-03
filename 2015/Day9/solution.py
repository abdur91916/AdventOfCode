import re


class Solution:
    locations = []
    paths = {}

    def __init__(self):
        reader = open('input.txt')
        paths = reader.read().splitlines()
        for x in paths:
            route_distance = x.split(" = ")
            route = route_distance[0].split(" to ")
            from_location = route[0]
            to_location = route[1]
            distance = int(route_distance[1])
            if to_location not in self.locations:
                self.locations.append(to_location)
                self.paths[to_location] = {}
            if from_location not in self.locations:
                self.locations.append(from_location)
                self.paths[from_location] = {}
            self.paths[from_location][to_location] = distance
            self.paths[to_location][from_location] = distance


    def part_one(self):
        shortest_distance = 0
        for start in self.locations:
            locations = self.locations.copy()
            locations.remove(start)
            distance = self.find_shortest_path(locations, start)
            if distance < shortest_distance or shortest_distance == 0:
                shortest_distance = distance
        print("The answer to Day 9 part one is " + str(shortest_distance))

    def find_shortest_path(self, locations, start):
        if len(locations) == 1:
            return self.paths[start][locations[0]]

        shortest_distance = 0
        for next_place in locations:
            new_locations = locations.copy()
            new_locations.remove(next_place)
            distance = self.paths[start][next_place] + self.find_shortest_path(new_locations, next_place)
            if distance < shortest_distance or shortest_distance == 0:
                shortest_distance = distance
        return shortest_distance



    def find_longest_path(self, locations, start):
        if len(locations) == 1:
            return self.paths[start][locations[0]]

        longest_distance = 0
        for next_place in locations:
            new_locations = locations.copy()
            new_locations.remove(next_place)
            distance = self.paths[start][next_place] + self.find_longest_path(new_locations, next_place)
            if distance > longest_distance:
                longest_distance = distance
        return longest_distance

    def part_two(self):
        longest_dist = 0
        for start in self.locations:
            locations = self.locations.copy()
            locations.remove(start)
            distance = self.find_longest_path(locations, start)
            if distance > longest_dist:
                longest_dist = distance
        print("The answer to Day 9 part two is " + str(longest_dist))



sol = Solution()
sol.part_one()
sol.part_two()
