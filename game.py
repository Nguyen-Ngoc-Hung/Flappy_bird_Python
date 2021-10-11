import pygame,sys
import random
pygame.init()

screen=pygame.display.set_mode((768,1024))

pygame.display.set_caption("Flappy bird")
background = pygame.image.load("images/background.png")
bird1 = pygame.image.load('images/bird1.png')
bird2 = pygame.image.load('images/bird2.png')
bird3 = pygame.image.load('images/bird3.png')
ground = pygame.image.load('images/ground.png')
logo = pygame.image.load('images/logo.png')
pipe = pygame.image.load('images/pipe.png')
floor = pygame.image.load('images/floor.png')

clock = pygame.time.Clock()

x=0
y=0
voCanh=0
posBird = 400.0
print(sys.platform)

def drawBackground():
    global y
    if y>760: y=0
    screen.blit(background,(0-y,0))
    screen.blit(background,(760-y,0))
    y+=1

def drawGround():
    global x
    if x>37: x=0
    for i in range(0,22):
        screen.blit(ground,(37*i-x,896))
    x+=4

def drawBird():
    global voCanh
    global alpha
    if voCanh < 10:
        screen.blit(pygame.transform.rotate(bird1,int(alpha)),(200,int(posBird)))
        voCanh+=1
    elif voCanh < 20:
        screen.blit(pygame.transform.rotate(bird2,int(alpha)),(200,int(posBird)))
        voCanh+=1
    elif voCanh < 30:
        screen.blit(pygame.transform.rotate(bird3,int(alpha)),(200,int(posBird)))
        voCanh +=1
        if voCanh >= 30: voCanh =0

def drawPipe(n):
    global khoangCachOng
    global doRongOng
    global speedPipe
    global mangOng
    screen.blit(pipe,(mangOng[n][0],mangOng[n][1]))
    screen.blit(pygame.transform.rotate(pipe, 180),(mangOng[n][0],mangOng[n][1]-doRongOng-793))
    mangOng[n][0] -=4

def drawPipes():
    drawPipe(0)
    drawPipe(1)
    drawPipe(2)
    drawPipe(3)
def drawBase():
    global x
    if x >= 768:
        x=0
    screen.blit(floor,(0-x,896))
    screen.blit(floor,(768-x,896))
    x += 4

giaToc=0.6
doRoi = 0
alpha=30.0
khoangCachOng = 400
doRongOng = 250
alphaX = 50
speedPipe = 0
posPipe = 768
mangOng = []

for i in range(1,5):
    temp = []
    temp.append(posPipe)
    temp.append(random.randint(300,800))
    mangOng.append(temp)
    posPipe += khoangCachOng


print(mangOng)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)  or event.type ==5:
            doRoi = -12
            alphaX = 50

    drawBackground()
    drawPipes()
    drawBase()
    drawBird()

    doRoi += giaToc
    posBird += doRoi
    alphaX -=1.5
    if alphaX <-60:
        alphaX = -60
    alpha = alphaX
    if alpha > 30: 
        alpha =30
    if posBird > 832:
        posBird = 832
    if mangOng[0][0] < -138:
        del mangOng[0]
        temp = []
        temp.append(mangOng[2][0] + khoangCachOng)
        temp.append(random.randint(300,800))
        mangOng.append(temp)
    pygame.display.update()
    clock.tick(40)
        
    






