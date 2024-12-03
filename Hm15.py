import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг Понг")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Paddle:
    def __init__(self, x, y, width, height, up_key, down_key):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 6
        self.up_key = up_key
        self.down_key = down_key

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[self.up_key] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[self.down_key] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)

class Ball:
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.speed_x = 5
        self.speed_y = 5

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1

    def draw(self, surface):
        pygame.draw.ellipse(surface, WHITE, self.rect)

    def reset(self):
        self.rect.x = WIDTH // 2 - self.rect.width // 2
        self.rect.y = HEIGHT // 2 - self.rect.height // 2
        self.speed_x = 5 if self.speed_x > 0 else -5

paddle1 = Paddle(50, HEIGHT // 2 - 60, 10, 120, pygame.K_UP, pygame.K_DOWN)
paddle2 = Paddle(WIDTH - 60, HEIGHT // 2 - 60, 10, 120, pygame.K_LEFT, pygame.K_RIGHT)
ball = Ball(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30)

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    paddle1.move()
    paddle2.move()
    ball.move()

    if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
        ball.speed_x *= -1

    if ball.rect.x < 0 or ball.rect.x > WIDTH:
        ball.reset()

    screen.fill(BLACK)
    paddle1.draw(screen)
    paddle2.draw(screen)
    ball.draw(screen)
    pygame.display.flip()

    clock.tick(60)