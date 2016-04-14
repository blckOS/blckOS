import pygame
from gooeyParticles import Box
from slider import Slider

"""
NOTE: Double tap keys for best usage
Controls:
a = animate mode
   Mouse: interact with points
   Click on sliders: change constants
   Top Slider: Attraction/repulsion to mouse
   Middle Slider: Spring constant
   Bottom Slider: Velocity dampening
d = draw mode
   Mouse: Click and hold to draw points
r = reset all points (sends you to animate mode)
c = clear (delete) all points (sends you to draw mode)
"""

class App:
    def __init__(self,size = (600,400),color = (255,255,255)):
        self.particle_size = 10
        self.running = True
        self.size = self.width, self.height = size
        self.window = pygame.display.set_mode(self.size)
        self.screen = pygame.display.get_surface()
        self.buttons = []
        self.color_sliders = []
        self.color = color
        self.sliders = []

        pygame.init()
        self.screen.fill(self.color)
        self.init_sliders()
        pygame.display.flip()

    def main(self):
        while self.running:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.goo_loop()
                if event.key == pygame.K_d:
                    self.draw_loop()
                if event.key == pygame.K_c:
                    self.buttons = []
                    self.screen.fill(self.color)
                    self.draw_loop()
                if event.key == pygame.K_r:
                    for b in self.buttons:
                        b.accel = [0,0]
                        b.vel = [0,0]
                        b.rect.center = b.center
                        b.pos = b.center
                    self.screen.fill(self.color)
                    self.goo_loop()
    def draw_loop(self):
        color = [0,150,0]
        running = True
        clock = pygame.time.Clock()
        for b in self.buttons:
            b.draw(self.screen)
        for s in self.color_sliders:
            s.draw(self.screen)
            
        pygame.display.flip()
        while running:
            event = pygame.event.poll()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                skip = False
                for i in range(len(self.color_sliders)):
                    if self.color_sliders[i].update(mouse):
                        color[i] = self.color_sliders[i].get()
                        skip = True
                if skip:
                    self.screen.fill(self.color)
                    for s in self.color_sliders:
                        s.draw(self.screen)
                    for b in self.buttons:
                        b.draw(self.screen)
                    pygame.display.flip()
                if not skip:
                    previous = (-1,-1)
                    while  event.type != pygame.MOUSEBUTTONUP:
                        mouse = pygame.mouse.get_pos()
                        if mouse != previous:
                            self.buttons.append(Box(self.particle_size,(mouse),color))
                            self.buttons[-1].draw(self.screen)
                            pygame.display.flip()
                        previous = pygame.mouse.get_pos()
                        event = pygame.event.poll()
            if pygame.event.peek(pygame.QUIT):
                running = False
                self.running = False
            if pygame.event.peek(pygame.KEYDOWN):
                running = False
        self.main()

    def goo_loop(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            pygame.mouse.get_rel()
            clock.tick(20)
            state = False
            if pygame.event.peek(pygame.MOUSEMOTION):
                state = True
            if pygame.event.peek(pygame.QUIT):
                running = False
            if len(self.buttons) == 0:
                running = False
            mouse = pygame.mouse.get_pos()
            for b in self.buttons:
                event = pygame.event.poll()
                if event.type == pygame.KEYDOWN:
                    running = False
                if event.type == pygame.QUIT:
                    self.running = False
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for s in self.sliders:
                        s.update(mouse)
                b.grav_state = state
                b.update_const(self.sliders)
                b.update(mouse,self.size)

            for b in self.buttons:
                b.draw(self.screen)
            for s in self.sliders:
                s.draw(self.screen)
            pygame.display.flip()
            self.screen.fill(self.color)
        self.main()

    #initializes sliders for drawGooey
    def init_sliders(self):
        self.sliders.append(Slider(-5000,(-10000,5000),'g',(0,5),"Gravity"))       
        self.sliders.append(Slider(.1,(-1.0,1.0),'k',(0,35),"Spring"))
        self.sliders.append(Slider(.6,(0,1.0),'d',(0,65),"Dampening"))

        self.color_sliders.append(Slider(150,(0,255),'red',(0,5),"red",(100,10),(255,0,0)))       
        self.color_sliders.append(Slider(150,(0,255),'green',(0,35),"green",(100,10), (0,255,0)))       
        self.color_sliders.append(Slider(150,(0,255),'blue',(0,65),"blue",(100,10), (0,0,255)))       
a = App((600,400),(200,200,200))
a.draw_loop()