import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
BALL_RADIUS = 20
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
FPS = 60
PADDLE_SPEED = 5
BALL_SPEED = 5

# Set up some colors
BLUE = (135,206,235)
WHITE=(255,255,255)
BLACK = (0, 0, 0)
PURPLE = (160,32,240)
PINK = (255,192,203)  # Cyan

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Set up the clock
clock = pygame.time.Clock()

# Set up the ball
ball_x = WIDTH / 2
ball_y = HEIGHT / 2
ball_dx = BALL_SPEED
ball_dy = BALL_SPEED

# Set up the paddles
paddle1_y = HEIGHT / 2
paddle2_y = HEIGHT / 2

# Set up button
button_width = 200
button_height = 50
button_x = WIDTH / 2 - button_width / 2
button_y = HEIGHT / 2 - button_height / 2
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

def reset_game():
    global ball_x, ball_y, ball_dx, ball_dy
    ball_x = WIDTH / 2
    ball_y = HEIGHT / 2
    ball_dx = BALL_SPEED
    ball_dy = BALL_SPEED

# Game loop
game_over = False
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("Restarting...")
                game_over = False
                reset_game()

    # Move the paddles
    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_w] and paddle1_y - PADDLE_HEIGHT / 2 > 0:
            paddle1_y -= PADDLE_SPEED
        if keys[pygame.K_s] and paddle1_y + PADDLE_HEIGHT / 2 < HEIGHT:
            paddle1_y += PADDLE_SPEED
        if keys[pygame.K_UP] and paddle2_y - PADDLE_HEIGHT / 2 > 0:
            paddle2_y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and paddle2_y + PADDLE_HEIGHT / 2 < HEIGHT:
            paddle2_y += PADDLE_SPEED

        # Move the ball
        ball_x += ball_dx
        ball_y += ball_dy

        # Bounce the ball off the walls
        if ball_y - BALL_RADIUS < 0 or ball_y + BALL_RADIUS > HEIGHT:
            ball_dy *= -1

        # Bounce the ball off the paddles
        if ball_x - BALL_RADIUS < PADDLE_WIDTH and paddle1_y - PADDLE_HEIGHT / 2 < ball_y < paddle1_y + PADDLE_HEIGHT / 2:
            ball_dx *= -1
        if ball_x + BALL_RADIUS > WIDTH - PADDLE_WIDTH and paddle2_y - PADDLE_HEIGHT / 2 < ball_y < paddle2_y + PADDLE_HEIGHT / 2:
            ball_dx *= -1

        # Check if the ball goes out of bounds
        if ball_x < 0 or ball_x > WIDTH:
            print("You lost. Restarting...")
            game_over = True

    # Draw everything
    screen.fill(PINK)
    pygame.draw.rect(screen, BLUE, (0, paddle1_y - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, BLUE, (WIDTH - PADDLE_WIDTH, paddle2_y - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(screen, BLUE, (int(ball_x), int(ball_y)), BALL_RADIUS)

    if game_over:
        # Draw restart button
        pygame.draw.rect(screen,PURPLE, button_rect)
        font = pygame.font.Font(None, 36)
        text = font.render("Restart", True, WHITE)
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

