import sys
import pygame

def check_events(ship):
    """ 响应按键和鼠标事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # 向右移动飞船
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.keey == pygame.K_RIGHT:
                ship.moving_right = False

def update_screen(ai_settings, screen, ship):
    """ 更新屏幕上的图像，并切换到新屏幕 """
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 让最近的绘制在屏幕外可见
    pygame.display.flip()