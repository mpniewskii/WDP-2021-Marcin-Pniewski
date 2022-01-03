import pygame, random, sys
from pygame.locals import *


pygame.init()





WIDTH = 900
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Zaskroniec')
TLO = (50, 205, 50)
owocek = pygame.Rect(310, 30, 15, 15)
KOLOREK = (250, 250, 250)
ruch = 5
Xglowy = 10
Yglowy = 10

FPS = 60
fpsClock = pygame.time.Clock()




is_running = True
while is_running:
    glowa = pygame.image.load('glowa.jpg').convert_alpha()
    glowa = pygame.transform.scale(glowa, (20, 20))
    SCREEN.fill(TLO)

    klawisz = pygame.key.get_pressed()

    if klawisz[pygame.K_LEFT] and Xglowy > 10:
        Xglowy -= ruch
    if klawisz[pygame.K_RIGHT] and Xglowy < 870:
        Xglowy += ruch
    if klawisz[pygame.K_UP] and Yglowy > 10:
        Yglowy -= ruch
    if klawisz[pygame.K_DOWN] and Yglowy < 770:
        Yglowy += ruch
    SCREEN.blit(glowa, (Xglowy, Yglowy))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False





pygame.quit()