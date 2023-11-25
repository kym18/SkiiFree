from pico2d import load_image
import random

class boardMan:
    def __init__(self): #생성자 함수, 객체 생성될 때 맨 처음 자동 호출 -> 객체 초기 상태
        self.image = load_image('Images/boardman.png')
        self.frame = 0
        self.x, self.y = random.randint(50, 750), 820
        self.speed = 5

    def draw(self):
            self.image.clip_draw(self.frame * 70 + 4 , 0, 73, 100, self.x, self.y, 50, 60)

    def update(self):
        self.frame = (self.frame + 1) % 3
        self.y -= self.speed
