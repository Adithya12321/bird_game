from email.mime import image
import pygame, sys
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.gravity = 0.5
        self.score = 0
        self.direction = pygame.math.Vector2()
        self.jump_speed = 10
        self.rect = self.image.get_rect(topleft = (10, screen_height//2))
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.direction.y = -self.jump_speed
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        if pygame.sprite.spritecollide(self, enemy_group, True):
            Ene()
            self.score += 1

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect(bottomleft = (x_pos, y_pos))
    def update(self):
        self.rect.x -= 10
        if self.rect.x <= -50: 
            self.kill()
            Ene()
    
class Life(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((screen_width, 10))
        self.rect = self.image.get_rect(topleft = (0, 0))
        self.image.fill((0, 250, 0))
    def update(self):
        self.rect.x -= 1
        if self.rect.x <= -1000:
            self.kill()
            pygame.quit()
        if pygame.sprite.spritecollide(player, enemy_group, False):
            self.rect.x += 95
        
def draw_text(surface, score, size, x, y,color):
    font = pygame.font.Font(pygame.font.match_font('arial'), size)
    text_surface = font.render((str(score)), True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def Run():
    player_group.draw(screen)
    player_group.update()
    enemy_group.draw(screen)
    enemy_group.update()
    life_group.draw(screen)
    life_group.update()
    draw_text(screen, player.score, 16, 80, 10, (255, 255, 255))
    draw_text(screen, "SCORE :", 16, 40, 10, (255, 255, 255))

pygame.init()
clock = pygame.time.Clock()

screen_width, screen_height = 1000, 500 
screen = pygame.display.set_mode((screen_width, screen_height))

#Sprites
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)
life = Life()
life_group = pygame.sprite.Group()
life_group.add(life)
enemy_group = pygame.sprite.Group()

def Ene():
    enemy_group.add(Enemy(1000, random.randint(50, 450)))
Ene()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((100, 100, 100))
    run = Run()
    pygame.display.update()
    clock.tick(60)