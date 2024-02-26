import pygame
import random
import time
import winsound
pygame.init()
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Blessings Collector Game by Zidaan")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
player_width = 50
player_height = 50
player_x = width // 2 - player_width // 2
player_y = height - player_height - 10
player_speed = 5
player_color = WHITE
coin_radius = 15
coin_x = random.randint(coin_radius, width - coin_radius)
coin_y = -coin_radius
coin_speed = 3
coin_color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
score = 0
font = pygame.font.SysFont(None, 36)
message = "Blessings Collector Game " #customization
message2 = "The More Orbs You Collect"
message3 = "The More Blessings You Receive"
message4 = "Use Left and Right Arrow Keys To Play"
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed
    coin_y += coin_speed
    if player_x < coin_x + coin_radius and player_x + player_width > coin_x - coin_radius and player_y < coin_y + coin_radius and player_y + player_height > coin_y - coin_radius:
        coin_x = random.randint(coin_radius, width - coin_radius)
        coin_y = -coin_radius
        score += 1
        winsound.Beep(600, 100)
        coin_color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        player_color = coin_color
    if coin_y > height + coin_radius:
        coin_x = random.randint(coin_radius, width - coin_radius)
        coin_y = -coin_radius
        coin_color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    window.fill(BLACK)
    pygame.draw.rect(window, player_color, (player_x, player_y, player_width, player_height))
    pygame.draw.circle(window, coin_color, (coin_x, int(coin_y)), coin_radius)
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))
    message_text = font.render(message, True, WHITE)
    message2_text = font.render(message2, True, WHITE)
    message3_text = font.render(message3, True, WHITE)
    message4_text = font.render(message4, True, WHITE)
    window.blit(message_text, (width // 2 - message_text.get_width() // 2, height // 2 - message_text.get_height() // 2))
    window.blit(message2_text, (width // 2 - message2_text.get_width() // 2, height // 2 + message_text.get_height() // 2 + 10))
    window.blit(message3_text, (width // 2 - message3_text.get_width() // 2, height // 2 + message_text.get_height() // 2 + 50))
    window.blit(message4_text, (width // 2 - message4_text.get_width() // 2, height // 2 + message_text.get_height() // 2 + 90))
    pygame.display.flip()
window.fill(BLACK)
final_message = "Game Over !!! You got " + str(score) + " Blessings"
final_message_text = font.render(final_message, True, WHITE)
a = font.render("I Hope You Enjoyed This Game", True, WHITE)
z = font.render("A Game Developed by :-> Zidaan", True, WHITE)
window.blit(final_message_text, (width // 2 - final_message_text.get_width() // 2, height // 2 - final_message_text.get_height() // 2))
window.blit(a, (width // 2 - a.get_width() // 2, height // 2 - a.get_height() // 2 + 50))
window.blit(z, (width // 2 - z.get_width() // 2, height // 2 - z.get_height() // 2 + 100))
pygame.display.flip()
time.sleep(8)
pygame.quit()
