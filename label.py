import pygame
import pygame.freetype

class label(object):
	def __init__(self,color,x=0,y=0,
		text="",font="Din Round Pro",fontSize=16,
		appWidth=250,appHeight=444):
		self.x = x
		self.y = y
		self.color = color
		self.text = text
		self.fontSize = fontSize
		self.font = pygame.freetype.SysFont(font, self.fontSize)
		self.font.strong = True
		self.appWidth = appWidth
		self.appHeight = appHeight
		#Label always is 5% of app height
		self.padding = int(self.appHeight*0.05)


	def make(self,Surface,x=0,y=0,color=(255,255,255)):

		box = self.font.get_rect(self.text)
		pos = (self.appWidth//2 + x - box[3]//2, self.padding+y)

		self.font.render_to(Surface, pos, self.text, fgcolor=color,
			size=self.fontSize//4)

	def isInRect(self,x,y):
		return False

