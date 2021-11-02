import pygame,sys
import random
pygame.init()

screen=pygame.display.set_mode((384,512))

pygame.display.set_caption("Flappy bird")
background = pygame.image.load("images/background.png")
bird1 = pygame.image.load('images/bird1.png')
bird2 = pygame.image.load('images/bird2.png')
bird3 = pygame.image.load('images/bird3.png')
logo = pygame.image.load('images/logo.png')
pipe = pygame.image.load('images/pipe.png')
floor = pygame.image.load('images/floor.png')
res =pygame.image.load("images/restart.png").convert()

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

def drawGameOver():
    screen.blit(res,(100,100))

def vaCham():
    global gameOver
    global posBird
    global mangOng
    if posBird == 416:
        gameOver = True
    if mangOng[0][0] > 31 and mangOng[0][0] < 145:
        if posBird > mangOng[0][1] - 32 or posBird < mangOng[0][1] - 125 - 5:
            gameOver = True
    elif mangOng[1][0] > 31 and mangOng[1][0] < 145 :
        if posBird > mangOng[1][1] - 32 or posBird < mangOng[1][1] - 125 - 5:
            gameOver = True

x=0
y=0
voCanh=0
posBird = 200.0
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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)  or event.type == 5:
            doRoi = -7
            alphaX = 50

    drawBackground()
    drawPipes()
    drawBase()
    drawBird()
    vaCham()
    if gameOver == True:
        drawGameOver()
    while gameOver == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)  or event.type == 5:
                x=0
                y=0
                voCanh=0
                posBird = 200.0
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
                for i in range(1,5):
                    temp = []
                    temp.append(posPipe)
                    temp.append(random.randint(150,400))
                    mangOng.append(temp)
                    posPipe += khoangCachOng      
        
        print("game over")

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
        
    






