import pygame
from os.path import join
import random

class player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load("/home/oumer/Documents/python-game/5games-main/space shooter/images/player.png").convert_alpha()
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH / 2,WINDOW_HEIGHT / 2))
        player_speed = 300
        self.direction = pygame.Vector2()
    
    
    def update(self, dt):
        player_direction = player_direction.normalize() if player_direction else player_direction
        player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        keys = pygame.keys.get_pressed()
        self.direction.x = int()
        player_rect.center += player_direction * player_speed * dt


pygame.init()
WINDOW_WIDTH,WINDOW_HEIGHT = 1000,680
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('oumer')
running = True
clock = pygame.time.Clock()

surf = pygame.Surface((100,200))
surf.fill('red')
x = 100
player_direction = pygame.math.Vector2()
all_sprites = pygame.sprite.Group()
player = player(all_sprites)



# player_surf = pygame.image.load("/home/oumer/Documents/python-game/5games-main/space shooter/images/player.png").convert_alpha()
# player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2,WINDOW_HEIGHT / 2))
stars_surf = pygame.image.load('/home/oumer/Documents/python-game/5games-main/space shooter/images/star.png').convert_alpha()
meteor_surf = pygame.image.load('/home/oumer/Documents/python-game/5games-main/space shooter/images/meteor.png').convert_alpha()
laser_surf = pygame.image.load('/home/oumer/Documents/python-game/5games-main/space shooter/images/laser.png').convert_alpha()
laser_rect = laser_surf.get_rect(bottomleft = (20,WINDOW_HEIGHT -20))
meteor_rect = meteor_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
star_positions = [(random.randint(0,WINDOW_WIDTH),random.randint(0,WINDOW_HEIGHT)) for i in range(20)]

meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)

while running:
    dt = clock.tick() / 1000
    # print(clock.get_fps())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            print("create meteor")
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
        #     print("1")
        # if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
        #     player_rect.center = event.pos

# print(pygame.mouse.get_pos)
    # keys = pygame.key.get_pressed()
    recent_key = pygame.key.get_pressed()
    if recent_key[pygame.K_SPACE]:
        print("fire laser ")

    display_surface.fill('darkgray')
    for pos in star_positions:
        display_surface.blit(stars_surf, pos)
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)
    # display_surface.blit(player.image, player.rect)
    # display_surface.blit(player_surf, player_rect)
    # if player_rect.bottom >= WINDOW_HEIGHT or player_rect.top <= 0:
        # player_direction.y *= -1
    # if player_rect.right >= WINDOW_WIDTH or player_rect.left <= 0:
        # player_direction.x *= -1 
    all_sprites.draw(display_surface)
    pygame.display.update()
pygame.quit()