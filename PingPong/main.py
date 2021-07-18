import pygame, sys

class Ball:
    def __init__(self, screen, posX, posY, color, radius):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.dx = 0
        self.dy = 0
        self.show()

    def show(self):
        pygame.draw.circle(self.screen, self.color, (self.posX, self.posY), self.radius)

    def start_moving(self):
        self.dx = 0.5
        self.dy = 0.2

    def move(self):
        # self.posX = self.posX + self.dx
        self.posX += self.dx
        # self.posY = self.posY + self.dy
        self.posY += self.dy

    def paddle_collision(self):
        self.dx = -self.dx

    def wall_collision(self):
        self.dy = -self.dy

    def restart_pos(self):
        self.posX = WIDTH // 2
        self.posY = HEIGHT // 2
        self.dx = 0
        self.dy = 0
        self.show()

class Paddle:
    def __init__(self, screen, color, posX, posY, width, height):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.state = "stopped"
        self.show()

    def show(self):
        pygame.draw.rect(self.screen, self.color, (self.posX, self.posY, self.width, self.height))

    def move(self):
        if self.state == "up":
            self.posY -= 0.5
        elif self.state == "down":
            self.posY += 0.5

    def clamp(self):
        if self.posY <= 0:
            self.posY = 0

        if self.posY + self.height >= HEIGHT:
            self.posY = HEIGHT - self.height

class Score:
    def __init__(self, screen, points, posX, posY):
        self.screen = screen
        self.points = points
        self.posX = posX
        self.posY = posY
        self.font = pygame.font.SysFont("monospace", 50, bold=True)
        self.label = self.font.render(self.points, 0, WHITE)
        self.show()
    def show(self):
        self.screen.blit(self.label, (self.posX - self.label.get_rect().width//2, self.posY))

    def increase(self):
        points = int(self.points) + 1
        self.points = str(points)
        self.label = self.font.render(self.points, 0, WHITE)


class CollisionManager:

    def ball_and_paddle01(self, ball, paddle01):
        if ball.posY + ball.radius > paddle01.posY and ball.posY - ball.radius < paddle01.posY + paddle01.height:
            if ball.posX - ball.radius <= paddle01.posX - paddle01.width:
                return True

    def ball_and_paddle02(self, ball, paddle02):
        if ball.posY + ball.radius > paddle02.posY and ball.posY - ball.radius < paddle02.posY + paddle02.height:
            if ball.posX - ball.radius >= paddle02.posX:
                return True

    def ball_and_wall(self, ball):
        #top
        if ball.posY - ball.radius <= 0:
            return True
        #bottom
        if ball.posY + ball.radius >= HEIGHT:
            return True

    def check_goal_player01(self, ball):
        return ball.posX - ball.radius >= WIDTH

    def check_goal_player02(self, ball):
        return ball.posX + ball.radius <=0


pygame.init()

WIDTH = 900
HEIGHT = 500
BLACK = (0,0,0)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )

def paint_screen():
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 5)

paint_screen()

# object
ball = Ball(screen, WIDTH//2, HEIGHT//2, WHITE, 15)
paddle01 = Paddle(screen, WHITE, 15, HEIGHT//2 - 60, 20, 120)
paddle02 = Paddle(screen, WHITE, WIDTH - 20 - 15, HEIGHT//2 - 60, 20, 120)
collision = CollisionManager()
score01 = Score(screen, "0", WIDTH//4, 15)
score02 = Score(screen, "0", WIDTH - WIDTH//4, 15)


running = True

playing = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                ball.start_moving()
                playing = True

            if event.key == pygame.K_w:
                paddle01.state = "up"
            if event.key == pygame.K_s:
                paddle01.state = "down"

            if event.key == pygame.K_UP:
                paddle02.state = "up"
            if event.key == pygame.K_DOWN:
                paddle02.state = "down"

        if event.type == pygame.KEYUP:
            paddle01.state = "stopped"
            paddle02.state = "stopped"

    if playing:
        paint_screen()
        # ball movement
        ball.move()
        ball.show()

        # paddle 01
        paddle01.move()
        paddle01.clamp()
        paddle01.show()

        # paddle 02
        paddle02.move()
        paddle02.clamp()
        paddle02.show()

        #collision check
        if collision.ball_and_paddle01(ball, paddle01):
            ball.paddle_collision()
        if collision.ball_and_paddle02(ball, paddle02):
            ball.paddle_collision()
        if collision.ball_and_wall(ball):
            ball.wall_collision()
        if collision.check_goal_player01(ball):
            score01.increase()
            ball.restart_pos()
        if collision.check_goal_player02(ball):
            score02.increase()
            ball.restart_pos()

    score01.show()
    score02.show()


    pygame.display.flip()


