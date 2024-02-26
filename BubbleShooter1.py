import pygame
import random
import tkinter as tk
from tkinter import messagebox
import winsound
pygame.init()
root = tk.Tk()
root.withdraw()
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bubble Shooting Game by Zidaan")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
bubble_radius = 30
bubble_speed = 0.5  
bubble_color = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
font = pygame.font.SysFont(None, 48)
bubble_x = random.randint(bubble_radius, width - bubble_radius)
bubble_y = height + bubble_radius
score = 0
message = "Bubble Shooting Game " #customizable
message2 = "Shoot All The Negativities Of Your Life !!!"
def show_score():
    score_text = font.render("Score: " + str(score), True, WHITE)
    message_text = font.render(message, True, WHITE)
    shoot_text = font.render("Shoot All The Negativities Of Your Life !!!", True, WHITE) 
    love_text = font.render("Shoot The Bubbles By Clicking On Them", True, WHITE)  
    window.blit(score_text, (10, 10))
    window.blit(message_text, (width // 2 - message_text.get_width() // 2, height // 2 - message_text.get_height() // 2))
    window.blit(shoot_text, (width // 2 - shoot_text.get_width() // 2, height // 2 - shoot_text.get_height() // 2 + 50))  
    window.blit(love_text, (width // 2 - love_text.get_width() // 2, height // 2 - love_text.get_height() // 2 + 100))  
running = True
while running:
    window.fill(BLACK)
    bubble_y -= bubble_speed
    pygame.draw.circle(window, bubble_color, (bubble_x, bubble_y), bubble_radius)
    show_score()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance = ((mouse_x - bubble_x) ** 2 + (mouse_y - bubble_y) ** 2) ** 0.5
            if distance <= bubble_radius:
                bubble_x = random.randint(bubble_radius, width - bubble_radius)
                bubble_y = height + bubble_radius
                score += 1
                winsound.Beep(1000, 100)
    if bubble_y < -bubble_radius:
        bubble_x = random.randint(bubble_radius, width - bubble_radius)
        bubble_y = height + bubble_radius
        bubble_color = (random.randint(1, 200), random.randint(1, 200), random.randint(1, 200))
    pygame.display.flip() 
window.fill(BLACK)
final_message = "Game Over !!! You Got " + str(score) + " Positive Energy "
final_message_text = font.render(final_message, True, WHITE)
a = font.render("I Hope You Enjoyed This Game", True, WHITE)
z = font.render("A Game Developed by :-> Zidaan", True, WHITE)
window.blit(final_message_text, (width // 2 - final_message_text.get_width() // 2, height // 2 - final_message_text.get_height() // 2))
window.blit(a, (width // 2 - a.get_width() // 2, height // 2 - a.get_height() // 2+50))
window.blit(z, (width // 2 - z.get_width() // 2, height // 2 - z.get_height() // 2+100))
pygame.display.flip()
pygame.time.wait(8000)
pygame.quit()
