import pygame
from pygame.locals import *
import random
class TicTac:
    imagess=[]
    fll=[]
    fll.append([0,10,160,10,150])
    fll.append([0,170,336,10,150])
    fll.append([0,348,489,10,150])
    fll.append([0,10,160,163,311])
    fll.append([0,170,336,163,311])
    fll.append([0,348,489,163,311])
    fll.append([0,10,160,325,485])
    fll.append([0,170,336,325,485])
    fll.append([0,348,489,325,485])

    def __init__(self,screen):
        self.filled=False
        self.parent_screen=screen
        self.bIm=pygame.image.load("resources/background.png")
        self.circ=pygame.image.load("resources/circle.png")
        self.cross=pygame.image.load("resources/cross.png")
        self.p1=pygame.image.load("resources/p1.png")
        self.scross=pygame.image.load("resources/cross_sml.png")
        self.scirc=pygame.image.load("resources/circle_sml.png")
        self.p1_val=(490,120)
        self.p2_val=(490,370)
        self.p2=pygame.image.load("resources/p2.png")
        self.flag=random.randint(0,1)
        self.imagess.append([self.bIm,(0,0)])
        self.imagess.append([self.p1,(490,20)])
        if self.flag:
            self.p1_symb=self.scross
            self.p2_symb=self.scirc
        else:
            self.p2_symb=self.scross
            self.p1_symb=self.scirc
        self.imagess.append([self.p1_symb,(490,120)])
        self.imagess.append([self.p2,(490,270)])
        self.imagess.append([self.p2_symb,(490,370)])

    def checkwin(self):
        count=0
        main=[]
        d1=[]
        main.append(d1)
        d2=[]
        main.append(d2)
        v1=[]
        main.append(v1)
        v2=[]
        main.append(v2)
        v3=[]
        main.append(v3)
        h1=[]
        main.append(h1)
        h2=[]
        main.append(h2)
        h3=[]
        main.append(h3)
        flag=True
        for x in range(3):
            for y in range(3):
                if(self.fll[y*3 + x][0]==0) flag=False
                if y==1:
                    v2.append(self.fll[3+(x)][0])
                if y==0:
                    v1.append(self.fll[x][0])
                if y==2:
                    v3.append(self.fll[6+x][0])
                if x==1:
                    h2.append(self.fll[(y*3) +1][0])
                if x==0:
                    h1.append(self.fll[3*y][0])
                if x==2:
                    h3.append(self.fll[(3*y)+2][0])
                if(x==y):   d1.append(self.fll[(y+x)*2][0])
                if(x+y==2):
                    n=2
                    d2.append(x+y*n)
                    n+=2
        if flag:self.filled=True
        for x in main:
            temp=set(x)
            if len(temp)==1 :
                for x in temp:
                    if(x!=0):return x
            else: return 0

                

    def fillbox(self,posx,posy):
        if(self.filled): 
            
        else:
            for x in self.fll:
                if(x[0]==0 and (posx>=x[1] and posx<=x[2] and posy>=x[3] and posy<=x[4])):
                    if self.flag: 
                        self.imagess.append([self.circ,(x[1],x[3])])
                        self.flag=False
                        x[0]=1
                    else:
                        self.flag=True
                        self.imagess.append([self.cross,(x[1],x[3])])
                        x[0]=2
                chk=self.checkwin()
                if chk!=0:print("Player",chk,"wins this round")
            self.draw()
                
    def draw(self):
        for i in self.imagess:
            self.parent_screen.blit(i[0],i[1])
        pygame.display.flip()

class Game:
    def __init__(self):
        pygame.init()
        clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((600,500))
        self.tictac=TicTac(self.screen)
        self.tictac.draw()

    def run(self):
        running = True
        while running:
            pos = pygame.mouse.get_pos()
            pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
            if pressed1:
                self.tictac.fillbox(pos[0],pos[1])
            for event in pygame.event.get():
                if event.type==QUIT:
                    running=False

class Menu:
    def __init__(self):
        pygame.init()
        self.parent_screen=pygame.display.set_mode((600,500))
        self.fill=(30,123,156)
        self.buttons=pygame.image.load("resources/button1.png")
        self.logo=pygame.image.load("resources/tic.png")
    
    def draw(self):
        self.parent_screen.fill(self.fill)
        self.parent_screen.blit(self.logo,(150,150))
        self.parent_screen.blit(self.buttons,(50,350))
        pygame.display.flip()

    def onclick(self,x,y):
        if(x>=50 and x<=500 and y>=350 and y<=450):
            pygame.time.wait(500)
            game=Game()
            game.run()
    def run(self):
        running = True
        self.draw()
        while running:
            pos = pygame.mouse.get_pos()
            pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
            if pressed1:
                self.onclick(pos[0],pos[1])
            for event in pygame.event.get():
                if event.type==QUIT:
                    running=False
if __name__=='__main__':
    game=Menu()
    game.run()