class Solution:
    packet = {}
    version_sum = 0

    def __init__(self):
        reader = open('input.txt')
        input = reader.read()
        self.input = ""
        for c in input:
            self.input += self.convert_to_bin(c)

    def convert_to_bin(self, c):
        if c == "0":
            return "0000"
        elif c == "1":
            return "0001"
        elif c == "2":
            return "0010"
        elif c == "3":
            return "0011"
        elif c == "4":
            return "0100"
        elif c == "5":
            return "0101"
        elif c == "6":
            return "0110"
        elif c == "7":
            return "0111"
        elif c == "8":
            return "1000"
        elif c == "9":
            return "1001"
        elif c == "A":
            return "1010"
        elif c == "B":
            return "1011"
        elif c == "C":
            return "1100"
        elif c == "D":
            return "1101"
        elif c == "E":
            return "1110"
        elif c == "F":
            return "1111"
        else:
            print("ERROR")

    def parse_input(self, input):
        self.packet = self.find_packet(input)

    def find_packet(self, input):
        version = input[0:3]
        type = input[3:6]
        if type == "100":
            packet = {'version': int(version, 2), 'type': int(type, 2)}
            self.version_sum += int(version, 2)
            last_group = False
            group_start = 6
            literal = ''
            while not last_group:
                group = input[group_start:group_start+5]
                if group[0] == '0':
                    last_group = True
                literal += group[1:5]
                group_start += 5
            packet['value'] = int(literal, 2)
            packet_string = input[:group_start]
            return packet_string, packet

        elif type != "100":
            packet = {'version': int(version, 2), 'type': int(type, 2), 'subpackets': []}
            self.version_sum += int(version, 2)
            length_type = input[6]
            if length_type == '0':
                length = int(input[7:22], 2)
                packets_size_found = 0
                while packets_size_found != length:
                    remaining = input[22+packets_size_found:]
                    next_packet_string, next_packet = self.find_packet(remaining)
                    packets_size_found += len(next_packet_string)
                    packet['subpackets'].append(next_packet)
                return input[:22+length], packet
            elif length_type == '1':
                number_of_packets = int(input[7:18], 2)
                current_string = input[:18]
                current_index = 0
                for i in range(0, number_of_packets):
                    remaining = input[18+current_index:]
                    next_packet_string, next_packet = self.find_packet(remaining)
                    current_index += len(next_packet_string)
                    current_string += next_packet_string
                    packet['subpackets'].append(next_packet)
                return current_string, packet

    def resolve(self, packet):
        type = packet['type']
        if type == 4:
            return packet['value']
        elif type == 0:
            sum = 0
            for p in packet['subpackets']:
                sum += self.resolve(p)
            return sum
        elif type == 1:
            mult = 1
            for p in packet['subpackets']:
                mult = mult * self.resolve(p)
            return mult
        elif type == 2:
            values = [self.resolve(p) for p in packet['subpackets']]
            return min(values)
        elif type == 3:
            values = [self.resolve(p) for p in packet['subpackets']]
            return max(values)
        elif type == 5:
            if self.resolve(packet['subpackets'][0]) > self.resolve(packet['subpackets'][1]):
                return 1
            else:
                return 0
        elif type == 6:
            if self.resolve(packet['subpackets'][0]) < self.resolve(packet['subpackets'][1]):
                return 1
            else:
                return 0
        elif type == 7:
            if self.resolve(packet['subpackets'][0]) == self.resolve(packet['subpackets'][1]):
                return 1
            else:
                return 0

    def part_one(self):
        packet_string, packet = self.find_packet(self.input)
        self.packet = packet
        print("The answer to Day 16 part one is " + str(self.version_sum))

    def part_two(self):
        answer = self.resolve(self.packet)
        print("The answer to Day 14 part two is " + str(answer))

sol = Solution()
sol.part_one()
sol.part_two()
