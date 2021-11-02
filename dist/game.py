import pygame,sys
import random

from pygame.constants import MOUSEBUTTONDOWN
from pygame.image import load

pygame.mixer.pre_init()
pygame.init()
screen=pygame.display.set_mode((384,512))
pygame.display.set_caption("Flappy bird")

wing = pygame.mixer.Sound("sound/wing.wav")
point = pygame.mixer.Sound("sound/point.wav")
die = pygame.mixer.Sound("sound/die.wav")


background = pygame.image.load("images/background.png")
bird1 = pygame.image.load('images/bird1.png')

bird2 = pygame.image.load('images/bird2.png')
bird3 = pygame.image.load('images/bird3.png')
logo = pygame.image.load('images/logo.jpg')
pygame.display.set_icon(logo)
pipe = pygame.image.load('images/pipe.png')
floor = pygame.image.load('images/floor.png')
res =pygame.image.load("images/restart.png").convert()
result = pygame.image.load('images/score.png')

clock = pygame.time.Clock()

print(sys.platform)

def drawBackground():
    global y
    if y>380: y=0
    screen.blit(background,(0-y,0))
    screen.blit(background,(380-y,0))
    y+=1

def drawBird():
    global voCanh
    global alpha
    if voCanh < 10:
        screen.blit(pygame.transform.rotate(bird1,int(alpha)),(100,int(posBird)))
        voCanh+=1
    elif voCanh < 20:
        screen.blit(pygame.transform.rotate(bird2,int(alpha)),(100,int(posBird)))
        voCanh+=1
    elif voCanh < 30:
        screen.blit(pygame.transform.rotate(bird3,int(alpha)),(100,int(posBird)))
        voCanh +=1
        if voCanh >= 30: voCanh =0

def drawPipe(n):
    global khoangCachOng
    global doRongOng
    global speedPipe
    global mangOng
    screen.blit(pipe,(mangOng[n][0],mangOng[n][1]))
    screen.blit(pygame.transform.rotate(pipe, 180),(mangOng[n][0],mangOng[n][1]-doRongOng-397))
    mangOng[n][0] -=2

def drawPipes():
    drawPipe(0)
    drawPipe(1)
    drawPipe(2)
    drawPipe(3)

def drawBase():
    global x
    if x >= 384:
        x=0
    screen.blit(floor,(0-x,448))
    screen.blit(floor,(384-x,448))
    x += 2

def vaCham():
    global gameOver
    global posBird
    global mangOng
    if posBird == 416:
        gameOver = True
    if mangOng[0][0] > 31 and mangOng[0][0] < 145:
        if posBird > mangOng[0][1] - 32 or posBird < mangOng[0][1] - 125 - 5:
            gameOver = True
            die.play()
    elif mangOng[1][0] > 31 and mangOng[1][0] < 145 :
        if posBird > mangOng[1][1] - 32 or posBird < mangOng[1][1] - 125 - 5:
            gameOver = True
            die.play()

def drawGameOver():
    global score
    global best
    if score > best:
        best = score
    textScore = font.render(str(score), True, (0,0,0), )
    textBest = font.render(str(best), True, (0,0,0), )
    screen.blit(res,(139,330))
    screen.blit(result,(149,200))
    screen.blit(textScore,(185,230))
    screen.blit(textBest,(185,270))

def countScore():
    global score
    if mangOng[0][0] == 32 :
        score += 1
        point.play()

score = 0
best = 0

x=0
y=0
voCanh=0
posBird = 150.0
giaToc=0.4
doRoi = 0
alpha=30.0
khoangCachOng = 200
doRongOng = 125
alphaX = 50
speedPipe = 0
posPipe = 384
gameOver = False
mangOng = []

for i in range(1,5):
    temp = []
    temp.append(posPipe)
    temp.append(random.randint(150,400))
    mangOng.append(temp)
    posPipe += khoangCachOng
print(mangOng)
font = pygame.font.SysFont('Arial', 25)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)  or event.type == MOUSEBUTTONDOWN:
            wing.play()
            doRoi = -7
            alphaX = 50

    drawBackground()
    drawPipes()
    drawBase()
    drawBird()
    vaCham()
    countScore()
    while gameOver == True:
        drawGameOver()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)  or (event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0]<246 and pygame.mouse.get_pos()[0] > 139 and pygame.mouse.get_pos()[1]>330 and pygame.mouse.get_pos()[1] <354):
                x=0
                y=0
                voCanh=0
                posBird = 150.0
                giaToc=0.4
                doRoi = 0
                alpha=30.0
                khoangCachOng = 200
                doRongOng = 125
                alphaX = 50
                speedPipe = 0
                posPipe = 384
                mangOng = []
                gameOver = False
                score = 0
                for i in range(1,5):
                    temp = []
                    temp.append(posPipe)
                    temp.append(random.randint(150,400))
                    mangOng.append(temp)
                    posPipe += khoangCachOng    
        pygame.display.flip()
          
        
    screen.blit(font.render("Score: "+str(score), True, (0,0,0), ), (0,0))
    doRoi += giaToc
    posBird += doRoi
    alphaX -=1.5
    if alphaX <-60:
        alphaX = -60
    alpha = alphaX
    if alpha > 30: 
        alpha =30
    if posBird > 416:
        posBird = 416
    if mangOng[0][0] < -69:
        del mangOng[0]
        temp = []
        temp.append(mangOng[2][0] + khoangCachOng)
        temp.append(random.randint(150,400))
        mangOng.append(temp)
    pygame.display.update()
    clock.tick(40)
        
    






