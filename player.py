import pygame
from random import randint
from config import (  
    MOVE_SPEED, PLAYER_X_MIN, PLAYER_X_MAX, 
    PLAYER_Y_MIN, PLAYER_Y_MAX, SHAKE_FRAMES,
    X_LEN_CAR, Y_LEN_CAR )

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shake_timer = 0
        self.shake_offset_x = 0
        self.shake_offset_y = 0
        self.image = None  # загрузка в game_loop
    
    def handle_input(self):
        """Обработка клавиш"""
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: self.y -= MOVE_SPEED
        if pressed[pygame.K_DOWN]: self.y += MOVE_SPEED
        if pressed[pygame.K_LEFT]: self.x -= MOVE_SPEED
        if pressed[pygame.K_RIGHT]: self.x += MOVE_SPEED
    
    def check_bounds(self):
        """Ограничение движения"""
        self.x = max(PLAYER_X_MIN, min(PLAYER_X_MAX, self.x))
        self.y = max(PLAYER_Y_MIN, min(PLAYER_Y_MAX, self.y))
    
    def update_shake(self):
        """Обновление тряски"""
        if self.shake_timer > 0:
            self.shake_timer -= 1
            self.shake_offset_x = randint(-5, 5)
            self.shake_offset_y = randint(-5, 5)
        else:
            self.shake_offset_x = 0
            self.shake_offset_y = 0
    
    def start_shake(self):
        """Запуск тряски при столкновении"""
        self.shake_timer = SHAKE_FRAMES
    
    def update(self):
        """Полный апдейт"""
        self.handle_input()
        self.check_bounds()
        self.update_shake()
    
    def get_rect(self):
        """Для проверки столкновений"""
        return pygame.Rect(
            self.x, self.y, X_LEN_CAR, Y_LEN_CAR  
        )
    
    def draw(self, screen):
        """Отрисовка с тряской"""
        screen.blit(self.image, (self.x + self.shake_offset_x, 
                                self.y + self.shake_offset_y))