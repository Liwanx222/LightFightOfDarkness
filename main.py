#coding:utf8
#py3 pip install pygame
import pygame

from game import *

pygame.init()

if __name__=="__main__":
    game=Game()
    game.run()
