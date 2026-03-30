import pygame
import pygame_menu
from game_loop import start_game
from scoreboard import show_scoreboard
from config import FPS

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption("Car Game")
    clock = pygame.time.Clock()
    
    # Меню
    menu = pygame_menu.Menu('Welcome!', 600, 300, 
                          theme=pygame_menu.themes.THEME_BLUE)
    
    # Поле ввода имени
    widget_name = menu.add.text_input('Name:', default='Player')
    
    def play_with_name():
        player_name = widget_name.get_value()
        start_game(screen, player_name)
    
    # Кнопки меню
    menu.add.button("Play", play_with_name)
    menu.add.button("Score", lambda: show_scoreboard(screen))
    menu.add.button("Quit", pygame_menu.events.EXIT)
    
    menu.mainloop(screen)
    pygame.quit()

if __name__ == '__main__':
    main()