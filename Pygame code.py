import pygame
import sys

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FONT_SIZE = 32
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
DARK_BLUE = (0, 50, 150)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PayGame')

# Fonts
font = pygame.font.Font(None, FONT_SIZE)
title_font = pygame.font.Font(None, 64)

# Global variables
budget = 0
setting_budget = False
input_text = ""
background_color = BLACK

def draw_text(text, x, y, font, color=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def main_menu():
    global budget, setting_budget, input_text, background_color
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if setting_budget:
                    if event.key == pygame.K_RETURN:
                        try:
                            budget = float(input_text)
                            setting_budget = False
                            input_text = ""
                            game_loop()
                        except ValueError:
                            input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

        screen.fill(background_color)
        draw_text("Welcome to PayGame", SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2 - 200, title_font)
        draw_text("Press Enter to Start", SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2 - 100, font)
        
        if not setting_budget:
            draw_text(f"Current Budget: ${budget:.2f}", SCREEN_WIDTH // 2 - 160, SCREEN_HEIGHT // 2, font)
            draw_text("Press 'B' to Set Budget", SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2 + 50, font)
        
        if setting_budget:
            draw_text("Enter your budget: " + input_text, SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2 + 150, font)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] and not setting_budget:
            setting_budget = True
        
        pygame.draw.rect(screen, BLUE, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 30, 160, 50))
        draw_text("Start", SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2 - 20, font, BLACK)
        
        pygame.display.flip()

def game_loop():
    global budget
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(DARK_BLUE)
        draw_text("Game Started!", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, title_font)
        draw_text(f"Budget: ${budget:.2f}", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, font)
        draw_text("Press ESC to Quit", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, font)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        
        pygame.display.flip()
    
    main_menu()

if __name__ == "__main__":
    main_menu()
