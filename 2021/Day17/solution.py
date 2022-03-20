class Solution:
    will_stop_in_x = {}
    will_pass_x = {}
    will_pass_y = {}

    def __init__(self):
        self.target_x_low = 244
        self.target_x_high = 303
        self.target_y_low = -91
        self.target_y_high = -54

    def find_all_x(self):
        for x in range(1, self.target_x_high+1):
            max_dist = self.sum_n(x)
            will_stop_in_zone = False
            if max_dist in range(self.target_x_low, self.target_x_high+1):
                will_stop_in_zone = True
            found_all_points = False
            step = 0
            points = []
            while not found_all_points:
                dist = max_dist - self.sum_n(x-step)
                if dist in range(self.target_x_low, self.target_x_high+1):
                    points.append(step)
                    if will_stop_in_zone:
                        found_all_points = True
                elif dist > self.target_x_high or step > x:
                    found_all_points = True
                step += 1

            if will_stop_in_zone:
                for p in points:
                    if p not in self.will_stop_in_x:
                        self.will_stop_in_x[p] = []
                    self.will_stop_in_x[p].append(x)
            else:
                for p in points:
                    if p not in self.will_pass_x:
                        self.will_pass_x[p] = []
                    self.will_pass_x[p].append(x)


    def find_all_y(self):
        for y in range(self.target_y_low, -self.target_y_low):
            steps_to_get_to_zero = 0
            negative_velocity = y
            if y > 0:
                steps_to_get_to_zero = (y * 2) + 1
                negative_velocity = -y -1


            dist = 0
            steps = 0
            points = []
            all_points_found = False
            while not all_points_found:
                steps += 1
                dist = dist + negative_velocity
                negative_velocity = negative_velocity - 1
                if dist in range(self.target_y_low, self.target_y_high + 1):
                    points.append(steps_to_get_to_zero + steps)
                elif dist < self.target_y_low:
                    all_points_found = True

            for p in points:
                if p not in self.will_pass_y:
                    self.will_pass_y[p] = []
                self.will_pass_y[p].append(y)


    def sum_n(self, x):
        return (x * (x + 1)) // 2

    def find_intersections(self):
        all = set()
        for step in self.will_pass_y:
            if step in self.will_pass_x:
                for x in self.will_pass_x[step]:
                    for y in self.will_pass_y[step]:
                        all.add((x, y))

            for step2 in self.will_stop_in_x:
                if step >= step2:
                    for x in self.will_stop_in_x[step2]:
                        for y in self.will_pass_y[step]:
                            all.add((x, y))

        return len(all)

    def part_two(self):
        self.find_all_x()
        self.find_all_y()
        total = self.find_intersections()
        print("The answer to Day 17 part two is " + str(total))


sol = Solution()
sol.part_two()
