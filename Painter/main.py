import pygame
from pygame.locals import *

class drawPose:
    drawTask=[]
    colorselect=None
    def __init__(self,screen):
        self.parent_screen=screen

        #color palettes 
        self.bcol=pygame.image.load("resources/black.png")
        self.blcol=pygame.image.load("resources/blue.png")
        self.wcol=pygame.image.load("resources/white.png")
        self.rcol=pygame.image.load("resources/red.png")
        self.gcol=pygame.image.load("resources/green.png")
        self.ycol=pygame.image.load("resources/yellow.png")
        self.mcol=pygame.image.load("resources/magenta.png")
        self.ccol=pygame.image.load("resources/cyan.png")
        
        self.colorselect=self.wcol
        #drawing color palettes
        self.drawTask.append([self.bcol,(10,20,10,20)])
        self.drawTask.append([self.wcol,(25,35,10,20)])
        self.drawTask.append([self.rcol,(40,50,10,20)])
        self.drawTask.append([self.gcol,(55,65,10,20)])
        self.drawTask.append([self.blcol,(70,80,10,20)])
        self.drawTask.append([self.ycol,(85,95,10,20)])
        self.drawTask.append([self.ccol,(100,110,10,20)])
        self.drawTask.append([self.mcol,(115,125,10,20)])

    def drawp(self,p1,p2):
        flag=True
        for i in range(0,7):
            print(p1,p2)
            if(self.drawTask[i][1][0]<p1<self.drawTask[i][1][1] and self.drawTask[i][1][2]<p2<self.drawTask[i][1][3]):
                self.colorselect=self.drawTask[i][0]
                flag=False
        self.drawTask.append([self.colorselect,(p1,p1,p2,p2)])
        self.draw()   

    def draw(self):
        for i in self.drawTask:
            self.parent_screen.blit(i[0],(i[1][0],i[1][3]))
        pygame.display.flip()


class Game:#Game driver code
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((800,800))
        self.drawPose=drawPose(self.screen)
        self.drawPose.draw()

    def run(self):
        running= True

        while running:
            pos=pygame.mouse.get_pos()
            m1,m2,m3=pygame.mouse.get_pressed()
            if m1:#draws things
                self.drawPose.drawp(pos[0],pos[1])
                print(len(self.drawPose.drawTask))
            for event in pygame.event.get():
                if event.type==QUIT:
                    running=False#terminates the game


if __name__=='__main__':
    game=Game()
    game.run()