import pygame
import sys
import time
import random

# Directions for the snake
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

class SnakeGame:
    def __init__(self):
        self.size = width, height = 800, 600
        self.black = 0, 0, 0
        self.white = 255, 255, 255
        pygame.init()
        self.display = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()

        # Initialize the snake
        self.snake = [(100, 50), (90, 50), (80, 50)]
        self.direction = RIGHT

        # Place a random food point
        self.food = (random.randint(0, width-10), random.randint(0, height-10))

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != DOWN:
                    self.direction = UP

                elif event.key == pygame.K_DOWN and self.direction != UP:
                    self.direction = DOWN

                elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                    self.direction = LEFT

                elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                    self.direction = RIGHT

    def move_snake(self):
        head = self.snake[0]

        if self.direction == UP:
            new_head = (head[0], head[1] - 10)
        elif self.direction == DOWN:
            new_head = (head[0], head[1] + 10)
        elif self.direction == LEFT:
            new_head = (head[0] - 10, head[1])
        elif self.direction == RIGHT:
            new_head = (head[0] + 10, head[1])

        self.snake.insert(0, new_head)

        if self.snake[0] == self.food:
            return True
        else:
            self.snake.pop()

    def check_collision(self):
        if self.snake[0][0] < 0 or self.snake[0][0] >= self.size[0]:
            return True

        elif self.snake[0][1] < 0 or self.snake[0][1] >= self.size[1]:
            return True

        for part in self.snake[1:]:
            if part == self.snake[0]:
                return True

    def game_loop(self):
        while True:
            self.check_events()

            if self.move_snake():
                self.food = (random.randint(0, width-10), random.randint(0, height-10))

            screen.fill(self.black)

            for part in self.snake:
                pygame.draw.rect(screen, self.white, pygame.Rect(part[0], part[1], 10, 10))

            pygame.draw.rect(screen, self.white, pygame.Rect(self.food[0], self.food[1], 10, 10))

            if self.check_collision():
                screen.fill(self.black)
                font = pygame.font.Font(None, 72)
                text = font.render("Game Over", True, self.white)
                screen.blit(text, (self.size[0]//2 - 100, self.size[1]//2))
                pygame.display.update()
                time.sleep(3)
                pygame.quit()
                sys.exit()

            pygame.display.flip()
            self.clock.tick(10)

game = SnakeGame()
screen = pygame.display.get_surface()
pygame.display.set_mode((800,600), pygame.FULLSCREEN)
game.game_loop()