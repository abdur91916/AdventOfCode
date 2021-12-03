class DayTwo:

    def __init__(self):
        reader = open('input.txt')
        entries = reader.read().splitlines()
        self.entries = entries
        self.numberOfEntries = len(entries)
        self.bitLength = len(entries[0])

    def part_one(self):
        gamma_rate = ""
        epsilon_rate = ""
        for i in range(0, self.bitLength):
            count = 0
            for x in self.entries:
                bit = int(x[i])
                if bit == 1:
                    count = count + 1
                else:
                    count = count - 1
            if count > 0:
                gamma_rate = gamma_rate + str(1)
                epsilon_rate = epsilon_rate + str(0)
            elif count < 0:
                gamma_rate = gamma_rate + str(0)
                epsilon_rate = epsilon_rate + str(1)
            else:
                print("error")
        epsilon = int(epsilon_rate, 2)
        gamma = int(gamma_rate, 2)
        power = epsilon * gamma
        print("The answer to Day 3 part one is " + str(power))

    def part_two(self):
        oxygen = self.entries.copy()
        c02 = self.entries.copy()
        for i in range(0, self.bitLength):

            count_oxygen = 0
            one_list_oxygen = []
            zero_list_oxygen = []
            count_c02 = 0
            one_list_c02 = []
            zero_list_c02 = []
            if len(oxygen) > 1:
                for x in oxygen:
                    bit = int(x[i])
                    if bit == 1:
                        count_oxygen = count_oxygen + 1
                        one_list_oxygen.append(x)
                    else:
                        count_oxygen = count_oxygen - 1
                        zero_list_oxygen.append(x)

                if count_oxygen > 0:
                    oxygen = one_list_oxygen.copy()
                elif count_oxygen < 0:
                    oxygen = zero_list_oxygen.copy()
                elif count_oxygen == 0:
                    oxygen = one_list_oxygen.copy()

            if len(c02) > 1:
                for x in c02:
                    bit = int(x[i])
                    if bit == 1:
                        count_c02 = count_c02 + 1
                        one_list_c02.append(x)
                    else:
                        count_c02 = count_c02 - 1
                        zero_list_c02.append(x)

                if count_c02 > 0:
                    c02 = zero_list_c02.copy()
                elif count_c02 < 0:
                    c02 = one_list_c02.copy()
                elif count_c02 == 0:
                    c02 = zero_list_c02.copy()

        oxygen_value = int(oxygen[0], 2)
        c02_value = int(c02[0], 2)

        life_support = oxygen_value * c02_value
        print("The answer to Day 3 part two is " + str(life_support))





sol = DayTwo()
sol.part_one()
sol.part_two()
