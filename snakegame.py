import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 600
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the screen
pygame.display.set_caption("Snake Game")

# Set the initial snake position
snake_x = 300
snake_y = 300

# Set the initial snake size
snake_block = 10
snake_speed = 0.2

# Set the initial direction of the snake
snake_direction = "right"

# Set the initial size of the food
food_size = 10

# Set the initial position of the food
food_x = 0
food_y = 0

# Set the initial score
score = 0

# Initialize the font
font_style = pygame.font.SysFont(None, 50)

# Function to display the score
def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, (255, 255, 255))
    screen.blit(value, [0, 0])

def game_over():
    pygame.quit()
    quit()

def new_food():
    food_x = round(random.randrange(0, screen_width - food_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - food_size) / 10.0) * 10.0
    return food_x, food_y

# Main game loop
while True:
    for event in pygame.event.get():
        # Check for quit event
        if event.type == pygame.QUIT:
            game_over()
        # check for keydown events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                snake_direction = "left"
            elif event.key == pygame.K_d:
                snake_direction = "right"
            elif event.key == pygame.K_w:
                snake_direction = "up"
            elif event.key == pygame.K_s:
                snake_direction = "down"

    # Fill the screen with a black background
    screen.fill((0, 0, 0))

    # Move the snake based on the direction
    if snake_direction == "right":
        snake_x += snake_block
    if snake_direction == "left":
        snake_x -= snake_block
    if snake_direction == "up":
        snake_y -= snake_block
    if snake_direction == "down":
        snake_y += snake_block

    # Check if the snake hits the edge of the screen
    if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
        game_over()

      # Create the snake
    pygame.draw.rect(screen, (255, 255, 255), [snake_x, snake_y, snake_block, snake_block])

    # Generate random coordinates for the food if it's not visible
    if food_x == 0 and food_y == 0:
        food_x, food_y = new_food()

    # Create the food
    pygame.draw.rect(screen, (255, 0, 0), [food_x, food_y, food_size, food_size])

    # Check if the snake hits the food
    if snake_x == food_x and snake_y == food_y:
        score += 1
        food_x = food_y = 0

    # Display the score
    Your_score(score)

    # Update the screen
    pygame.display.update()

    # Wait for a while
    time.sleep(snake_speed)
    