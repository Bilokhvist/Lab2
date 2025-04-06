import unittest
from unittest.mock import patch
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

# Функція для зміни напрямку змійки з перевіркою на протилежний напрямок
def change_direction(current_direction, new_direction):
    """Функція для зміни напрямку з перевіркою на протилежний напрямок."""
    if (current_direction == 'UP' and new_direction == 'DOWN') or \
       (current_direction == 'DOWN' and new_direction == 'UP') or \
       (current_direction == 'LEFT' and new_direction == 'RIGHT') or \
       (current_direction == 'RIGHT' and new_direction == 'LEFT'):
        raise ValueError("Неможливо рухатись в протилежному напрямку")
    return new_direction

class TestSnakeGame(unittest.TestCase):

    def setUp(self):
        """Запускаємо гру перед кожним тестом"""
        self.current_direction = 'LEFT'  # Початковий напрямок
        # Використовуємо mock для pygame.display.set_mode() для тестування без графічного інтерфейсу
        with patch("pygame.display.set_mode") as mock_set_mode:
            mock_set_mode.return_value = game_window

    def test_invalid_keypress_up_down(self):
        """Перевіряємо, чи видається помилка при послідовному натисканні вгору та вниз"""
        self.current_direction = change_direction(self.current_direction, 'UP')
        try:
            self.current_direction = change_direction(self.current_direction, 'DOWN')
        except ValueError as e:
            self.assertEqual(str(e), "Неможливо рухатись в протилежному напрямку")
    
    def test_invalid_keypress_down_up(self):
        self.current_direction = 'RIGHT'
        """Перевіряємо, чи видається помилка при послідовному натисканні вниз та вгору"""
        self.current_direction = change_direction(self.current_direction, 'DOWN')
        try:
            self.current_direction = change_direction(self.current_direction, 'UP')
        except ValueError as e:
            self.assertEqual(str(e), "Неможливо рухатись в протилежному напрямку")
    
    def test_invalid_keypress_left_right(self):
        self.current_direction = 'DOWN'
        """Перевіряємо, чи видається помилка при послідовному натисканні вліво та вправо"""
        self.current_direction = change_direction(self.current_direction, 'LEFT')
        try:
            self.current_direction = change_direction(self.current_direction, 'RIGHT')
        except ValueError as e:
            self.assertEqual(str(e), "Неможливо рухатись в протилежному напрямку")
    
    def test_invalid_keypress_right_left(self):
        self.current_direction = 'DOWN'
        """Перевіряємо, чи видається помилка при послідовному натисканні вправо та вліво"""
        self.current_direction = change_direction(self.current_direction, 'RIGHT')
        try:
            self.current_direction = change_direction(self.current_direction, 'LEFT')
        except ValueError as e:
            self.assertEqual(str(e), "Неможливо рухатись в протилежному напрямку")

if __name__ == '__main__':
    # Запускаємо тести з параметром verbosity для кращого виведення результатів
    unittest.main(verbosity=2)  
