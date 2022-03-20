
class Solution:
    people = []
    happiness = {}

    def __init__(self):
        reader = open('input.txt')
        happiness_table = reader.read().splitlines()
        for x in happiness_table:
            person_1 = ""
            person_2 = ""
            happiness = 0
            if "gain" in x:
                data_array = x.split(" would gain ")
                happiness_and_person_2 = data_array[1].split(" happiness units by sitting next to ")
                person_1 = data_array[0]
                happiness = int(happiness_and_person_2[0])
                person_2 = happiness_and_person_2[1]
                person_2 = person_2[0:len(person_2) - 1]
            if "lose" in x:
                data_array = x.split(" would lose ")
                happiness_and_person_2 = data_array[1].split(" happiness units by sitting next to ")
                person_1 = data_array[0]
                happiness = - int(happiness_and_person_2[0])
                person_2 = happiness_and_person_2[1]
                person_2 = person_2[0:len(person_2)-1]
            if person_1 not in self.people:
                self.people.append(person_1)
                self.happiness[person_1] = {}
            self.happiness[person_1][person_2] = happiness

    def find_ideal_seating(self, people_left_to_seat, starting_person, last_placed_person):
        overall_happiness = 0
        if len(people_left_to_seat) == 1:
            last_person = people_left_to_seat[0]
            overall_happiness = overall_happiness + self.seat_together(last_person, last_placed_person)
            overall_happiness = overall_happiness + self.seat_together(last_person, starting_person)
        else:
            for p in people_left_to_seat:
                new_left_to_seat = people_left_to_seat.copy()
                new_left_to_seat.remove(p)
                happiness_if_seated = self.seat_together(p, last_placed_person) + self.find_ideal_seating(
                    new_left_to_seat, starting_person, p)
                if happiness_if_seated > overall_happiness:
                    overall_happiness = happiness_if_seated
        return overall_happiness

    def seat_together(self, p1, p2):
        if p1 == "santa" or p2 == "santa":
            return 0
        return self.happiness[p1][p2] + self.happiness[p2][p1]


    def part_one(self):
        people_left = self.people.copy()
        first_person = people_left[0]
        people_left.remove(first_person)
        happiness = self.find_ideal_seating(people_left, first_person, first_person)

        print("The answer to Day 13 part two is " + str(happiness))

    def part_two(self):
        people_left = self.people.copy()
        first_person = "santa"
        happiness = self.find_ideal_seating(people_left, first_person, first_person)

        print("The answer to Day 13 part two is " + str(happiness))

sol = Solution()
sol.part_one()
sol.part_two()

