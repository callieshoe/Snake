#Imports
import pygame
import time
import random
 
 #Setting speed
snake_speed = 15
 
#Window size
window_x = 720
window_y = 480
 
#defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
 
#Setting up pygame
pygame.init()
 
#Setting up window display
pygame.display.set_caption("Callie and Kendle's Snakes")
game_window = pygame.display.set_mode((window_x, window_y))
 
#Creating the clock
fps = pygame.time.Clock()
 
#Setting the original snake position
snake_position = [100, 50]
 
#Setting up first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
#fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
 
fruit_spawn = True
 
#setting default snake direction to right
direction = 'RIGHT'
change_to = direction
 
#Setting up score
score = 0
 
#Displaying Score
def show_score(choice, color, font, size):
   
    #Setting score font
    score_font = pygame.font.SysFont(font, size)
     
    #Display
    score_surface = score_font.render('Score : ' + str(score), True, color)
     
    #create a rectangular object for the text
    score_rect = score_surface.get_rect()
     
    #displaying text
    game_window.blit(score_surface, score_rect)
 
#Game over function
def game_over():
   
    #Setting font
    my_font = pygame.font.SysFont('times new roman', 50)
     
    #Setting game over text
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
     
    #Putting game over text in rectangle
    game_over_rect = game_over_surface.get_rect()
     
    #setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    #Putting text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    #Ending game after 2 seconds
    time.sleep(2)
     
    #Stopping pygame
    pygame.quit()
     
    #Ending the program
    quit()
 
 
#Main Function
while True:
     
    #Setting up controls
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    #When two keys are pressed 
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    #Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    #Increasing snake body when fruit is eaten
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(black)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
 
    #Game over
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
 
    #Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
 
    #Displaying the score
    show_score(1, white, 'times new roman', 20)
 
    #Updating the window
    pygame.display.update()
 
    #Refreshing screen
    fps.tick(snake_speed)