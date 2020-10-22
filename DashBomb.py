import pygame

pygame.init()
width = 1600
height = 900
screen = pygame.display.set_mode((width, height))

player = pygame.image.load("player.png")

while True:
    screen.fill(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(player, [500, 400])

    pygame.display.flip()