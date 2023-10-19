import random
from pico2d import load_image

class BigTree:
    def __init__(self):
        self.image = load_image('BigTree.png')
        self.x, self.y = random.randint(50, 750), random.randint(50, 750)

    def draw(self):
        self.image.draw(self.x, self.y, 30, 50)
        print(self.x, self.y)

    def update(self):
        pass