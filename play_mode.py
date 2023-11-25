from pico2d import *
from background import Snow, Start
from tree import BigTree
from stone import Stone
from man import Man
from boardman import boardMan
import game_world
import game_framework

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
    global bigtrees
    global stones
    global man
    global Bboy

    running = True

    snow = Snow()
    game_world.add_object(snow)


    start = Start()
    game_world.add_object(start)

    bigtrees = [BigTree() for _ in range(30)]
    game_world.add_objects(bigtrees)
    for bigtree in bigtrees:
        game_world.add_collision_pair('man:bigtree', None, bigtree)
        #print('man tree 충돌')


    stones = [Stone() for _ in range(2)]
    game_world.add_objects(stones)
    for stone in stones:
        game_world.add_collision_pair('man:stone', None, stones)


    man=Man()
    game_world.add_object(man)
    game_world.add_collision_pair('man:bigtree', man, None)



    Bboy=boardMan()
    game_world.add_object(Bboy)

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def update_world():
    game_world.update()
    game_world.handle_collisions()