import random
from pico2d import load_image, draw_rectangle


class BigTree:
    def __init__(self): #생성자 함수, 객체 생성될 때 맨 처음 자동 호출 -> 객체 초기 상태
        self.image = load_image('BigTree.png')
        self.x, self.y = random.randint(50, 750), random.randint(50, 750)

    def draw(self):
        self.image.draw(self.x, self.y, 30, 50)
        draw_rectangle(*self.get_bb())  # 튜플을 풀어해쳐서 분리해서 인자로 제공

        #print(self.x, self.y)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 15, self.y - 20, self.x + 15, self.y + 20

    def handle_collision(self, groub, other):
        if groub == 'man:bigree':
            pass