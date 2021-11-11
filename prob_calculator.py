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

        for choosen_ball_index in range(num_draw):
            choosen_ball_index = random.randrange(0, len(self.contents))
            choosen_balls.append(self.contents[choosen_ball_index])
            self.contents.pop(choosen_ball_index)
        return choosen_balls



# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):