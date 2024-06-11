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
isGravity = True

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
    global isGravity

    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_RIGHT]:
        x += velocity
    if keys[pygame.K_UP]:
        y -= velocity *2
        time = 0
        isGravity = True
    if keys[pygame.K_DOWN]:
        y += velocity

    p1.update()

    pass

def gravity():
    if isGravity == True:
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


def draw_stage():
    width = 800
    height = 100
    x = 0
    y = 700
    pygame.draw.rect(wind,(255,255,255), (x,y, width, height))
    pass
######################################

def distance(x1,x2, y1, y2):
    ret = math.sqrt((math.pow((x2-x1), 2))+(math.pow((y2-y1), 2)))
    return ret

def touches_block(obj1, obj2):
    global isGravity
    global y

    bx = obj1.x_pos()
    by = obj1.y_pos()
    bheight = obj1.rheight()
    bwidth = obj1.rwidth()

    ox = obj2.x_pos()
    oy = obj2.y_pos()
    height = obj2.rheight()
    width = obj2.rwidth()

    if bx <= (ox+width/2) and (ox+width/2) <= (bx+bwidth):
        if by <= (oy+height) and (oy+height) <= (by+bheight):
            isGravity = False
            while by <= (oy+height) and (oy+height) <= (by+bheight):
                y -= 1
                oy -=1


    pass

def fix_self(bx, by, x1, y2):

    pass


def main():
    global time
    
    run = True
    while run:
        pygame.time.delay(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()


        gravity()
        movement(keys)
        touches_block(s,p1)
        wind.fill((0,0,0))
        draw_player(x,y,width,height)
        draw_stage()

        #print(p1.y_pos())
        ox = x
        oy = y

        pygame.draw.rect(wind,(0,255, 0), (x,y, 5, 5))
        pygame.display.update()
        time += 1
p1 = player(width,height)
s = stage(800,100, 0, 700)

main()