import pygame
import sys,random,time
from pygame.locals import*

pygame.init()
resolucion=(442,630)

ventana=pygame.display.set_mode(resolucion)
fondo=pygame.image.load('menu.jpg')
creditos=pygame.image.load('creditos.png')
botonPlay=pygame.image.load('play.png')
trofeo=pygame.image.load('trofeo.png')
instrucciones=pygame.image.load('instrucciones.png')

while True:
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
            
            fondo.blit(creditos,(12,25))
            fondo.blit(instrucciones,(90,496))
            fondo.blit(botonPlay,(170,496))
            fondo.blit(trofeo,(250,496))
            ventana.blit(fondo,(0,0))
            pygame.display.flip()
    