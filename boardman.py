from pico2d import load_image, get_time
import random


class boardMan:
    def __init__(self):
        self.image = load_image('Images/boardman.png')
        self.frame = 0
        self.x, self.y = random.randint(30, 770), -100  # 시작 시 y 좌표를 화면 밖으로 설정
        self.speed = 5
        self.last_time = get_time()

    def draw(self):
        self.image.clip_draw(self.frame * 70 + 4, 0, 73, 100, self.x, self.y, 50, 60)

    def update(self):
        current_time = get_time()
        if current_time - self.last_time > 25.0:  # 25초가 지난 후에 나타남
            self.y = 810  # 새로운 y 좌표 설정
            self.last_time = current_time
        else:
            self.frame = (self.frame + 1) % 3
            self.y -= self.speed
