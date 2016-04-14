import pygame
from shapes import*
class layer(object):
    #Layers handle the drawing of their sublayers
    #so we do need to keep track of what is a 
    #subLayer to avoid drawing it.

    #Layers are drawn globally for elegant
    #z-index tracking and implementation

    allLayers = []
    allSubLayers = []

    #Adding a color 2 will define a gradient
    def __init__(self,width=300,height=533,x=0,y=0,color1="blue",
        color2=None,radius=0,blur=0,isSublayer=False,isBackground=False):
        self.width = width
        self.height = height
        self.color1 = color1
        self.color2 = color2
        self.x = x
        self.y = y
        self.subLayerList = []
        self.blur = blur
        self.radius = radius
        self.isSublayer = isSublayer

        self.mousePosition = pygame.mouse.get_pos()

        if (self.isSublayer == False):
            layer.allLayers.insert(0, self)
        else:
            layer.allSubLayers.append(self)
        

    #Tests if a given (x,y) is in the rectangular
    #boundary of the layer
    def isInRect(self,x,y):
        if (self.x < x < self.x + self.width and
        self.y < y < self.y + self.height):
            return True
        else:
            return False

    #Tests if a given (x,y) is in any of the
    #layer's subLayers. In the case of an
    #app we want buttons, not the app to 
    #recognize clicks
    def isInSubLayer(self,x,y):
        if (len(self.subLayerList) == 0): 
            return False
        for layer in self.subLayerList:
            if layer.isInRect(x,y):
                return True
        return False
    
    #This function is used to test if the layer
    #itself is being clicked, i.e., not any
    #of its sublayers
    def isInBounds(self,x,y):
        if (self.isInRect(x,y)
        and not self.isInSubLayer(x,y)):
            return True
        else:
            return False
   
    def mouseOver(self):
        pass

    def mousePress(self):
        pass

    def mouseReleased(self):
        pass

    def mouseMotion(self):
        pass

    def mouseDrag(self):
        pass

    @classmethod
    def handleEvent(layerClass,event):
        x,y = pygame.mouse.get_pos()

        def handleEventLayer(targetLayer,event,x,y):
            #Tests a event and calls one of the defined methods
            #these methods can/will be overidden in instances of layer
            if (targetLayer.isInBounds(x,y)):
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                    print(targetLayer)
                    targetLayer.mousePress()
                elif (event.type == pygame.MOUSEBUTTONUP and event.button == 1):
                    targetLayer.mouseReleased()
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    targetLayer.mouseMotion()
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    targetLayer.mouseDrag()
                return True

        for subLayer in layerClass.allSubLayers:
            if(handleEventLayer(targetLayer=subLayer,event=event,x=x,y=y)):
                return 0

        for layers in layerClass.allLayers:
            if (handleEventLayer(targetLayer=layers,event=event,x=x,y=y)):
                return 0 #When a top layer has an event we don't want
                         #to check the layers below it.

    #You can give a layer a list of sublayers
    def subLayers(self, subLayerList):
        if (len(self.subLayerList) == 0):
            self.subLayerList = subLayerList
        else:
            self.subLayerList.extend(subLayerList)

    #You can simply add one single layer otherwise
    def addSubLayer(self,subLayer):
        self.subLayerList.append(subLayer)

    #This linearly interpolates two colors, 
    #used to draw gradients.
    @staticmethod  
    def lerpColors(color1,color2,t):

        #Plain linear interpolation algorithm
        #read about in Wikipedia Article on Linear interpolation
        lerp = lambda v0,v1,t: (1-t)*v0 + t*v1

        r1,g1,b1 = color1
        r2,g2,b2 = color2

        #Applying linear interpolation between each
        #color component.
        r,g,b = lerp(r1,r2,t), lerp(g1,g2,t), lerp(b1,b2,t)

        return (r,g,b)

    #Classic result I learned in 21-241, but
    #to jog my memory I looked it up at rosettacode.org/wiki/Map_range
    @staticmethod
    def linearMap(x,A,B):
        a0,a1 = A
        b0,b1 = B
        return b0 + (((x-a0)*b1-b0)/float(a1-a0))

    #Draws all sublayers
    def drawSubLayers(self,Surface):
        if (len(self.subLayerList) != 0):
            for subLayer in self.subLayerList: 
                subLayer.make(Surface, x=self.x, y=self.y)

    def drawGradient(self,Surface,x=0,y=0):
        x1,y1 = self.x, self.y
        x2,y2 = self.x + self.width, self.y + self.height

        #A is the interval between the y-coordinate of the top corner
        #and the y-coordinate of the bottom corner
        #We want to map values in A between [0,1] so we can linearly
        #interpolate the colors as a function of height

        A,B = (y1,y2), (0,1)
        index = y1

        while index <= y2:
            t = self.linearMap(index,A,B)

            r,g,b = self.lerpColors(self.color1,self.color2,t)

            color = (int(r), int(g), int(b))
            
            p1 = (x1, y1+index)
            p2 = (x2, y1+index)

            pygame.draw.line(Surface,color,p1,p2,1)
            index+=1

    #Draws the layer
    def make(self,Surface,x=0,y=0):
        #If it is a gradient
        if (self.color2 != None):
            self.drawGradient(Surface,self.x,self.y)
        else:
            frame = pygame.Rect(self.x+x,self.y+y, 
                self.width,self.height)

            roundedRectangle(Surface,frame,self.color1,radius=0.05)

        self.drawSubLayers(Surface)