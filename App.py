from Tkinter import *

class layer(object):

    def __init__(self,width,height,x=0,y=0,color1="blue",
        color2=None):
        self.width = width
        self.height = height
        self.color1 = color1
        self.color2 = color2
        self.x = x
        self.y = y

    def isClicked(self,x,y):
        if (self.x < x < self.x + self.width and
        self.y < y < self.y + self.height):
            return True
    
    def isDraggable(self,boolVal):
        pass

    
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

    def draw(self,canvas):
        if (self.color2 != None):

            x1,y1 = self.x, self.y
            x2,y2 = self.x + self.width, self.y + self.height

            A = (y1,y2)
            B = (0,1)
            index = y1

            while index <= y2:
                t = self.linearMap(index,A,B)
                print t
                r,g,b = self.lerpColors(self.color1,self.color2,t)
                previousColor = (int(r),int(g),int(b))

                color = "#%02x%02x%02x" % (int(r), int(g), int(b))
                
                p1 = (x1, y1+index)
                p2 = (x2, y1+index)

                canvas.create_line(p1, p2, fill = color)
                index+=1

        else:
            p1 = (self.x,self.y)
            p2 = (self.x + self.width, self.y + self.height)
            canvas.create_rectangle(p1,p2,fill = self.color1)


####################################
# customize these functions
####################################

def init(data):
    black,white = (254,164,31),(254,87,46)
    data.window = layer(300,400,50,50,black,white)
    pass

def mousePressed(event, data):
    pass
    
def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    drawDesktop(canvas,data)
    data.window.draw(canvas)

def drawDesktop(canvas,data):
    canvas.create_rectangle(0,0,data.width+100,data.height+100,fill = "black")

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    
    #########Full Screen code TravisJoe at https://gist.github.com/TravisJoe/5576258#########
    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.focus_set()
    #########################################################################################

    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1440, 900)