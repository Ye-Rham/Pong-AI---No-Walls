import random


class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        self.speedup_scale = 1.1

        self.vertical_paddle_width = 10
        self.vertical_paddle_height = self.screen_height / 4
        self.horizontal_paddle_width = self.screen_width / 8
        self.horizontal_paddle_height = 10
        self.ball_width = 10
        self.ball_height = 10
        self.paddle1_color = 0, 20, 150
        self.paddle2_color = 150, 20, 0
        self.ball_color = 150, 150, 150

        self.vertical_paddle_speed = self.screen_height/333
        self.horizontal_paddle_speed = self.screen_width/666

        self.ball_speedup = 1.05
        self.ball_rise = None
        self.ball_run = None
        self.ball_speed = None

        self.game_start = False

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ball_rise = (random.randint(4, 7) * ((-1)**random.randint(1, 2)))/7
        self.ball_run = (random.randint(4, 7) * ((-1)**random.randint(1, 2)))/7
        self.ball_speed = random.uniform(1.5, 2.5)