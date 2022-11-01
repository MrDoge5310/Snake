import sys
import pygame
import random


class Block:
    """block"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.width)

    def ClearPos(self):
        pygame.draw.rect(screen, 'black', self.rect, width=0)

    def DrawBlock(self):
        """drawing a part of a snake"""
        self.ClearPos()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.width)
        pygame.draw.rect(screen, 'blue', self.rect, width=0)

    def SpawnFruit(self):
        pygame.draw.rect(screen, 'yellow', self.rect, width=0)


class Snake:
    """snake"""

    def __init__(self):
        """cords and length"""
        self.direction = "top"
        self.head = Block(600, 400)
        self.body = [self.head, Block(self.head.x, self.head.y + 20), Block(self.head.x, self.head.y + 40)]
        self.size = 3

    def drawSnake(self):
        """drawing snake"""
        for i in range(len(self.body)):
            self.body[i].DrawBlock()

    def move(self):
        global tempXa, tempYa
        tempX = self.head.x
        tempY = self.head.y

        if self.direction == "top":
            self.head.y -= 20
        elif self.direction == "down":
            self.head.y += 20
        elif self.direction == "left":
            self.head.x -= 20
        elif self.direction == "right":
            self.head.x += 20

        for i in range(len(self.body)):
            if i % 2 != 0:
                tempXa = self.body[i].x
                tempYa = self.body[i].y
                self.body[i].x = tempX
                self.body[i].y = tempY
            elif i % 2 == 0 and i > 0:
                tempX = self.body[i].x
                tempY = self.body[i].y
                self.body[i].x = tempXa
                self.body[i].y = tempYa

    def growUp(self):
        if len(self.body) < 20:
            if self.direction == "top":
                self.body.append(Block(self.body[self.size - 1].x, self.body[self.size - 1].y+20))
            elif self.direction == "down":
                self.body.append(Block(self.body[self.size - 1].x, self.body[self.size - 1].y-20))
            elif self.direction == "left":
                self.body.append(Block(self.body[self.size - 1].x, self.body[self.size - 1].y-20))
            elif self.direction == "right":
                self.body.append(Block(self.body[self.size - 1].x, self.body[self.size - 1].y+20))


def GetRandomCords():
    x = 1
    y = 1
    while x % 20 != 0 and y % 20 != 0:
        x = random.randint(0, 1200)
        y = random.randint(0, 800)
    block = Block(x, y)
    return block


pygame.init()
clock = pygame.time.Clock()

FPS = 6
high = 800
width = 1200
screen = pygame.display.set_mode((width, high))

snake_ = Snake()
fruit = GetRandomCords()
fruit.SpawnFruit()
snake_.drawSnake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if snake_.direction != "right":
                    snake_.direction = "left"
            elif event.key == pygame.K_RIGHT:
                if snake_.direction != "left":
                    snake_.direction = "right"
            elif event.key == pygame.K_UP:
                if snake_.direction != "down":
                    snake_.direction = "top"
            elif event.key == pygame.K_DOWN:
                if snake_.direction != "top":
                    snake_.direction = "down"
    snake_.growUp()
    snake_.move()
    snake_.drawSnake()
    pygame.display.flip()
    clock.tick(FPS)
