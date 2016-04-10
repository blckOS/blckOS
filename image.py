import pygame
def drawImage(Surface,image,pos,width=32,height=32,
	transX=0, transY=0,cursor=False,transparentColor=None):
	
	image = pygame.transform.smoothscale(image, (width, height))
	rect = image.get_rect()
	x,y = pos

	if (cursor):
		transX,transY = -width//2,-height//2
	
	if (transparentColor!=None):
		image.set_colorkey(transparentColor)

	rect = rect.move((x+transX, y+transY))
	Surface.blit(image, rect)