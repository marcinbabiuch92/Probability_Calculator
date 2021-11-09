import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        contents = []
        for arg in kwargs:
            for ball in range(kwargs[arg]):
                contents.append(arg)
        print(contents)



# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):