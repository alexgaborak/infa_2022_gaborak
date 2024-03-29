# Параметры экрана и изображений
MAX_X, MAX_Y = 1200, 800
FPS = 60

# Цвета
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

# Параметры шариков
MIN_RADIUS = 20
MAX_RADIUS = 30
MIN_X_OF_CENTRE = MAX_RADIUS
MAX_X_OF_CENTRE = MAX_X - MAX_RADIUS
MIN_Y_OF_CENTRE = MAX_RADIUS
MAX_Y_OF_CENTRE = MAX_Y - MAX_RADIUS
MAX_SPEED = 25

x_0 = x_1 = x_2 = 0  # чтобы не вылетала ошибка при клике до появления первого шарика
y_0 = y_1 = y_2 = 0
r_0 = r_1 = r_2 = 0
