import pygame
import pygame.locals as pyg_locals

pygame.init()
width = 1600
height = 900
screen = pygame.display.set_mode((width, height))
playerPos = [500, 400]
movement = 100

player = pygame.image.load("player.png")
tiles = pygame.image.load("tiles.png")

while True:
    screen.fill(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pyg_locals.K_w:
                playerPos[1] -= movement

    for x in range(int(width / tiles.get_width())):
        for y in range(int(height / tiles.get_height())):
            screen.blit(tiles, (100 * x, 100 * y))

    screen.blit(player, [500, 400])

    pygame.display.flip()