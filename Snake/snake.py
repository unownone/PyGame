import pygame
import time
import random
from pygame.locals import *
from pygame import mixer
SIZE = 64
fsize = 32 
fzie = 16
class food:
    def __init__(self, surface):
        self.parent_screen = surface
        self.image = pygame.image.load("resource/food.png")
        self.x = random.randint(1,15)*fsize
        self.y = random.randint(1,7)*fsize

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 25)*fsize
        self.y = random.randint(1, 12)*fsize


class Snake:
    def __init__(self, surface, length):
        self.parent_screen = surface
        self.block = pygame.image.load("resource/blockh.png")
        self.body = pygame.image.load("resource/blockb.png")
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = 'down'

        self.length = length

    def move_left(self):
        if self.direction != 'right':
            self.direction = 'left'

    def move_right(self):
        if self.direction != 'left':
            self.direction = 'right'

    def move_up(self):
        if self.direction != 'down':
            self.direction = 'up'

    def move_down(self):
        if self.direction != 'up':
            self.direction = 'down'

    def walk(self):
        # MOVEMENT OF THE BODY
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # MOVEMENT OF HEAD
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        if self.x[0] >= 1000 + SIZE//2 :
            self.x[0] = 0 - SIZE//2 + 1
        if self.x[0] <= 0 - SIZE//2:
            self.x[0] = 1000 + SIZE//2 - 1
        if self.y[0] >= 500 + SIZE//2:
            self.y[0] = 0 - SIZE//2 + 1 
        if self.y[0] <= 0 - SIZE//2:
            self.y[0] = 500 + SIZE//2 - 1
        self.draw()

    def draw(self):
        self.parent_screen.fill((66, 10, 20))
        for i in range(self.length):
            if i==0:
                self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
            else:
                self.parent_screen.blit(self.body, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


class Game:
    def __init__(self):
        pygame.init()
        self.bgm=mixer
        self.bgm.init()
        self.bgm.music.load('resource/BG.mp3')
        self.bgm.music.set_volume(0.8)
        self.bgm.music.play()
        self.surface = pygame.display.set_mode((1000, 500))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.food = food(self.surface)
        self.food.draw()

    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.food = food(self.surface)
        self.bgm.music.unpause()

    def display_score(self):
        font = pygame.font.SysFont('arial', 20)
        score = font.render(f"Score: {self.snake.length*10}",True, (255,255,255))
        self.surface.blit(score,(850,5))

    def show_game_over(self):
        self.surface.fill((0, 0, 209))
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is Over!!! Your Score is {self.snake.length*10}", True, (0,0,0))
        self.surface.blit(line1,(200,300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (0,0,0))
        self.surface.blit(line2, (200, 350))
        pygame.display.flip()        
        
        
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 <= x2+SIZE//2:
            if y1 >= y2 and y1 <= y2+SIZE//2:
                return True
        return False
    def play(self):
        self.snake.walk()
        self.food.draw()
        self.display_score()
        pygame.display.flip()
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.food.x, self.food.y):
            self.snake.increase_length()
            self.food.move()
        
        for i in range(2,self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise Exception("Collision Occured")
    def run(self):
        running = True
        pause=False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pause = False
                    if event.key == K_a:
                        self.snake.move_left()
                    if event.key == K_d:
                        self.snake.move_right()
                    if event.key == K_w:
                        self.snake.move_up()
                    if event.key == K_s:
                        self.snake.move_down()
                elif event.type == QUIT:
                    running = False
            try:
                if not pause:
                    self.play()
                  
            except:
                self.bgm.music.pause()
                self.show_game_over()
                pause = True
                self.reset()
            
            
            time.sleep(0.18)


if __name__ == '__main__':
    game = Game()
    game.run()