import Math

def distance(p1:tuple,p2:tuple):
    x1,y1 = p1
    x2,y2 = p2

    dist = Math.sqrt((x2-x1)**2 + (y2-y1)**2)

    return dist

def unit_vector(p1:tuple,p2:tuple):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    dist = distance(p1,p2)

    if dist == 0:
        return (0,0)
    
    return (dx/dist, dy/dist)

# TODO
def angle_between(v1,v2):
    
    pass

# TODO
def point_to_line(v1,v2):
    pass