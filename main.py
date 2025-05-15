#Imports libraries needed
import pygame
from pygame import K_RIGHT, K_KP0, MOUSEBUTTONDOWN
from sys import exit
import math
import random
import time
import asyncio


##Constants
pygame.init()
window = pygame.display.set_mode((800,400)) #Sets window size
pygame.display.set_caption('Duck Blaster')
clock = pygame.time.Clock() #Set the clock for FPS
empty = (0,0,0,0)

async def main():
    pos = pygame.mouse.get_pos()  # Get mouse position
    score = 0
    music = pygame.mixer.music.load('duckblastersmusicpygame.ogg')  # Load background music
    ducksound = pygame.mixer.Sound('quackpygame.ogg')
    endgame = pygame.mixer.Sound('gameover.ogg')
    pygame.mixer.music.play(-1)  # Play background music on loop
    hp = 100  # Set initial player health to 100
    width = window.get_width()
    height = window.get_height()
    font = pygame.font.Font("Daydream.ttf", 32)  # Set font for text
    start_time = pygame.time.get_ticks()  # Start timer
    time_elapsed = 0
    game_over_flag = False  # Flag to track game over state


    async def game_over(final_score):
        global start_time, time_elapsed
        game_over_Text = font.render("Game Over", True, (200,200,200))
        restart_text = font.render("Press RMB To Restart", True, (200,200,200))
        score_text = font.render("Score:" + str(final_score), True, (200, 200, 200))
        window.fill("black")
        window.blit(game_over_Text, (width//2 - 150, height//2 - 50))
        window.blit(restart_text, (width //2 - 295, height//2))
        window.blit(score_text, (width // 2 - 110, height // 2 - 150))
        pygame.mixer.music.set_volume(0)
        time_elapsed = final_score
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    pygame.mixer.music.set_volume(1.0)
                    await main()
                    main()
                    time1 = time0
                    start_time = pygame.time.get_ticks()
                    time_elapsed = 0
                    game_over_flag = False






    keys = pygame.key.get_pressed()

    ##Background and Player Constants
    #Handles loading of images and such.
    land = pygame.image.load('ground.png').convert_alpha()
    sky = pygame.image.load('sky.png').convert_alpha()
    man = pygame.image.load('man.png').convert_alpha()
    manrect = man.get_rect()
    manrect.midbottom = (400,300)
    crosshair = pygame.image.load('crosshairpygame3.png').convert_alpha()
    gun = pygame.image.load('gun.png').convert_alpha()
    crosshairrect = crosshair.get_rect()
    pygame.mouse.set_visible(False)

    ##Enemy constants
    #Initialize position and speed of ducks
    #Duck 1
    duck_y_pos1 = list(range(0,75))
    rand_speed1 = list(range(4,8))
    xspeed1 = random.choice(rand_speed1)

    #Duck 2
    duck_y_pos2 = list(range(0,75))
    rand_speed2 = list(range(4,8))
    xspeed2 = random.choice(rand_speed2)

    #Duck 3
    duck_y_pos3 = list(range(0,75))
    rand_speed3 = list(range(4,8))
    xspeed3 = random.choice(rand_speed3)

    #Duck 4
    duck_y_pos4 = list(range(0,75))
    rand_speed4 = list(range(6,10))
    xspeed4 = random.choice(rand_speed4)

    #Duck 1l
    duck_y_pos1l = list(range(0,75))
    rand_speed1l = list(range(6,10))
    xspeed1l = random.choice(rand_speed1l)

    #Duck 2l
    duck_y_pos2l = list(range(0,75))
    rand_speed2l = list(range(6,10))
    xspeed2l = random.choice(rand_speed2l)

    #Duck 3l
    duck_y_pos3l = list(range(0,75))
    rand_speed3l = list(range(6,10))
    xspeed3l = random.choice(rand_speed3l)

    #Duck 4l
    duck_y_pos4l = list(range(0,75))
    rand_speed4l = list(range(6,10))
    xspeed4l = random.choice(rand_speed4l)

    #Load duck images and set positions
    #Duck 1
    white_duck1 = pygame.image.load('duckpygamewhite.png').convert_alpha()
    white_duck_rect1 = white_duck1.get_rect()
    white_duck_rect1.midright = (800, random.choice(duck_y_pos1))

    #Duck 2
    white_duck2 = pygame.image.load('duckpygamewhite.png').convert_alpha()
    white_duck_rect2 = white_duck2.get_rect()
    white_duck_rect2.midright = (800, random.choice(duck_y_pos2))

    #Duck 3
    white_duck3 = pygame.image.load('duckpygamewhite.png').convert_alpha()
    white_duck_rect3 = white_duck3.get_rect()
    white_duck_rect3.midright = (800, random.choice(duck_y_pos3))

    #Duck 4
    gold_duck = pygame.image.load('duckpygamegold.png').convert_alpha()
    gold_duck_rect = gold_duck.get_rect()
    gold_duck_rect.midright = (800, random.choice(duck_y_pos4))

    #Duck 1l
    white_duck1l = pygame.image.load('duckpygamewhiteflip.png').convert_alpha()
    white_duck_rect1l = white_duck1l.get_rect()
    white_duck_rect1l.midleft = (-25, random.choice(duck_y_pos1l))

    #Duck 2l
    white_duck2l = pygame.image.load('duckpygamewhiteflip.png').convert_alpha()
    white_duck_rect2l = white_duck2l.get_rect()
    white_duck_rect2l.midleft = (-25, random.choice(duck_y_pos2l))

    #Duck 3l
    white_duck3l = pygame.image.load('duckpygamewhiteflip.png').convert_alpha()
    white_duck_rect3l = white_duck3l.get_rect()
    white_duck_rect3l.midleft = (-25, random.choice(duck_y_pos3l))

    #Duck 4
    gold_duck4l = pygame.image.load('pygamegoldduckflip.png').convert_alpha()
    gold_duck_rect4l = gold_duck4l.get_rect()
    gold_duck_rect4l.midleft = (-25, random.choice(duck_y_pos4l))

    # Start positions and intervals for ducks

    start_point = list(range(4000,5000))
    start_point2 = [-1000, -1500, -2000, -2500, -3000, -3500, -4000, -4500, -5000]
    gold_start_point = [-5000, -6000, -7000, -8000, -9000, -10000]

    time_interval = [-1000, -1500, -2000, -2500, -3000, -3500, -4000, -4500, -5000]
    time_interval2 = list(range(4000,5000))
    gold_time_interval2 = 7500


    ##Main Game Loop

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() #Quit game on window close
                exit()
        window.blit(land,(0,300))
        window.blit(sky, (0, 0))
        if not game_over_flag:
            time1 = pygame.time.get_ticks()
            time_elapsed = (time1 - start_time) // 1000 # Calculate elapsed time in seconds
        score = font.render(str(time_elapsed), True, (0,0,0)) # Render score
        window.blit(score, (70, 300)) #Display score
        await asyncio.sleep(0)

        ## Duck game logic (movement and collision)
        # Update and move ducks, check for collisions, play sounds, and update health points
        #Duck 1
        if white_duck_rect1.right <= random.choice(time_interval):
            white_duck_rect1.left = 800
            white_duck_rect1.centery = random.choice(duck_y_pos1)
            xspeed1 = random.choice(rand_speed1)
        white_duck_rect1.x = white_duck_rect1.x - xspeed1
        window.blit(white_duck1, (white_duck_rect1.x, white_duck_rect1.centery))
        if white_duck_rect1.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True:
                ducksound.play()
                white_duck_rect1.left = random.choice(start_point)
        if white_duck_rect1.collidepoint(-5,random.choice(duck_y_pos1)):
            hp -=1


        #Duck 2
        if white_duck_rect2.right <= random.choice(time_interval):
            white_duck_rect2.left = 800
            white_duck_rect2.centery = random.choice(duck_y_pos2)
            xspeed2 = random.choice(rand_speed2)
        white_duck_rect2.x = white_duck_rect2.x - xspeed2
        window.blit(white_duck2, (white_duck_rect2.x, white_duck_rect2.centery))
        if white_duck_rect2.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True:
                ducksound.play()
                white_duck_rect2.left = random.choice(start_point)
        if white_duck_rect2.collidepoint(-5,random.choice(duck_y_pos2)):
            hp -=1

        #Duck 3
        if white_duck_rect3.right <= random.choice(time_interval):
            white_duck_rect3.left = 800
            white_duck_rect3.centery = random.choice(duck_y_pos3)
            xspeed3 = random.choice(rand_speed3)
        white_duck_rect3.x = white_duck_rect3.x - xspeed3
        window.blit(white_duck3, (white_duck_rect3.x, white_duck_rect3.centery))
        if white_duck_rect3.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True:
                ducksound.play()
                white_duck_rect3.left = random.choice(start_point)
        if white_duck_rect3.collidepoint(-5,random.choice(duck_y_pos3)):
            hp -=1

        #Duck 4
        if gold_duck_rect.right <= -10000:
            gold_duck_rect.left = 800
            gold_duck_rect.centery = random.choice(duck_y_pos4)
            xspeed4 = random.choice(rand_speed4)
        gold_duck_rect.x = gold_duck_rect.x - xspeed4
        window.blit(gold_duck, (gold_duck_rect.x, gold_duck_rect.centery))
        if gold_duck_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True:
                ducksound.play()
                gold_duck_rect.left = random.choice(start_point)
        if gold_duck_rect.collidepoint(-5,random.choice(duck_y_pos4)):
            hp -=2

        #Duck 1l
        if white_duck_rect1l.x >= random.choice(time_interval2):
            white_duck_rect1l.x = -25
            white_duck_rect1l.centery = random.choice(duck_y_pos1l)
            xspeed1l = random.choice(rand_speed1l)
        white_duck_rect1l.x = white_duck_rect1l.x - xspeed1l
        window.blit(white_duck1l, (white_duck_rect1l.x, white_duck_rect1l.centery))
        if white_duck_rect1l.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True:
                ducksound.play()
                white_duck_rect1l.left = random.choice(start_point2)
        if white_duck_rect1l.collidepoint(825,random.choice(duck_y_pos1l)):
            hp -=1

        #Duck 2l
        if white_duck_rect2l.x >= random.choice(time_interval2):
            white_duck_rect2l.x = -25
            white_duck_rect2l.centery = random.choice(duck_y_pos2l)
            xspeed2l = random.choice(rand_speed2l)
        white_duck_rect2l.x = white_duck_rect2l.x + xspeed2l
        window.blit(white_duck2l, (white_duck_rect2l.x, white_duck_rect2l.centery))
        if white_duck_rect2l.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True:
                ducksound.play()
                white_duck_rect2l.left = random.choice(start_point2)
        if white_duck_rect2l.collidepoint(825,random.choice(duck_y_pos2l)):
            hp -=1

        #Duck 3l
        if white_duck_rect3l.x >= random.choice(time_interval2):
            white_duck_rect3l.x = -25
            white_duck_rect3l.centery = random.choice(duck_y_pos3l)
            xspeed3l = random.choice(rand_speed3l)
        white_duck_rect3l.x = white_duck_rect3l.x + xspeed3l
        window.blit(white_duck3l, (white_duck_rect3l.x, white_duck_rect3l.centery))
        if white_duck_rect3l.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True:
                ducksound.play()
                white_duck_rect3l.left = random.choice(start_point2)
        if white_duck_rect3l.collidepoint(825,random.choice(duck_y_pos3l)):
            hp -=1

        #Duck 4l
        if gold_duck_rect4l.x >= gold_time_interval2:
            gold_duck_rect4l.x = 0
            gold_duck_rect4l.centery = random.choice(duck_y_pos4l)
            xspeed4l = random.choice(rand_speed4l)
        gold_duck_rect4l.x = gold_duck_rect4l.x + xspeed4l
        window.blit(gold_duck4l, (gold_duck_rect4l.x, gold_duck_rect4l.centery))
        if gold_duck_rect4l.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True:
                ducksound.play()
                gold_duck_rect4l.left = random.choice(gold_start_point)
        if gold_duck_rect4l.collidepoint(825,random.choice(duck_y_pos4l)):
            hp -=2

        for i in range(len(start_point)):
           start_point[i] += 1
        if start_point[0] >= -1000:
         for i in range(len(start_point)):
             start_point[i] -= 500
        if start_point[8] >= -1000:
           for i in range(len(start_point)):
             start_point[i] -= 500

        for i in range(len(time_interval)):
           time_interval[i] += 1
        if time_interval[0] >= -1000:
         for i in range(len(time_interval)):
             time_interval[i] -= 500
        if time_interval[8] >= -1000:
           for i in range(len(time_interval)):
             time_interval[i] -= 500

        for i in range(len(time_interval2)):
            time_interval2[i] -= 1
        if time_interval2[0] <= 1000 :
            for i in range(len(time_interval2)):
                time_interval2[i] += 1000
        if time_interval2[999] <= 1000:
            for i in range(len(time_interval2)):
                time_interval2[i] += 1000

        gold_time_interval2 -= 0.5
        if gold_time_interval2 <= 1000:
            gold_time_interval2 += 1000




        ### Player game logic (display character, gun, crosshair)
        window.blit(crosshair, (pos[0] - 75, pos[1] - 75))
        window.blit(man, manrect)
        angle = 360 - math.atan2(pos[1] - 300, pos[0] - 400) * 180 / math.pi #Common technique for converting radians to angle, not written or developed by us. Credit to conorbuck on github.
        rotigun = pygame.transform.rotate(gun, angle)
        rotigunrect = rotigun.get_rect(center=(425, 275))
        window.blit(rotigun, rotigunrect)
        score = 0
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(window, "red", (30, 350, 100, 25))
        pygame.draw.rect(window, "green", (30,350,hp,25))

        if hp <= 0:
            game_over_flag = True
            await game_over(time_elapsed)









        pygame.display.update() #Constantly update display
        clock.tick(90) #Set FPS

# Start the game
asyncio.run(main())





