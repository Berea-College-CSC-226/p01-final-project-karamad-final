
import pygame
import random
from balloon_class import Balloon

# Constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, GREEN]

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Balloon Game")

# Function to draw text on the screen
def draw_text(text, x, y, color):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Main game loop
def main():
    clock = pygame.time.Clock()
    balloons = []  # Start with an empty list of balloons
    score = 0
    missed_balloons = 0
    total_balloons = 0  # Keep track of the total number of balloons that dropped
    running = False
    game_over = False
    last_balloon_time = pygame.time.get_ticks()  # Keep track of the last time a balloon was added

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if not running and not game_over:
                    if 150 <= pos[0] <= 250 and 250 <= pos[1] <= 300:
                        # Start the game
                        running = True
                        score = 0
                        missed_balloons = 0
                        total_balloons = 0
                        balloons = []
                    elif 150 <= pos[0] <= 250 and 350 <= pos[1] <= 400:
                        pygame.quit()
                        return
                elif running:
                    for balloon in balloons[:]:
                        if balloon.is_clicked(pos):
                            balloons.remove(balloon)
                            score += 1

        if not running and not game_over:
            # Draw Start and Quit buttons
            pygame.draw.rect(screen, GREEN, (150, 250, 100, 50))
            draw_text("Start", 165, 260, WHITE)
            pygame.draw.rect(screen, RED, (150, 350, 100, 50))
            draw_text("Quit", 165, 360, WHITE)
        elif game_over:
            # Game over screen
            draw_text("Game Over", 130, 200, BLACK)
            draw_text(f"Score: {score}", 150, 250, BLACK)
            if score >= 15:
                draw_text("You Won!", 140, 300, BLACK)
            else:
                draw_text("You Lost!", 140, 300, BLACK)
            draw_text("Click Start to Play Again", 70, 350, BLACK)
            pygame.draw.rect(screen, GREEN, (150, 400, 100, 50))
            draw_text("Start", 165, 410, WHITE)
        else:
            # Add 5 new balloons every second
            current_time = pygame.time.get_ticks()
            if current_time - last_balloon_time >= 1000 and total_balloons < 30:
                # Add 5 new balloons at a time
                for _ in range(5):  # Add 5 balloons each second
                    balloons.append(Balloon(random.randint(20, SCREEN_WIDTH - 20), random.randint(-100, -20), random.randint(2, 5), random.choice(COLORS)))
                    total_balloons += 1
                last_balloon_time = current_time  # Update the last balloon time

            # Update and draw balloons
            for balloon in balloons[:]:
                balloon.move()
                if balloon.y - balloon.radius > SCREEN_HEIGHT:
                    balloons.remove(balloon)
                    missed_balloons += 1

                balloon.draw(screen)

            # Check win/lose conditions
            if score >= 15:
                running = False
                game_over = True
            elif missed_balloons >= 15:
                running = False
                game_over = True

            # Display score, missed balloons, and total dropped balloons
            draw_text(f"Score: {score}", 10, 10, BLACK)
            draw_text(f"Missed: {missed_balloons}", 10, 40, BLACK)
            draw_text(f"Dropped: {total_balloons}", 10, 70, BLACK)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
