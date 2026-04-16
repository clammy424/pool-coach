import math

class Pocket:
    def __init__(self, x, y, mouth_width, capture_radius, orientation):
        self.x = x
        self.y = y
        self.mouth_width = mouth_width
        self.capture_radius = capture_radius
        self.orientation = orientation
        
    
    def mouth_segment(self):
        half = self.mouth_width / 2

        if self.orientation == "horizontal":
            # segment left ↔ right
            p1 = (self.x - half, self.y)
            p2 = (self.x + half, self.y)

        else:  # vertical
            # segment bottom ↕ top
            p1 = (self.x, self.y - half)
            p2 = (self.x, self.y + half)

        return p1, p2
    
    def distance_point_to_segment(self, px, py, ax, ay, bx, by):
        # vector projection magic
        apx, apy = px - ax, py - ay
        abx, aby = bx - ax, by - ay
        ab_len_sq = abx*abx + aby*aby

        t = (apx*abx + apy*aby) / ab_len_sq
        t = max(0, min(1, t))

        closest_x = ax + t * abx
        closest_y = ay + t * aby

        dx = px - closest_x
        dy = py - closest_y
        return math.sqrt(dx*dx + dy*dy)
    
    def is_ball_captured(self, ball):
        # 1) Ball must pass through mouth
        (ax, ay), (bx, by) = self.mouth_segment()
        dist_to_mouth = self._distance_point_to_segment(
            ball.x, ball.y, ax, ay, bx, by
        )

        if dist_to_mouth > ball.radius:
            return False  # ball missed the opening

        # 2) Ball center must enter drop zone
        dx = ball.x - self.x
        dy = ball.y - self.y
        dist_to_center = math.sqrt(dx*dx + dy*dy)

        return dist_to_center < self.capture_radius