import random
from pico2d import load_image

class Stone:
    def __init__(self): #생성자 함수, 객체 생성될 때 맨 처음 자동 호출 -> 객체 초기 상태
        self.image = load_image('stone.png')
        self.x, self.y = random.randint(40, 780), random.randint(40, 780)

    def draw(self):
        self.image.draw(self.x, self.y, 20, 25)
        #print(self.x, self.y)

    def update(self):
        pass