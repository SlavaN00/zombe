# Pygame шаблон - скелет для нового проекта Pygame
import pygame
from random import randint as rd
from player import Player
from enemy import Enemy
# РАЗМЕРЫ ОКОШКА
WIDTH = 500
HEIGHT = 300

FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


player = Player("./тагилла.png",150,120, 200,200)
zombie = Enemy('./guy.jpg',10,40, 500,300)
x = 0
enemyGroup = pygame.sprite.Group()
def spawnEnemy():
    enemy = Enemy('./guy.jpg',width=rd(20,50))
    enemyGroup.add(enemy)







# Цикл игры
running = True
while running:

    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN,(x,200,50,20))
    player.draw(screen)
    zombie.draw(screen)
    zombie.follow(player, speed=0.5)
    if x >= WIDTH+20:
        x = -70
    # Держим цикл на правильной скорости





    player.movement()

    for enemy in enemyGroup:
        enemyGroup.draw(screen)
        enemy.follow(player,1)



    if pygame.sprite.spritecollideany(player,enemyGroup):
        print('грызут')
        player.hp -= 1
        if player.hp <= 0:
            print('побег не успешен')
            running = False








    pygame.display.update()
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    clock.tick(FPS)
pygame.quit()


# домашка 21.12.2024
# TODO Сделать движение вверх-вниз через клавиши, сделать проверки на пересечение верхней границы, нижней, и левой границ