import pygame
import os

# Grid and block settings
GRID_WIDTH = 320    
GRID_HEIGHT = 200
BLOCK_SIZE = 4
WINDOW_WIDTH = GRID_WIDTH * BLOCK_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * BLOCK_SIZE

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player settings
player_x = GRID_WIDTH // 2
player_y = GRID_HEIGHT - 5
player_width = 7

# Load alien sprites
alien_sprites = []
for i in range(8):
    img = pygame.image.load(f'images/sprites/alien_{i}.png')
    img = pygame.transform.scale(img, (5 * BLOCK_SIZE * 3, 4 * BLOCK_SIZE * 3))
    alien_sprites.append(img)

alien_width = alien_sprites[0].get_width()
alien_height = alien_sprites[0].get_height()

# Invader settings - multiple aliens
invaders = []
ALIEN_ROWS = 6
ALIENS_PER_ROW = 10
ALIEN_SPACING_X = 24
ALIEN_SPACING_Y = 16
ALIEN_START_X = 5
ALIEN_START_Y = 10
alien_dir = 1
alien_speed = 1

def init_invaders():
    inv = []
    for row in range(ALIEN_ROWS):
        for col in range(ALIENS_PER_ROW):
            inv.append({
                'x': ALIEN_START_X + col * ALIEN_SPACING_X,
                'y': ALIEN_START_Y + row * ALIEN_SPACING_Y,
                'alive': True,
                'sprite_idx': row
            })
    return inv

invaders = init_invaders()

# Bullet settings
BULLET_LIMIT = 25
bullets = []
bullet_speed = 2

# Shooting auto-repeat settings
SHOOT_DELAY = 40
shoot_timer = 0

# Score
score = 0
font = None

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders - Multiple Aliens")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)

# Load background image
background = pygame.image.load('images/background2.png')
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    # Player movement
    keys = pygame.key.get_pressed()
    PLAYER_SPEED = 3
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_x < GRID_WIDTH - player_width:
        player_x += PLAYER_SPEED

    # Shooting
    if keys[pygame.K_SPACE]:
        shoot_timer += dt
        if shoot_timer >= SHOOT_DELAY and len(bullets) < BULLET_LIMIT:
            bullets.append({
                'x': player_x + player_width // 2,
                'y': player_y - 1
            })
            shoot_timer = 0
    else:
        shoot_timer = SHOOT_DELAY

    # Invader movement
    move_down = False
    for inv in invaders:
        if inv['alive']:
            if inv['x'] <= 0 or inv['x'] >= GRID_WIDTH - alien_width // BLOCK_SIZE:
                move_down = True
                break
    
    if move_down:
        alien_dir *= -1
        for inv in invaders:
            if inv['alive']:
                inv['y'] += 4

    for inv in invaders:
        if inv['alive']:
            inv['x'] += alien_dir * alien_speed

    # Check if aliens reached bottom or touched player
    for inv in invaders:
        if inv['alive']:
            alien_bottom = inv['y'] + alien_height // BLOCK_SIZE
            alien_right = inv['x'] + alien_width // BLOCK_SIZE
            # Check collision with player
            if (alien_bottom >= player_y and 
                inv['x'] < player_x + player_width and 
                alien_right > player_x):
                running = False
            elif alien_bottom >= GRID_HEIGHT:
                score -= 100
                invaders = init_invaders()
                alien_speed = 1
                break

    # Bullet movement and collision
    for bullet in bullets[:]:
        bullet['y'] -= bullet_speed
        if bullet['y'] < 0:
            bullets.remove(bullet)
            continue
        
        for inv in invaders:
            if inv['alive']:
                grid_x = inv['x']
                grid_y = inv['y']
                if (grid_y <= bullet['y'] <= grid_y + alien_height // BLOCK_SIZE and
                    grid_x <= bullet['x'] <= grid_x + alien_width // BLOCK_SIZE):
                    inv['alive'] = False
                    bullets.remove(bullet)
                    score += 10
                    break

    # Check if all aliens are dead
    if all(not inv['alive'] for inv in invaders):
        alien_speed += 1
        invaders = init_invaders()

    # Draw everything - background replaces black fill
    screen.blit(background, (0, 0))
    
    # Draw
    for i in range(player_width):
        rect = pygame.Rect((player_x + i) * BLOCK_SIZE, player_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, GREEN, rect)
    
    # Draw invaders
    for inv in invaders:
        if inv['alive']:
            sprite = alien_sprites[inv['sprite_idx']]
            screen.blit(sprite, (inv['x'] * BLOCK_SIZE, inv['y'] * BLOCK_SIZE))
    
    # Draw bullets
    for bullet in bullets:
        rect = pygame.Rect(bullet['x'] * BLOCK_SIZE, bullet['y'] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, RED, rect)

    # Draw score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Draw score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
