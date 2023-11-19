import random
from pico2d import load_image, draw_rectangle


class Stone:
    def __init__(self): #생성자 함수, 객체 생성될 때 맨 처음 자동 호출 -> 객체 초기 상태
        self.image = load_image('stone.png')
        self.x, self.y = random.randint(40, 780), random.randint(40, 780)

    def draw(self):
        self.image.draw(self.x, self.y, 20, 25)
        draw_rectangle(*self.get_bb())  # 튜플을 풀어해쳐서 분리해서 인자로 제공

        #print(self.x, self.y)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10
