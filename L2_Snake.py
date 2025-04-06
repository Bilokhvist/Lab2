import pygame
import time
import random

# Ініціалізація pygame
pygame.init()

# Розміри вікна гри
window_width = 600
window_height = 400

# Кольори (RGB)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Розмір блоку змійки
block_size = 20

# Швидкість змійки
snake_speed = 10

# Шрифт для тексту
font_style = pygame.font.SysFont(None, 35)

# Створення вікна гри
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Змійка на Python 🐍")


def message(msg, color, position):
    text = font_style.render(msg, True, color)
    game_window.blit(text, position)


def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(game_window, green, [block[0], block[1], block_size, block_size])


def game_loop():
    game_over = False
    game_close = False

    x = window_width // 2
    y = window_height // 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    # Позиція яблука
    apple_x = round(random.randrange(0, window_width - block_size) / 20.0) * 20.0
    apple_y = round(random.randrange(0, window_height - block_size) / 20.0) * 20.0

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            game_window.fill(black)
            message("Програв! Натисни Q - Вихід або C - Продовжити", red, [15, window_height // 2])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        if x >= window_width or x < 0 or y >= window_height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        game_window.fill(black)
        pygame.draw.rect(game_window, red, [apple_x, apple_y, block_size, block_size])
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Перевірка на зіткнення з тілом
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)

        pygame.display.update()

        # Якщо з’їла яблуко
        if x == apple_x and y == apple_y:
            apple_x = round(random.randrange(0, window_width - block_size) / 20.0) * 20.0
            apple_y = round(random.randrange(0, window_height - block_size) / 20.0) * 20.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
