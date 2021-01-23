import pygame               #import module pygame
print("Movement key for Player1 : W to move Up , S to move Down" )
print("Movement key for Player2 : Up arrow to move up , Down arrow to move down")

pygame.init()                       #initialize function from pygame

win=pygame.display.set_mode((750,500))     #game window size
pygame.display.set_caption("Ping-Pong Game")  #title_bar
white=(255,255,255)
black=(0,0,0)

class Paddle1(pygame.sprite.Sprite):   #player paddle class
    def __init__(self):
        pygame.sprite.Sprite. __init__(self)
        self.image=pygame.Surface([10,75])
        self.image.fill("blue")
        self.rect=self.image.get_rect()
        self.points=0

class Paddle2(pygame.sprite.Sprite):   #player paddle class
    def __init__(self):
        pygame.sprite.Sprite. __init__(self)
        self.image=pygame.Surface([10,75])
        self.image.fill("red")
        self.rect=self.image.get_rect()
        self.points=0
       
paddle1=Paddle1()
paddle1.rect.x=25
paddle1.rect.y=225

paddle2=Paddle2()
paddle2.rect.x=715
paddle2.rect.y=225

paddle_speed=10             #paddle sprites speed

class Ball(pygame.sprite.Sprite):     #ball class
    def __init__(self):
        pygame.sprite.Sprite. __init__(self)
        self.image=pygame.Surface([10,10])
        self.image.fill(white)
        self.rect=self.image.get_rect()
        self.speed=12
        self.dx=1
        self.dy=1

ball=Ball()   #calling ball class
ball.rect.x=375
ball.rect.y=250
all_sprites=pygame.sprite.Group()
all_sprites.add(paddle1,paddle2,ball)

def redraw():         #draws sprites on window
    win.fill(black)
    font = pygame.font.SysFont('Comic Sans MS',30)
    text=font.render('PING-PONG',False,white)
    textRect = text.get_rect()
    textRect.center =(750//2,25)
    win.blit(text,textRect)

#Player1 score_board
    p1_score =font.render(str(paddle1.points),False,white)
    p1Rect =p1_score.get_rect()
    p1Rect.center =(50,50)
    win.blit(p1_score, p1Rect)
#Player2 score_board
    p2_score =font.render(str(paddle2.points),False,white)
    p2Rect =p2_score.get_rect()
    p2Rect.center =(705,50)
    win.blit(p2_score, p2Rect)
    
    all_sprites.draw(win)
    pygame.display.update()
    


run=True
while run:          #game loop
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:     #quit when clicked on x in the title bar
            run=False
    key=pygame.key.get_pressed()
    if key[pygame.K_w]:
        paddle1.rect.y+= -paddle_speed
    if key[pygame.K_s]:
        paddle1.rect.y+= paddle_speed
    if key[pygame.K_UP]:
        paddle2.rect.y+= -paddle_speed
    if key[pygame.K_DOWN]:
        paddle2.rect.y+= paddle_speed
    ball.rect.x += ball.speed * ball.dx
    ball.rect.y += ball.speed * ball.dy

    if ball.rect.y > 485:
        ball.dy= -1
        
    if ball.rect.x > 735:
        ball.rect.x , ball.rect.y =375,250
        ball.dx = -1
        paddle1.points += 1

    if ball.rect.y < 5:
        
        ball.dy = 1
        

    if ball.rect.x < 5:
        ball.rect.x , ball.rect.y =375,250
        ball.dx = 1
        paddle2.points += 1

    if paddle1.rect.colliderect(ball.rect):
        ball.dx = 1

    if paddle2.rect.colliderect(ball.rect):
        ball.dx = -1

    
    redraw()
pygame.quit()



