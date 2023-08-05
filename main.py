import pygame
from pygame.locals import *

background = [1,1,2,2,2,1] 
screen = [0] * 6

for i in range(6):
    screen[i] = background[i]
print(screen)




playerpos = 3
#playerpos = playerpos - 1
screen[playerpos] = 8
# illustrate movement with array
print(screen)