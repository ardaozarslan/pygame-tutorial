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
bullets = []
isBadGuyDead = 0
healthValue = 5
gameOver = 1

player = pygame.image.load("player.png")
tiles = pygame.image.load("tiles.png")
badGuyImg = pygame.image.load("badguy.png")


def draw_text(surface, text, size, x, y, color):
    font = pygame.font.Font(pygame.font.match_font("arial"), size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)


while gameOver:
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

        if event.type == pyg_locals.MOUSEBUTTONDOWN:
            bullets.append([playerPosReal, 50])

    for x in range(int(width / tiles.get_width())):
        for y in range(int(height / tiles.get_height())):
            screen.blit(tiles, (100 * x, 100 * y))

    draw_text(screen, "Health= " + str(healthValue), 30, 19, 14, (255, 0, 0))

    bulletIndex = 0
    for bullet in bullets:
        pygame.draw.circle(screen, (30, 30, 122), bullet[0], bullet[1], 10)
        bullet[1] += 8
        if bullet[1] >= 150:
            del bullets[bulletIndex]
        else:
            bulletIndex += 1

    if badGuysTimer == 0:
        badGuys.append([random.randint(30, 1570), random.randint(30, 870), 0])
        badGuysTimer = 20

    index = 0
    for kotuAdam in badGuys:
        if kotuAdam[2] == 0:
            kotuAdam[2] = math.atan2(playerPosReal[1] - 20 - kotuAdam[1], playerPosReal[0] - 20 - kotuAdam[0])

        if ((playerPosReal[0] - 20 - kotuAdam[0])**2 + (playerPosReal[1] - 20 - kotuAdam[1])**2)**0.5 <= 70:
            badGuys.pop(index)
            healthValue -= 1
            if healthValue <= 0:
                gameOver = 0
            continue

        if kotuAdam[0] < -40 or kotuAdam[0] > 1600 or kotuAdam[1] < -40 or kotuAdam[1] > 900:
            badGuys.pop(index)
            continue

        for bullet in bullets:
            if ((bullet[0][0] - 20 - kotuAdam[0])**2 + (bullet[0][1] - 10 - kotuAdam[1])**2)**0.5 <= (bullet[1] + 20):
                badGuys.pop(index)
                isBadGuyDead = 1
                break

        if not isBadGuyDead:
            kotuAdam[0] += math.cos(kotuAdam[2]) * speed
            kotuAdam[1] += math.sin(kotuAdam[2]) * speed
            index += 1

        isBadGuyDead = 0

    for kotuAdam in badGuys:
        screen.blit(badGuyImg, [kotuAdam[0], kotuAdam[1]])

    screen.blit(player, playerPos)
    pygame.display.flip()
    badGuysTimer -= 1