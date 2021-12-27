# This file contains Player, enemy and Bullet information(code)

# importing the required files into main file
import random
from GameGUI import *
from PlayerNEnemies import *
from os.path import exists
import pygame as pg


# Intialize the pygame library 
pg.init()

# Loading the player image and room
playerImg = pg.image.load('Shooter.png')
playerX = 370
playerY = 480
playerX_change = 0

# Initializing the empty list for enemey
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 8

for i in range(num_of_enemies):
    enemyImg.append(pg.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)


# Bullet States
# Ready - it can not be seeen on the screen
# Fire - it can be seen in fire state

bulletImg = pg.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"