from pico2d import load_image
import random
from pico2d import *

Snow_WIDTH, Snow_HEIGHT = 800, 800


class Snow:
    def __init__(self):  # 생성자 함수, 객체 생성될 때 맨 처음 자동 호출 -> 객체 초기 상태
        self.image = load_image('snowBG.png')

    def draw(self):
        self.image.draw(Snow_WIDTH // 2, Snow_HEIGHT // 2)

    def update(self):
        pass


class Start:
    def __init__(self):  # 생성자 함수, 객체 생성될 때 맨 처음 자동 호출 -> 객체 초기 상태
        self.image = load_image('start.png')

    def draw(self):
        self.image.draw(Snow_WIDTH // 2 - 50, Snow_HEIGHT - 80, 80, 50)

    def update(self):
        pass
