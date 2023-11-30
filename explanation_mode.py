from pico2d import load_image, get_events, clear_canvas, update_canvas, get_time
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE

import game_framework
import play_mode
def init():
    global image
    image = load_image('Images/title.png')

# def update():
#     global running
#     pass
def finish():
    global image
    del image
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_mode(play_mode)
def draw():
    clear_canvas()
    image.draw(400,400)
    update_canvas()
