from pico2d import open_canvas, delay, close_canvas
import play_mode

Snow_WIDTH, Snow_HEIGHT = 800, 800
open_canvas(Snow_WIDTH, Snow_HEIGHT)

play_mode.init()

while play_mode.running:
    play_mode.handle_events()  # 사용자의 입력 받음
    play_mode.update_world()  # 월드 안의 객체들의 상호작용 계산, 그 결과 update
    play_mode.draw()  # 월드의 현재 내용 그린다
    delay(0.05)

close_canvas()