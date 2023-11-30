import random
from pico2d import load_image, draw_rectangle, get_time


class Stone:
    def __init__(self): #생성자 함수, 객체 생성될 때 맨 처음 자동 호출 -> 객체 초기 상태
        global start_Count
        self.image = load_image('Images/stone.png')
        self.x, self.y = random.randint(40, 780), random.randint(40, 780)
        self.screen_height = 800  # 화면 높이 설정
        self.last_time = get_time()
        self.dir = 0

    def draw(self):
        if self.y < 800:
            self.image.draw(self.x, self.y, 20, 25)
            draw_rectangle(*self.get_bb())  # 튜플을 풀어해쳐서 분리해서 인자로 제공

        #print(self.x, self.y)

    def update(self):
        current_time = get_time()
        if self.dir == 0:
            if current_time - self.last_time > 3.0:  # 3초가 지난 후에 나타남
                self.y += 10
            if self.y > self.screen_height:
                self.y = 0  # 화면 상단 밖에서 랜덤한 위치로 다시 생성
                self.x = random.randint(0, 800)
        elif self.dir == 1:
            None

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, groub, other):
        if groub == 'man:stone':
            pass
