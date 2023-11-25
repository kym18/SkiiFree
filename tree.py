import random
from pico2d import load_image, draw_rectangle, get_events
from man import Man
from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT, SDLK_DOWN, SDLK_UP
#
#
# class BigTree:
#     def __init__(self):  # 생성자 함수, 객체 생성될 때 맨 처음 자동 호출 -> 객체 초기 상태
#         self.image = load_image('Images/BigTree.png')
#         self.x, self.y = random.randint(50, 750), random.randint(50, 750)
#         self.moving_up = False
#
#     # def movingTree(self):
#     #     self.moving_up = True
#
#     def draw(self):
#         if self.y < 800:
#             self.image.draw(self.x, self.y, 30, 50)
#         draw_rectangle(*self.get_bb())  # 튜플을 풀어해쳐서 분리해서 인자로 제공
#
#
#     def update(self):
#         # if self.man_instance.RetrunGameStart():
#         self.y += 10
#     def get_bb(self):
#         return self.x - 15, self.y - 20, self.x + 15, self.y + 20
#
#     def handle_collision(self, groub, other):
#         if groub == 'man:bigree':
#             pass
#
class BigTree:
    def __init__(self):
        self.image = load_image('Images/BigTree.png')
        self.x, self.y = random.randint(50, 750), random.randint(50, 750)
        self.moving_up = False
        self.screen_height = 800  # 화면 높이 설정

    def draw(self):
        if self.y < self.screen_height:
            self.image.draw(self.x, self.y, 30, 50)
            draw_rectangle(*self.get_bb())

    def update(self):
        self.y += 10
        if self.y > self.screen_height:
            self.y = 0  # 화면 상단 밖에서 랜덤한 위치로 다시 생성
            self.x = random.randint(0, 800)

    def get_bb(self):
        return self.x - 15, self.y - 20, self.x + 15, self.y + 20

    def handle_collision(self, groub, other):
        if groub == 'man:bigree':
            pass
