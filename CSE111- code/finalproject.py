import pygame
import math

pygame.init()

wind = pygame.display.set_mode((800,800))
pygame.display.set_caption("tester")

x = 50
y = 40
width = 40
height = 60
velocity = 10
time = 0
points = 0
run = True

######################################
class player:
    px = 0
    py = 0

    def __init__(self, width, height):
        self.height = height
        self.width = width

    def x_pos(self):
        return self.px

    def y_pos(self):
        return self.py

    def rwidth(self):
        return self.width
    def rheight(self):
        return self.height

    def update(self):
        global x
        global y
        self.px = x
        self.py = y
        pass

def movement(keys):
    global x
    global y
    global time

    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_RIGHT]:
        x += velocity
    if keys[pygame.K_UP]:
        y -= velocity *2
        time = 0
    if keys[pygame.K_DOWN]:
        y += velocity

    p1.update()

    pass

def gravity():
    global y
    global time
    y += (velocity/2) * time

def draw_player( x, y, width, height):
        pygame.draw.rect(wind,(0,0,255), (x,y, width, height))
        pass
######################################

class stage():
    def __init__(self, width, height, x, y):
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def x_pos(self):
        return self.x

    def y_pos(self):
        return self.y
        
    def rwidth(self):
        return self.width
    def rheight(self):
        return self.height
    pass


def draw_stage(platforms):
    for plat in platforms:
        width = plat.rwidth()
        height = plat.rheight()
        x = plat.x_pos()
        y = plat.y_pos()
        pygame.draw.rect(wind,(255,255,255), (x,y, width, height))
        pass
######################################

class coin():
    isExistant = True

    def __init__(self, width, height, x, y):
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def x_pos(self):
        return self.x

    def y_pos(self):
        return self.y
        
    def rwidth(self):
        return self.width
    def rheight(self):
        return self.height
    pass

def draw_coin(coins):
    for coin in coins:    
        if coin.isExistant == True:
            width = coin.rwidth()
            height = coin.rheight()
            x = coin.x_pos()
            y = coin.y_pos()
            pygame.draw.rect(wind,(255,255,0), (x,y, width, height))
            pass

def touches_coin(coins, obj2):
    for coin in coins:      
        if coin.isExistant == True:
            global y
            global points

            bx = coin.x_pos()
            by = coin.y_pos()
            bheight = coin.rheight()
            bwidth = coin.rwidth()

            ox = obj2.x_pos()
            oy = obj2.y_pos()
            height = obj2.rheight()
            width = obj2.rwidth()

            if bx <= (ox+width/2) and (ox+width/2) <= (bx+bwidth):
                if by <= (oy+height) and (oy+height) <= (by+bheight):
                    if by <= (oy+height) and (oy+height) <= (by+bheight):
                        points += 1
                        coin.isExistant = False
                        print(points)

    pass

######################################

def distance(x1,x2, y1, y2):
    ret = math.sqrt((math.pow((x2-x1), 2))+(math.pow((y2-y1), 2)))
    return ret

def touches_block(platforms, obj2):
    global time
    global y

    for plat in platforms:
        bx = plat.x_pos()
        by = plat.y_pos()
        bheight = plat.rheight()
        bwidth = plat.rwidth()

        ox = obj2.x_pos()
        oy = obj2.y_pos()
        height = obj2.rheight()
        width = obj2.rwidth()

        if bx <= (ox+width/2) and (ox+width/2) <= (bx+bwidth) and by <= (oy+height) and (oy+height) <= (by+bheight):
            time = 0
            while by <= (oy+height) and (oy+height) <= (by+bheight):
                y -= 1
                oy -=1


    pass

def oob(obj):
    global run
    ox = obj.x_pos()
    oy = obj.y_pos()
    height = obj.rheight()
    width = obj.rwidth()

    if 0 >= (ox+width/2) or (ox+width/2) >= 800 or 0 >= (oy+height) or (oy+height) >= 800:
        print("Game Over")
        run = False
    pass

def portal(obj):
    global run
    global points

    bx = 80
    by = 550
    bheight = 50
    bwidth = 50

    ox = obj.x_pos()
    oy = obj.y_pos()
    height = obj.rheight()
    width = obj.rwidth()

    if points == 3:
        pygame.draw.rect(wind,(0,255,0), (bx,by, bwidth, bheight))
        if bx <= (ox+width/2) and (ox+width/2) <= (bx+bwidth) and by <= (oy+height) and (oy+height) <= (by+bheight):
            print("You Win!")
            run = False
    pass

######################################

def main():
    global time
    global run

    while run:
        pygame.time.delay(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()

        oob(p1)
        gravity()
        movement(keys)
        touches_block(platforms,p1)
        touches_coin(coins,p1)
        wind.fill((0,0,0))
        draw_player(x,y,width,height)
        draw_stage(platforms)
        draw_coin(coins)
        portal(p1)

        #print(p1.y_pos())
        ox = x
        oy = y

        pygame.display.update()
        time += 1
p1 = player(width,height)


s = stage(600,80, 80, 600)
s2 = stage(200,80,50,250)
s3 = stage(200,80,600,350)
platforms = [s,s2, s3]


c = coin(50,50,100,100)
c2 = coin(50,50,550,300)
c3 = coin(50,50,400,550)
coins = [c, c2, c3]

main()