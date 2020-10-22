import pygame
import pygame.locals as pyg_locals
import random
import math

pygame.init()
width = 1600
height = 900
screen = pygame.display.set_mode((width, height))
playerPos = [500, 400]
playerPosReal = [550, 450]
movement = 100
badGuysTimer = 20
badGuys = []
speed = 4

player = pygame.image.load("player.png")
tiles = pygame.image.load("tiles.png")
badGuyImg = pygame.image.load("badguy.png")

while True:
    screen.fill(0)
    playerPosReal = [playerPos[0] + 50, playerPos[1] + 50]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pyg_locals.K_w:
                playerPos[1] -= movement

            if event.key == pyg_locals.K_a:
                playerPos[0] -= movement

            if event.key == pyg_locals.K_s:
                playerPos[1] += movement

            if event.key == pyg_locals.K_d:
                playerPos[0] += movement

        playerPosReal = [playerPos[0] + 50, playerPos[1] + 50]

    for x in range(int(width / tiles.get_width())):
        for y in range(int(height / tiles.get_height())):
            screen.blit(tiles, (100 * x, 100 * y))

    if badGuysTimer == 0:
        badGuys.append([random.randint(30, 1570), random.randint(30, 870), 0])
        badGuysTimer = 20

    index = 0
    for kotuAdam in badGuys:
        if kotuAdam[2] == 0:
            kotuAdam[2] = math.atan2(playerPosReal[1] - kotuAdam[1], playerPosReal[0] - kotuAdam[0])

        if ((playerPosReal[0] - kotuAdam[0])**2 + (playerPosReal[1] - kotuAdam[1])**2)**0.5 <= 70:
            badGuys.pop(index)

        kotuAdam[0] += math.cos(kotuAdam[2]) * speed
        kotuAdam[1] += math.sin(kotuAdam[2]) * speed

        index += 1

    for kotuAdam in badGuys:
        screen.blit(badGuyImg, [kotuAdam[0], kotuAdam[1]])

    screen.blit(player, playerPos)
    pygame.display.flip()
    badGuysTimer -= 1