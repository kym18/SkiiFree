from pico2d import load_image
import random
from pico2d import *

Snow_WIDTH, Snow_HEIGHT = 800, 800


class Count:
    def __init__(self):
        self.image = load_image('Images/count.png')
        self.last_time = get_time()
        self.x, self.y = Snow_WIDTH // 2, Snow_HEIGHT // 2
        self.Count = 3
        self.frame = 0

    def draw(self):
        if self.Count == 3:
            self.image.clip_draw(self.frame * 100 + 250, 0, 130, 165, self.x, self.y, 100, 110)
        elif self.Count == 2:
            self.image.clip_draw(self.frame * 100 + 100, 0, 130, 165, self.x, self.y, 100, 110)
        elif self.Count == 1:
            self.image.clip_draw(self.frame * 100, 0, 130, 165, self.x, self.y, 100, 110)
        elif self.Count == 0:
            None

    def update(self):
        current_time = get_time()
        time_elapsed = current_time - self.last_time  # 경과한 시간 계산

        if time_elapsed >= 1.0:  # 1초 이상 경과한 경우
            self.Count = max(0, self.Count - int(time_elapsed))  # self.Count를 0까지 감소시킴
            self.last_time = current_time  # 마지막 시간 갱신


class Snow:
    def __init__(self):  # 생성자 함수, 객체 생성될 때 맨 처음 자동 호출 -> 객체 초기 상태
        self.image = load_image('Images/snowBG.png')

    def draw(self):
        self.image.draw(Snow_WIDTH // 2, Snow_HEIGHT // 2)

    def update(self):
        pass


class Start:
    def __init__(self):  # 생성자 함수, 객체 생성될 때 맨 처음 자동 호출 -> 객체 초기 상태
        self.image = load_image('Images/start.png')
        self.screen_height = 800  # 화면 높이 설정
        self.y = Snow_HEIGHT - 80
        self.last_time = get_time()

    def draw(self):
        if self.y < 800:
            self.image.draw(Snow_WIDTH // 2 - 50, self.y, 80, 50)

    def update(self):
        current_time = get_time()
        if current_time - self.last_time > 3.0:  # 25초가 지난 후에 나타남
            self.y += 10
