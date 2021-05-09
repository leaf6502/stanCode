"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.graphics.gobjects import GLabel
import random
from campy.gui.events.timer import pause

"""
TO ASK:
1. 如何讓邊框變透明
2. 開關沒有用
3. 碰到paddle不會彈起來
"""

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.window_height = window_height
        self.window_width = window_width

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(window_width-paddle_width) / 2, y=window_height-PADDLE_OFFSET)
        self.paddle_width = paddle_width

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball_width = ball_radius * 2
        self.ball_height = ball_radius * 2
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=(window_width-ball_radius * 2) / 2, y=(window_height-ball_radius * 2) / 2)

        # add the bricks
        # for i in range(BRICK_ROWS):  # 印下1-10行磚塊
        #     for j in range(BRICK_COLS):
        #         brick_space = GRect(BRICK_WIDTH, BRICK_SPACING)
        #         brick_space.color = 'white'
        #         brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
        #         brick.color = 'black'
        #         brick.filled = True
        #         if i in range(0, 2):
        #             brick.fill_color = 'red'
        #         if i in range(2, 4):
        #             brick.fill_color = 'orange'
        #         if i in range(4, 6):
        #             brick.fill_color = 'yellow'
        #         if i in range(6, 8):
        #             brick.fill_color = 'green'
        #         if i in range(8, 10):
        #             brick.fill_color = 'blue'
        #         self.window.add(brick, x=(BRICK_WIDTH + BRICK_SPACING) * j, y=(BRICK_HEIGHT + BRICK_SPACING) * i +
        #         BRICK_OFFSET)  # 印下磚塊
        #         self.window.add(brick_space, x=(BRICK_WIDTH + BRICK_SPACING) * j, y=BRICK_HEIGHT * (i + 1) +
        #         BRICK_SPACING * i + BRICK_OFFSET)  # 印下空白

        for i in range(BRICK_ROWS):  # 印下1-10行磚塊
            for j in range(BRICK_COLS):
                brick_space = GRect(BRICK_WIDTH, BRICK_SPACING)
                brick_space.color = 'white'
                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                brick.color = 'black'
                brick.filled = True
                if i in range(0, 2):
                    brick.fill_color = 'red'
                if i in range(2, 4):
                    brick.fill_color = 'orange'
                if i in range(4, 6):
                    brick.fill_color = 'yellow'
                if i in range(6, 8):
                    brick.fill_color = 'green'
                if i in range(8, 10):
                    brick.fill_color = 'blue'
                self.window.add(brick, x=(BRICK_WIDTH + BRICK_SPACING) * j, y=(BRICK_HEIGHT + BRICK_SPACING) * i +
                BRICK_OFFSET)  # 印下磚塊
                self.window.add(brick_space, x=(BRICK_WIDTH + BRICK_SPACING) * j, y=BRICK_HEIGHT * (i + 1) +
                BRICK_SPACING * i + BRICK_OFFSET)  # 印下空白

        # add the score lable
        self.score = 0
        self.score_label = GLabel('Score: ' + str(self.score))
        self.window.add(self.score_label, 0, self.score_label.height)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # 設定paddle
        onmousemoved(self.drag_the_paddle)

        # 設定開關
        self.start_the_game_on =  True
        onmouseclicked(self.start_the_game)

    # 滑鼠控制paddle
    def drag_the_paddle(self, mouse):
        self.window.add(self.paddle, x=mouse.x-self.paddle_width / 2, y=self.window_height-PADDLE_OFFSET)
        if self.paddle.x <= 0:
            self.paddle.x = 0
        if self.paddle.x + self.paddle_width >= self.window_width:
            self.paddle.x = self.window_width - self.paddle_width

    # ball的動向碰到編編可以反彈
    def ball_rebound(self):

        if self.ball.x <= 0 or self.ball.x + self.ball_width >= self.window_width:
            self.__dx = - self.__dx
            # 超出邊框就反彈
        if self.ball.y <= 0:
            self.__dy = - self.__dy

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def start_the_game(self, mouse):
        # 會給球速度，讓球開始動
        if self.start_the_game_on:  # 如果開始遊戲
            self.start_the_game_on = False  # 進入後先關開關
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED

    # def check_edge(self):
    #     a = self.window.get_object_at(self.ball.x, self.ball.y)
    #     b = self.window.get_object_at(self.ball.x, self.ball.y + self.ball_height)
    #     c = self.window.get_object_at(self.ball.x + self.ball_width, self.ball.y)
    #     d = self.window.get_object_at(self.ball.x + self.ball_width, self.ball.y + self.ball_height)
    #     if a is not None and a is not self.paddle and a is not self.score_label:
    #         self.__dy = - self.__dy
    #         self.window.remove(a)
    #         self.score += 1
    #         self.score_label.text = 'Score: ' + str(self.score)
    #     # 撞到paddle強制往上彈：取絕對值
    #     elif a is self.paddle:
    #         self.__dy = -abs(self.__dy)
    #     if b is not None and b is not self.paddle and b is not self.score_label:
    #         self.__dy = - self.__dy
    #         self.window.remove(b)
    #         self.score += 1
    #         self.score_label.text = 'Score: ' + str(self.score)
    #     elif b is self.paddle:
    #         self.__dy = -abs(self.__dy)
    #     if c is not None and c is not self.paddle and c is not self.score_label:
    #         self.__dy = - self.__dy
    #         self.window.remove(c)
    #         self.score += 1
    #         self.score_label.text = 'Score: ' + str(self.score)
    #     elif c is self.paddle:
    #         self.__dy = -abs(self.__dy)
    #     if d is not None and d is not self.paddle and d is not self.score_label:
    #         self.__dy = - self.__dy
    #         self.window.remove(d)
    #         self.score += 1
    #         self.score_label.text = 'Score: ' + str(self.score)
    #     # 撞到paddle強制往上彈，才不會讓球黏在板子上
    #     elif d is self.paddle:
    #         self.__dy = -abs(self.__dy)

    def reach_anything(self):
        for x in self.ball.x, self.ball.x + self.ball_width:
            for y in self.ball.y, self.ball.y + self.ball_height:
                maybe_none = self.window.get_object_at(x, y)
                if maybe_none is not None and maybe_none is not self.paddle and maybe_none is not self.score_label:
                # 如果碰到的是磚塊，就消除磚塊然後加分
                    self.__dy = - self.__dy
                    self.window.remove(maybe_none)
                    self.score += 1
                    self.score_label.text = 'Score: ' + str(self.score)
                if maybe_none is self.paddle:  # 如果碰到的是paddle，就反彈
                    self.__dy = -abs(self.__dy)


    # def eliminate(self):
    #     a = self.window.get_object_at(球的四個座標)
    #     b = self.window.get_object_at(球的四個座標)
    #     c = self.window.get_object_at(球的四個座標)
    #     d = self.window.get_object_at(球的四個座標)
    #     # 我依樣示範一組給你看
    #     if a is not None:
    #         self.window.remove(a)

    def restart(self):
        # 球放在中間且不要讓球動
        self.ball.x = (self.window_width-self.ball_width * 2) / 2
        self.ball.y = (self.window_height-self.ball_height * 2) / 2
        self.__dx = 0
        self.__dy = 0
        # onmouseclick的開關要打開，準備下一run
        self.start_the_game_on = True


