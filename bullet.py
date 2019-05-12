import math
import pygame
import game_functions as gf


class Bullet():
    def __init__(self, source_rect, source_atk, target, ai_settings, screen):
        pass

    def update(self):
        if self.is_alive:
            # Wheter collide a wall
            for i in range(0, len(self.ai_settings.walls)):
                if self.rect.colliderect(self.ai_settings.walls[i].rect):
                    self.is_alive = False
                    return
            # Whether out of screen
            if self.rect.centerx < self.screen_rect.left or self.rect.centerx > self.screen_rect.right or \
                    self.rect.centery < self.screen_rect.top or self.rect.centery > self.screen_rect.bottom:
                self.is_alive = False
                return

            # Whether collide the target. If true, give a damage to target
            if self.rect.colliderect(self.target):
                if self.target.is_alive == True:
                    self.target.health -= self.atk
                    self.is_alive = False
                    return

            # Update the bullet's position
            self.centerx += self.x_speed
            self.centery += self.y_speed
            self.rect.centerx = self.centerx
            self.rect.centery = self.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class BlueBullet(Bullet):
    """Monster bullet, rank1"""

    def __init__(self, source_rect, source_atk, target, ai_settings, screen):
        self.is_alive = True
        self.target = target
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.atk = source_atk
        self.speed = self.ai_settings.bluebullet_speed_factor

        self.image = self.ai_settings.bluebullet_img
        self.rect = self.image.get_rect()
        self.centerx = float(source_rect.centerx)
        self.centery = float(source_rect.centery)
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        len_x = target.rect.centerx - self.centerx
        len_y = target.rect.centery - self.centery
        s = math.sqrt(len_x ** 2 + len_y ** 2)
        times = s / self.speed
        self.x_speed = len_x / times
        self.y_speed = len_y / times


class Fireball(Bullet):
    """Monster bullet, rank2"""

    def __init__(self, source_rect, source_atk, target, ai_settings, screen):
        self.is_alive = True
        self.target = target
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.atk = source_atk
        self.speed = self.ai_settings.fireball_speed_factor

        self.image = self.ai_settings.fireball_img
        self.rect = self.image.get_rect()
        self.centerx = float(source_rect.centerx)
        self.centery = float(source_rect.centery)
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        len_x = target.rect.centerx - self.centerx
        len_y = target.rect.centery - self.centery
        s = math.sqrt(len_x ** 2 + len_y ** 2)
        times = s / self.speed
        self.x_speed = len_x / times
        self.y_speed = len_y / times


class Lightning_ball(Bullet):
    """Monster bullet, rank3"""

    def __init__(self, source_rect, source_atk, target, ai_settings, screen):
        self.is_alive = True
        self.target = target
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.atk = source_atk
        self.speed = self.ai_settings.lightning_ball_speed_factor

        self.image = self.ai_settings.lightning_ball_img
        self.rect = self.image.get_rect()
        self.centerx = float(source_rect.centerx)
        self.centery = float(source_rect.centery)
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        len_x = target.rect.centerx - self.centerx
        len_y = target.rect.centery - self.centery
        s = math.sqrt(len_x ** 2 + len_y ** 2)
        times = s / self.speed
        self.x_speed = len_x / times
        self.y_speed = len_y / times


class Black_fireball(Bullet):
    """Monster bullet, rank4"""

    def __init__(self, source_rect, source_atk, target, ai_settings, screen):
        self.is_alive = True
        self.target = target
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.atk = source_atk
        self.speed = self.ai_settings.black_fireball_speed_factor

        self.image = self.ai_settings.black_fireball_img
        self.rect = self.image.get_rect()
        self.centerx = float(source_rect.centerx)
        self.centery = float(source_rect.centery)
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        len_x = target.rect.centerx - self.centerx
        len_y = target.rect.centery - self.centery
        s = math.sqrt(len_x ** 2 + len_y ** 2)
        times = s / self.speed
        self.x_speed = len_x / times
        self.y_speed = len_y / times


class Player_Bullet(Bullet):
    def update(self):
        if self.is_alive:
            # Wheter collide a wall
            for i in range(0, len(self.ai_settings.walls)):
                if self.rect.colliderect(self.ai_settings.walls[i].rect):
                    self.is_alive = False
                    return
            # Whether out of screen
            if self.rect.centerx < self.screen_rect.left or self.rect.centerx > self.screen_rect.right or \
                    self.rect.centery < self.screen_rect.top or self.rect.centery > self.screen_rect.bottom:
                self.is_alive = False
                return

            # Whether collide the target. If true, give a damage to target
            for enemy in self.enemies:
                if self.rect.colliderect(enemy.rect):
                    if enemy.is_alive:
                        enemy.health -= self.atk
                        self.is_alive = False
                        return

            # Update the bullet's position
            self.centerx += self.x_speed
            self.centery += self.y_speed
            self.rect.centerx = self.centerx
            self.rect.centery = self.centery


class RedBullet(Player_Bullet):

    def __init__(self, source_rect, source_atk, enemies, mouse_x, mouse_y, ai_settings, screen):
        self.is_alive = True
        self.enemies = enemies
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.atk = source_atk
        self.speed = self.ai_settings.redbullet_speed_factor

        self.image = self.ai_settings.redbullet_img
        self.rect = self.image.get_rect()
        self.centerx = float(source_rect.centerx)
        self.centery = float(source_rect.centery)
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        len_x = mouse_x - self.centerx
        len_y = mouse_y - self.centery
        s = math.sqrt(len_x ** 2 + len_y ** 2)
        times = s / self.speed
        self.x_speed = len_x / times
        self.y_speed = len_y / times

    # def update(self):
    #     if self.is_alive:
    #         # Wheter collide a wall
    #         for i in range(0, len(self.ai_settings.walls)):
    #             if self.rect.colliderect(self.ai_settings.walls[i].rect):
    #                 self.is_alive = False
    #                 return
    #         # Whether out of screen
    #         if self.rect.centerx < self.screen_rect.left or self.rect.centerx > self.screen_rect.right or \
    #                 self.rect.centery < self.screen_rect.top or self.rect.centery > self.screen_rect.bottom:
    #             self.is_alive = False
    #             return
    #
    #         # Whether collide the target. If true, give a damage to target
    #         for enemy in self.enemies:
    #             if self.rect.colliderect(enemy.rect):
    #                 if enemy.is_alive:
    #                     enemy.health -= self.atk
    #                     self.is_alive = False
    #                     return
    #
    #         # Update the bullet's position
    #         self.centerx += self.x_speed
    #         self.centery += self.y_speed
    #         self.rect.centerx = self.centerx
    #         self.rect.centery = self.centery


class CoinBullet(Player_Bullet):

    def __init__(self, source_rect, source_atk, enemies, mouse_x, mouse_y, ai_settings, screen):
        self.is_alive = True
        self.enemies = enemies
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.atk = source_atk
        self.speed = self.ai_settings.coin_bullet_speed_factor

        self.image = self.ai_settings.coin_bullet_img
        self.rect = self.image.get_rect()
        self.centerx = float(source_rect.centerx)
        self.centery = float(source_rect.centery)
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        len_x = mouse_x - self.centerx
        len_y = mouse_y - self.centery
        s = math.sqrt(len_x ** 2 + len_y ** 2)
        times = s / self.speed
        self.x_speed = len_x / times
        self.y_speed = len_y / times

    # def update(self):
    #     if self.is_alive:
    #         # Wheter collide a wall
    #         for i in range(0, len(self.ai_settings.walls)):
    #             if self.rect.colliderect(self.ai_settings.walls[i].rect):
    #                 self.is_alive = False
    #                 return
    #         # Whether out of screen
    #         if self.rect.centerx < self.screen_rect.left or self.rect.centerx > self.screen_rect.right or \
    #                 self.rect.centery < self.screen_rect.top or self.rect.centery > self.screen_rect.bottom:
    #             self.is_alive = False
    #             return
    #
    #         # Whether collide the target. If true, give a damage to target
    #         for enemy in self.enemies:
    #             if self.rect.colliderect(enemy.rect):
    #                 if enemy.is_alive:
    #                     enemy.health -= self.atk
    #                     self.is_alive = False
    #                     return
    #
    #         # Update the bullet's position
    #         self.centerx += self.x_speed
    #         self.centery += self.y_speed
    #         self.rect.centerx = self.centerx
    #         self.rect.centery = self.centery


class Skull_Bullet(Player_Bullet):
    def __init__(self, source_rect, source_atk, enemies, mouse_x, mouse_y, ai_settings, screen):
        self.is_alive = True
        self.enemies = enemies
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.atk = source_atk
        self.speed = self.ai_settings.skull_bullet_speed_factor

        self.image = self.ai_settings.skull_bullet_img
        self.rect = self.image.get_rect()
        self.centerx = float(source_rect.centerx)
        self.centery = float(source_rect.centery)
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        len_x = mouse_x - self.centerx
        len_y = mouse_y - self.centery
        s = math.sqrt(len_x ** 2 + len_y ** 2)
        times = s / self.speed
        self.x_speed = len_x / times
        self.y_speed = len_y / times
