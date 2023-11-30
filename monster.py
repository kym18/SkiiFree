import math

from pico2d import load_image, get_time, draw_rectangle
import random
import play_mode


class Monster:
    def __init__(self):
        self.image = load_image('Images/monster.png')
        self.frame = 0
        self.x, self.y = random.randint(300, 500), -100  # 시작 시 y 좌표를 화면 밖으로 설정
        self.speed = 3
        self.last_time = get_time()
        self.action = 0  # 0이면 달려감. 1이면 잡아먹음

    def draw(self):
        draw_rectangle(*self.get_bb())  # 튜플을 풀어해쳐서 분리해서 인자로 제공
        if self.action == 0:
            self.image.clip_draw(self.frame * 80 + 30, 0, 76, 130, self.x, self.y, 50, 60)
        elif self.action == 1:
            self.image.clip_draw(self.frame * 80 + 30, 0, 76, 130, self.x, self.y, 50, 60)

    def move_slightly_to(self, tx, ty):  # 조금씩 움직이는거
        self.dir = math.atan2(ty - self.y, tx - self.x)
        # self.speed = RUN_SPEED_PPS
        self.x += self.speed * math.cos(self.dir)
        self.y += self.speed * math.sin(self.dir)

    def move_away(self, tx, ty):  # 조금씩 움직이는거
        self.dir = math.atan2(ty - self.y, tx - self.x)
        # self.speed = RUN_SPEED_PPS
        self.x += self.speed * math.cos(self.dir)
        self.y += self.speed * math.sin(self.dir)

    def update(self):
        current_time = get_time()
        if current_time - self.last_time > 5.0:  # 25초가 지난 후에 나타남
            self.y = 810  # 새로운 y 좌표 설정
            self.last_time = current_time
        else:
            if self.action == 0: #달려감
                self.frame = (self.frame + 1) % 4
                self.move_slightly_to(play_mode.man.x, play_mode.man.y)

            elif self.action == 1: #멀어딤
                self.frame = (self.frame + 1) % 4
                self.move_slightly_to(-play_mode.man.x, -play_mode.man.y)


    def get_bb(self):
        return self.x - 10, self.y - 20, self.x + 10, self.y + 20

    def handle_collision(self, groub, other):
        pass

