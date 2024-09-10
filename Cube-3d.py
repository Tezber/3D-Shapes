import pygame
import numpy as np
from math import *

RESOLUTION = (800, 800)
screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("3D Cube")
clock = pygame.time.Clock()

#cube vertices
points = []
points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1,  1, 1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([-1, 1, -1]))

projection_matrix = np.matrix([[1,0,0], 
                               [0,1,0], 
                               [0,0,0]])

projected_points = [[n, n] for n in range(len(points))]

def connect_points(i, j, points):
    pygame.draw.line(screen, "white", (points[i][0], points[i][1]), (points[j][0], points[j][1]))

angle_x = angle_y = angle_z = 0
scale = 100
circle_pos = [400, 400]  # x, y
rSpeed = 0.02
while True:
    clock.tick(60)

    rotation_z = np.matrix([
        [cos(angle_x), -sin(angle_x), 0],
        [sin(angle_x), cos(angle_x), 0],
        [0, 0, 1],
    ])

    rotation_y = np.matrix([
        [cos(angle_y), 0, sin(angle_y)],
        [0, 1, 0],
        [-sin(angle_y), 0, cos(angle_y)],
    ])

    rotation_x = np.matrix([
        [1, 0, 0],
        [0, cos(angle_z), -sin(angle_z)],
        [0, sin(angle_z), cos(angle_z)],
    ])

    screen.fill("black")
    i = 0
    for point in points:
        rotated2d = np.dot(rotation_z, point.reshape((3, 1)))
        rotated2d = np.dot(rotation_y, rotated2d)
        rotated2d = np.dot(rotation_x, rotated2d)

        projected2d = np.dot(projection_matrix, rotated2d)

        x = int(projected2d[0][0] * scale) + circle_pos[0]
        y = int(projected2d[1][0] * scale) + circle_pos[1]

        projected_points[i] = [x, y]
        pygame.draw.circle(screen, "purple", (x, y), 5)
        i += 1

    for p in range(4):
        connect_points(p, (p+1) % 4, projected_points)
        connect_points(p+4, ((p+1) % 4) + 4, projected_points)
        connect_points(p, (p+4), projected_points)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            angle_y = angle_x = angle_z = 0
        if keys[pygame.K_a]:
            angle_y += rSpeed
        if keys[pygame.K_d]:
            angle_y -= rSpeed      
        if keys[pygame.K_w]:
            angle_x += rSpeed
        if keys[pygame.K_s]:
            angle_x -= rSpeed
        if keys[pygame.K_q]:
            angle_z -= rSpeed
        if keys[pygame.K_e]:
            angle_z += rSpeed
    pygame.display.update()
