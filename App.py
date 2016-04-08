import pygame
from layer import*

class app(layer):

    def __init__(self, width=300, height=400, x=0, y=0, color1="blue", color2=None):
        super().__init__(width,height,x,y,color1,color2)
        self.isSelected = False
        self.pressMouseXY = (self.x,self.y)

    #Double clicking on an app would deselect it.
    def isClicked(self):
        self.isSelected = not self.isSelected
        self.pressMouseXY = pygame.mouse.get_pos()
    
    #If the app is dragging we calculate the offset
    #of the mouse click, and update its position
    def isDragging(self,surface):
        if (self.isSelected):
            x1,y1 = self.pressMouseXY
            x,y = pygame.mouse.get_pos()
            self.x,self.y = x - x1, y - y1
