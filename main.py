import sys
import pygame


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
        pygame.draw.rect(screen, 'blue', self.rect, width=0)


class Snake:
    """snake"""
    def __init__(self):
        """cords and length"""
        self.size = 2
        self.direction = "top"
        self.head = Block(width / 2, high / 2)
        self.body = [self.head, Block(self.head.x, self.head.y + 20)]

    def drawSnake(self):
        """drawing snake"""
        for i in range(self.size):
            self.body[i].DrawBlock()

    def move(self, direction):
        self.direction = direction
        for i in range(self.size):
            self.body[i].ClearPos()

            if self.direction == "left":
                self.body[i].x -= self.body[i].width
            if self.direction == "right":
                self.body[i].x += self.body[i].width
            if self.direction == "top":
                self.body[i].y -= self.body[i].width
            if self.direction == "down":
                self.body[i].y += self.body[i].width

    def growUp(self):
        """growing up the snake"""


def GetRandomCords():
    """Getting random cords (x, y)"""


pygame.init()
clock = pygame.time.Clock()
GameOver = False

FPS = 2
high = 800
width = 1200
screen = pygame.display.set_mode((width, high))

snake_ = Snake()
snake_.drawSnake()

while not GameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_.move("left")
            elif event.key == pygame.K_RIGHT:
                snake_.move("right")
            elif event.key == pygame.K_UP:
                snake_.move("top")
            elif event.key == pygame.K_DOWN:
                snake_.move("down")

    snake_.drawSnake()
    clock.tick(FPS)
    pygame.display.flip()
