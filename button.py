import pygame
import pygame.freetype

from layer import*
from image import*

class button(layer):

    def __init__(self,width=50,height=50,x=0,y=0,color1=(0,0,255),
        color2=None,text="",font="Din Round Pro Bold",fontSize=15,
        textColor=(255,255,255),image=None,isSublayer=False,scale=3):

        super().__init__(width=width,height=height,x=x,y=y,color1=color1,
            color2=color2,isSublayer=isSublayer)

        self.fontSize = fontSize
        pygame.freetype.set_default_resolution(300)
        self.font = pygame.freetype.SysFont(font, fontSize)
        self.text = text
        self.textColor = textColor
        self.image = image
        self.scale = scale

    def isInBounds(self,x,y):
        if (self.isInRect(x,y)):
            return True
        else:
            return False

    def make(self,Surface,x=0,y=0):
        if (self.image == None):
            pos = (self.x+x,self.y+y)
            back = pygame.Rect(self.x+x,self.y+y, self.width, self.height)
            pygame.draw.rect(Surface, self.color1, back)

            self.font.render_to(Surface, pos, self.text, fgcolor=self.textColor,
            size=self.fontSize/self.scale)

        else:
            pos = (self.x,self.y)
            drawImage(Surface,self.image,pos,width=self.width,
                height=self.height,transX=x,transY=y)
