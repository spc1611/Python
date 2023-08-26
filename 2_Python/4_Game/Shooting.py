import pygame
import os           # Anytime I wanna access another file in python
import random

pygame.init()

# Game  Configuration
screen_w = 480 
screen_h = 640
screen = pygame.display.set_mode((screen_w, screen_h))          # Write width first

game_path = os.path.dirname(__file__)           # Anytime I wanna access another file in python

# Background 
background = pygame.image.load(f"{game_path}/Images/background.png")

# Character
char = pygame.image.load(f"{game_path}/Images/character.png")
char_size = char.get_rect().size # [30, 30]
char_w = char_size[0]
char_h = char_size[1]
char_x = screen_w/2 - char_w/2        # for character to be in the middle
char_y = screen_h/2 - char_h/2

char_to_x = 0;
char_to_y = 0;
char_speed = 0.6;

# Bullets
bullet = pygame.image.load(f"{game_path}/Images/bullet.png")
bullet_size = bullet.get_rect().size 
bullet_w = bullet_size[0]
bullet_h = bullet_size[1]

bullets = []

bullet_speed = 5

# Enemies
enemy = pygame.image.load(f"{game_path}/Images/enemy_1.png")
enemy_size = enemy.get_rect().size 

enemy_img = [
    pygame.image.load(f"{game_path}/Images/enemy_1.png"),
    pygame.image.load(f"{game_path}/Images/enemy_2.png"),
    pygame.image.load(f"{game_path}/Images/enemy_3.png")
]

enemies = []

enemy_speed = random.randint(1, 2)

enemies.append({
    "pos_x" : random.randint(0, screen_w - enemy_size[0]),
    "pos_y" : 0, 
    "img_idx" : 0, 
    "to_x" : enemy_speed + random.randint(-2, 0), 
    "to_y" : enemy_speed + random.randint(0, 2),
})

enemies.append({
    "pos_x" : random.randint(0, screen_w - enemy_size[0]),
    "pos_y" : 0, 
    "img_idx" : 0, 
    "to_x" : enemy_speed + random.randint(0, 2), 
    "to_y" : enemy_speed + random.randint(0, 2),
})

bullet_remove = -1
enemy_remove = -1




# FPS : Frame per second
clock = pygame.time.Clock()

game_font = pygame.font.Font(None, 40)
total_time = 30 #5
start_ticks = pygame.time.get_ticks()

# Running Game 
running = True 
while running: 
    frame = clock.tick(60)

    for event in pygame.event.get():            # Event = any movement/key pressing, etc.
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:        # KEYDOWN = Prssing any keys 
            if event.key == pygame.K_UP: 
                char_to_y -= char_speed
            elif event.key == pygame.K_DOWN:
                char_to_y += char_speed 
            elif event.key == pygame.K_LEFT:
                char_to_x -= char_speed 
            elif event.key == pygame.K_RIGHT:
                char_to_x += char_speed 
            elif event.key == pygame.K_SPACE:          # Bullet
                bullets.append([char_x + char_w/2 - bullet_w/2, char_y])


        if event.type == pygame.KEYUP:            # KEYUP = Not pressing any keys  
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                char_to_y = 0;
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                char_to_x = 0;

    # Character Move
    char_x += char_to_x * frame
    char_y += char_to_y * frame

    if char_x < 0:
        char_x = 0
    elif char_x > screen_w - char_w:
        char_x = screen_w - char_w
    
    if char_y < 0:
        char_y = 0
    elif char_y > screen_h - char_h:
        char_y = screen_h - char_h

    # Bullet Move
    bullets = [[b_pos[0], b_pos[1] - bullet_speed ]for b_pos in bullets]
    bullets = [[b_pos[0], b_pos[1]]for b_pos in bullets if b_pos[1] < screen_h]

    # Enemy Move 
    for enemy in enemies:
        enemy_x = enemy["pos_x"]
        enemy_y = enemy["pos_y"]
        enemy_img_idx = enemy["img_idx"]
        enemy_size = enemy_img[enemy_img_idx].get_rect().size

        if enemy_x < 0 or enemy_x > screen_w - enemy_size[0]:
            enemy["to_x"] *= -1
        if enemy_y < 0 or enemy_y > screen_h - enemy_size[1]:
            enemy["to_y"] *= -1

        enemy["pos_x"] += enemy["to_x"]
        enemy["pos_y"] += enemy["to_y"]

    # Character Hitbox
    char_hit = char.get_rect()          # get_rectangle
    char_hit.left = char_x
    char_hit.top = char_y

    # Enemy Hitbox
    for e_idx, e_val in enumerate(enemies):
        enemy_x = e_val["pos_x"]
        enemy_y = e_val["pos_y"]
        e_img_idx = e_val["img_idx"]

        e_hit = enemy_img[e_img_idx].get_rect()
        e_hit.left = enemy_x
        e_hit.top = enemy_y

        # Enemy vs Character
        if char_hit.colliderect(e_hit):
            game_result = "GAME OVER ^^ "
            running = False
            break

        # Bullets Hitbox
        for b_idx, b_val in enumerate(bullets):
            b_x = b_val[0]
            b_y = b_val[1]

            bullet_hit = bullet.get_rect()
            bullet_hit.left = b_x
            bullet_hit.top = b_y

            # Check collision with Enemies
            if bullet_hit.colliderect(e_hit):
                bullet_remove = b_idx
                enemy_remove = e_idx

                # Change enemy status
                if e_img_idx < 2 :
                    enemy_w = e_hit.size[0]    
                    enemy_h = e_hit.size[1]
                    next_enemy_hit = enemy_img[e_img_idx + 1].get_rect()
                    next_enemy_w = next_enemy_hit.size[0]
                    next_enemy_h = next_enemy_hit.size[1]

                    enemy_speed *= 1.5

                    # Enemy change
                    enemies.append({
                        "pos_x" : enemy_x,
                        "pos_y" : enemy_y, 
                        "img_idx" : e_img_idx + 1, 
                        "to_x" : enemy_speed + random.randint(-2, 0), 
                        "to_y" : enemy_speed,
                    })

                    enemies.append({
                        "pos_x" : enemy_x + next_enemy_w,
                        "pos_y" : enemy_y, 
                        "img_idx" : e_img_idx + 1, 
                        "to_x" : enemy_speed + random.randint(0, 2), 
                        "to_y" : enemy_speed,
                    })
                break
        else:
            continue
        break

    if bullet_remove > -1:
        del bullets[bullet_remove]
        bullet_remove = -1          # For error check

    if enemy_remove > -1:
        del enemies[enemy_remove]
        enemy_remove = -1 
    
    if len(enemies) == 0:
        game_result = "CLEAR!!"
        running = False



    # Rendering
    screen.blit(background, (0,0))              # blit = rendering or drawing on canvas
    screen.blit(char, (char_x, char_y))         # Drawing of chararcter must be after background. It will be covered by the background if it is drawn first.

    for b_x, b_y in bullets:        # Bullet in loop, since it is continuous
        screen.blit(bullet, (b_x,b_y))
    
    for val in enemies:
        enemy_x = val["pos_x"]
        enemy_y = val["pos_y"]
        enemy_img_idx = val["img_idx"]
        screen.blit(enemy_img[enemy_img_idx], (enemy_x, enemy_y))

    # Timer
    past_time = (pygame.time.get_ticks() - start_ticks)/1000
    timer = game_font.render(str(round((total_time - past_time), 2)), True, (255, 255, 255))
    screen.blit(timer, (10,10))

    if total_time - past_time < 0 :
        game_result = "TIME OUT! >:D"
        running = False
    
    pygame.display.update()

# MSG
msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(center = (int(screen_w/2), int(screen_h/2))) # Msg_rect = message rectangle
screen.blit(msg, msg_rect)
pygame.display.update()

pygame.time.delay(1000)
pygame.quit()
