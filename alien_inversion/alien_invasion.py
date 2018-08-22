import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    pygame.init() 
    ai_settings = Settings()
    
    # 创建一个宽1000像素、高600像素的游戏窗口
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)

    # 游戏主循环
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # 每次循环都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # 让最近的绘制在屏幕外可见
        pygame.display.flip()

run_game()