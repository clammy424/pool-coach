from app.physics.ball import Ball
from app.physics.pockets import Pocket

class Table:
    def __init__(self, balls: list[Ball], pockets: list[Pocket]):
        self.balls = balls
        self.pockets = pockets

    def update(self, dt):
        self.move_balls(dt)
        self.handle_collisions()
        self.check_pockets()

    # TODO
    def move_balls(dt):
        pass
    
    def check_pockets(self):
        for ball in self.balls:
            if ball.is_pocketed:
                continue

            for pocket in self.pockets:
                if pocket.is_ball_captured(ball):
                    ball.pocket()

    # TODO
    def handle_collisions(self):
        # ball-ball collisions
        # ball-rail collisions
        pass