import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("catch the ball game")
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
basket_width = 100
basket_height = 15
basket_x = WIDTH//2
basket_y = HEIGHT-40
basket_speed = 7
ball_x=random.randint(0,WIDTH)
ball_y=0
ball_radius=10
ball_speed=5
score=0
font= pygame.font.SysFont(None,35)
clock=pygame.time.Clock()
running=True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket_x -=basket_speed
    if keys[pygame.K_RIGHT]:
        basket_x +=basket_speed
    ball_y += ball_speed

    if(basket_y < ball_y + ball_radius < basket_y + basket_height) and (basket_x < ball_x <basket_x +basket_width):
        score+=1
        ball_y=0
        ball_x = random.randint(0,WIDTH)
    

    if ball_y > HEIGHT:
        print("Game Over")
        running = False
    pygame.draw.rect(screen, BLUE, (basket_x, basket_y, basket_width, basket_height))
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    score__text=font.render("Score" +str(score),True,(0,0,0))
    screen.blit(score__text,(10,10))

    pygame.display.update()
    clock.tick(60)
pygame.quit()


