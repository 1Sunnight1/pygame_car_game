from random import randint
from config import (
    ROAD_LEFT, ROAD_RIGHT, Y_LEN_CAR, 
    SPAWN_FRAMES, LINE_WIDTH, LINE_HEIGHT, LINE_X
)

class Generators:
    @staticmethod
    def create_enemy_car(enemy_cars, frame_count):
        """Спавн врагов каждые SPAWN_FRAMES кадров"""
        if frame_count % SPAWN_FRAMES == 0:
            x = randint(ROAD_LEFT, ROAD_RIGHT - Y_LEN_CAR)
            enemy_cars.append([x, -120])
        return enemy_cars
    
    @staticmethod
    def create_white_line(white_lines, frame_count):
        """Спавн белых линий каждые SPAWN_FRAMES кадров"""
        if frame_count % SPAWN_FRAMES == 0:
            white_lines.append([LINE_X, -100])
        return white_lines
    
    @staticmethod
    def update_lines(lines, speed):
        """Движение и удаление линий"""
        for line in lines[:]:
            line[1] += speed
            if line[1] >= 500:
                lines.remove(line)
        return lines
    
    @staticmethod
    def update_enemies(enemies, speed):
        """Движение и удаление врагов"""
        for enemy in enemies[:]:
            enemy[1] += speed
            if enemy[1] >= 500:  # исправлена ошибка с 740
                enemies.remove(enemy)
        return enemies