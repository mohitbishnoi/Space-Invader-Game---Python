# This file is created to define font style and size

# importing the required files into main file
from GameGUI import *
from PlayerNEnemies import *
from os.path import exists
import pygame as pg

# Intialize the pygame library 
pg.init()

# Initializing the current score value to zero
score_value = 0

# defining font text and size
font = pg.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# defining font text and size
over_font = pg.font.Font('freesansbold.ttf', 64)