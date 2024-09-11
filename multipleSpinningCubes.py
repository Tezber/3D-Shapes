import pygame
from numpy import *
import numpy as np
from math import *
from rotation import *
from cube import *

RESOLUTION = (600, 600) # screen resolution
screen = pygame.display.set_mode(RESOLUTION) # creates the screen to be displayed with the resolution boundaries
clock = pygame.time.Clock() # sets a limit to how much the game refreshes per second (fps cap)
#colours
BLACK = (0, 0, 0)
WHITE = (255, 255 ,255)
RED = (255, 0, 0)
#plane dimensions
X = "x"
Y = "y"
Z = "z"

nCube_Values = [[X, -4], [X, 4], [Y, -4], [Y, 4], [Z, -4], [Z, 4]] # 6 repeats
pointsArr = []
points = [np.matrix([-1, -1, 1]), 
          np.matrix([1, -1, 1]), 
          np.matrix([1, 1, 1]), 
          np.matrix([-1, 1, 1]),
          np.matrix([-1, -1, -1]),
          np.matrix([1, -1, -1]),
          np.matrix([1, 1, -1]),
          np.matrix([-1, 1, -1])]
pointsArr.append(points)
#enter vertices of shape [x,y,z] as a matrix
#all cubes
for a in range(len(nCube_Values)):
    pointsArr.append(new_cube(points, nCube_Values[a][0], nCube_Values[a][1]))
print(pointsArr)

#all points in 3 dimensions
projected_points = []
for a in range(len(pointsArr)):
    projected_points.append([[n, n] for n in range(len(pointsArr[a]))])
print(projected_points)

#line creation
def connect_points(i, j, points):
    pygame.draw.line(screen, WHITE, (points[i][0], points[i][1]), (points[j][0], points[j][1]))
    pygame.draw.line(screen, WHITE, (points[i][0], points[i][1]), (points[j][0], points[j][1]))    


#variables for the cube projection/rotation
scale = 25
positions = [300, 300]
rotation_speed = 0.02
angle = 0
while True:
    clock.tick(60)
    screen.fill(BLACK)

    #draw the dots
    for x in range(len(pointsArr)):
        for y in range(len(projected_points)):
            projection_points(pointsArr[x], positions, scale, angle, screen, RED, projected_points)
    angle += 0.01
    #draw the lines
    for p in range(4):
        for q in range(len(projected_points)):
            connect_points(p, (p+1) % 4, projected_points[q])
            connect_points(p+4, ((p+1) % 4) + 4, projected_points[q])
            connect_points(p, (p+4), projected_points[q])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    pygame.display.update()