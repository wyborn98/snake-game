import pygame
import time
import random

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

snake_speed = 30
snake_block = 10
clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25) 

def message(msg, color):
    message = font_style.render(msg, True, color)
    dis.blit(message, [dis_width/3.5, dis_height/2.25])
    
    pygame.display.update()

def gameLoop():
    
    game_over = False
    game_close = False

    x_snake = dis_width / 2
    y_snake = dis_height / 2
    x_dir = 0
    y_dir = 0

    food_x = (random.randrange(0, dis_width - snake_block) / 10) * 10
    food_y = (random.randrange(0, dis_height - snake_block) / 10) * 10

    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("You Lose! Press Q-Quit or P-Play again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

                    if event.key == pygame.K_p:
                        gameLoop()

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

        if x_snake >= dis_width or x_snake < 0 or y_snake >= dis_height or y_snake < 0:
            game_close = True

        x_snake = x_snake + x_dir
        y_snake = y_snake + y_dir
        dis.fill(black)
        pygame.draw.rect(dis, green, [food_x, food_y, snake_block, snake_block])
        pygame.draw.rect(dis, blue, [x_snake, y_snake, snake_block, snake_block])
        pygame.display.update()   

        clock.tick(snake_speed)   

    pygame.quit()

    quit()

gameLoop()