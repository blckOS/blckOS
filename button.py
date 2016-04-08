import pygame
from layer import*

class button(layer):

    def __init__(self,width=300,height=400,x=0,y=0,color1=(00,0,255),
        color2=None,text="",font="Din Round Pro",fontSize=15):
        super().__init__(width,height,x,y,color1,color2)
        self.fontSize = fontSize
        self.font = pygame.font.SysFont(font, fontSize)
        self.text = text

    def make(self,Surface,x=0,y=0):
        pos = (self.x+x,self.y+y)
        back = pygame.Rect(self.x+x,self.y+y, self.width, self.height)
        pygame.draw.rect(Surface, self.color1, back)
        if (self.color2 != None):

            x1,y1 = self.x + x, self.y + y
            x2,y2 = self.x + self.width + x, self.y + self.height + y

            A,B = (y1,y2), (0,1)
            index = y1

            while index <= y2:
                t = self.linearMap(index,A,B)

                r,g,b = self.lerpColors(self.color1,self.color2,t)

                color = (int(r), int(g), int(b))
                
                p1 = (x1, y1+index)
                p2 = (x2, y1+index)
                pygame.draw.line(Surface, color, p1, p2, 3)
                index+=1

        label = self.font.render(self.text, 100, (255,255,0))
        Surface.blit(label, pos)

