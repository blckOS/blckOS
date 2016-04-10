import pygame
import pygame.freetype

from layer import*
from image import*

class button(layer):

    def __init__(self,width=50,height=50,x=0,y=0,color1=(0,0,255),
        color2=None,text="",font="Din Round Pro Bold",fontSize=15,
        textColor=(255,255,255),image=None):

        super().__init__(width,height,x,y,color1,color2)

        self.fontSize = fontSize
        pygame.freetype.set_default_resolution(300)
        self.font = pygame.freetype.SysFont(font, fontSize)
        self.text = text
        self.textColor = textColor
        self.action = lambda: 0
        self.image = image

    def addAction(self,function):
        self.action = funtion

    def isInBounds(self,x,y):
        if (self.isInRect(x,y)):
            return True
            self.action()
        else:
            return False

    def make(self,Surface,x=0,y=0):
        if (self.image == None):
            pos = (self.x+x,self.y+y)
            back = pygame.Rect(self.x+x,self.y+y, self.width, self.height)
            pygame.draw.rect(Surface, self.color1, back)
            label = self.font.pygame.freetype.Font.render_to(self.text, 100, self.textColor)
            Surface.blit(label, pos)
        else:
            pos = (self.x,self.y)
            drawImage(Surface,self.image,pos,width=self.width,
                height=self.height,transX=x,transY=y)
