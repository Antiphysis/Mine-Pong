#1 player pong style game with mines/tokens that take away/increase life count.
#"w" and "s" keys control up/down ball movement

import pygame
from random import randint

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)

size = (850,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mine Pong")

#creates Padde, Mine and Ball objects with attributes of "pygame" parent
#class "sprite" that controls movement
class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [0, 3]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

class Mine(pygame.sprite.Sprite):

    def __init__(self, color, width, height, speed):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
       
        self.velocity = [0, speed]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

class Token(pygame.sprite.Sprite):

    def __init__(self, color, width, height, speed):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
       
        self.velocity = [0, speed]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height, alpha):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [4, 0]
        self.rect = self.image.get_rect()
        self.image.set_alpha(alpha)

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = -self.velocity[1]

    def moveup(self):
        self.velocity[1] = self.velocity[1] - .25

    def movedown(self):
        self.velocity[1] = self.velocity[1] + .25
    
def rand_x():
    return randint(100, 750)

def rand_speed():
    return randint(1, 4)

def rand_speed_neg():
    return -randint(1, 4)

#creates trail for ball by storing previous x,y coords or original ball and assigning to other "ball" objects
#with increasing transparency 
def ball_trail(ball):
    coors = ball.rect

    if len(x_cor) < 5:
        x_cor.append(coors[0])
        y_cor.append(coors[1])
        
    else:
        x_cor.pop(0)
        x_cor.append(coors[0])
        y_cor.pop(0)
        y_cor.append(coors[1])
        ball_t1.rect.x = x_cor[0]
        ball_t1.rect.y = y_cor[0]
        ball_t2.rect.x = x_cor[1]
        ball_t2.rect.y = y_cor[1]
        ball_t3.rect.x = x_cor[2]
        ball_t3.rect.y = y_cor[2]
        ball_t4.rect.x = x_cor[3]
        ball_t4.rect.y = y_cor[3]
        ball_t5.rect.x = x_cor[4]
        ball_t5.rect.y = y_cor[4]

#creates Paddles and Ball objects        
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
paddleA.velocity = [0,-2]

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 830
paddleB.rect.y = 200
paddleB.velocity = [0, 2]

ball = Ball(WHITE, 10, 10, 255)
ball.rect.x = 345
ball.rect.y = 195

ball_t1 = Ball(WHITE, 10, 10, 30)
ball_t2 = Ball(WHITE, 10, 10, 70)
ball_t3 = Ball(WHITE, 10, 10, 100)
ball_t4 = Ball(WHITE, 10, 10, 150)
ball_t5 = Ball(WHITE, 10, 10, 200)

all_sprites_list = pygame.sprite.Group()
mines = pygame.sprite.Group()
tokens = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)
all_sprites_list.add(ball_t1)
all_sprites_list.add(ball_t2)
all_sprites_list.add(ball_t3)
all_sprites_list.add(ball_t4)
all_sprites_list.add(ball_t5)


carryOn = True

clock = pygame.time.Clock()

Time = 0
Lives = 5

x_cor = []
y_cor = []

mine1_timer = 1
mine2_timer = 1
token1_timer = 1
token2_timer = 1

start_ticks=pygame.time.get_ticks()

#game loop
while carryOn:

    seconds=(pygame.time.get_ticks()-start_ticks)

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            carryOn = False
        if Lives == 0:
            carryOn=False

        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x:
                    carryOn=False

#creates mines and tokens at random times based on current game clock
    if mine1_timer <= Time:
        new_mine = Mine(RED, 20, 20, rand_speed())
        new_mine.rect.x = rand_x()
        new_mine.rect.y = 0
        mines.add(new_mine)
        all_sprites_list.add(new_mine)
        mine1_timer = Time + randint(1, 5)

    if mine2_timer <= Time:
        new_mine = Mine(RED, 20, 20, rand_speed_neg())
        new_mine.rect.x = rand_x()
        new_mine.rect.y = 500
        mines.add(new_mine)
        all_sprites_list.add(new_mine)
        mine2_timer = Time + randint(1, 6)

    if token1_timer <= Time:
        new_token = Token(WHITE, 20, 20, rand_speed())
        new_token.rect.x = rand_x()
        new_token.rect.y = 0
        tokens.add(new_token)
        all_sprites_list.add(new_token)
        token1_timer = Time + randint(1, 15)

    if token2_timer <= Time:
        new_token = Token(WHITE, 20, 20, rand_speed_neg())
        new_token.rect.x = rand_x()
        new_token.rect.y = 500
        tokens.add(new_token)
        all_sprites_list.add(new_token)
        token2_timer = Time + randint(1, 15)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        ball.moveup()
    if keys[pygame.K_s]:
        ball.movedown()
  
    ball_trail(ball)
    all_sprites_list.update()

#checks for boundries and collisions     
    if ball.rect.x>=840:
        Lives-=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        Lives-=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]
    if paddleA.rect.y>400:
        paddleA.velocity[1] = -paddleA.velocity[1]
    if paddleA.rect.y<0:
        paddleA.velocity[1] = -paddleA.velocity[1]
    if paddleB.rect.y>400:
        paddleB.velocity[1] = -paddleB.velocity[1]
    if paddleB.rect.y<0:
        paddleB.velocity[1] = -paddleB.velocity[1]
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()
    if pygame.sprite.spritecollide(ball, mines, True):
         Lives-=1
    if pygame.sprite.spritecollide(ball, tokens, True):
         Lives+=1
    
    Time = round(seconds/1000)

    screen.fill(BLACK)

    pygame.draw.line(screen, RED, [0,0], [0, 500], 10)
    pygame.draw.line(screen, RED, [850,0], [850, 500], 10)

    all_sprites_list.draw(screen)

    font = pygame.font.Font(None, 74)
    text = font.render(str(Time), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(Lives), 1, WHITE)
    screen.blit(text, (690,10))
    text = font.render("Time", 1, WHITE)
    screen.blit(text, (100,10))
    text = font.render("Lives", 1, WHITE)
    screen.blit(text, (520,10))

    pygame.display.flip()

    clock.tick(30)

pygame.quit()

