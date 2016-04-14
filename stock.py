from layer import*
from label import*
from stockData import*
from shapes import*

class stocks(layer):
    def __init__(self,width=112,height=128,x=0,y=0,color1=(33,33,33),
        color2=(10,10,10),title="",blur=0,radius=.2):
        
        super().__init__(width=width,height=height,x=x,y=y,color1 = color1,radius = radius)
        self.title = title

        stockData = getStockData()
        apple = stockData["AAPL"]
        google = stockData["GOOG"]

        appTitle = label(color=(255,255,255),text="Stocks",fontSize=10,
            x=35, y=8, appWidth=112, appHeight=128, centered=False,
            strong=True)

        appleTitle = label(color=(153,153,153),text="AAPL",fontSize=10,
            x=11, y=35, appWidth=112, appHeight=128, centered=False,
            strong=False) 

        applePrice = label(color=(255,255,255),text=apple,fontSize=12,
            x=11, y=51, appWidth=112, appHeight=128, centered=False,
            strong=True)

        box1 = layer(width=98,height=43,x=7,y=27,color1=(255,255,255,25),
            radius=0.2,isSublayer=True) 

        googleTitle = label(color=(153,153,153), text="GOOG", fontSize=10,
            x=11, y=82, appWidth=112, appHeight=128, centered=False,
            strong=False)

        googlePrice = label(color=(255,255,255), text=google, fontSize=12,
            x=11, y=97, appWidth=112, appHeight=128, centered=False,
            strong=True) 
        
        box2 = layer(width=98,height=43,x=7,y=74,color1=(255,255,255,25),
            radius=0.2,isSublayer=True) 

        self.subLayerList=[appTitle,appleTitle,applePrice,box1,googleTitle,googlePrice,box2]

