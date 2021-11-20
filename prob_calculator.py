import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for arg in kwargs:
            for ball in range(kwargs[arg]):
                self.contents.append(arg)

    def draw(self, num_draw):
        choosen_balls = []
        if num_draw > len(self.contents):
            return self.contents

        for i in range(num_draw):
            random_ball = random.randint(0, len(self.contents) - 1)
            choosen_balls.append(self.contents[random_ball])
            self.contents.remove(self.contents[random_ball])
        return choosen_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0

    for numbers in range(num_experiments):
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        colors_gotten = hat_copy.draw(num_balls_drawn)
        list_of_trues = []
        for key in expected_copy:
            if colors_gotten.count(key) >= expected_copy[key]:
                list_of_trues.append(True)
                if len(list_of_trues) == len(expected_balls):
                    M += 1

    return M/num_experiments
