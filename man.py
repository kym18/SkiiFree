from pico2d import load_image
from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT, SDLK_DOWN, SDLK_UP



Snow_WIDTH, Snow_HEIGHT = 800, 800
def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE
def time_out(e):
    return e[0] == 'TIME_OUT'  # and e[1] > 3.0
def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT
def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT
def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT
def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

class Man:
    def __init__(self): #생성자 함수, 객체 생성될 때 맨 처음 자동 호출 -> 객체 초기 상태
        self.x, self.y = Snow_WIDTH // 2 - 10, Snow_HEIGHT - 130
        self.frame = 0
        #self.action = 3 # 0:정지(왼쪽),2: 정지(오른쪽), 1:오른쪽,-1:왼쪽,
        self.image = load_image('snowman.png')
        self.speed = 10
        self.dir = 0
        # 0:정지(왼쪽), 1:오른쪽,-1:왼쪽,
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def draw(self):
        self.state_machine.draw()


    def update(self):
        self.state_machine.update()
        # if self.dir == 0:
        #     self.speed = 0
        # elif self.dir != 0:
        #     self.y -= self.speed

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))


class Idle:  #내려가기
    @staticmethod
    def enter(man, e):
        if left_up(e) or right_up(e):
            man.dir, man.action = 3, 0

    @staticmethod
    def exit(man, e):
        pass

    @staticmethod
    def do(man):
        man.frame = (man.frame + 1) % 8
        if man.dir == 3:
            man.y -= 10

    @staticmethod
    def draw(man):
        if man.dir == 3:  # 정면
            man.image.clip_draw(man.frame * 0 + 200 - 2, 0, 45, 100, man.x, man.y, 30, 55)
        elif man.dir == 0:
            man.image.clip_draw(man.frame * 0 + 18, 0, 72, 100, man.x, man.y, 50, 60)


class Stop:  #w정지
    @staticmethod
    def enter(man, e):
        if space_down(e):
            man.dir = 0

        print('오른쪽 보기')

    @staticmethod
    def exit(man, e):
        pass

    @staticmethod
    def do(man):
        man.frame = (man.frame + 1) % 8

    @staticmethod
    def draw(man):
        if man.dir == 0: #왼쪽 보고 정지
            man.image.clip_draw(man.frame * 0 + 18, 0, 72, 100, man.x, man.y, 50, 60)
        elif man.dir == 2: #오른쪽 보고 정지
            man.image.clip_composite_draw(man.frame * 0 + 18, 0, 72, 100, 0, 'h', man.x, man.y, 50, 60)


class Run:  #내려가기
    @staticmethod
    def enter(man,e):
        if right_down(e) or left_up(e) : #오른쪽으로 내려가기
            man.dir, man.action = 1, 1
        elif left_down(e) or right_up(e): #왼쪽으로 내려각
            man.dir, man.action = -1, -1

    @staticmethod
    def exit(man, e):
        pass

    @staticmethod
    def do(man):
        man.frame = (man.frame + 1) % 8
        if man.dir == -1 or man.dir == 1: #오른쪽/ 왼쪽
            man.y -= 10
            man.x += man.dir * 5

    @staticmethod
    def draw(man):
        if man.dir == 1:
            man.image.clip_draw(man.frame * 0 + 135, 0, 65, 100, man.x, man.y, 50, 60)
        elif man.dir == -1:  # 왼쪽
            man.image.clip_composite_draw(man.frame *  0 + 135, 0, 65, 100, 0, 'h', man.x, man.y, 50, 60)


class StateMachine:
    def __init__(self,man):
        self.man = man
        self.cur_state = Idle
        self.transitions = {
            Run:{space_down: Stop, right_up:Idle, left_up:Idle},
            Idle:{right_down: Run, left_down:Run, right_up:Run, left_up:Run, space_down: Stop},  #정면하강
            Stop:{right_down: Run, left_down:Run, right_up:Idle, left_up:Idle}
        }

    def start(self):
        self.cur_state.enter(self.man, ('START', 0))

    def update(self):
        self.cur_state.do(self.man)
    def draw(self):
        self.cur_state.draw(self.man)

    def handle_event(self,e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.man, e)
                self.cur_state = next_state
                self.cur_state.enter(self.man, e)
                return True
        return False

