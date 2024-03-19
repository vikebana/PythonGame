import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
running = True
gravity = 0.25
pinkVelocity = 0
dt = 0
i = 1
j = 1
#dogCode #Womeninstem
pink = pygame.image.load('pink.png')
imageSize = (100,100)
pinkScaled = pygame.transform.scale(pink,imageSize)
pinkRect = pinkScaled.get_rect()
pinkRect.center = (screen.get_width() / 2, screen.get_height() / 2)
pygame.display.set_caption("pinks big adventure", 'pink.png')

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    screen.fill("Pink")
    screen.blit(pinkScaled,pinkRect)
    pinkVelocity += gravity
    pinkRect.y += pinkVelocity

    if pinkRect.y > screen.get_width() - 300:
        pinkRect.y = screen.get_width() - 300
        pinkVelocity = 0

    if keys[pygame.K_w]:
        pinkRect.y -= 300 * dt
    if keys[pygame.K_s]:
        pinkRect.y += 300 * dt
    if keys[pygame.K_a]:
        pinkRect.x -= 300 * dt
    if keys[pygame.K_d]:
        pinkRect.x += 300 * dt



    # Automoving code
    #pinkRect.x += i * (200 * dt)
    pinkRect.y += j * (200 * dt)
    if pinkRect.x < 0:
        i = 1
    if pinkRect.x > screen.get_width()-100:
        i = -1
    if pinkRect.y < 0:
        j = 1
    if pinkRect.y > screen.get_height()-100:
        j = -1

    pygame.display.flip()
    dt = clock.tick(60) / 1000
