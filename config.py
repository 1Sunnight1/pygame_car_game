from os.path import join

# Размеры
X_LEN_CAR = 60
Y_LEN_CAR = 80
SCORE_DIR = "table_score"

# Дорога
ROAD_LEFT = 150
ROAD_WIDTH = 450
ROAD_HEIGHT = 500
ROAD_RIGHT = ROAD_LEFT + ROAD_WIDTH

# Игрок границы
PLAYER_X_MIN = ROAD_LEFT
PLAYER_X_MAX = ROAD_RIGHT - X_LEN_CAR
PLAYER_Y_MIN = 0
PLAYER_Y_MAX = 390

# Пути изображений
PLAYER_IMG_PATH = "image/player.png"
ENEMY_IMG_PATH = "image/ecar.png"

# Игровые параметры
FPS = 60
SPAWN_FRAMES = 60
MOVE_SPEED = 3
SHAKE_FRAMES = 300
LINE_WIDTH = 20
LINE_HEIGHT = 75
LINE_X = 380  # центр дороги