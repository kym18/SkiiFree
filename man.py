from pico2d import load_image
from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT

Snow_WIDTH, Snow_HEIGHT = 800, 800

class Man:
    def __init__(self): #생성자 함수, 객체 생성될 때 맨 처음 자동 호출 -> 객체 초기 상태
        self.image = load_image('snowman.png')
        self.frame = 0
        self.x, self.y = Snow_WIDTH // 2 - 10, Snow_HEIGHT - 130
        self.speed = 10
        self.dir = 3 # 0:정지, 1:오른쪽,-1:왼쪽, 3:정지



    def draw(self):
        if self.dir == 3: #정면
            self.image.clip_draw(self.frame * 0 + 200 -2, 0, 45, 100, self.x, self.y, 30, 55)
        elif self.dir == 1: #오른쪽
            self.image.clip_draw(self.frame * 0 + 135, 0, 65, 100, self.x, self.y, 50, 60)
            self.x += 3
        elif self.dir == -1: #왼쪽
            self.image.clip_composite_draw(self.frame * 0 + 135, 0, 65, 100, 0, 'h', self.x, self.y, 50, 60)
            self.x -= 3
        elif self.dir == 0: #정지
            self.image.clip_draw(self.frame * 0 + 18, 0, 72, 100, self.x, self.y, 50, 60)



    def update(self):
        #self.frame = (self.frame + 1) % 8

        if self.dir == 0:
            self.speed = 0
        elif self.dir != 0:
            self.y -= self.speed
