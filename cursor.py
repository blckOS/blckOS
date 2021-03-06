import pygame
from image import*

def drawCursor(Surface,image,pos,width=32,height=32):
	image = pygame.transform.smoothscale(image, (width, height))
	rect = image.get_rect()
	x,y = pos
	rect = rect.move((x-width//2, y-height//2))
	Surface.blit(image, rect)