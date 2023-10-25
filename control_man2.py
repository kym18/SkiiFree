from pico2d import *
from tree import BigTree
from stone import Stone
from man import Man

Snow_WIDTH, Snow_HEIGHT = 800, 800
open_canvas(Snow_WIDTH, Snow_HEIGHT)

Snow = load_image('snowBG.png')
start_p = load_image('start.png')

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                man.dir = 1
            elif event.key == SDLK_LEFT:
                man.dir = -1
            elif event.key == SDLK_SPACE: #정ㅈ;ㅣ
                man.dir = 0
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT and man.dir == 1:
                man.dir = 3
            elif event.key == SDLK_LEFT and man.dir == -1:
                man.dir = 3


running = True
def reset_world():
    global running
    global bigtree
    global stone
    global man
    global world
 
    running = True
    world = []

    bigtree = [BigTree() for i in range(10)]
    world += bigtree

    stone = [Stone() for i in range(2)]
    world += stone

    man=Man()
    world.append(man)

def renderer_world():
    clear_canvas()
    Snow.draw(Snow_WIDTH // 2, Snow_HEIGHT // 2)
    start_p.draw(Snow_WIDTH // 2 - 50, Snow_HEIGHT - 80, 80, 50)
    for o in world:
        o.draw()
    update_canvas()

def update_world():
    for o in world:
        o.update()

reset_world()

while running:
    handle_events()  # 사용자의 입력 받음
    update_world()  # 월드 안의 객체들의 상호작용 계산, 그 결과 update
    renderer_world()  # 월드의 현재 내용 그린다
    delay(0.05)

close_canvas()
