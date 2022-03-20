import re
import math


class Solution:
    weapons = []
    armors = []
    rings = []

    def __init__(self):

        reader = open('shop.txt')
        shop = reader.read().split("\n\n")
        weapons = shop[0].splitlines()
        armors = shop[1].splitlines()
        rings = shop[2].splitlines()
        weapons.pop(0)
        armors.pop(0)
        rings.pop(0)

        for w in weapons:
            weapon_info = w.split()
            weapon = {'name': weapon_info[0], 'cost': int(weapon_info[1]), 'damage': int(weapon_info[2]), 'armor': 0}
            self.weapons.append(weapon)

        no_armor = {'name': 'none', 'cost': 0, 'damage': 0, 'armor': 0}
        self.armors.append(no_armor)

        for a in armors:
            armor_info = a.split()
            armor = {'name': armor_info[0], 'cost': int(armor_info[1]), 'damage': 0, 'armor': int(armor_info[3])}
            self.armors.append(armor)

        no_ring_one = {'name': 'none1', 'cost': 0, 'damage': 0, 'armor': 0}
        no_ring_two = {'name': 'none2', 'cost': 0, 'damage': 0, 'armor': 0}
        self.rings.append(no_ring_one)
        self.rings.append(no_ring_two)
        for r in rings:
            ring_info = r.split()
            ring = {'name': ring_info[0] + " " + ring_info[1], 'cost': int(ring_info[2]), 'damage': int(ring_info[3]),
                    'armor': int(ring_info[4])}
            self.rings.append(ring)

        reader = open('input.txt')
        boss_info = reader.read()
        boss_stats = re.findall(r"\d+", boss_info)
        self.boss = {'hp': int(boss_stats[0]), 'damage': int(boss_stats[1]), 'armor': int(boss_stats[2])}
        self.player = {'hp': 100, 'damage': 0, 'armor': 0}

    def find_cheapest_sol(self, boss, player):
        cheapest = 400
        weapon_combos = self.weapons
        armor_combos = self.armors
        ring_combos = self.find_combos(self.rings)
        items = []
        maximum_spent_and_lost = 0

        for w in weapon_combos:
            weapon_cost = w['cost']
            total_cost = weapon_cost
            if total_cost < cheapest:
                for a in armor_combos:
                    armor_cost = a['cost']
                    total_cost = weapon_cost + armor_cost
                    for r in ring_combos:
                        ring_cost = r['cost']
                        total_cost = weapon_cost + armor_cost + ring_cost
                        if self.would_win(boss, player, [w, a, r]):
                            if total_cost < cheapest:
                                cheapest = total_cost
                                items = [w, a, r]
                        elif total_cost > maximum_spent_and_lost:
                            maximum_spent_and_lost = total_cost

        return cheapest,maximum_spent_and_lost


    def find_combos(self, items):
        item_combos = []
        for i in range(0, len(items)):
            for j in range(i + 1, len(items)):
                item = {}
                item1 = items[i]
                item2 = items[j]
                item['name'] = item1['name'] + " and " + item2['name']
                item['cost'] = item1['cost'] + item2['cost']
                item['damage'] = item1['damage'] + item2['damage']
                item['armor'] = item1['armor'] + item2['armor']
                item_combos.append(item)
        return item_combos


    def would_win(self, boss, player, items):
        for i in items:
            player['damage'] = player['damage'] + i['damage']
            player['armor'] = player['armor'] + i['armor']
        player_hit = player['damage'] - boss['armor']
        player_hit = player_hit if player_hit > 0 else 1
        boss_hit = boss['damage'] - player['armor']
        boss_hit = boss_hit if boss_hit > 0 else 1

        player_turns_to_kill = math.ceil(boss['hp'] / player_hit)
        boss_turns_to_kill = math.ceil(player['hp'] / boss_hit)

        player['damage'] = 0
        player['armor'] = 0

        return player_turns_to_kill <= boss_turns_to_kill


    def part_one(self):
        answer, part_two = self.find_cheapest_sol(self.boss, self.player)
        print("The answer to Day 21 part one is " + str(answer))


    def part_two(self):
        part_one, answer = self.find_cheapest_sol(self.boss, self.player)
        print("The answer to Day 21 part two is " + str(answer))


sol = Solution()
sol.part_one()
sol.part_two()

