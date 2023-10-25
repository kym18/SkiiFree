from pico2d import load_image
Snow_WIDTH, Snow_HEIGHT = 800, 800
class Man:
    def __init__(self): #생성자 함수, 객체 생성될 때 맨 처음 자동 호출 -> 객체 초기 상태
        self.image = load_image('skii.png')
        self.frame = 0
        self.x, self.y = Snow_WIDTH // 2 - 10, Snow_HEIGHT - 130
    def draw(self):
        self.image.clip_draw(self.frame * 100, 220, 30, 60, self.x, self.y, 20, 60)
        print(self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8
