import collections

import numpy as np
import re


class Solution:
    wins = {1: 0, 2: 0}
    dice_combos = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

    def __init__(self):
        self.player_1_start = 4
        self.player_2_start = 10

    def play_dice_1(self, player_1_start, player_2_start):
        player_1_pos = player_1_start
        player_2_pos = player_2_start
        player_1_score = 0
        player_2_score = 0
        number_of_rolls = 0
        current_player = 1
        while player_1_score < 1000 and player_2_score < 1000:
            # roll 3 times
            movement = (3 * (number_of_rolls % 10) + 6) % 10
            number_of_rolls += 3
            if current_player == 1:
                player_1_pos = (player_1_pos + movement -1 ) % 10 +1
                player_1_score += player_1_pos
            else:
                player_2_pos = (player_2_pos + movement -1) % 10 +1
                player_2_score += player_2_pos
            current_player = (current_player + 1) % 2
        if player_1_score >= 1000:
            return player_2_score * number_of_rolls
        else:
            return player_1_score * number_of_rolls

    def play_dice_2(self, player_1_pos, player_2_pos, player_1_score, player_2_score, current_player, stakes):
        if player_1_score >= 21:
            self.wins[1] += stakes
            return
        elif player_2_score >= 21:
            self.wins[2] += stakes
            return

        if current_player == 1:
            next_player = 2
            for i in self.dice_combos:
                new_player_1_pos = (player_1_pos + i -1) % 10 +1
                new_score = player_1_score + new_player_1_pos
                new_stakes = stakes * self.dice_combos[i]
                self.play_dice_2(new_player_1_pos, player_2_pos, new_score, player_2_score, next_player, new_stakes)
        elif current_player == 2:
            next_player = 1
            for i in self.dice_combos:
                new_player_2_pos = (player_2_pos + i -1) % 10 +1
                new_score = player_2_score + new_player_2_pos
                new_stakes = stakes * self.dice_combos[i]
                self.play_dice_2(player_1_pos, new_player_2_pos, player_1_score, new_score, next_player, new_stakes)

    def part_one(self):
        score = self.play_dice_1(self.player_1_start, self.player_2_start)

        print("The answer to Day 21 part one is " + str(score))

    def part_two(self):
        self.play_dice_2(self.player_1_start, self.player_2_start, 0, 0, 1, 1)

        print("The answer to Day 21 part two is " + str(max(self.wins.values())))


sol = Solution()
sol.part_one()
sol.part_two()
