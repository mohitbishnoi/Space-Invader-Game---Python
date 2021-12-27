# This file is created to manage all the different actions in the game

# importing the required files into main file
import math
import random
from GameGUI import *
from PlayerNEnemies import *
from ScoreNGameOver import *
from os.path import exists
import pygame as pg
from pygame import mixer

# Intialize the pygame library 
pg.init()

# Function to show the score on game window and to store the highest scroe to text file
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    file_exists = exists("ManageScore.txt")
    if file_exists == True:
        f = open("ManageScore.txt","r+")
        lastScore = int(f.read())
        f.close()
        # print(lastScore)
        if lastScore < int(score_value):
            f = open("ManageScore.txt",'w')
            f.write(str(score_value))
            f.close()
    else:
        f = open("ManageScore.txt","w+")
        f.write(str(score_value))
        f.close()
    screen.blit(score, (x, y))

# Function to show Game over when it is ended and also reads and display the highest score made till now
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    f = open("ManageScore.txt","r")
    highestScore = int(f.read())
    over_text = over_font.render("HIGHEST SCORE : "+ str(highestScore),  True, (255, 255, 255))
    screen.blit(over_text, (90, 350))
    

# Function to initiate the player
def player(x, y):
    screen.blit(playerImg, (x, y))


# Function to initiate the enemeies
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))
  

# Function to initiate the bullets
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

# Function to capture the collision when hitted
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Looping over again and again
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # Capture the left and right keys for player movement
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                playerX_change = -5
            if event.key == pg.K_RIGHT:
                playerX_change = 5
            if event.key == pg.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the player
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                playerX_change = 0


    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # For movement of enemeies 
    for i in range(num_of_enemies):

        # Game Over text
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # to play collision sound when occured
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # For bullet movements
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, testY)
    pg.display.update()
