"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts
graphics = BreakoutGraphics()


def main():
    count = 0
    while count < NUM_LIVES:  # Add animation loop here!
        pause(FRAME_RATE)
        #  讓球超出邊框就反彈
        graphics.ball_rebound()
        # 取速度要放在while裡面
        dx = graphics.get_dx()  # 取得x速度
        dy = graphics.get_dy()  # 取得y速度
        graphics.ball.move(dx, dy)
        # 檢查邊界＆反彈＋消除磚塊
        # graphics.check_edge()
        graphics.reach_anything()
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            count += 1
            # 重新開始
            graphics.restart()


if __name__ == '__main__':
    main()
