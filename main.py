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
funny_green=(50, 250, 30)

FPS = 30
screen = pygame.display.set_mode((700, 500))
screen.fill(disgusting_light_blue)
rect(screen, disgusting_green, (0, 300, 700, 200))
circle(screen, disgusting_skintone2, (195, 172), 25)
circle(screen, disgusting_skintone1, (400, 160), 25)
polygon(screen, disgusting_skintone2, ((230, 195), (240, 230), (300, 300)))
polygon(screen, disgusting_skintone2, ((160, 200), (165, 230), (100, 120)))
polygon(screen, disgusting_skintone1,((365,205), (370, 183), (300, 300)) )
polygon(screen, disgusting_skintone1, ((440, 189), (420, 200), (500, 300)))
polygon(screen, disgusting_red, ((160, 200), (230, 195), (240, 230), (230, 270), (170,270)))
polygon(screen, disgusting_blue, ((370, 183), (440, 189), (420, 250), (380, 250), (365, 200)))
polygon(screen, disgusting_blue, ((170, 270), (230, 270), (250, 400), (200, 300), (160, 400)))
polygon(screen, disgusting_red, ((420, 250), (380, 250), (350, 400), (400, 280), (450, 400)))
lines(screen, disgusting_black, False, ((102, 160), (90, 40)), 2)
circle(screen,disgusting_white, (505, 265), 8 )
circle(screen,disgusting_pink, (520, 273), 8 )
circle(screen,disgusting_brown, (517, 258), 8 )
polygon(screen, disgusting_waffle_colour_wtf, ((500, 300), (495, 265), (525, 280)))
ellipse(screen, funny_green,(60, 5, 60, 75) )


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()