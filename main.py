import pygame
from pygame.draw import *

pygame.init()
disgusting_pink=(200, 50, 100)
disgusting_yellow=(200, 255, 0)
disgusting_light_blue=(150, 250, 255)
disgusting_green=(100, 150, 20)
disgusting_red=(200, 20, 0)
disgusting_skintone1= (247, 183, 136)
disgusting_skintone2= (251, 150, 106)
really_disgusting_skintone= (236, 55, 51)
disgusting_grey=(130 ,130 ,130)
disgusting_black=(0, 1, 2)
disgusting_waffle_colour_wtf=(234, 186, 60)
disgusting_blue=(20, 120, 200)
disgusting_white=(255, 254, 255)
disgusting_brown=(150, 60, 2)
funny_red=(250, 50, 30)

FPS = 30
screen = pygame.display.set_mode((700, 500))
screen.fill(disgusting_light_blue)
rect(screen, disgusting_green, (0, 300, 700, 200))
lines(screen, disgusting_black, False, ((300, 300), (380, 195), (420, 195), (500, 300)), 2)
lines(screen, disgusting_black, False, ((350, 400), (400, 250), (450, 400)), 2)
lines(screen, disgusting_black, False, ((300, 300), (200, 200), (185, 200), (102, 160)), 2)
lines(screen, disgusting_black, False, ((150, 400), (200, 200), (250, 400)), 2)
circle(screen, disgusting_skintone2, (195, 175), 25)
polygon(screen, disgusting_pink, ((185, 200),(205, 200), (250, 330), (150, 330)))
circle(screen, disgusting_skintone1, (400, 160), 25)
ellipse(screen, disgusting_grey, (350, 185, 100, 170))
lines(screen, disgusting_black, False, ((102, 175), (90, 50)), 2)
circle(screen,disgusting_white, (505, 265), 8 )
circle(screen,disgusting_pink, (520, 273), 8 )
circle(screen,disgusting_brown, (517, 258), 8 )
polygon(screen, disgusting_waffle_colour_wtf, ((500, 300), (495, 265), (525, 280)))
polygon(screen, funny_red, ((97, 100), (60, 55), (130, 50)))
circle(screen, funny_red, (80, 50), 20)
circle(screen, funny_red, (110, 50), 20)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()