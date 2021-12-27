# This file is created to build Game GUI using Pygame

# importing the required files into main file
from GameGUI import *
from PlayerNEnemies import *
from os.path import exists
import pygame as pg
from pygame import mixer

# Intialize the pygame library 
pg.init()

# create the screen
Display_Width = 800
Display_height = 600
screen = pg.display.set_mode((Display_Width, Display_height))

# Background
background = pg.image.load('GameWindowBG.png')

# Sound
mixer.music.load("BGmusic.wav")
mixer.music.play(-1)

# Caption and Icon
pg.display.set_caption("Space Invader")
icon = pg.image.load('icon.png')
pg.display.set_icon(icon)