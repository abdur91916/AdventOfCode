import collections

import numpy as np
import re
from typing import NamedTuple


class Solution:
    energies = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    rooms_1 = {'A': [(2, 3), (3, 3)], 'B': [(2, 5), (3, 5)], 'C': [(2, 7), (3, 7)], 'D': [(2, 9), (3, 9)]}
    rooms = {'A': [(2, 3), (3, 3), (4, 3), (5, 3)],
             'B': [(2, 5), (3, 5), (4, 5), (5, 5)],
             'C': [(2, 7), (3, 7), (4, 7), (5, 7)],
             'D': [(2, 9), (3, 9), (4, 9), (5, 9)]}

    min_energy = 10000000

    def __init__(self):
        playing_board = []
        reader = open('input2.txt')
        input = reader.read().splitlines()
        for c in input:
            playing_board.append(list(c))
        self.playing_board = np.array(playing_board)
        self.players = []
        self.empty_pos = []

        for i in range(0, len(playing_board)):
            for j in range(0, len(playing_board[i])):
                if playing_board[i][j] != '#' and playing_board[i][j] != '.':
                    self.players.append((playing_board[i][j], (i, j)))
                elif playing_board[i][j] == '.' and playing_board[i+1][j] == '#':
                    self.empty_pos.append((i,j))
        print()


    def can_move_to_position_on_corridor(self, game_board, player, target):
        player_letter, position = player
        i_player, j_player = position
        i_target, j_target = target
        if i_player == 1:
            return False
        up = game_board[i_target:i_player, j_player: j_player+1].flatten()
        step = -1 if j_target > j_player else 1
        across = game_board[i_target:i_target+1, j_target:j_player:step].flatten()

        unblocked = (up == '.').sum() == len(up) and (across == '.').sum() == len(across)

        return unblocked

    def can_move_to_room(self, player, game_board):
        player_letter, position = player
        pos_i, pos_j = position
        target = self.rooms[player_letter]
        slot_1 = target[0]
        slot_2 = target[1]

        if position == slot_2:
            return True, 0, slot_2

        occupant_1 = game_board[slot_1[0]][slot_1[1]]
        occupant_2 = game_board[slot_2[0]][slot_2[1]]

        if occupant_1 != player_letter and occupant_1 != '.':
            return False, 0, None
        if occupant_2 != player_letter and occupant_2 != '.':
            return False, 0, None

        steps = 0
        current_i = pos_i
        current_j = pos_j
        for i in range(pos_i, 1, -1):
            current_i += -1
            steps += 1
            cell_above = game_board[i-1][pos_j]
            if cell_above != '.':
                return False, 0, None

        step = -1 if pos_j > slot_1[1] else 1
        for i in range(pos_j, slot_1[1], step):
            steps += 1
            current_j += step
            cell_adjacent = game_board[current_i][i+step]
            if cell_adjacent != '.':
                return False, 0, None

        for i in range(1, slot_1[0]):
            steps += 1
            current_i += 1
            cell_adjacent = game_board[i+1][current_j]
            if cell_adjacent != '.':
                return False, 0, None

        if occupant_2 == '.':
            steps += 1
            return True, steps, slot_2

        return True, steps, slot_1

    def can_move_to_room_2(self, player, game_board):
        player_letter, position = player
        pos_i, pos_j = position
        targets = self.rooms[player_letter]
        room_to_give = len(targets) - 1

        if position == targets[-1]:
            return True, 0, position

        for t in targets:
            if game_board[t[0]][t[1]] != '.':
                room_to_give += -1
                if game_board[t[0]][t[1]] != player_letter:
                    return False, 0, None

        slot_1 = targets[0]


        steps = 0
        current_i = pos_i
        current_j = pos_j
        for i in range(pos_i, 1, -1):
            current_i += -1
            steps += 1
            cell_above = game_board[i-1][pos_j]
            if cell_above != '.':
                return False, 0, None

        step = -1 if pos_j > slot_1[1] else 1
        for i in range(pos_j, slot_1[1], step):
            steps += 1
            current_j += step
            cell_adjacent = game_board[current_i][i+step]
            if cell_adjacent != '.':
                return False, 0, None

        for i in range(1, slot_1[0]):
            steps += 1
            current_i += 1
            cell_adjacent = game_board[i+1][current_j]
            if cell_adjacent != '.':
                return False, 0, None

        steps += room_to_give


        return True, steps, targets[room_to_give]

    def play(self, game_board, energy, unsorted_players, empty_slots, d):

        if energy < self.min_energy:
            players_moved = True
            while players_moved:
                sorted_players = []
                players_moved = False
                for p in unsorted_players:
                    can_move, steps, new_pos = self.can_move_to_room_2(p, game_board)
                    char, old_slot = p
                    if can_move:
                        players_moved = True
                        energy += self.energies[char] * steps
                        sorted_players.append(p)
                        game_board[old_slot[0]][old_slot[1]] = '.'
                        game_board[new_pos[0]][new_pos[1]] = char
                        if old_slot[0] == 1:
                            empty_slots.append(old_slot)
                for p in sorted_players:
                    unsorted_players.remove(p)

            if len(unsorted_players) == 0:
                if energy < self.min_energy:
                    self.min_energy = energy
                    print(energy)
            else:
                for p in unsorted_players:
                    for positon in empty_slots:
                        if self.can_move_to_position_on_corridor(game_board, p, positon):
                            char, old_pos = p
                            new_game_board = game_board.copy()
                            new_game_board[positon[0]][positon[1]] = char
                            new_game_board[old_pos[0]][old_pos[1]] = '.'
                            moves = abs(positon[0] - old_pos[0]) + abs(positon[1] - old_pos[1])
                            new_energy = energy + moves * self.energies[char]
                            new_unsorted_players = unsorted_players.copy()
                            new_unsorted_players.remove(p)
                            new_unsorted_players.append((char, positon))
                            new_empty_slots = empty_slots.copy()
                            new_empty_slots.remove(positon)

                            self.play(new_game_board, new_energy, new_unsorted_players, new_empty_slots, d+1)



    def part_one(self):
        self.play(self.playing_board, 0, self.players, self.empty_pos, 0)
        print("The answer to Day 21 part one is " + str(self.min_energy))


sol = Solution()
sol.part_one()
