import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
running = True
dt = 0
i = 1
j = 1
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2,)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    screen.fill("Blue")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # Automoving ball
    player_pos.x += i * (200 * dt)
    player_pos.y += j * (200 * dt)
    if player_pos.x < 40:
        i = 1
    if player_pos.x > screen.get_width()-39:
        i = -1
    if player_pos.y < 40:
        j = 1
    if player_pos.y > screen.get_height()-39:
        j = -1
    pygame.display.flip()
    dt = clock.tick(60) / 1000
