class DayTwo:
    up = "up"
    down = "down"
    forward = "forward"

    def __init__(self):
        reader = open('input.txt')
        entries = reader.read().splitlines()
        self.entries = entries
        self.numberOfEntries = len(entries)

    def partOne(self):
        horiz = 0
        depth = 0
        for x in self.entries:
            entry = x.split()
            command = entry[0]
            value = int(entry[1])

            if command == self.up:
                depth = depth - value
            elif command == self.down:
                depth = depth + value
            elif command == self.forward:
                horiz = horiz + value
            else:
                print("error cant find sub string in " + x)
        print("depth is " + str(depth) + " and forward is " + str(horiz))
        print("The answer to Day 1 part one is " + str(depth*horiz))

    def partTwo(self):
        horiz = 0
        depth = 0
        aim = 0
        for x in self.entries:
            entry = x.split()
            command = entry[0]
            value = int(entry[1])

            if command == self.up:
                aim = aim - value
            elif command == self.down:
                aim = aim + value
            elif command == self.forward:
                horiz = horiz + value
                depth = depth + (value*aim)
            else:
                print("error cant find sub string in " + x)
        print("depth is " + str(depth) + " and forward is " + str(horiz))
        print("The answer to Day 1 part one is " + str(depth*horiz))

sol = DayTwo()
sol.partOne()
sol.partTwo()
