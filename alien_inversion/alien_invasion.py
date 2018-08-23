import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init() 
    ai_settings = Settings()
    
    # 创建一个宽1000像素、高600像素的游戏窗口
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    bullets = Group()

    # 游戏主循环
    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        # 删除已消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        # print(len(bullets))

        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()