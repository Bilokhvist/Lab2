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

# Функція для виведення повідомлення на екран
def message(msg, color, position):
    text = font_style.render(msg, True, color)
    game_window.blit(text, position)

# Функція для малювання змійки
def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(game_window, green, [block[0], block[1], block_size, block_size])

# Функція для зміни напрямку змійки з перевіркою на протилежний напрямок
def change_direction(current_direction, new_direction):
    """Функція для зміни напрямку з перевіркою на протилежний напрямок."""
    opposite_directions = {
        'UP': 'DOWN',
        'DOWN': 'UP',
        'LEFT': 'RIGHT',
        'RIGHT': 'LEFT'
    }
    if opposite_directions.get(current_direction) == new_direction:
        raise ValueError("Неможливо рухатись в протилежному напрямку")
    return new_direction

# Функція для перевірки зіткнень та виходу за межі екрану
def check_game_over(x, y, snake_list, window_width, window_height):
    if x >= window_width or x < 0 or y >= window_height or y < 0:
        return True
    for block in snake_list[:-1]:
        if block == [x, y]:
            return True
    return False

# Основна функція гри
def game_loop():
    game_over = False
    game_close = False

    x = window_width // 2
    y = window_height // 2

    x_change = 0
    y_change = 0
    current_direction = 'UP'

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
                        game_loop()  # Перезапуск гри

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    try:
                        current_direction = change_direction(current_direction, 'LEFT')
                        x_change = -block_size
                        y_change = 0
                    except ValueError as e:
                        print(e)
                elif event.key == pygame.K_RIGHT:
                    try:
                        current_direction = change_direction(current_direction, 'RIGHT')
                        x_change = block_size
                        y_change = 0
                    except ValueError as e:
                        print(e)
                elif event.key == pygame.K_UP:
                    try:
                        current_direction = change_direction(current_direction, 'UP')
                        y_change = -block_size
                        x_change = 0
                    except ValueError as e:
                        print(e)
                elif event.key == pygame.K_DOWN:
                    try:
                        current_direction = change_direction(current_direction, 'DOWN')
                        y_change = block_size
                        x_change = 0
                    except ValueError as e:
                        print(e)

        if check_game_over(x, y, snake_list, window_width, window_height):
            game_close = True

        x += x_change
        y += y_change
        game_window.fill(black)
        pygame.draw.rect(game_window, red, [apple_x, apple_y, block_size, block_size])
        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        draw_snake(block_size, snake_list)

        pygame.display.update()

        # Якщо змійка з'їла яблуко
        if x == apple_x and y == apple_y:
            apple_x = round(random.randrange(0, window_width - block_size) / 20.0) * 20.0
            apple_y = round(random.randrange(0, window_height - block_size) / 20.0) * 20.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
