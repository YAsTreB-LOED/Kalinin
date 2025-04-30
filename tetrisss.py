
import pygame
import random

# Константы
WIDTH, HEIGHT = 800, 600
GRID_WIDTH, GRID_HEIGHT = 10, 20
CELL_SIZE = 30
DELAY = 200
MENU_DELAY = 20
MENU_FADE_SPEED = 5
PAUSE_DELAY = 10
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 1, 0], [0, 1, 1]],  # S
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[0, 1, 0], [1, 1, 1]]   # T
]
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]
HORIZONTAL_MOVE_DELAY = 120  # Задержка для автоматического движения вбок
VERTICAL_MOVE_DELAY = 40  # Задержка для ускоренного падения

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Тетрис")
clock = pygame.time.Clock()

# Шрифты
font_large = pygame.font.Font(None, 60)
font_medium = pygame.font.Font(None, 40)
font_small = pygame.font.Font(None, 25)

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
MENU_BG = (50, 50, 50)


# Класс фигуры тетриса
class Piece:
    def __init__(self, shape):
        self.shape = shape
        self.color = COLORS[SHAPES.index(shape)]
        self.x = GRID_WIDTH // 2 - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        rotated_shape = list(zip(*self.shape[::-1]))
        if self.check_collision(rotated_shape):
            return
        self.shape = rotated_shape

    def check_collision(self, new_shape):
        for i, row in enumerate(new_shape):
            for j, cell in enumerate(row):
                if cell:
                    x = self.x + j
                    y = self.y + i
                    if x < 0 or x >= GRID_WIDTH or y >= GRID_HEIGHT or grid[y][x]:
                        return True
        return False

    def move(self, dx):
        self.x += dx
        if self.check_collision(self.shape):
            self.x -= dx
            return False
        return True

    def move_down(self):
        self.y += 1
        if self.check_collision(self.shape):
            self.y -= 1
            return False
        return True

    def draw(self):
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.color,
                                     ( (self.x + j) * CELL_SIZE, (self.y + i) * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(screen, WHITE,
                                     ( (self.x + j) * CELL_SIZE, (self.y + i) * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)


# Глобальные переменные
grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
current_piece = None
next_piece = None
score = 0
level = 1
lines_cleared = 0
game_over = False
paused = False
records = []
nickname = ""
nickname_input_active = False
menu_active = True
running = True
fall_delay = DELAY
menu_alpha = 0
menu_fade_direction = 1
horizontal_move_timer = 0
vertical_move_timer = 0
horizontal_direction = 0  # -1 для влево, 1 для вправо, 0 для нет движения
vertical_down = False # True - ускоренное падение, False - обычное


# Загрузка рекордов
def load_records():
    global records
    try:
        with open("records.txt", "r") as f:
            for line in f:
                nickname, score = line.strip().split(",")
                records.append((nickname, int(score)))
        records.sort(key=lambda x: x[1], reverse=True)
        records = records[:5]  # Сохраняем только топ-5
    except FileNotFoundError:
        pass

# Сохранение рекордов
def save_records():
    with open("records.txt", "w") as f:
        for nickname, score in records:
            f.write(f"{nickname},{score}\n")

# Создание новой фигуры
def new_piece():
    global current_piece, next_piece
    if next_piece:
        current_piece = next_piece
    else:
        current_piece = Piece(random.choice(SHAPES))

    next_piece = Piece(random.choice(SHAPES))
    if current_piece.check_collision(current_piece.shape):
        return False  # Игра окончена
    return True

# Очистка заполненных линий
def clear_lines():
    global score, lines_cleared, level, fall_delay
    lines_to_clear = []
    for i, row in enumerate(grid):
        if all(row):
            lines_to_clear.append(i)

    for i in lines_to_clear:
        del grid[i]
        grid.insert(0, [0] * GRID_WIDTH)

    num_lines = len(lines_to_clear)
    if num_lines > 0:
        lines_cleared += num_lines
        score += (num_lines ** 2) * 100 * level
        if lines_cleared >= level * 10:
            level += 1
            fall_delay = max(50, DELAY - (level - 1) * 20)
            lines_cleared = 0
    return num_lines > 0

# Фиксация фигуры на поле
def freeze_piece():
    for i, row in enumerate(current_piece.shape):
        for j, cell in enumerate(row):
            if cell:
                grid[current_piece.y + i][current_piece.x + j] = current_piece.color

# Отрисовка сетки
def draw_grid():
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            pygame.draw.rect(screen, GRAY, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            if grid[i][j]:
                pygame.draw.rect(screen, grid[i][j], (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(screen, WHITE, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

# Отрисовка следующей фигуры
def draw_next_piece():
    text = font_medium.render("Next:", True, WHITE)
    screen.blit(text, (WIDTH - 150, 50))
    if next_piece:
        for i, row in enumerate(next_piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, next_piece.color,
                                     (WIDTH - 150 + j * CELL_SIZE, 100 + i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(screen, WHITE,
                                     (WIDTH - 150 + j * CELL_SIZE, 100 + i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

# Отрисовка статистики
def draw_stats():
    text_score = font_medium.render(f"Score: {score}", True, WHITE)
    text_level = font_medium.render(f"Level: {level}", True, WHITE)
    screen.blit(text_score, (WIDTH - 150, 250))
    screen.blit(text_level, (WIDTH - 150, 300))

# Отрисовка текста
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Отрисовка меню
def draw_menu():
    global menu_alpha

    # Управление прозрачностью
    menu_alpha = max(0, min(255, menu_alpha + MENU_FADE_SPEED * menu_fade_direction))

    # Создание полупрозрачной поверхности для меню
    menu_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    menu_surface.fill((MENU_BG[0], MENU_BG[1], MENU_BG[2], menu_alpha))
    screen.blit(menu_surface, (0, 0))

    draw_text("Тетрис", font_large, WHITE, WIDTH // 2, 150)
    draw_text("Играть (ENTER)", font_medium, WHITE, WIDTH // 2, 300)
    draw_text("Рекорды (R)", font_medium, WHITE, WIDTH // 2, 350)
    draw_text("Выход (ESC)", font_medium, WHITE, WIDTH // 2, 400)

# Отрисовка экрана рекордов
def draw_records():
    screen.fill(BLACK)
    draw_text("Рекорды", font_large, WHITE, WIDTH // 2, 100)
    y_offset = 200
    for i, (nickname, score) in enumerate(records):
        draw_text(f"{i+1}. {nickname}: {score}", font_medium, WHITE, WIDTH // 2, y_offset)
        y_offset += 50
    draw_text("Нажмите любую клавишу для возврата в меню", font_small, WHITE, WIDTH // 2, 550)

# Обработка ввода никнейма
def handle_nickname_input(event):
    global nickname
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            return True  # Enter
        elif event.key == pygame.K_BACKSPACE:
            nickname = nickname[:-1]
        else:
            nickname += event.unicode
    return False

# Отрисовка экрана ввода никнейма
def draw_nickname_input():
    screen.fill(BLACK)
    draw_text("Игра окончена!", font_large, WHITE, WIDTH // 2, 100)
    draw_text(f"Ваш счет: {score}", font_medium, WHITE, WIDTH // 2, 200)
    draw_text("Введите ваш никнейм:", font_medium, WHITE, WIDTH // 2, 300)
    pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 150, 330, 300, 40), 2)
    text_surface = font_medium.render(nickname, True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 350))
    screen.blit(text_surface, text_rect)

    draw_text("Нажмите Enter, чтобы сохранить рекорд.", font_small, WHITE, WIDTH // 2, 400)
    draw_text("Для перехода в меню нажмите Escape.", font_small, WHITE, WIDTH // 2, 450)


# Функция паузы и меню после проигрыша
def pause_or_gameover_menu(is_gameover=False):
    global paused, menu_active, nickname_input_active, running, records # Добавляем records в global

    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Завершение игры при закрытии окна
                return True # Выход из меню и из game_loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter
                    if is_gameover:
                        nickname_input_active = True # Ввод никнейма после проигрыша
                        menu = False # выходим из меню, чтобы обрабатывать ввод никнейма
                    else:
                        menu_active = False  # Продолжаем игру из паузы
                        return False # не выходим в главное меню
                elif event.key == pygame.K_ESCAPE:  # Escape
                    reset_game()
                    menu_active = True # Возврат в главное меню
                    return True # Выходим в главное меню
                elif event.key == pygame.K_r and not is_gameover: #Рестарт только если игра не окончена
                    reset_game()
                    menu_active = False
                    return False

        # Отрисовка затемнения
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))  # Черный цвет с прозрачностью
        screen.blit(overlay, (0, 0))

        # Отрисовка текста меню
        if is_gameover:
            draw_text("Игра окончена!", font_large, WHITE, WIDTH // 2, HEIGHT // 2 - 100)
            draw_text(f"Ваш счет: {score}", font_medium, WHITE, WIDTH // 2, HEIGHT // 2 - 50)
            draw_text("Сохранить рекорд (ENTER)", font_medium, WHITE, WIDTH // 2, HEIGHT // 2 + 50)
            draw_text("Выйти в меню (ESC)", font_medium, WHITE, WIDTH // 2, HEIGHT // 2 + 100)
        else:
            draw_text("Пауза (P)", font_large, WHITE, WIDTH // 2, HEIGHT // 2 - 50)
            draw_text("Продолжить (ENTER)", font_medium, WHITE, WIDTH // 2, HEIGHT // 2 )
            draw_text("Выйти в меню (ESC)", font_medium, WHITE, WIDTH // 2, HEIGHT // 2 + 50)
            draw_text("Рестарт (R)", font_medium, WHITE, WIDTH // 2, HEIGHT // 2 + 100)

        pygame.display.flip()
        clock.tick(PAUSE_DELAY)
    return False


# Сброс игры
def reset_game():
    global grid, current_piece, next_piece, score, level, lines_cleared, game_over, fall_delay
    global horizontal_direction, vertical_down
    grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    current_piece = None
    next_piece = None
    score = 0
    level = 1
    lines_cleared = 0
    game_over = False
    fall_delay = DELAY
    horizontal_direction = 0
    vertical_down = False

# Главный игровой цикл
def game_loop():
    global grid, current_piece, next_piece, score, level, lines_cleared, game_over, nickname, nickname_input_active, menu_active, running, fall_delay, menu_alpha, menu_fade_direction
    global horizontal_move_timer, vertical_move_timer, horizontal_direction, vertical_down

    # Переменные для управления падением фигуры
    fall_time = 0

    reset_game()

    if not new_piece():
        game_over = True
        return False

    # Основной игровой цикл
    while not game_over:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True  # Завершение игры
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    horizontal_direction = -1
                    horizontal_move_timer = 0
                    current_piece.move(horizontal_direction) # Движение по нажатию
                elif event.key == pygame.K_RIGHT:
                    horizontal_direction = 1
                    horizontal_move_timer = 0
                    current_piece.move(horizontal_direction) # Движение по нажатию
                elif event.key == pygame.K_DOWN:
                    vertical_down = True
                    vertical_move_timer = 0
                elif event.key == pygame.K_UP:
                    current_piece.rotate()
                elif event.key == pygame.K_p:  # Пауза
                    if pause_or_gameover_menu():
                        return True # Выход в главное меню

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and horizontal_direction == -1:
                    horizontal_direction = 0
                elif event.key == pygame.K_RIGHT and horizontal_direction == 1:
                    horizontal_direction = 0
                elif event.key == pygame.K_DOWN:
                    vertical_down = False
                    vertical_move_timer = 0

        # Автоматическое движение вбок при удержании клавиши
        if horizontal_direction != 0:
            horizontal_move_timer += clock.get_time()
            if horizontal_move_timer > HORIZONTAL_MOVE_DELAY:
                current_piece.move(horizontal_direction)
                horizontal_move_timer = 0

        # Ускоренное падение при удержании клавиши
        if vertical_down:
            vertical_move_timer += clock.get_time()
            if vertical_move_timer > VERTICAL_MOVE_DELAY:
                if current_piece.move_down():
                    score += 1  # Небольшая награда за быстрое падение
                vertical_move_timer = 0

        # Автоматическое падение фигуры
        delta_time = clock.get_time()
        fall_time += delta_time
        if fall_time > fall_delay:
            fall_time = 0
            if not current_piece.move_down():
                freeze_piece()
                if clear_lines():
                    fall_time = 0  # Небольшая задержка после очистки линий
                if not new_piece():
                    game_over = True
                    break

        # Отрисовка игры
        screen.fill(BLACK)
        draw_grid()
        current_piece.draw()
        draw_next_piece()
        draw_stats()
        pygame.display.flip()
        clock.tick(60)

    return False # Игра закончена

# Главный цикл игры (включает меню и игровую логику)
def main_loop():
    global menu_active, running, nickname_input_active, game_over, records
    global grid, current_piece, next_piece, score, level, lines_cleared, game_over, nickname, nickname_input_active, menu_active, records, running, fall_delay, menu_alpha, menu_fade_direction
    global horizontal_move_timer, vertical_move_timer, horizontal_direction, vertical_down
    load_records()

    game_over = False # Инициализируем game_over перед циклом
    while running:
        if menu_active:
            # Обработка событий в меню
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Вход
                        menu_active = False
                        nickname_input_active = False  # Сброс input
                        break  # Выход из цикла меню и запуск игры
                    elif event.key == pygame.K_r:  # R
                        menu_active = False
                        draw_records_screen = True
                        while draw_records_screen:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    running = False
                                    draw_records_screen = False
                                    break
                                if event.type == pygame.KEYDOWN:
                                    draw_records_screen = False
                                    menu_active = True
                                    break
                            draw_records()
                            pygame.display.flip()
                            clock.tick(MENU_DELAY)
                    elif event.key == pygame.K_ESCAPE:  # Выход
                        running = False
                        break

            # Отрисовка меню
            screen.fill(BLACK)
            draw_menu()
            pygame.display.flip()
            clock.tick(MENU_DELAY)

        else:
            # Запуск игры
            game_over = False  # Устанавливаем game_over в False перед началом игры
            if game_loop(): # Если вернулись в меню из игры (пауза/выход)
                continue # Возвращаемся к отрисовке меню

            # Если игра окончена, отображаем меню Game Over и обрабатываем ввод никнейма
            while game_over and running:
                 if nickname_input_active:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            break
                        if handle_nickname_input(event):
                            # Сохранение рекорда и возврат в меню
                            records.append((nickname, score))
                            records.sort(key=lambda x: x[1], reverse=True)
                            records = records[:5]
                            save_records()
                            nickname = ""
                            nickname_input_active = False
                            game_over = False  # Выйти из меню Game Over
                            menu_active = True # Возврат в меню
                            break
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                nickname = ""
                                nickname_input_active = False
                                game_over = False  # Выйти из меню Game Over
                                menu_active = True
                                break
                    draw_nickname_input()
                    pygame.display.flip()
                    clock.tick(MENU_DELAY)

                 else: # Отрисовка меню Game Over и ожидание выбора
                    if pause_or_gameover_menu(is_gameover=True):
                        game_over = False
                        break # Возврат в главное меню из game over

            # После завершения игры, если не вышли из главного меню, сбрасываем состояние и готовимся к новой игре
            if running:
                reset_game()

    save_records()
    pygame.quit()

# Запуск главного цикла игры
main_loop()
