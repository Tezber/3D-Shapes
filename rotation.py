from math import *
import numpy as np

def projection_matrix():
    return np.matrix([[1,0,0],
                      [0,1,0],
                      [0,0,0]])

def rotation_z(angle):
    return np.matrix([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1]])

def rotation_y(angle):
    return np.matrix([
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)]])

def rotation_x(angle):
    return np.matrix([
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)]])
