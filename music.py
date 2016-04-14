import pygame
import random
import os
from layer import*
from label import*
from shapes import*
from button import*

#I am aware that pygame has a specific protocol
#for managing music, however I am not a fan
#of how it is setup, so I am using sounds.

class song(object):
    def __init__(self,file,title,composer="anonymous"):
        self.file = file #Actual file name
        self.path = os.path.join("music",self.file) #location of file
        self.title = title #For display
        self.composer = composer #might use for display
        self.song = pygame.mixer.Sound(self.path) #actually a sound

    def playSong(self):
        self.song.play()

    def stopSong(self):
        self.song.stop()

    def volume(self,val):
        self.song.set_volume()

class playlist(object):
    def __init__(self,songList):
        self.songs = songList
        self.currentSong = 0
        self.currentSongTitle = self.songs[self.currentSong].title
        self.isPlaying = False
        self.firstSong = songList[0]

    def start(self):
        if (self.isPlaying == False):
            self.songs[self.currentSong].playSong()
            self.isPlaying = True

    def stop(self):
        self.isPlaying = False
        self.songs[self.currentSong].stopSong()

    def next(self):
        self.currentSong+=1
        self.start()

    def previous(self):
        self.currentSong-=1
        self.start()
    
    def shuffle(self):
        self.songs.random.shuffe() 
        self.start()      

class playButton(button):
    def __init__(self,playList,width=15,height=18,x=0,y=0,image=None,
        isSublayer=False):
        self.pic = pygame.image.load("images/music/play.png")
        super().__init__(width=width,height=height,x=x,y=y,
            isSublayer=isSublayer,image=self.pic)
        self.playList = playList
        self.test = 2

    def mouseReleased(self):
        if (self.test%3 != 0):
            self.playList.start()
            self.pic = pygame.image.load("images/music/pause.png")
        else:
            self.playList.stop() 
            self.pic = pygame.image.load("images/music/play.png")
        self.test+=1  

    def make(self,Surface,x=0,y=0):
        pos = (self.x,self.y)
        drawImage(Surface,self.pic,pos,width=self.width,
                height=self.height,transX=x,transY=y)

class volumeAdjust(button):
    def __init__(self,playList,func,x=0,y=0,image=None):
        if(func == "+"):
            pic = pygame.image.load("images/music/plus.png")
            width,height=12,12
            x,y = 51+x,109+y
        elif(func == "-"):
            pic = pygame.image.load("images/music/minus.png")
            width,height=11,4
            x,y = 17+x,113+y
        super().__init__(width=width,height=height,x=x,y=y,image=pic)
        self.playList = playList
        self.func = func
        self.currentVolume = self.playList.firstSong.song.get_volume()

    def mouseReleased(self):
        if (self.func == "+"):
            for song in self.playList.songs:
                self.currentVolume+=0.1
                song.song.set_volume(self.currentVolume)
        elif (self.func == "-"):
            for song in self.playList.songs:
                self.currentVolume-=.1
                song.song.set_volume(self.currentVolume)

class music(layer):
    def __init__(self,width=112,height=128,x=0,y=0,color1=(255,215,49),
        color2=(254,164,31),title="",blur=0,radius=.2):
        super().__init__(width=width,height=height,x=x,y=y,color1=color1)
        
        # song1 = song(file="Mahler_5.ogg",title="Symphony No. 5",
        #     composer="Hector Berlioz")
        song2 = song(file="test.wav",title="Nocturne",
            composer="Chopin")
        # song3 = song(file="Symphony_No. 40.ogg",title="Symphonie fantastique",
        #     composer="Gustav Mahler")

        #songList = playlist([song1,song2,song3])
        songList = playlist([song2])
        
        play = playButton(playList=songList, x=49+x, y=55+y) 
        minus = volumeAdjust(playList=songList, func="-",x=x,y=y)
        plus = volumeAdjust(playList=songList, func="+",x=x,y=y)

        appTitle = label(color=(255,255,255),text=songList.currentSongTitle,fontSize=10,
            x=35, y=8, appWidth=112, appHeight=128, centered=False,
            strong=True)

        self.subLayerList=[appTitle]

