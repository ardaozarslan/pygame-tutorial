import pygame
import pygame.locals as pyg_locals
import random

pygame.init()
width = 1600
height = 900
screen = pygame.display.set_mode((width, height))
playerPos = [500, 400]
movement = 100
badGuysTimer = 20
badGuys = []

player = pygame.image.load("player.png")
tiles = pygame.image.load("tiles.png")
badGuyImg = pygame.image.load("badguy.png")

while True:
    screen.fill(0)
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

    for x in range(int(width / tiles.get_width())):
        for y in range(int(height / tiles.get_height())):
            screen.blit(tiles, (100 * x, 100 * y))

    if badGuysTimer == 0:
        badGuys.append([random.randint(30, 1570), random.randint(30, 870)])
        badGuysTimer = 20

    for kotuAdam in badGuys:
        kotuAdam[0] += 5
        kotuAdam[1] += 5

    for kotuAdam in badGuys:
        screen.blit(badGuyImg, kotuAdam)

    screen.blit(player, playerPos)
    pygame.display.flip()
    badGuysTimer -= 1