from random import randint

import pygame
import pygame_menu


#функия контоля игрока
def control_player(x,y):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y-=3
    if pressed[pygame.K_DOWN]: y+=3
    if pressed[pygame.K_LEFT]: x-=3
    if pressed[pygame.K_RIGHT]: x+=3
    return x,y

class Generators:
#генерация вражеских машинок
    def create_enemy_car(enemy_cars=list(),frame_count = 0):
        import random
        if frame_count%60 == 0:
            enemy_cars.append([random.randint(150,520),-120])
        return enemy_cars
    #генерация белых линий
    def create_white_line(white_line,frame_count = 0):
        if frame_count % 60 == 0:
            white_line.append([380,-100])
        return white_line       
   

#главная функция
def start_game(screen):

    player_image = pygame.image.load("image/player.png").convert_alpha()
    player_image = pygame.transform.scale(player_image,(80,110))

    enemy_image = pygame.image.load("image/ecar.png").convert_alpha()
    enemy_image = pygame.transform.scale(enemy_image,(80,110))

    clock = pygame.time.Clock()
    is_blue = True
    car_x = 340
    car_y = 340
    freame_count = 0
    enemy_cars = list()
    white_lines =list()
    max_score = 0
    paused = False
    shake_timer = 0
    shake_ofset_x = 0
    shake_ofset_y = 0

    #основой цикл
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or(event.type == pygame.KEYDOWN 
                                            and event.key == pygame.K_ESCAPE):
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                paused = not paused

        #очищает весь экран чёрным цветом
        screen.fill((0,0,0))    
        if not paused:
            freame_count += 1
            # дорога
            pygame.draw.rect(screen, (100,100,100), pygame.Rect(150, 0, 450, 500))#  серая
            white_lines = Generators.create_white_line(white_lines,freame_count)
            for line in white_lines[:]:
                line[1]+=3
                pygame.draw.rect(screen, (255,255,255), pygame.Rect(380, line[1], 20, 75))#  белые полосы
                if line[1]==500:
                    white_lines.remove(line)
            
            #тряска игрока при столкновении
            if shake_timer > 0:
                shake_timer -= 1
                shake_ofset_x = randint(-5,5)
                shake_ofset_y = randint(-5,5)
            else:
                shake_ofset_y = 0
                shake_ofset_x = 0

            #машинка игрока отрисовка
            car_x, car_y = control_player(car_x,car_y)
            car_x = max(150,min(520,car_x)) #ограничение по длине
            car_y = max(0,min(390,car_y)) #ограничение по ширине                
            screen.blit(player_image,(car_x+shake_ofset_x,car_y+shake_ofset_y,))

            #отрисовка вражеских машин на поле
            enemy_cars = Generators.create_enemy_car(enemy_cars,freame_count)
            for e_car in enemy_cars[:]:
                e_car[1]+=3
                screen.blit(enemy_image,(e_car[0],e_car[1]))
                if e_car[0]==740:
                    enemy_cars.remove(e_car)  #удаление машин после конца пути
                if (e_car[0] < car_x + 75 and e_car[0] + 75 > car_x and 
                    e_car[1] < car_y + 105 and e_car[1] + 105 > car_y):
                    if max_score<freame_count/60:
                        max_score = freame_count/60
                    freame_count = 0  # обнуление счета
                    #удаление вражеской машинки и тряска для машинки игрока
                    enemy_cars.remove(e_car)                
                    shake_timer = 300

            #вывод счеткика
            font = pygame.font.Font(None,30)
            text = font.render(f'счет: {str(int(freame_count/60))}',True,(255,255,255))
            screen.blit(text, (650,10))
            text = font.render(f'max: {str(int(max_score))}',True,(255,255,255))
            screen.blit(text, (650,50))        
        else:
            font = pygame.font.Font(None,80)
            text = font.render('Pause (Space)',True,(255,255,255) )
            screen.blit(text,(200,200))

        clock.tick(60)
        pygame.display.flip()

    
def main():
    pygame.init()
    screen = pygame.display.set_mode((800,500))
    menu = pygame_menu.Menu('Welcome!',600,300,theme = pygame_menu.themes.THEME_BLUE)
    menu.add.text_input('Name:',default = 'Player')
    menu.add.button("Play",start_game,screen)
    menu.add.button("Quit",pygame_menu.events.EXIT)
    
    menu.mainloop(screen)

if __name__ == '__main__':
    main()
