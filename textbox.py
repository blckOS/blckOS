import pygame
import string
from layer import*
from shiftKey import*

class textbox(layer):

    def __init__(self, width=300, height=400, x=0, y=0, color1="blue",
        font="",text="",maxLength=140,prompt="Type Something Here"):
        
        super().__init__(width,height,x,y,color1)
        self.isSelected = False
        self.font = font
        self.text = text
        self.maxLength = abs(maxLength)
        self.prompt = prompt
        self.focus = False
        self.capitalized = False
        self.size = None
    
    #This function is used to test if the layer
    #itself is being clicked, i.e., not any
    #of its sublayers
    def isInBounds(self,x,y):
        if (self.isInRect(x,y)):
            self.focus = True
            return True
        else:
            self.focus = False
            return False

    def lowercase(self):
        self.text = string.lower(self.text)

    def uppercase(self):
        self.text = string.upper(self.text)

    def edit(self,events):
        if self.focus == False:
            return 0
        if (len(self.text) > self.maxLength): 
            self.text = self.text[:-1]
        #HEAVILY modified from example, the original was
        #very messy(cascade of 94 if,elif statements) so
        #I kept the overall idea of binding key recognition
        #to the class but this implementation is much more
        #elegant.
        for event in events:
            if (event.type == KEYUP):
                #Tests if key is shift
                if (event.key == K_LSHIFT or event.key == K_RSHIFT or 
                    event.key == K_CAPSLOCK): 
                    self.capitalized = False
            if (event.type == KEYDOWN):
                if (event.key == K_BACKSPACE): 
                    self.text = self.text[:-1]
                elif (event.key == K_LSHIFT or event.key == K_RSHIFT
                    or event.key == K_CAPSLOCK): 
                    self.capitalized = True
                elif (event.key == K_SPACE): 
                    self.text += ' '
                elif (event.key == K_TAB):
                    self.text += '    '
                
                pressedKey = pygame.key.name(event.key)
                if (pressedKey in string.printable and self.shift == False):
                    self.text += pygame.key.name(event.key)
                elif (pressedKey in string.printable and self.shift == True):
                    self.text += pygame.key.name(shift(event.key))

    def make(self,Surface,x=0,y=0):
        text = self.font.render(self.prompt+self.value, 10, self.color)
        surface.blit(text, (self.x + x, self.y + y))
