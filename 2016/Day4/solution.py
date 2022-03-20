import re


class Solution:

    def __init__(self):
        reader = open('input.txt')
        rooms = reader.read().splitlines()
        self.rooms = []
        for r in rooms:
            sector = re.search(r"\d+", r).group()
            checksum = re.search(r"\[\w+\]", r).group()
            room = r
            room = room.replace(checksum, '')
            room = room.replace(sector, '')
            room = room[0:-1]
            checksum = checksum.replace('[', '')
            checksum = checksum.replace(']', '')
            self.rooms.append({'room': room, 'sector': int(sector), 'check': checksum})


    def find_valid_rooms(self, rooms):
        valid = []
        combined_sum = 0
        for r in rooms:
            room = r['room']
            chars = {}
            for c in room:
                if c != '-':
                    if c not in chars:
                        chars[c] = 1
                    else:
                        chars[c] = chars[c] + 1
            sorted_dict = {k: chars[k] for k in sorted(chars)}
            sorted_chars = sorted(sorted_dict.items(), key=lambda item: item[1], reverse=True)
            check_expected = ''
            for c, count in sorted_chars:
                check_expected = check_expected + c
            check_expected = check_expected[0:5]

            check = r['check']
            sector = r['sector']
            if check_expected == check:
                valid.append(r)
                combined_sum = combined_sum + sector
        return combined_sum, valid



    def decrypt(self, rooms):
        decrypted_rooms = []
        for r in rooms:
            room_copy = r.copy()
            name = r['room']
            sector = r['sector']
            new_name = ''
            for c in name:
                new_char = ' '
                if c != '-':
                    old_char_int = ord(c) - 97
                    new_char_int = (old_char_int + sector) % 26 + 97
                    new_char = chr(new_char_int)
                new_name = new_name + new_char
            room_copy['room'] = new_name
            decrypted_rooms.append(room_copy)
        return decrypted_rooms

    def find(self, rooms, target):
        found = []
        for r in rooms:
            name = r['room']
            if target in name:
                found.append(r)
        return found


    def part_one(self):
        sum, valid = self.find_valid_rooms(self.rooms)
        self.valid_rooms = valid
        print("The answer to Day 4 part one is " + str(sum))

    def part_two(self):
        rooms = self.decrypt(self.valid_rooms)
        rooms = self.find(rooms, 'northpole')
        room = rooms[0]
        sector = room['sector']
        print("The answer to Day 4 part one is " + str(sector))



sol = Solution()
sol.part_one()
sol.part_two()
