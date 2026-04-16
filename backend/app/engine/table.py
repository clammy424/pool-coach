class Table:
    def __init__(self, balls, pockets):
        self.balls = balls
        self.pockets = pockets

    def update(self, dt):
        self.move_balls(dt)
        self.handle_collisions()
        self.check_pockets()

    def check_pockets(self):
        for ball in self.balls:
            if ball.is_pocketed:
                continue

            for pocket in self.pockets:
                if pocket.is_ball_captured(ball):
                    ball.pocket()

    def handle_collisions(self):
        # ball-ball collisions
        # ball-rail collisions
        pass