class Solution:
    up = "^"
    down = "v"
    left = "<"
    right = ">"

    def __init__(self):
        reader = open('input.txt')
        directions = reader.read()
        self.directions = directions

    def house_to_string(self, x, y):
        return str(x) + "," + str(y)

    def part_one(self):
        current_house_x = 0
        current_house_y = 0
        houses_visited = {self.house_to_string(current_house_x, current_house_y)}
        for x in self.directions:
            if x == self.up:
                current_house_y = current_house_y + 1
            elif x == self.down:
                current_house_y = current_house_y - 1
            elif x == self.right:
                current_house_x = current_house_x + 1
            elif x == self.left:
                current_house_x = current_house_x - 1
            else:
                print("error")
                break
            houses_visited.add(self.house_to_string(current_house_x, current_house_y))
        print("The answer to Day 1 part one is " + str(len(houses_visited)))

    def part_two(self):
        current_house_santa_x = 0
        current_house_santa_y = 0
        current_house_robot_x = 0
        current_house_robot_y = 0
        santas_turn = True
        houses_visited = {self.house_to_string(current_house_santa_x, current_house_santa_y)}
        for x in self.directions:
            if x == self.up:
                if santas_turn:
                    current_house_santa_y = current_house_santa_y + 1
                else:
                    current_house_robot_y = current_house_robot_y + 1
            elif x == self.down:
                if santas_turn:
                    current_house_santa_y = current_house_santa_y - 1
                else:
                    current_house_robot_y = current_house_robot_y - 1
            elif x == self.right:
                if santas_turn:
                    current_house_santa_x = current_house_santa_x + 1
                else:
                    current_house_robot_x = current_house_robot_x + 1
            elif x == self.left:
                if santas_turn:
                    current_house_santa_x = current_house_santa_x - 1
                else:
                    current_house_robot_x = current_house_robot_x - 1
            else:
                print("error")
                break
            if santas_turn:
                houses_visited.add(self.house_to_string(current_house_santa_x, current_house_santa_y))
            else:
                houses_visited.add(self.house_to_string(current_house_robot_x, current_house_robot_y))
            santas_turn = not santas_turn
        print("The answer to Day 1 part two is " + str(len(houses_visited)))

sol = Solution()
sol.part_one()
sol.part_two()