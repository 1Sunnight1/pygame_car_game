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

class generators:
#генерация вражеских машинок
    def create_enemy_car(enemy_cars=list(),freame_count = 0):
        import random
        if freame_count%60 == 0:
            enemy_cars.append([random.randint(150,540),-60])
        return enemy_cars
    #генерация белых линий
    def create_white_line(white_line,freame_count = 0):
        if freame_count%60 == 0:
            white_line.append([380,-100])
        return white_line       
   

#главная функция
def start_game(screen):

    clock = pygame.time.Clock()
    is_blue = True
    car_x = 340
    car_y = 340
    freame_count = 0
    enemy_cars = list()
    white_lines =list()
    max_score = 0
    paused = False

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
            white_lines = generators.create_white_line(white_lines,freame_count)
            for line in white_lines:
                line[1]+=3
                pygame.draw.rect(screen, (255,255,255), pygame.Rect(380, line[1], 20, 75))#  белые полосы
                if line[1]==500:
                    white_lines.remove(line)
                

            #машинка игрока отрисовка
            car_x, car_y = control_player(car_x,car_y)
            car_x = max(150,min(540,car_x)) #ограничение по длине
            car_y = max(0,min(440,car_y)) #ограничение по ширине                
            pygame.draw.rect(screen, (100,255,100), pygame.Rect(car_x, car_y, 60, 60))# квадратик игрока


            #отрисовка вражеских машин на поле
            enemy_cars = generators.create_enemy_car(enemy_cars,freame_count)
            for car in enemy_cars[:]:
                car[1]+=3
                pygame.draw.rect(screen,(255,0,0), pygame.Rect(car[0],car[1],60,60))
                if car[0]==740:
                    enemy_cars.remove(car)  #удаление машин после конца пути
                if (  #логика столкновения машин с игроком
                    car_x in range(car[0],car[0]+60) and car_y in range(car[1],car[1]+60)  #левый верх
                or car_x+60 in range(car[0],car[0]+60) and car_y+60 in range(car[1],car[1]+60)  # правая  верх
                or car_x in range(car[0],car[0]+60) and car_y+60 in range(car[1],car[1]+60)  #левый низ
                or car_x+60 in range(car[0],car[0]+60) and car_y in range(car[1],car[1]+60)):  #правый низ 
                    if max_score<freame_count/60:
                        max_score = freame_count/60
                    freame_count = 0  # обнуление счета
                    car_y += 31 # отталкивание игрока назад и в сторону
                    if car_x+30 >= car[0]+30:
                        car_x+=31
                    else:
                        car_x-=31    
                    

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
