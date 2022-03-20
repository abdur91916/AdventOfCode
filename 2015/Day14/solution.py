import re


class Solution:
    racers = []
    speed = {}
    stamina = {}
    rest = {}

    def __init__(self):
        reader = open('input.txt')
        entries = reader.read().splitlines()
        for e in entries:
            racer = re.search(r"^([\w\-]+)", e).group()
            speed_info = re.search(r"\d+ km/s for \d+", e).group()
            speed_info = re.findall(r"\d+", speed_info)
            speed = int(speed_info[0])
            run_time = int(speed_info[1])

            rest_info = re.search(r"rest for \d+", e).group()
            rest_time = int(re.search(r"\d+", rest_info).group())

            self.racers.append(racer)
            self.speed[racer] = speed
            self.stamina[racer] = run_time
            self.rest[racer] = rest_time

    def race(self, time):
        winners = []
        distance_by_winner = 0

        for r in self.racers:
            distance = 0
            distance_in_cycle = self.speed[r] * self.stamina[r]
            cycle_time = self.stamina[r] + self.rest[r]

            full_cycles = time // cycle_time
            distance = distance_in_cycle * full_cycles


            remaining_time = time % cycle_time

            if remaining_time != 0:
                if remaining_time > self.stamina[r]:
                    distance = distance + distance_in_cycle
                else:
                    distance = distance + (self.speed[r] * remaining_time)

            if distance > distance_by_winner:
                winners = [r]
                distance_by_winner = distance
            elif distance == distance_by_winner:
                winners.append(r)

        return winners, distance_by_winner


    def race_by_points(self, time):
        points = {}
        for r in self.racers:
            points[r] = 0

        for i in range(1, time+1):
            winners, distance = self.race(i)
            for w in winners:
                points[w] = points[w] + 1

        highest_scorer = ""
        highest_score = 0

        for r in points:
            if points[r] > highest_score:
                highest_scorer = r
                highest_score = points[r]

        return highest_scorer, highest_score


    def part_one(self):
        winner, distance = self.race(2503)

        print("The answer to Day 14 part one is " + str(distance))

    def part_two(self):
        winner, distance = self.race_by_points(2503)

        print("The answer to Day 14 part two is " + str(distance))


sol = Solution()
sol.part_one()
sol.part_two()
