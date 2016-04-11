import pygame
from layer import*
from label import*
from button import*
import os

class app(layer):
    #openApps = []

    def __init__(self, width=300, height=533, x=0, y=0, color1="blue", color2=None,
        title="TO DO",mainColor=(255,255,255)):
        super().__init__(width,height,x,y,color1,color2)
        self.isSelected = False
        self.initialClick = None
        self.isOpen = False
        self.title = title

        if (mainColor == (255,255,255)):
            image = pygame.image.load("images/doneWhite.png").convert_alpha()
        else:
            image = pygame.image.load("images/doneBlack.png").convert_alpha()
        
        closeButton = button(width=24,height=17,x=0.05*self.height,
            y=0.05*self.height,image=image)

        title = label(text=self.title,fontSize=16,color=mainColor)

        self.subLayerList = [closeButton,title]


    #Double clicking on an app would deselect it.
    def isClicked(self):
        self.isSelected = not self.isSelected
        self.initialClick = pygame.mouse.get_pos()
    
    #If the app is dragging we calculate the offset
    #of the mouse click, and update its position
    def isDragging(self):
        if (self.isSelected):
            x1,y1 = self.initialClick
            x,y = pygame.mouse.get_pos()
            self.x = x - x1
            self.y = y - y1

    def close(self):
        pass
