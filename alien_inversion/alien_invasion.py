import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init() 
    ai_settings = Settings()
    
    # 创建一个宽1000像素、高600像素的游戏窗口
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)

    # 游戏主循环
    while True:

        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)      

run_game()