import re


class Solution:
    ingredients = []
    effects = {}
    solutions = []

    def __init__(self):
        reader = open('input.txt')
        entries = reader.read().splitlines()
        self.flavours = set()
        for e in entries:
            ingredient = re.search(r"^([\w\-]+)", e).group()
            self.ingredients.append(ingredient)
            self.effects[ingredient] = {}
            effects = re.findall(r"\w+ -*\d+", e)
            effects = [x.split(" ") for x in effects]
            for effect in effects:
                variable = effect[0]
                self.flavours.add(variable)
                change = int(effect[1])
                self.effects[ingredient][variable] = change

    def find_solutions(self, ingredient_list, ingredient_count, space_left):
        next_ingredient = ingredient_list[0]
        new_ingredients = ingredient_list.copy()
        new_ingredients.remove(next_ingredient)

        for i in range(0, space_left + 1):
            new_ingredient_count = ingredient_count.copy()
            new_ingredient_count[next_ingredient] = new_ingredient_count[next_ingredient] + i
            can_balance = self.remove_zeros(new_ingredients, new_ingredient_count)
            space_left = 100 - sum(new_ingredient_count.values())
            if can_balance and space_left == 0:
                self.solutions.append(new_ingredient_count)
            elif can_balance and space_left > 0 and len(new_ingredients) > 0:
                self.find_solutions(new_ingredients, new_ingredient_count, space_left)

    def remove_zeros(self, ingredients, ingredients_count):
        flavour_profile = self.find_flavour_profile(ingredients_count)
        while not self.flavour_profile_valid(flavour_profile):
            for f in self.flavours:
                if flavour_profile[f] <= 0:
                    flavour_profile, can_balance = self.balance_ingredient(f, ingredients_count, flavour_profile,
                                                                           ingredients)
                    if not can_balance:
                        return False
        return True

    def balance_ingredient(self, flavour, ingredients_count, flavour_profile, ingredients):
        flavour_value = flavour_profile[flavour]
        for ingredient in ingredients:
            if self.effects[ingredient][flavour] > 0:
                amount_to_add = (-flavour_value // self.effects[ingredient][flavour]) + 1
                ingredients_count[ingredient] = ingredients_count[ingredient] + amount_to_add
                flavour_profile = self.find_flavour_profile(ingredients_count)
                return flavour_profile, True
        return flavour_profile, False

    def flavour_profile_valid(self, flavour_profile):
        flavour_values = flavour_profile.values()
        for flavour in flavour_values:
            if flavour <= 0:
                return False

        return True

    def find_flavour_profile(self, ingredient_count):
        flavour_profile = {}
        for f in self.flavours:
            flavour_profile[f] = 0

        for i in ingredient_count:
            count = ingredient_count[i]
            for f in self.flavours:
                flavour_profile[f] = flavour_profile[f] + self.effects[i][f] * count
        return flavour_profile

    def part_one(self):
        ingredient_count = {}
        for i in self.ingredients:
            ingredient_count[i] = 0

        self.find_solutions(self.ingredients, ingredient_count, 100)
        solution, value = self.find_optimum_one(0)
        print("The answer to Day 15 part one is " + str(value))

    def part_two(self):
        solution, value = self.find_optimum_one(500)
        print("The answer to Day 15 part two is " + str(value))

    def find_optimum_one(self, ideal_calories):
        optimum = []
        highest_score = 0
        for s in self.solutions:
            flavour_profile = self.find_flavour_profile(s)
            score = 1
            calories = 0
            for f in flavour_profile:
                if f != "calories":
                    score = score * flavour_profile[f]
                else:
                    calories = flavour_profile[f]

            if score > highest_score and (ideal_calories == 0 or calories == ideal_calories):
                optimum = s
                highest_score = score
        return optimum, highest_score


#     winner, distance = self.race(2503)
#
#     print("The answer to Day 14 part one is " + str(distance))
#
# def part_two(self):
#     winner, distance = self.race_by_points(2503)
#
#     print("The answer to Day 14 part two is " + str(distance))


sol = Solution()
sol.part_one()
sol.part_two()
