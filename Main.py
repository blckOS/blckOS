# Structure from pygame lecture by Lukas Peraza

import pygame
import pygame.freetype

#Custom
from app import*
from button import*
from image import*
#from animation import*
from textbox import*
from layer import*
from widgets import*

#Other
#from pygame.locals import*
import os
import numpy
import string

class PygameGame(object):

    def init(self):
        ToDo = app(x = 0, 
            y = 0,color1=(255,164,31)) #,color2=(255,88,46))
        Weather = app(x=20,y=20,color1=(47,202,250),
            title = "CMU")
        stockWidget = stocks(x=31,y=343)
        self.widgets = [stockWidget]
        self.apps = [ToDo,Weather]
        self.cursor = pygame.image.load("images/cursor.png").convert_alpha()

    def mousePressed(self, x, y):
        for app in list(reversed(self.apps)):
            if app.isInBounds(x,y):
                self.apps.remove(app)
                self.apps.append(app)
                app.isClicked()
                return 0

    def mouseReleased(self, x, y):
        for app in list(reversed(self.apps)):
            if (app.isSelected):
                app.isClicked()
                return 0

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        pygame.quit()

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        for widget in self.widgets:
            widget.make(screen)
        for app in self.apps:
            app.make(screen)
            app.isDragging()

        drawImage(screen,self.cursor,pygame.mouse.get_pos(),50,50,cursor=True)

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=1440, height=900, fps=60, title="blckOS"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (0, 0, 0)
        pygame.init()

    def run(self):
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height),pygame.FULLSCREEN)
        # set the title of the window
        pygame.display.set_caption(self.title)

        pygame.mouse.set_visible(False)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                    self.mousePressed(*(event.pos))
                elif (event.type == pygame.MOUSEBUTTONUP and event.button == 1):
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == K_ESCAPE):
                        break
                        pygame.quit() 
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif (event.type == pygame.KEYUP):
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif (event.type == pygame.QUIT):
                    playing = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()

def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()
