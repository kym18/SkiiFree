from pico2d import *
from background import Snow, Start, Count, Over
from tree import BigTree
from stone import Stone
from man import Man
from boardman import boardMan
from monster import Monster
import game_world
import game_framework
import explanation_mode

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT :
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(explanation_mode)
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
    global count
    global gameover

    running = True

    snow = Snow()
    game_world.add_object(snow)

    gameover = Over()
    game_world.add_object(gameover, 1)

    count = Count()
    game_world.add_object(count, 1)

    start = Start()
    game_world.add_object(start)

    bigtrees = [BigTree() for _ in range(30)]
    game_world.add_objects(bigtrees, 0)
    for bigtree in bigtrees:
        game_world.add_collision_pair('man:bigtree', None, bigtree)
        game_world.add_collision_pair('Bboy:bigtree', None, bigtree)
        #print('man tree 충돌')


    stones = [Stone() for _ in range(2)]
    game_world.add_objects(stones, 0)
    for stone in stones:
        game_world.add_collision_pair('man:stone', None, stone)
        game_world.add_collision_pair('Bboy:stone', None, stone)


    man=Man()
    game_world.add_object(man, 0)
    game_world.add_collision_pair('man:bigtree', man, None)
    game_world.add_collision_pair('man:stone', man, None)
    game_world.add_collision_pair('man:Bboy', man, None)
    game_world.add_collision_pair('man:monster', man, None)

    Bboy=boardMan()
    game_world.add_object(Bboy, 0)
    game_world.add_collision_pair('Bboy:stone', Bboy, None)
    game_world.add_collision_pair('Bboy:bigtree', Bboy, None)
    game_world.add_collision_pair('man:Bboy', Bboy, None)

    monster = Monster()
    game_world.add_object(monster, 0)
    game_world.add_collision_pair('man:monster', None, monster)


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def update_world():
    game_world.update()
    game_world.handle_collisions()


def finish():
    game_world.clear()
    pass

def pause():
    pass

def resume():
    pass