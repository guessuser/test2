import pygame
import math
import random
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((500, 700))
clock = pygame.time.Clock()
FPS = 30

rect(screen, (60, 179, 113), (0, 0, 700, 430))
rect(screen, (130, 110, 80), (0, 430, 700, 270))
rect(screen, (218, 165, 32), (0, 0, 40, 470)) #trees
rect(screen, (218, 165, 32), (65, 0, 95, 700))
rect(screen, (218, 165, 32), (350, 0, 40, 470))
rect(screen, (218, 165, 32), (460, 0, 35, 520))
ellipse(screen, (190, 170, 150), (383, 597, 27, 19))
ellipse(screen, (90, 70, 40), (384, 598, 25, 17)) #leg
ellipse(screen, (190, 170, 150), (277, 589, 27, 19))
ellipse(screen, (90, 70, 40), (278, 590, 25, 17)) #leg
ellipse(screen, (190, 170, 150), (279, 539, 133, 83)) #body
ellipse(screen, (100, 80, 50), (280, 540, 130, 80))
ellipse(screen, (190, 170, 150), (282, 604, 27, 19))
ellipse(screen, (90, 70, 40), (283, 605, 25, 17)) #leg
ellipse(screen, (190, 170, 150), (369, 604, 27, 19))
ellipse(screen, (90, 70, 40), (370, 605, 25, 17)) #leg
ellipse(screen, (255, 0, 0), (365, 535, 35, 35)) #apple

for _ in range(50):
    bias_x = random.randint(0, 120)
    bias_y = random.randint(0, 50)
    x, y = [278+bias_x, 555+bias_y]
    curx = 400
    cury = 300

    angle = math.atan2(x - curx, y - cury)
    distance = math.sqrt(200 - (200 * math.cos(angle)))
    x = x + distance
    y = y + distance
    turn=random.randint(-10, 10)
    polygon(screen, (50, 40, 40), [[x, y-turn], [x + 10,y+turn], [x+2*turn,y-80]])
    polygon(screen, (30, 20, 20), [[x, y - turn], [x + 10, y + turn], [x + 2 * turn, y - 80]], 2)

ellipse(screen, (190, 170, 150), (379, 569, 63, 38)) #head
ellipse(screen, (100, 80, 50), (380, 570, 60, 35))
ellipse(screen, (0, 0, 0), (410, 578, 7, 7)) #eye
ellipse(screen, (0, 0, 0), (425, 574, 7, 7)) #eye
ellipse(screen, (0, 0, 0), (438, 585, 5, 5)) #nouse
ellipse(screen, (255, 140, 0), (288, 540, 30, 30))
ellipse(screen, (255, 140, 0), (310, 554, 33, 33))
ellipse(screen, (255, 0, 0), (365, 535, 35, 35))
ellipse(screen, (255, 255, 255), (340, 520, 12, 45))
ellipse(screen, (255, 0, 0), (320, 520, 55, 20))
ellipse(screen, (255, 255, 255), (326, 530, 5, 5))
ellipse(screen, (255, 255, 255), (334, 528, 5, 5))
ellipse(screen, (255, 255, 255), (346, 522, 5, 5))
ellipse(screen, (255, 255, 255), (360, 526, 5, 5))
ellipse(screen, (255, 255, 255), (352, 530, 5, 4))
#pallet
body=  (100, 80, 50)
bodyline= (190, 170, 150)
spikes=(50, 40, 40)
spikesline=(30, 20, 20)
black=(0, 0, 0)
white=(255, 255, 255)
#more hedgehogs
ellipse(screen, body, (170, 450, 80, 40))
ellipse(screen, bodyline, (170, 450, 80, 40), 2)
ellipse(screen, body, (170, 485, 20, 15))
ellipse(screen, body, (235, 485, 20, 15))
ellipse(screen, bodyline, (170, 482, 20, 15), 2)
ellipse(screen, bodyline, (235, 482, 20, 15), 2)

for _ in range(24):
    bias_x = random.randint(0, 65)
    bias_y = random.randint(0, 25)
    x, y = [165+bias_x, 450+bias_y]
    curx = 400
    cury = 300

    angle = math.atan2(x - curx, y - cury)
    distance = math.sqrt(200 - (200 * math.cos(angle)))
    x = x + distance
    y = y + distance
    turn=random.randint(-5, 5)
    polygon(screen, (50, 40, 40), [[x, y-turn], [x + 10,y+turn], [x+4*turn,y-40]])
    polygon(screen, (30, 20, 20), [[x, y - turn], [x + 10, y + turn], [x + 4 * turn, y - 40]], 2)
circle(screen, (255, 20, 0), (200, 450), 10)
ellipse(screen, body, (235, 450, 35, 20))
ellipse(screen, bodyline, (235, 450, 35, 20), 2)
circle(screen, black, (270, 460), 3)
circle(screen, black, (260, 455), 2)
circle(screen, black, (255, 458), 2)

#am i supposed to make a cycle to generate random hedgehogs?

ellipse(screen, body, (470, 430, 80, 40))
ellipse(screen, bodyline, (470, 430, 80, 40), 2)
ellipse(screen, body, (470, 465, 20, 15))
ellipse(screen, body, (535, 465, 20, 15))
ellipse(screen, bodyline, (470, 462, 20, 15), 2)
ellipse(screen, bodyline, (535, 462, 20, 15), 2)

for _ in range(24):
    bias_x = random.randint(0, 65)
    bias_y = random.randint(0, 25)
    x, y = [465+bias_x, 430+bias_y]
    curx = 400
    cury = 300

    angle = math.atan2(x - curx, y - cury)
    distance = math.sqrt(200 - (200 * math.cos(angle)))
    x = x + distance
    y = y + distance
    turn=random.randint(-5, 5)
    polygon(screen, (50, 40, 40), [[x, y-turn], [x + 10,y+turn], [x+4*turn,y-40]])
    polygon(screen, (30, 20, 20), [[x, y - turn], [x + 10, y + turn], [x + 4 * turn, y - 40]], 2)
circle(screen, (255, 20, 0), (500, 430), 10)
ellipse(screen, body, (535, 430, 35, 20))
ellipse(screen, bodyline, (535, 430, 35, 20), 2)
circle(screen, black, (570, 440), 3)
circle(screen, black, (560, 435), 2)
circle(screen, black, (555, 438), 2)

#one more
ellipse(screen, body, (20, 650, 80, 40))
ellipse(screen, bodyline, (20, 650, 80, 40), 2)
ellipse(screen, body, (20, 685, 20, 15))
ellipse(screen, body, (85, 685, 20, 15))
ellipse(screen, bodyline, (20, 682, 20, 15), 2)
ellipse(screen, bodyline, (85, 682, 20, 15), 2)

for _ in range(24):
    bias_x = random.randint(0, 65)
    bias_y = random.randint(0, 25)
    x, y = [15+bias_x, 650+bias_y]
    curx = 400
    cury = 300

    angle = math.atan2(x - curx, y - cury)
    distance = math.sqrt(200 - (200 * math.cos(angle)))
    x = x + distance
    y = y + distance
    turn=random.randint(-5, 5)
    polygon(screen, (50, 40, 40), [[x, y-turn], [x + 10,y+turn], [x+4*turn,y-40]])
    polygon(screen, (30, 20, 20), [[x, y - turn], [x + 10, y + turn], [x + 4 * turn, y - 40]], 2)
circle(screen, (255, 20, 0), (50, 650), 10)
ellipse(screen, body, (85, 650, 35, 20))
ellipse(screen, bodyline, (85, 650, 35, 20), 2)
circle(screen, black, (120, 660), 3)
circle(screen, black, (110, 655), 2)
circle(screen, black, (105, 658), 2)
ellipse(screen, white, (65, 645, 10, 30))
ellipse(screen, (255, 0, 0), (50, 635, 40, 15))
#mushrooms
sx=100
sy=625
for _ in range(5):
    sx=sx+65
    sy=sy+random.randint(-20, 20)
    midx=sx+30
    midy=sy+18
    ellipse(screen, (255, 255, 255), (midx-10,sy,20, 200))
    ellipse(screen, (255, 20, 20), (sx, sy, 60, 36))
    for _ in range(5):
        ox=midx+random.randint(-15, 15)
        oy=midy+random.randint(-10, 10)
        circle(screen, (255, 255, 255), (ox, oy), 2)

pygame.display.update()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()