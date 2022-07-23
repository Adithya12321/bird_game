import pygame
import random

#Sprite class for background
class Background(pygame.sprite.Sprite):
    def __init__(self,scene) -> None:
        super().__init__()
        self.image = pygame.image.load("sprites/background.png")
        self.rect = self.image.get_rect(topleft = (scene*280, 0))
    def update(self):
        self.rect.x -= 2
        if self.rect.x <= -280:
            self.rect.x = 280

#Sprite class for base
class Base(pygame.sprite.Sprite):
    def __init__(self, scene) -> None:
        super().__init__()
        self.image = pygame.image.load("sprites/base.png")
        self.image = pygame.transform.scale(self.image, (280, 100))
        self.rect = self.image.get_rect(topleft = (scene*280, 400))
    def update(self):
        self.rect.x -= 2
        if self.rect.x <= -280:
            self.rect.x = 280

#Sprite class for pipe
class Pipe(pygame.sprite.Sprite):
    def __init__(self, pos, flip) -> None:
        super().__init__()
        self.image = pygame.image.load("sprites/pipe.png")
        if flip == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect(topleft = (280, pos))
        else:
            self.rect = self.image.get_rect(topleft = (280, pos+450))
    def update(self):
        self.rect.x -= 2
        if self.rect.x <= -100:
            self.kill()
    def create(self, k):
        global i
        pipe_group.add(Pipe(-250, i))
        i *= -1

#Sprite class for bird
class Box(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.screen = pygame.Surface((100, 100))
        self.image = pygame.image.load("sprites/bird.png")
        self.screen.blit(self.image, (0, 0))
        self.rect = self.screen.get_rect(topleft = (10, 250))
        self.screen = pygame.mask.from_surface(self.screen)
        self.gravity = 1
        self.direction = pygame.math.Vector2()
        self.arr = [(380, 185, 20, 20), (380, 210, 20, 70), (380, 238, 20, 20)]
    def update(self):
        self.direction.y += self.gravity
        if self.direction.y >= 4:
            self.direction.y = 4
        self.rect.y += self.direction.y
        if pygame.sprite.spritecollide(self, pipe_group, False, pygame.sprite.collide_mask):
            pygame.quit()
    
#Background sprite group
background_group = pygame.sprite.Group()
background_group.add(Background(0))
background_group.add(Background(1))

#Background base sprite group
base_group = pygame.sprite.Group()
base_group.add(Base(0))
base_group.add(Base(1))

#Pipe sprte group
pipe_group = pygame.sprite.Group()
pipe_group.add(Pipe(-250, 1))
pipe_group.add(Pipe(-100, -1))

#Test sprite group
box = Box()
test_group = pygame.sprite.Group()
test_group.add(box)
i = 0