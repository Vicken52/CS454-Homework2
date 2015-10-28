import random, sys, os, math, time
from direct.gui.DirectGui import *
#from direct.gui.DirectGui import DirectFrame, DirectEntry
#import direct.directbase.DirectStart

CHAT_TXT_SCALE = 0.05
CHAT_CHAR_WIDTH_RATIO = 0.4
#MAX_CHAR_LINE =

class Chat:
    def __init__(self, world):
        self.world = world
        self.msgPosition = 1.95
        self.chatFrame = self.addChat()
        self.hideChat()
        self.chat = 0
        self.loadControls()

        taskMgr.add(self.showChat,"Show Chat")

    def hideChat(self):
        self.chatFrame.hide()

    def showChat(self, task):
        if(self.chat != 0):
            #print("Showing Chat")
            self.chatFrame.show()
            self.chat = 0
        return task.cont

    def setKey(self, value):
        self.chat = value

    def loadControls(self):
        self.world.accept("m", self.setKey, [1])
        self.world.accept("m-up", self.setKey, [1])

    def addChat(self):
        chatFrame =  DirectFrame(
                        frameColor=(255, 0, 0, 0.5), #(R,G,B,A)
                        frameSize=(-1, 0.7, -1, 0.6),#(Left,Right,Bottom,Top)
                        pos=(-1, 0, -0.5) #(X,Y,Z)
                        )
        def setText(textEntered):
            #TO DO : implent function send message
            if(textEntered == "/q" or textEntered == "/Q"):
                self.hideChat()
            else:
                #send message
                self.printMessage("Maxime",textEntered)

        #clear the text
        def clearText():
            #entry.enterText('')
            test = "test"

        entry = DirectEntry(
                    parent = chatFrame,
                    text = "",
                    scale=.05,
                    command=setText,
                    initialText="Type Something",
                    numLines = 1,
                    focus=0,
                    focusInCommand=clearText,
                    width= 20)
        entry.setPos(-0.327, 0, -0.46)
        self.scrollFrame = DirectScrolledFrame(
                        parent = chatFrame,
                        manageScrollBars = True,
                        autoHideScrollBars = True,
                        scrollBarWidth = 0.05,
                        canvasSize = (-.5,.45,-2,2),
                        frameSize = (-.5,.51,-.5,.5))
        self.scrollFrame.setPos(0.17, 0, 0.1)
        label = DirectLabel(parent = self.scrollFrame.getCanvas(),text = "Welcome to the Chat",scale =  CHAT_TXT_SCALE)
        width = label.getWidth()
        label.setPos(-.48+(width/40),0,self.msgPosition)
        self.msgPosition -= CHAT_TXT_SCALE
        label2 = DirectLabel(parent = self.scrollFrame.getCanvas(),text = "To Close the chat box enter /q",scale = CHAT_TXT_SCALE)
        width = label2.getWidth()
        label2.setPos(-.48+(width/40),0,self.msgPosition)
        self.msgPosition -= CHAT_TXT_SCALE
        label3 = DirectLabel(parent = self.scrollFrame.getCanvas(),text = "To send a private message enter /m followed by the player ID and your message",scale = CHAT_TXT_SCALE)
        width = label3.getWidth()
        label3.setPos(-.48+(width/40),0,self.msgPosition)
        return chatFrame

    def printMessage(self, user, msg):
        label = DirectLabel(
            parent = self.scrollFrame.getCanvas(),
            text = user+" : "+msg,
            scale = CHAT_TXT_SCALE
            )
        width = label.getWidth()
        label.setPos(-.48+(width/40),0,self.msgPosition)
        self.msgPosition -= CHAT_TXT_SCALE

    #TODO     
    #function that cut messages too long for the chat box
    def cutMesage(self, txt):
        nextxt = txt[len(txt)-1]

        if(len(newtxt)*CHAT_TXT_SCALE * CHAT_CHAR_WIDTH_RATIO > 0.95):
            #Cut the string
            new
            txtArray = cutMesage(txt)

        return txtArray
