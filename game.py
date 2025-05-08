import pygame
import random
import math 
import os

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Космос")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

try:
    spaceship_image = pygame.image.load("spaceship.png").convert_alpha()
    spaceship_image = pygame.transform.scale(spaceship_image, (50, 50))
except:
    spaceship_image = pygame.Surface((30, 20))
    spaceship_image.fill(white)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = spaceship_image
        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.bottom = height - 10
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left >0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < width:
            self.rect.x += self.speed

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([4, 10])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        size = random.randint(20, 50)
        self.image = pygame.Surface([size,  size])
        self.image.fill([150, 150, 150])
        pygame.draw.circle(self.image, (150, 150, 150), (size//2, size//2), size//2)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed = random.randrange(1, 4)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > height:
            self.kill()

all_sprites = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

running = True
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        all_sprites.update()

        if random.randrange(100) < 3:
            asteroid = Asteroid()
            all_sprites.add(asteroid)
            asteroids.add(asteroid)

        hits = pygame.sprite.groupcollide(asteroids, bullets, True, True)
        for hit in hits:
            score += 10

        if pygame.sprite.spritecollide(player, asteroids, False):
            running = False
        
        screen.fill(black)
        all_sprites.draw(screen)

        score_text = font.render(f"Счет: {score}", True, white)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
print(f"Игра окончена! Ваш счет: {score}")