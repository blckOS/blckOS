import pygame
import pygame.freetype

class label(object):
	def __init__(self,color=(255,255,255),x=0,y=0,
		text="",font="Din Round Pro",fontSize=97,
		appWidth=300,appHeight=533,centered=True,
		scale=2.8,strong=True):
		self.x = x
		self.y = y
		self.color = color
		self.text = text
		self.fontSize = fontSize
		self.font = pygame.freetype.SysFont(font, self.fontSize)
		self.font.strong = strong #Bolds font
		self.appWidth = appWidth
		self.appHeight = appHeight
		self.scale = scale
		self.centered = centered #Basically asks if the label is for an app

		if (self.centered):
			#Label always is 5% of app height
			self.padding = int(self.appHeight*0.05)


	def make(self,Surface,x=0,y=0):
		box = self.font.get_rect(self.text)
		if (self.centered):
			pos = (self.appWidth//2 + x - box[1]//2, self.padding+y)
		else:
			pos = (self.x+x,self.y+y)
		self.font.render_to(Surface, pos, self.text, fgcolor=self.color,
			size=self.fontSize/self.scale)

	#labels do not perform any actions so
	#in apps when we test if a click is in 
	#a sublayer, we can safely ignore labels
	def isInRect(self,x,y):
		return False

