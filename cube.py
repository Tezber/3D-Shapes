import numpy as np
from rotation import *
import pygame

def new_cube(points, plane, value):
    new_points = []
    if plane == "x":
        scalar = np.matrix([value, 0, 0])
    elif plane == "y":
        scalar = np.matrix([0, value, 0])
    else:
        scalar = np.matrix([0, 0, value])
    
    for i in points:
        new_vertices = np.add(i, scalar)
        new_points.append(np.matrix(new_vertices))
    return new_points

def projected_pointer(points):
    return [[n, n] for n in range(len(points))]

def projection_points(points, position, scale, angle_x, angle_y, angle_z, screen, colour, projectionPointed):
    i = 0
    for point in points:
        rotated2d = np.dot(rotation_z(angle_z), point.reshape((3,1)))
        rotated2d = np.dot(rotation_y(angle_y), rotated2d)
        rotated2d = np.dot(rotation_x(angle_x), rotated2d)

        projected2d = np.dot(projection_matrix(), rotated2d)

        x = int(projected2d[0][0] * scale) + position[0]
        y = int(projected2d[1][0] * scale) + position[1]
        for a in range(len(projectionPointed)):
            projectionPointed[a][i] = x, y
        pygame.draw.circle(screen, colour, (x, y), 5)
        i += 1
