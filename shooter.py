import pygame
import os

pygame.init()

# Game window variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

# Game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooter")

# Set framerate
clock = pygame.time.Clock()
FPS = 60

# Define game variables
GRAVITY = 0.75

# Define player action variables
moving_left = False
moving_right = False

# Define colours
BG = (144, 201, 120)
RED = (255, 0, 0)


# Define background
def draw_bg():
    screen.fill(BG)
    pygame.draw.line(screen, RED, (0, 300), (SCREEN_WIDTH, 300))


# Soldier sprite class
class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        # 1 means right
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.in_air = True
        # Flip direction
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        # Load all images for the players
        animation_types = ["Idle", "Run", "Jump"]
        for animation in animation_types:
            # Reset temporary list of images
            temp_list = []
            # Count number of files in the folder
            num_of_frames = len(os.listdir(f"img/{self.char_type}/{animation}"))
            for i in range(num_of_frames):
                img = pygame.image.load(f"img/{self.char_type}/{animation}/{i}.png")
                img = pygame.transform.scale(
                    img, (int(img.get_width() * scale), int(img.get_height() * scale))
                )
                temp_list.append(img)
            self.animation_list.append(temp_list)
        self.img = self.animation_list[self.action][self.frame_index]
        self.rect = self.img.get_rect()
        self.rect.center = (x, y)

    def move(self, moving_left, moving_right):
        # Reset movement variables
        dx = 0
        dy = 0
        # Assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        # Jump
        if self.jump == True and self.in_air == False:
            self.vel_y = -11
            self.jump = False
            self.in_air = True
        # Apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y
        # Check collision with floor
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.in_air = False
        # Update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    # Update animation
    def update_animation(self):
        # Cool down in ms
        ANIMATION_COOLDOWN = 100
        # Update image depending on current frame
        self.img = self.animation_list[self.action][self.frame_index]
        # Check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # If the animation has run out the reset back to start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        # Check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # Update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    # Draw player onto screen
    def draw(self):
        screen.blit(pygame.transform.flip(self.img, self.flip, False), self.rect)


# Soldiers
player = Soldier("player", 200, 200, 3, 5)
enemy = Soldier("enemy", 400, 200, 3, 5)

# Window loop
run = True
while run:
    # Set clock tick
    clock.tick(FPS)

    draw_bg()

    # Draw player | Set movement | Set animation
    player.update_animation()
    player.draw()
    enemy.draw()

    # Update player actions
    if player.alive:
        if player.in_air:
            # 2: jump
            player.update_action(2)
        elif moving_left or moving_right:
            # 1: run
            player.update_action(1)
        else:
            # 0: idle
            player.update_action(0)
        player.move(moving_left, moving_right)

    # Event handler
    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            run = False
        # Keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_SPACE and player.alive:
                player.jump = True
            if event.key == pygame.K_ESCAPE:
                run = False
        # Keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False

    # Update game window
    pygame.display.update()

pygame.quit()
