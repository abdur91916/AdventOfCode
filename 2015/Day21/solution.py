import re
import math


class Solution:
    moves = {}
    effects = {}
    minimun_mana = 1000000000

    def __init__(self):

        self.moves['Magic Missile'] = 53
        self.moves['Drain'] = 73
        self.moves['Shield'] = 113
        self.moves['Poison'] = 173
        self.moves['Recharge'] = 229

        self.boss = {'hp': 51, 'damage': 9}
        self.player = {'hp': 50, 'mana': 500, 'armor': 0}


    def win_least_mana(self, player, boss, effects, turn, mana_used, health_lost_per_turn):
        current_player = player.copy()
        current_boss = boss.copy()
        current_effects = effects.copy()
        current_mana = mana_used

        current_effects = self.resolve_effects(current_effects, current_boss, current_player)

        if turn == 'boss':
            if current_boss['hp'] <= 0:
                if current_mana < self.minimun_mana:
                    self.minimun_mana = current_mana
                return

            attack = current_boss['damage'] - current_player['armor']
            player_hp = current_player['hp'] - attack
            if player_hp <= 0:
                return
            current_player['hp'] = player_hp
            turn = 'player'
            self.win_least_mana(current_player, current_boss, current_effects, turn, current_mana, health_lost_per_turn)
        else:
            current_player['hp'] = current_player['hp'] - health_lost_per_turn
            if current_player['hp'] <= 0:
                return

            if current_mana >= self.minimun_mana:
                return
            moves_to_check = [k for k in self.moves]
            available_moves = []
            for m in moves_to_check:
                if m not in current_effects and self.moves[m] <= current_player['mana']:
                    available_moves.append(m)
            if len(available_moves) == 0:
                return

            for m in available_moves:
                new_player = current_player.copy()
                new_boss = current_boss.copy()
                new_effects = current_effects.copy()
                new_mana = current_mana
                new_mana = new_mana + self.use_move(m, new_player, new_boss, new_effects)
                if current_boss['hp'] <= 0:
                    if new_mana < self.minimun_mana:
                        self.minimun_mana = new_mana
                    return
                turn = 'boss'
                self.win_least_mana(new_player, new_boss, new_effects, turn, new_mana, health_lost_per_turn)

    def resolve_effects(self, effects, boss, player):
        player['armor'] = 0
        for e in effects:
            if e == 'Shield':
                player['armor'] = 7
            elif e == 'Poison':
                boss['hp'] = boss['hp'] - 3
            elif e == 'Recharge':
                player['mana'] = player['mana'] + 101
            effects[e] = effects[e] - 1
        return {key: val for key, val in effects.items() if val != 0}


    def use_move(self, move, player, boss, effects):
        player['mana'] = player['mana'] - self.moves[move]
        if move == 'Magic Missile':
            boss['hp'] = boss['hp'] - 4
        elif move == 'Drain':
            boss['hp'] = boss['hp'] - 2
            player['hp'] = player['hp'] + 2
        elif move == 'Poison':
            effects['Poison'] = 6
        elif move == 'Shield':
            effects['Shield'] = 6
        elif move == 'Recharge':
            effects['Recharge'] = 5
        else:
            print(move)
        return self.moves[move]





    def part_one(self):
        self.win_least_mana(self.player, self.boss, {},'player', 0, 0)
        answer = self.minimun_mana
        print("The answer to Day 21 part one is " + str(answer))

    def part_two(self):
        self.minimun_mana = 1000000000
        self.win_least_mana(self.player, self.boss, {},'player', 0, 1)
        answer = self.minimun_mana
        print("The answer to Day 21 part one is " + str(answer))


sol = Solution()
sol.part_one()
sol.part_two()

