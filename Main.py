# Structure from pygame lecture by Lukas Peraza

#Custom
import pygame
from app import*
from button import*
from cursor import*

#Other
from pygame.locals import*
import os
import numpy

class PygameGame(object):

    def init(self):
        ToDo = app(x = 0, 
            y = 0,color1 = (255,255,255),
            color2 = (0,0,0))

        self.test = button(height = 50, width=50,text="To Do")
        ToDo.addSubLayer(self.test)
        self.apps = [ToDo]

        self.cursor = pygame.image.load("cursor.png").convert_alpha()

    def mousePressed(self, x, y):
        for app in self.apps:
            if app.isInBounds(x,y):
                app.isClicked()

    def mouseReleased(self, x, y):
        for app in self.apps:
            if (app.isSelected):
                app.isClicked()

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        pass

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        for app in self.apps:
            app.make(screen)
            app.isDragging(screen)
        
        drawCursor(screen,self.cursor,pygame.mouse.get_pos(),50,50)

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=800, height=600, fps=60, title="blckOS"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (0, 0, 0)
        pygame.init()

    def run(self):
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
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
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
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
