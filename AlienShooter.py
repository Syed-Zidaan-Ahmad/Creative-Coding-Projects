import pygame
import random
import winsound
pygame.init()
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Negativity Shooting Game by Zidaan")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
player_size = 40
player_x = (WIDTH - player_size) // 2
player_y = HEIGHT - player_size - 20
player_speed = 5
bullet_size = 8
bullet_color = YELLOW
bullet_speed = 10
bullets = []
enemy_size = 30
enemy_speed = 2
enemies = []
score = 0
enemy_attack_size = 60
enemy_attack_speed = 5
enemy_attack_color = RED
enemy_attack_active = False
enemy_attack_x = 0
enemy_attack_y = 0
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
last_attack_time = 0
attack_interval = 10000  
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = player_x + player_size // 2 - bullet_size // 2
                bullet_y = player_y
                bullets.append([bullet_x, bullet_y])
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    for bullet in bullets:
        bullet[1] -= bullet_speed
    for enemy in enemies:
        enemy[1] += enemy_speed
    if enemy_attack_active:
        enemy_attack_y += enemy_attack_speed
        if (
            player_x < enemy_attack_x + enemy_attack_size
            and player_x + player_size > enemy_attack_x
            and player_y < enemy_attack_y + enemy_attack_size
            and player_y + player_size > enemy_attack_y
        ):
            running = False  
        if enemy_attack_y > HEIGHT:
            enemy_attack_active = False
    for bullet in bullets:
        for enemy in enemies:
            if (
                enemy[0] <= bullet[0] <= enemy[0] + enemy_size
                and enemy[1] <= bullet[1] <= enemy[1] + enemy_size
            ):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                winsound.Beep(7000, 100)
    bullets = [bullet for bullet in bullets if bullet[1] > 0]
    enemies = [enemy for enemy in enemies if enemy[1] < HEIGHT]
    if len(enemies) < 6:
        enemy_x = random.randint(0, WIDTH - enemy_size)
        enemy_y = 0
        enemy_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        enemies.append([enemy_x, enemy_y, enemy_color])
    current_time = pygame.time.get_ticks()
    if current_time - last_attack_time >= attack_interval and not enemy_attack_active:
        enemy_attack_x = random.randint(0, WIDTH - enemy_attack_size)
        enemy_attack_y = 0
        enemy_attack_active = True
        last_attack_time = current_time
    win.fill(BLACK)
    pygame.draw.polygon(
        win,
        WHITE,
        [
            (player_x, player_y + player_size),
            (player_x + player_size // 2, player_y),
            (player_x + player_size, player_y + player_size),
        ],
    )
    for bullet in bullets:
        pygame.draw.rect(win, bullet_color, (bullet[0], bullet[1], bullet_size, bullet_size))
    for enemy in enemies:
        pygame.draw.circle(
            win,
            enemy[2],
            (enemy[0] + enemy_size // 2, enemy[1] + enemy_size // 2),
            enemy_size // 2,
        )
    if enemy_attack_active:
        pygame.draw.rect(
            win,
            enemy_attack_color,
            (enemy_attack_x, enemy_attack_y, enemy_attack_size, enemy_attack_size),
        )
    message1 = font.render("Negativity Shooter Game", True, WHITE)
    message2 = font.render("Shoot All The Negativities Of Your Life !!!", True, WHITE)
    message3 = font.render("Use Left and Right Arrow For Movements", True, WHITE)
    message4 = font.render("Use Space Bar For Shooting", True, WHITE)
    win.blit(message1, (WIDTH // 2 - message1.get_width() // 2, HEIGHT // 2 - 100))
    win.blit(message2, (WIDTH // 2 - message2.get_width() // 2, HEIGHT // 2 - 50))
    win.blit(message3, (WIDTH // 2 - message3.get_width() // 2, HEIGHT // 2))
    win.blit(message4, (WIDTH // 2 - message4.get_width() // 2, HEIGHT // 2 + 50))
    if enemy_attack_active:
        attack_message = font.render("Incoming Attack !!!", True, RED)
        dodge_message = font.render("Dodge Or You Will Loose !!!", True, RED)
        win.blit(attack_message, (WIDTH // 2 - attack_message.get_width() // 2, 20))
        win.blit(dodge_message, (WIDTH // 2 - dodge_message.get_width() // 2, 60))
    score_text = font.render("Score: " + str(score), True, WHITE)
    win.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)
game_over_message1 = font.render("Game Over !!! Your Score Is " + str(score) + " Positive Energy !!!", True, WHITE) 
game_over_message2 = font.render("I Hope You Enjoyed This Game", True, WHITE)
game_over_message3 = font.render("A Game Developed by :-> Zidaan", True, WHITE)
win.fill(BLACK)
win.blit(game_over_message1, (WIDTH // 2 - game_over_message1.get_width() // 2, HEIGHT // 2 - 100))
win.blit(game_over_message2, (WIDTH // 2 - game_over_message2.get_width() // 2, HEIGHT // 2 - 50))
win.blit(game_over_message3, (WIDTH // 2 - game_over_message3.get_width() // 2, HEIGHT // 2))
pygame.display.flip()
pygame.time.wait(6500)
pygame.quit()
