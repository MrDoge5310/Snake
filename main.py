import sys
import pygame
import random
from tkinter import messagebox


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

    def SpawnFruit(self, block):
        self.x = block.x
        self.y = block.y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.width)
        pygame.draw.rect(screen, 'yellow', self.rect, width=0)


class Snake:
    """snake"""

    def __init__(self):
        """cords and length"""
        self.direction = "top"
        self.head = Block(width // 2, high // 2)
        self.body = [self.head, Block(self.head.x, self.head.y + 20), Block(self.head.x, self.head.y + 40)]
        self.size = 3

    def drawSnake(self):
        """drawing snake"""
        for i in range(len(self.body)):
            self.body[i].DrawBlock()

    def move(self):
        tempXa = 0
        tempYa = 0
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
        if self.direction == "top":
            self.body.append(Block(self.body[self.size - 1].x, self.body[self.size - 1].y + 20))
        elif self.direction == "down":
            self.body.append(Block(self.body[self.size - 1].x, self.body[self.size - 1].y - 20))
        elif self.direction == "left":
            self.body.append(Block(self.body[self.size - 1].x, self.body[self.size - 1].y - 20))
        elif self.direction == "right":
            self.body.append(Block(self.body[self.size - 1].x, self.body[self.size - 1].y + 20))

    @property
    def checkCollisions(self):
        for i in range(len(self.body)):
            if i > 0:
                if self.head.rect == self.body[i].rect and self.head.rect == self.body[i].rect:
                    return True
        if self.head.x >= width or self.head.x == 0:
            return True
        elif self.head.y >= high or self.head.y == 0:
            return True
        else:
            return False

    def isFruitEaten(self):
        if self.head.rect == fruit.rect:
            self.growUp()
            fruit.SpawnFruit(GetRandomCords())
            return True
        else:
            return False


def GetRandomCords():
    xlist = []
    ylist = []
    xtemp = 0
    ytemp = 0
    for i in range(width // 20):
        xlist.append(xtemp)
        xtemp += 20
    for i in range(high // 20):
        ylist.append(ytemp)
        ytemp += 20
    x = xlist[random.randint(1, width // 20 - 1)]
    y = ylist[random.randint(1, high // 20 - 1)]
    block = Block(x, y)
    return block


pygame.init()
pygame.display.set_caption("Snake")
pygame.font.init()
GameOver = False
clock = pygame.time.Clock()
score_font = pygame.font.Font(None, 24)

FPS = 8
high = 600
width = 800
screen = pygame.display.set_mode((width, high))

snake_ = Snake()
fruit = GetRandomCords()
fruit.SpawnFruit(fruit)
snake_.drawSnake()
score = 0

score_display = score_font.render(f"Score: {score}", True, 'black', 'white')
screen.blit(score_display, (0, 0))

while not GameOver:
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

    snake_.move()
    snake_.drawSnake()
    if snake_.isFruitEaten():
        score += 15
        score_display = score_font.render(f"Score: {score}", True, 'black', 'white')
        screen.blit(score_display, (0, 0))
    GameOver = snake_.checkCollisions
    pygame.display.flip()
    clock.tick(FPS)

messagebox.showinfo("Fail", f"Game Over\nScore: {score}")
