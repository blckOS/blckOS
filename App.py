import pygame

class App(object):

    def __init__(self,width=300,height=400,x=0,y=0,color1="blue",
        color2=None):
        self.width = width
        self.height = height
        self.color1 = color1
        self.color2 = color2
        self.isSelected = False
        self.x = x
        self.y = y
        self.pressMouseXY = (self.x,self.y)

    def isInBounds(self,x,y):
        if (self.x < x < self.x + self.width and
        self.y < y < self.y + self.height):
            return True
        else:
            return False

    def isClicked(self):
        self.isSelected = not self.isSelected
        self.pressMouseXY = pygame.mouse.get_pos()

    def isDragging(self,surface):
        if (self.isSelected):
            delX,delY = self.pressMouseXY
            x,y = pygame.mouse.get_pos()
            self.x,self.y = x - delX, y - delY

    @staticmethod  
    def lerpColors(color1,color2,t):

        #Algorithm from Wikipedia Article on Linear interpolation
        lerp = lambda v0,v1,t: (1-t)*v0 + t*v1

        r1,g1,b1 = color1
        r2,g2,b2 = color2

        r,g,b = lerp(r1,r2,t), lerp(g1,g2,t), lerp(b1,b2,t)

        return (r,g,b)

    #Algorith from
    @staticmethod
    def linearMap(x,A,B):
        a0,a1 = A
        b0,b1 = B
        return b0 + (((x-a0)*b1-b0)/float(a1-a0))

    def drawApp(self,Surface):
        if (self.color2 != None):

            x1,y1 = self.x, self.y
            x2,y2 = self.x + self.width, self.y + self.height

            A = (y1,y2)
            B = (0,1)
            index = y1

            while index <= y2:
                t = self.linearMap(index,A,B)

                r,g,b = self.lerpColors(self.color1,self.color2,t)

                color = (int(r), int(g), int(b))
                
                p1 = (x1, y1+index)
                p2 = (x2, y1+index)
                pygame.draw.line(Surface, color, p1, p2, 3)
                index+=1

        else:

            #p1 = (self.x,self.y)
            #p2 = (self.x + self.width, self.y + self.height)
            pygame.draw.rect(Surface, self.color1, pygame.Rect(self.x,self.y, self.width, self.height))
