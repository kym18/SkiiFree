from pico2d import *
from background import Snow, Start
from tree import BigTree
from stone import Stone
from man import Man
from boardman import boardMan
import game_world

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT :
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            man.handle_event(event)

#running = True
def init():
    global running
    global snow
    global start
    global bigtree
    global stone
    global man
    global Bboy

    running = True

    snow = Snow()
    game_world.add_object(snow)

    start = Start()
    game_world.add_object(start)

    bigtree = [BigTree() for i in range(10)]
    game_world.add_objects(bigtree)

    stone = [Stone() for i in range(2)]
    game_world.add_objects(stone)

    man=Man()
    game_world.add_object(man)

    Bboy=boardMan()
    game_world.add_object(Bboy)

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def update_world():
    game_world.update()



