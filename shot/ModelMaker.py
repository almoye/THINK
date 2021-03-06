# coding=utf-8
import pygame
from pygame.locals import *
from sys import exit
import time
import random
import json

fp = open('t.json', 'w')
data_json = []

color_index = 0
color_set = []
color_set.append((255,192,203))
color_set.append((220,20,60))
color_set.append((199,21,133))
color_set.append((139,0,139))
color_set.append((0,0,139))
color_set.append((30,144,255))
color_set.append((0,191,255))
color_set.append((0,255,0))
color_set.append((255,69,0))
color_set.append((255,0,0))
color_set.append((70,130,180))
color_set.append((123,104,238))

screen = pygame.display.set_mode((800, 500), 0, 32)
screen.fill((255,255,255))
pygame.display.set_caption("ModelMaker")
for i in range(20):
    pygame.draw.line(screen, (165+i,165+i,165+i), (280+i,0), (280+i,500), 1)
    pygame.draw.line(screen, (165+i,165+i,165+i), (0,50+i), (280,50+i), 1)
    pygame.draw.line(screen, (165+i,165+i,165+i), (0,120+i), (280,120+i), 1)
    pygame.draw.line(screen, (165+i,165+i,165+i), (135+i,0), (135+i,50), 1)

'''
rect = Rect(0, 0, 140, 50)
pygame.draw.rect(screen, (165, 165, 165), rect)
'''
# 画网格
for i in range(10):
    pygame.draw.line(screen, (105, 105, 105), (300, i*50), (800, i*50), 1)
    pygame.draw.line(screen, (105, 105, 105), (300+i*50, 0), (300+i*50, 500), 1)

pygame.font.init()
myfont = pygame.font.SysFont("Comic Sans MS", 50)
textsurface = myfont.render('save', False, (0, 0, 0))
screen.blit(textsurface,(30,5))
textsurface = myfont.render('undo', False, (0, 0, 0))
screen.blit(textsurface,(175,5))
textsurface = myfont.render('color', False, (0, 0, 0))
screen.blit(textsurface,(100,75))

for i in range(4):
    for j in range(3):
        rect = Rect(20+j*80, 160+i*80, 75, 75)
        pygame.draw.rect(screen, color_set[i*3+j], rect)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 鼠标的事件和位置信息的获得
            mouse_event = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            if mouse_event[0]:
                # 点击左键后，得到鼠标的位置信息
                x = (mouse_pos[0]/50%16) * 50
                y = (mouse_pos[1]/50%10) * 50
                print x, ":",y
                if x >= 300 and x <= 800:
                    data = {"PosX":(x-300)/50,
		            "PosY":y/50,
		            "color":color_index,
                    }
                    data_json.append(data)
                    rect = Rect(x, y, 50, 50)
                    pygame.draw.rect(screen, color_set[color_index], rect)
                elif x>= 0 and x <= 250 and y >= 150 and y <= 450:
                    _x = mouse_pos[0]
                    _y = mouse_pos[1]
                    
                    _x = (_x- 20)/80
                    _y = (_y - 160)/80
                    color_index = _y*3+ _x
                    print "c is ",color_index
                elif x <= 100 and y == 0:
                    json.dump(data_json, fp)
                    
                    
                    
                
    pygame.display.update()
