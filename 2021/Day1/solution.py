class DayOne:
    def __init__(self):
        reader = open('input.txt')
        entries = reader.read().splitlines()
        self.entries = entries
        self.numberOfEntries = len(entries)

    def partOne(self):
        numberOfIncreases = 0
        for i in range(1, self.numberOfEntries):
            previous = int(self.entries[i - 1])
            current = int(self.entries[i])
            if current > previous:
                numberOfIncreases = numberOfIncreases + 1
        print("The answer to Day 1 part one is " + str(numberOfIncreases))

    def partTwo(self):
        numberOfIncreases = 0
        for i in range(3, self.numberOfEntries):
            previous = int(self.entries[i - 3]) + int(self.entries[i - 2]) + int(self.entries[i - 1])
            current = int(self.entries[i-2]) + int(self.entries[i-1]) + int(self.entries[i])
            if current > previous:
                numberOfIncreases = numberOfIncreases + 1
        print("The answer to Day 1 part two is " + str(numberOfIncreases))

sol = DayOne()
sol.partOne()
sol.partTwo()
