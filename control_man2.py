from pico2d import *

Snow_WIDTH, Snow_HEIGHT = 800, 800
open_canvas(Snow_WIDTH, Snow_HEIGHT)

Snow = load_image('snowBG.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

running = True
def renderer_world():
    clear_canvas()
    Snow.draw(Snow_WIDTH // 2, Snow_HEIGHT // 2)
    update_canvas()

def update_world():
    pass


while running:
    handle_events()  # 사용자의 입력 받음
    update_world()  # 월드 안의 객체들의 상호작용 계산, 그 결과 update
    renderer_world()  # 월드의 현재 내용 그린다
    delay(0.05)

close_canvas()
