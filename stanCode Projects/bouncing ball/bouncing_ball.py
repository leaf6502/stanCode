"""
File: bouncing_ball
Name: Amy Su
-------------------------
TODO:
1. onmouseclicked只能使用一次
2. 要計數然後加上開關，第一次點擊才有反應-->閘門如何開關


TO ASK:
1.重力加速度失敗了XD
--Gravity的while loop怎麼加
--REDUCE怎麼用...
2.為什麼REDUCE跟DELAY不用寫global REDUCE,DELAY也進得去bouncing_ball函數裡

3.開關無效，是因為在def start_bouncing(mouse)一開始的is_in_the_end = False沒有被回傳到def main嗎



ANSWER:
1. 我的想法是你先寫一個y的初始速度(=0)，然後每次進入while loop，你把y的速度加上Gravity，這樣就達到想要的效果了。
1_2. REDUCE是用在y的反彈高度，你可以把畫面上下各設一個邊界，如果ball超過上邊界或下邊界，y速度的正負號反過來即可。
2. 因為你沒有更改到REDUCE跟DELAY的值，如果沒有要更改，就不用使用global。

感覺你的程式越寫越好了，加油加油!!


"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
count = 0  # 計數器
is_in_the_end = True  # 設立開關

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(start_bouncing)  # 每次按滑鼠，都會執行bouncing_ball(information hiding)


def start_bouncing(mouse):
    global count, is_in_the_end
    while count < 3 and is_in_the_end:  # 三次內點擊才有反應
        y = 0
        count += 1
        is_in_the_end = False  # 一進來就要關閉開關
        while True:
            ball.move(VX, y)
            y += GRAVITY
            if ball.y + ball.height >= window.height:  # 如果球往上 ，高度會遞減
                y = -y * REDUCE
            pause(DELAY)
            if ball.x + ball.width >= window.width:  # 如果球跑出去，球要回到初始位置，畫面就停止，要再按滑鼠才會動
                window.add(ball, x=START_X, y=START_Y)
                is_in_the_end = True  # 彈跳結束了才能把開關打開
                break
        if is_in_the_end:
            break


if __name__ == "__main__":
    main()
