import random
from pico2d import load_image, draw_rectangle, get_events, get_time
from man import Man
from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT, SDLK_DOWN, SDLK_UP

class BigTree:
    def __init__(self):
        self.image = load_image('Images/BigTree.png')
        self.x, self.y = random.randint(50, 750), random.randint(50, 750)
        self.moving_up = False
        self.screen_height = 800  # 화면 높이 설정
        self.last_time = get_time()
        self.speed = 10
        self.dir = 0 #0이면 내려가기 ㄱㄴ 1이면 게임오버라 정지.

    def draw(self):
        if self.y < self.screen_height:
            self.image.draw(self.x, self.y, 30, 50)
            # draw_rectangle(*self.get_bb())

    def update(self):
        current_time = get_time()
        if self.dir == 0:
            if current_time - self.last_time > 3.0:  # 3초 후 증가
                self.y += self.speed
            # self.last_time = current_time
            if self.y > self.screen_height:
                self.y = 0  # 화면 상단 밖에서 랜덤한 위치로 다시 생성
                self.x = random.randint(0, 800)
        elif self.dir == 1:
            None


    def get_bb(self):
        return self.x - 8, self.y - 15, self.x + 8, self.y + 15

    def handle_collision(self, groub, other):
        if groub == 'man:bigtree':
            self.y -= self.speed / 2



