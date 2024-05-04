#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 17:50:35 2024

@author: chiarafischer
"""

def doesCircleExist(commands): # To solve this, I imagined the floor as a coordinate system, on which the robot is moving, starting at (0,0)
    N = 0 # north
    E = 1 # east
    S = 2 # south
    res = [] # result array 

    for move in commands: # iterate through all commands
        x, y, direction = 0, 0, N # default: Robot is at (0,0) and facing north
        
        for w in move: # iterate through all letters of one command
            if (w == 'R'):  # Change the direction the robot is facing
                direction = (direction + 1) % 4
            elif (w == 'L'):
                direction = (direction - 1) % 4
            else: # Walk
                if (direction == N):
                    y += 1 # if command says G and robot is facing north; therefore, only move up on y-axis
                elif (direction == E): # if command says G and robot is facing east; therefore, only move up on x-axis
                    x += 1
                elif (direction == S): # if command says G and robot is facing south; therefore, only move down on y-axis
                    y -= 1
                else: # if command says G and robot is facing west; therefore, only move on y-axis
                    x -= 1
        
        if (x == 0 and y == 0 and direction == N): # Check if the robot's path forms a circle after processing the entire command. If the robot is at its starting position and facing north, it's a circle
            res.append("YES")
        elif (direction != N or (x == 0 and y == 0)): # If the direction is not north, or the robot is at the starting position (0, 0), it will form a circle after repeating the command infinitely
            res.append("YES")
        else:
            res.append("NO")
    return res