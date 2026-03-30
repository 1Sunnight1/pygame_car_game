import os
import json
import pygame
from config import SCORE_DIR

def get_score_path():
    """Путь к файлу рекордов"""
    os.makedirs(SCORE_DIR, exist_ok=True)
    return os.path.join(SCORE_DIR, "scores.json")

def load_scores():
    """Загрузка таблицы рекордов"""
    score_path = get_score_path()
    if os.path.exists(score_path):
        with open(score_path, "r") as f:
            return json.load(f)
    return []

def save_scores(scores):
    """Сохранение таблицы рекордов"""
    score_path = get_score_path()
    with open(score_path, "w") as f:
        json.dump(scores, f)

def show_scoreboard(screen):
    """Отображение лидеров"""
    scores = load_scores()
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return
        
        # Очистка экрана ВНЕ обработчика событий
        screen.fill((0, 0, 0))
        
        # Заголовок
        font_title = pygame.font.Font(None, 60)
        title = font_title.render("Leaders", True, (255, 255, 255))
        screen.blit(title, (200, 50))
        
        # Топ-10 игроков
        font = pygame.font.Font(None, 40)
        y_pos = 150
        for i, (name, score) in enumerate(scores[:10], 1):
            text = font.render(f"{i}. {name}: {score}", True, (200, 200, 200))
            screen.blit(text, (200, y_pos))
            y_pos += 50
        
        # Подсказка
        font_small = pygame.font.Font(None, 35)
        back_text = font_small.render("ESC - menu", True, (200, 200, 200))
        screen.blit(back_text, (200, 450))
        
        clock.tick(60)
        pygame.display.flip()