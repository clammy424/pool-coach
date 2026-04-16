from pockets import Pocket
from ball import Ball
from ball_type import BallType

# TABLE CONSTANTS
TABLE_WIDTH = 100.0
TABLE_HEIGHT = 50.0


# BALL CONSTANTS + INITIALIZATION
BALL_RADIUS = 2.25 / 2

CUE_START_X = 20
CUE_START_Y = 25


def create_full_table():
    balls = []

    # cue ball
    balls.append(Ball(0, 20, 25, BALL_RADIUS, BallType.CUE))

    # object balls
    for i in range(1, 16):
        if i == 8:
            t = BallType.EIGHT
        elif i <= 7:
            t = BallType.SOLID
        else:
            t = BallType.STRIPE

        balls.append(Ball(i, 0, 0, BALL_RADIUS, t))

    pockets = create_pockets()

    return balls, pockets


# POCKET CONSTANTS + INITIALIZATION

POCKET_MOUTH = 4.5
POCKET_CAPTURE_RADIUS = 3.0

POCKETS = [
    Pocket(0, 0, POCKET_MOUTH, POCKET_CAPTURE_RADIUS),
    Pocket(TABLE_WIDTH/2, 0, POCKET_MOUTH, POCKET_CAPTURE_RADIUS),
    Pocket(TABLE_WIDTH, 0, POCKET_MOUTH, POCKET_CAPTURE_RADIUS),
    Pocket(0, TABLE_HEIGHT, POCKET_MOUTH, POCKET_CAPTURE_RADIUS),
    Pocket(TABLE_WIDTH/2, TABLE_HEIGHT, POCKET_MOUTH, POCKET_CAPTURE_RADIUS),
    Pocket(TABLE_WIDTH, TABLE_HEIGHT, POCKET_MOUTH, POCKET_CAPTURE_RADIUS),
]

def create_pockets():
    return POCKETS