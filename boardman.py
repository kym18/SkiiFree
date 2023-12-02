from pico2d import load_image, get_time, draw_rectangle
import random


class boardMan:
    def __init__(self):
        self.image = load_image('Images/boardman.png')
        self.frame = 0
        self.x, self.y = random.randint(300, 500), -100  # 시작 시 y 좌표를 화면 밖으로 설정
        self.speed = 5
        self.last_time = get_time()
        self.action = 0  # 0이면 하강중. 1이면 부닥침
        self.opCount = 0;  # 넘어지는
        self.optime = 0;  # 넘어지는 시간

    def draw(self):
        draw_rectangle(*self.get_bb())  # 튜플을 풀어해쳐서 분리해서 인자로 제공
        if self.action == 0:
            self.image.clip_draw(self.frame * 70 + 4, 0, 73, 100, self.x, self.y, 50, 60)
        elif self.action == 1:
            self.image.clip_draw(self.frame * 70 + 78 * 3 - 12, 0, 80, 100, self.x, self.y, 40, 55)

    def update(self):
        current_time = get_time()
        if current_time - self.last_time > 25.0:  # 25초가 지난 후에 나타남
            self.y = 810  # 새로운 y 좌표 설정
            self.last_time = current_time
        # else:
        if self.action == 0:
            self.frame = (self.frame + 1) % 3
        elif self.action == 1:  # 넘어짐
            self.frame = 0
            self.y += self.speed / 2
            self.opCount += 1
            self.optime += 1

            if self.opCount <= 15:
                self.opCount = 0
            if self.optime >= 29:
                self.action = 0

        self.y -= self.speed

    def get_bb(self):
        return self.x - 10, self.y - 20, self.x + 10, self.y + 20

    def handle_collision(self, groub, other):
        if groub == 'Bboy:bigtree':
            self.action = 1
        elif groub == 'Bboy:stone':
            self.action = 1
        elif groub == 'man:Bboy':
            self.action = 1
            print('보드맨 사람 ㅠㅠ')

    def reset(self):
        self.x, self.y = random.randint(300, 500), -100
        self.frame = 0
        self.speed = 5
        self.last_time = get_time()
        self.action = 0
        self.opCount = 0
        self.optime = 0
