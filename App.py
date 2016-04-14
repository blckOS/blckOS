import pygame
from layer import*
from label import*
from button import*
import os

class app(layer):

    def __init__(self, width=300, height=533, x=0, y=0, color1="blue", color2=None,
        title="TO DO",mainColor=(255,255,255),isSublayer=False):
        super().__init__(width,height,x,y,color1,color2)
        self.isSelected = False
        self.initialClick = (0,0)
        self.isOpen = False
        self.title = title

        self.tempX = 0
        self.tempY = 0

        if (mainColor == (255,255,255)):
            image = pygame.image.load("images/doneWhite.png").convert_alpha()
        else:
            image = pygame.image.load("images/doneBlack.png").convert_alpha()
        
        closeButton = button(width=24,height=17,x=0.05*self.height,
            y=0.05*self.height,image=image,isSublayer=True)

        title = label(text=self.title,fontSize=16,color=mainColor,isSublayer=True)

        self.subLayerList = [closeButton,title]

    def mousePress(self):
        self.isSelected = not self.isSelected
        self.tempX,self.tempY = self.x,self.y
        self.initialClick = pygame.mouse.get_pos()
        layer.allLayers.remove(self)
        layer.allLayers.insert(0, self)

    def mouseReleased(self):
        if (self.isSelected):
            self.isSelected = not self.isSelected

    def mouseMotion(self):
        pass

    def mouseDrag(self):
        x1,y1 = self.initialClick
        x,y = pygame.mouse.get_pos()
        self.x = self.tempX + (x - x1)
        self.y = self.tempY + (y - y1)

    def close(self):
        pass

    def open(self):
        pass
