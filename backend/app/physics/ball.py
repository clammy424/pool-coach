# MEASUREMENTS IN INCHES

class Ball:

    def __init__(self, ball_id: int, x: float, y: float, type: str):
        self.ball_id = ball_id
        self.x = x
        self.y = y
        self.radius = 1.125
        self.is_pocketed = False
        self.type = type
    
    def position(self) -> tuple[float,float]:
        return (self.x,self.y)

    def pocket(self) -> None:
        self.is_pocketed = True

    def move_to(self, x: float, y: float) -> None:
        self.x = x
        self.y = y