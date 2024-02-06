import pygame, sys
import time
from pygame.locals import *

pygame.init()
# 設定螢幕大小
DISPLAYSURF = pygame.display.set_mode((580, 400), 0, 32)
pygame.display.set_caption('tower')

# 設定顏色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0 ,255)
CYAN = (0, 255, 255)
BROWN = (155, 0, 0)
LGREEN = (0, 155, 155)
OE= (123, 34, 165)
GRAY =(155, 155, 155)


clock = pygame.time.Clock()

place=[7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5]


# 定義座標位置
POLYGON_1 = ((85, 106), (90, 106), (90, 400), (80, 400), (80, 106))
POLYGON_2 = ((185, 106), (190, 106), (190, 400), (180, 400), (180, 106))
POLYGON_3 = ((285, 106), (290, 106), (290, 400), (280, 400), (280, 106))
POLYGON_4 = ((385, 106), (390, 106), (390, 400), (380, 400), (380, 106))
POLYGON_5 = ((485, 106), (490, 106), (490, 400), (480, 400), (480, 106))
RECT = (30, 320, 50, 900)


fontObj = pygame.font.Font('freesansbold.ttf', 22) #創字體的物件
textSurfaceObj = fontObj.render('', True, GREEN,WHITE) #創文字Surface
textRectObj = textSurfaceObj.get_rect() #文字方塊
textRectObj.center = (200, 50)
def draw():
    DISPLAYSURF.fill(WHITE)

    pygame.draw.ellipse(DISPLAYSURF, RED   , (place[9], 365, 155, 8), 0)

    pygame.draw.ellipse(DISPLAYSURF, GREEN , (place[8], 351, 155, 8), 0)

    pygame.draw.ellipse(DISPLAYSURF, BLUE  , (place[7], 337, 155, 8), 0)

    pygame.draw.ellipse(DISPLAYSURF, YELLOW, (place[6], 323, 155, 8), 0)

    pygame.draw.ellipse(DISPLAYSURF, PURPLE, (place[5], 309, 155, 8), 0)

    pygame.draw.ellipse(DISPLAYSURF, CYAN  , (place[4], 295, 155, 8), 0)

    pygame.draw.ellipse(DISPLAYSURF, GRAY  , (place[3], 281, 155, 8), 0)

    pygame.draw.ellipse(DISPLAYSURF, BROWN , (place[2], 267, 155, 8), 0)

    pygame.draw.ellipse(DISPLAYSURF, LGREEN, (place[1], 253, 155, 8), 0)

    pygame.draw.ellipse(DISPLAYSURF, OE    , (place[0], 237, 155, 8), 0)



# 點擊 被點到就設定為False


def hanoi(n, source, target, auxiliary,d):
    global place

    if n > 0:
        # 先将 n-1 个圆盘从源柱移动到辅助柱
        hanoi(n - 1, source, auxiliary, target,d)
        pygame.time.delay(100)

        # 在每一步递归之前更新屏幕
        pygame.display.flip()
        clock.tick(60)

        # 将最大的圆盘从源柱移动到目标柱
        if target == 'A':
            d[0].extend(['A', n])
        elif target == 'D':
            d[0].extend(['D', n])
        elif target == 'E':
            d[0].extend(['E', n])

        # 在每一步递归之后更新屏幕


        # 将 n-1 个圆盘从辅助柱移动到目标柱
        hanoi(n - 1, auxiliary, target, source,d)






deta=[[]]
t=1
u=1
n=3

# 執行 Game loop
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        pygame.draw.polygon(DISPLAYSURF, BLACK, POLYGON_1)
        pygame.draw.polygon(DISPLAYSURF, BLACK, POLYGON_2)
        pygame.draw.polygon(DISPLAYSURF, BLACK, POLYGON_3)
        pygame.draw.polygon(DISPLAYSURF, BLACK, POLYGON_4)
        pygame.draw.polygon(DISPLAYSURF, BLACK, POLYGON_5)
        pygame.draw.line(DISPLAYSURF, BLACK, (5, 400), (575, 400), 40)
        pygame.display.update()
        draw()
        key=pygame.key.get_repeat()
        if event.type == MOUSEBUTTONDOWN:
            if t==1:
                hanoi(n, 'A', 'E', 'D',deta)
                t=0
            else:

                for i in range((2**n)-1):
                    if deta[0][t] == 'A':
                        place[deta[0][u]-1] = 7.5
                    elif deta[0][t] == 'D':
                        place[deta[0][u]-1] = 205
                    elif deta[0][t] == 'E':
                        place[deta[0][u]-1] = 405

                pygame.display.flip()
                clock.tick(1600)
                u+=2
                t+=2



