#import
import pygame, sys

#fenetre
pygame.init()
fenetre = pygame.display.set_mode([800, 400])
color = (50,200, 255)
fenetre.fill(color)
timer = pygame.time.Clock()
pygame.display.set_caption('minecraft 2D')
icon_32x32 = pygame.image.load("block_herbe.png")
pygame.display.set_icon(icon_32x32)
pygame.display.flip()

#variables
inventaire = []
ninventaire = []
sy = 0
saut = 0
pox = 0
poy = 200
posx = 0
posy = 4
a = 0
b = 0
autoav = 0
droite = 0
gauche = 0
pgr = 0
dire = "droite"

#chunk
x1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
x2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
x3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
x4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
x5 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
x6 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
x7 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
x8 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
x9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ch  = [x1, x2, x3, x4, x5, x6, x7, x8, x9]
x3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#fonction
def lpers():
    a = 0
    for i in range (8):
        a = a + 1
        try:
            pos = ch[a].index(1)
            ch[a][pos] = 0
            ch[posy][posx] = 1
        except:
            pass

def av():
    global dire
    global posx
    global droite
    global gauche
    global pgr
    global pox
    dire = "droite"
    d = posx + 1
    if pox == 750:
        pox = 0
        droite = 0
        gauche = 0
        pgr = 0
        posx = 0
    elif ch[posy][d] == 0:
        droite = 10
        pgr = pgr + 10

def rec():
    global dire
    global posx
    global pgr
    global gauche
    global droite
    global pox
    d = posx - 1
    dire = "gauche"
    if pox == 0:
        droite = 0
        pox = 750
        pgr = 0
        posx = 15
        gauche = 0
    elif ch[posy][d] == 0:
        gauche = 10
        pgr = pgr - 10
        
def jump():
    global posy
    global saut
    d = posy - 1
    if saut == 0 and ch[d][posx] == 0:
        saut = saut + 50
        posy = posy - 1

#block
def rafraichissement():
    global inventaire
    lpers()
    color = (50,200, 255)
    fenetre.fill(color)
    a = 0
    b = 0
    global droite
    global gauche
    global poy
    global pox
    global ch
    global posx
    global posy
    global saut
    inv = pygame.image.load("inventaire.png").convert_alpha()
    block_herbe = pygame.image.load("block_herbe.png").convert_alpha()
    block_pierre = pygame.image.load("block de pierre.png").convert_alpha()
    persd = pygame.image.load("blobd.png").convert_alpha()
    persg = pygame.image.load("blobg.png").convert_alpha()
    for i in range(8):
        for j in range(16):
            if ch[a][b] == 2:
                 fenetre.blit(block_pierre, (b*50, a*50))
            if ch[a][b] == 1:
                if dire == "droite":
                    fenetre.blit(persd, (pox, poy))
                else:
                    fenetre.blit(persg, (pox, poy))
            if ch[a][b] == 3:
                 fenetre.blit(block_herbe, (b*50, a*50))
            b = b + 1
        b = 0
        a = a + 1
        fenetre.blit(inv, (462, 0))
        if poy == 350:
            saut = 0
            gauche = 0
            droite = 0
            posx = 0
            posy = 4
            pox = 0
            poy = 200
            inventaire = []
        d = posy + 1
        if ch[d][posx] == 0 and saut == 0: 
            posy = posy + 1
            saut = -50
    e = 0
    g = 480
    if len(inventaire) >= 7:
        for i in range(len(inventaire)-6):
            inventaire.pop(len(inventaire)-1)
    for item in inventaire:
        f = inventaire[e]
        if f == 3:
            fenetre.blit(block_herbe, (g, 10))
        if f == 2:
            fenetre.blit(block_pierre, (g, 10))
        e = e + 1
        g = g + 50
    pygame.display.flip()

#boucle
while True :
    if pgr == 50:
        pgr = 0
        posx = posx + 1
    if pgr == -50:
        pgr = 0
        posx = posx - 1
    if droite != 0 and droite > 0:
        pox = pox + 1
        droite  = droite - 1
    if gauche != 0 and gauche > 0:
        pox = pox - 1
        gauche  = gauche - 1
    timer.tick(100)
    if saut != 0:
        if saut > 0:
            poy = poy - 2
            saut = saut - 2
        if saut < 0:
            poy = poy + 5
            saut = saut + 5
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RIGHT:
                 av()
             if  event.key == pygame.K_SPACE:
                 jump()
             if  event.key == pygame.K_LEFT:
                 rec()
             if  event.key == pygame.K_KP6:
                 d = posx + 1
                 dire = "droite"
                 if pox == 750:
                     pox = 0
                     posx = 0
                     pgr = 0
                 elif ch[posy][d] == 0:
                     droite = droite + 50
                     posx = posx + 1
             if  event.key == pygame.K_KP4:
                 d = posx - 1
                 dire = "gauche"
                 if pox == 0:
                     pox = 750
                     posx = 15
                     pgr = 0
                 elif ch[posy][d] == 0:
                     gauche = gauche + 50
             if event.key == pygame.K_r:
                 posx = 0
                 pox = 0
                 posy = 4
                 poy = 200
        if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
        if event.type == pygame.MOUSEMOTION:
                sy = event.pos[1]
                sx = event.pos[0]
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] == 1:
                sx = sx/50
                sy = sy/50
                sx = int(sx)
                sy = int(sy)
                if ch[sy][sx] != 1 and ch[sy][sx] != 0:
                    if ch[sy][sx] in inventaire:
                        f = inventaire.index(ch[sy][sx])
                        ninventaire[f] = ninventaire[f] + 1
                    else:
                        ninventaire.append(0)
                        inventaire.append(ch[sy][sx])
                    ch[sy][sx] = 0
    pygame.display.update()
    rafraichissement()
