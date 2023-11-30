from pico2d import load_image, draw_rectangle, get_time
from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT, SDLK_DOWN, SDLK_UP
import math

Snow_WIDTH, Snow_HEIGHT = 800, 800
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

def crash():
    return True;

class Man:
    def __init__(self): #생성자 함수, 객체 생성될 때 맨 처음 자동 호출 -> 객체 초기 상태
        self.x, self.y = Snow_WIDTH // 2 - 10, Snow_HEIGHT - 130
        self.frame = 0
        self.image = load_image('Images/snowman.png')
        self.speed = 10
        self.dir = 0
        self.opCount = 0; #넘어지는
        self.optime = 0;  #넘어지는 시간
        # 0:정지(왼쪽), 1:오른쪽,-1:왼쪽,
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.game_start = False
        self.last_time = get_time()

    def ReturnGameStart(self):
        return self.game_start
    def draw(self):
        self.state_machine.draw()
        # draw_rectangle(*self.get_bb())  # 튜플을 풀어해쳐서 분리해서 인자로 제공


    def update(self):
        current_time = get_time()
        if current_time - self.last_time > 3.0 and current_time - self.last_time < 3.2:  # 3초가 지난 후에 나타남
            self.dir = 3
            self.state_machine.update()
        else:
            self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def get_bb(self):
        return self.x - 10, self.y - 20, self.x + 10, self.y + 20

    def handle_collision(self, groub, other):
        if groub == 'man:bigtree':
            self.dir = 9
        elif groub == 'man:stone':
            self.dir = 9
        elif groub == 'man:Bboy':
            self.dir = 9


class Idle:  #내려가기
    @staticmethod
    def enter(man, e):
        if left_up(e) or right_up(e):
            man.dir = 3

    @staticmethod
    def exit(man, e):
        pass

    @staticmethod
    def do(man):
        man.frame = (man.frame + 1) % 8
        if man.dir == 3:
            # man.y -= 10
            pass
        if man.dir == 9: #넘어지기
            man.opCount += 1
            man.optime += 1

            if man.opCount <= 15:
                # man.y -= 7
                man.opCount = 0
                if man.optime >= 29:
                    man.dir = 3

    @staticmethod
    def draw(man):
        if man.dir == 3:  # 정면
            man.image.clip_draw(man.frame * 0 + 200 - 2, 0, 45, 100, man.x, man.y, 30, 55)
        elif man.dir == 0:
            man.image.clip_draw(man.frame * 0 + 18, 0, 72, 100, man.x, man.y, 50, 60)
        elif man.dir == 9:
            man.image.clip_draw(man.frame * 0 + 325, 0, 80, 100, man.x, man.y, 40, 60)

class Run:  #내려가기
    @staticmethod
    def enter(man,e):
        if right_down(e) or left_up(e) : #오른쪽으로 내려가기
            man.dir, man.action = 1, 1
            game_start = True
        elif left_down(e) or right_up(e): #왼쪽으로 내려각
            man.dir, man.action = -1, -1
            game_start = True

    @staticmethod
    def exit(man, e):
        pass

    @staticmethod
    def do(man):
        man.frame = (man.frame + 1) % 8
        if man.dir == -1 or man.dir == 1: #오른쪽/ 왼쪽
            # man.y -= 10
            man.x += man.dir * 8
        if man.dir == 9:
            man.opCount += 1
            man.optime += 1
            #print(man.opCount)

            if man.opCount <= 15:
                # man.y -= 7
                man.opCount = 0
                if man.optime >= 29:
                    man.dir = 3

    @staticmethod
    def draw(man):
        if man.dir == 1:
            man.image.clip_draw(man.frame * 0 + 135, 0, 65, 100, man.x, man.y, 50, 60)
        elif man.dir == -1:  # 왼쪽
            man.image.clip_composite_draw(man.frame *  0 + 135, 0, 65, 100, 0, 'h', man.x, man.y, 50, 60)
        elif man.dir == 9:
            man.image.clip_draw(man.frame * 0 + 325, 0, 80, 100, man.x, man.y, 40, 60)


class StateMachine:
    def __init__(self,man):
        self.man = man
        self.cur_state = Idle
        self.transitions = {
            Run:{ right_up:Idle, left_up:Idle},
            Idle:{right_down: Run, left_down:Run, right_up:Run, left_up:Run},  #정면하강
        }

    def start(self):
        self.cur_state.enter(self.man, ('START', 0))

    def update(self):
        self.cur_state.do(self.man)
    def draw(self):
        self.cur_state.draw(self.man)

    def handle_event(self,e):
        if self.man.game_start == False:
            self.man.game_start = True

        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.man, e)
                self.cur_state = next_state
                self.cur_state.enter(self.man, e)
                return True
        return False



