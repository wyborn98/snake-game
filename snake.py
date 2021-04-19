import pygame
import time

pygame.init()

dis_width = 1024
dis_height = 720

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

#Colors
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 102)

#Snake
x_snake = dis_width / 2
y_snake = dis_height / 2
x_dir = 0
y_dir = 0
snake_speed = 30
snake_block = 10
clock = pygame.time.Clock()

game_over = False

while not game_over:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_dir = -snake_block
                y_dir = 0
            if event.key == pygame.K_RIGHT:
                x_dir = snake_block
                y_dir = 0    
            if event.key == pygame.K_UP:
                y_dir = -snake_block
                x_dir = 0
            if event.key == pygame.K_DOWN:
                y_dir = snake_block
                x_dir = 0

    x_snake = x_snake + x_dir
    y_snake = y_snake + y_dir
    dis.fill(black)
    pygame.draw.rect(dis, blue, [x_snake, y_snake, snake_block, snake_block])
    pygame.display.update()   

    clock.tick(snake_speed)   

pygame.quit()


quit()