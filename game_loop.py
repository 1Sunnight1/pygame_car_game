import pygame
from config import (
    FPS, ROAD_LEFT, ROAD_WIDTH, ROAD_HEIGHT,
    X_LEN_CAR, Y_LEN_CAR, MOVE_SPEED
)
from player import Player
from generators import Generators
from scoreboard import load_scores, save_scores

def start_game(screen, player_name):
    """Основной игровой цикл"""
    
    # Загрузка ресурсов
    player_image = pygame.image.load("image/player.png").convert_alpha()
    player_image = pygame.transform.scale(player_image, (X_LEN_CAR, Y_LEN_CAR))
    enemy_image = pygame.image.load("image/ecar.png").convert_alpha()
    enemy_image = pygame.transform.scale(enemy_image, (X_LEN_CAR, Y_LEN_CAR))
    
    # Инициализация объектов
    scores = load_scores()
    player = Player(340, 340)
    player.image = player_image
    
    clock = pygame.time.Clock()
    frame_count = 0
    enemy_cars = []
    white_lines = []
    current_score = 0
    max_score = 0
    paused = False
    
    # Игровой цикл
    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                if max_score > 0:
                    scores.append([player_name, int(max_score)])
                    scores.sort(key=lambda x: x[1], reverse=True)
                    scores = scores[:5]
                    save_scores(scores)
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                paused = not paused
        
        # Очистка экрана
        screen.fill((0, 0, 0))
        
        if not paused:
            frame_count += 1
            current_score = int(frame_count / FPS)
            if current_score > max_score:
                max_score = current_score
            
            # Игровая логика
            player.update()
            
            # Дорога
            pygame.draw.rect(screen, (100, 100, 100), 
                           (ROAD_LEFT, 0, ROAD_WIDTH, ROAD_HEIGHT))
            
            # Белые линии
            Generators.create_white_line(white_lines, frame_count)
            Generators.update_lines(white_lines, MOVE_SPEED)
            for line in white_lines:
                pygame.draw.rect(screen, (255, 255, 255), 
                               (line[0], line[1], 20, 75))
            
            # Враги
            Generators.create_enemy_car(enemy_cars, frame_count)
            Generators.update_enemies(enemy_cars, MOVE_SPEED)
            
            # Проверка столкновений
            player_rect = player.get_rect()
            for e_car in enemy_cars[:]:
                enemy_rect = pygame.Rect(e_car[0], e_car[1], X_LEN_CAR, Y_LEN_CAR)
                if player_rect.colliderect(enemy_rect):
                    current_score = 0
                    frame_count = 0
                    player.start_shake()
                    enemy_cars.remove(e_car)
                    break
            
            # Отрисовка врагов
            for e_car in enemy_cars:
                screen.blit(enemy_image, (e_car[0], e_car[1]))
            
            # Отрисовка игрока
            player.draw(screen)
        
        else:
            # Пауза
            font = pygame.font.Font(None, 80)
            text = font.render('Pause (Space)', True, (255, 255, 255))
            screen.blit(text, (200, 200))
        
        # UI счетчиков
        font = pygame.font.Font(None, 30)
        score_text = font.render(f'Счет: {current_score}', True, (255, 255, 255))
        max_text = font.render(f'Max: {int(max_score)}', True, (255, 255, 255))
        screen.blit(score_text, (650, 10))
        screen.blit(max_text, (650, 50))
        
        clock.tick(FPS)
        pygame.display.flip()