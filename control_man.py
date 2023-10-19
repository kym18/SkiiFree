from pico2d import *
import random

from tree import BigTree
Snow = load_image('snowBG.png')

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    pass

def create_world():
    global running
    #global bigtree
    global world

    running = True
    world = []

    # bigtree = BigTree()
    # world.append(BigTree)



def update_world():
    pass


def render_world():
    clear_canvas()
    Snow.draw(400, 400)
    update_canvas()



open_canvas()
create_world()

while running:
    render_world()  # 월드의 현재 내용 그린다
    handle_events()
    update_world()
    delay(0.01)
# finalization code
close_canvas()