# Timer Clock Version 1.0.0.2
#Change:
#1. add 50 minites option and break time is 10 minutes
#2. Change the behavior for, notification with the new feature.



import pygame
import time
import math

pygame.init()
screen = pygame.display.set_mode((500, 600))

GREY = (120, 120, 120)
WHITE = (255, 255, 255)
WHITE1 = (100, 255, 100)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


total_secs = 0
total = 0
count_pomodoro_day = 0
start = False
break_time = 0

count_pomodoro25_day = 0
count_pomodoro50_day = 0
select_time25 = 0
select_time50 = 0


# Font:
# 01: Create Font
font = pygame.font.SysFont('san', 50)
text_1 = font.render('+m', True, BLACK)
text_2 = font.render('+s', True, BLACK)
text_3 = font.render('-m', True, BLACK)
text_4 = font.render('-s', True, BLACK)
text_5 = font.render('Start', True, BLACK)
text_6 = font.render('Reset', True, BLACK)
text_70 = font.render('25 min', True, BLACK)
text_71 = font.render('50 min', True, BLACK)
text_8 = font.render('BREAK TIME 5 MINUTES', True, GREEN)





# 02 Create text
# 03 Display test on the screen

# Add sound
sound = pygame.mixer.Sound('Alarm.wav')

sound_tick_tock = pygame.mixer.Sound('Clock-sound-tick-tock2.wav')
sound_tick_tock.set_volume(0.1) #Version 1.0.0.1
    
clock = pygame.time.Clock() #blink 60 times per second
while True:
    clock.tick(60) #blink 60 times per second

    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.fill(GREY)
        

    # Draw rectangel and circle
    pygame.draw.rect(screen, WHITE, (100, 50, 50, 50)) # + minute
    if (100 < mouse_x < 150) and (50 < mouse_y < 100):
        pygame.draw.rect(screen, WHITE1, (100, 50, 50, 50))

    pygame.draw.rect(screen, WHITE, (200, 50, 50, 50)) # + second
    if (200 < mouse_x < 250) and (50 < mouse_y < 100): # - second
        pygame.draw.rect(screen, WHITE1, (200, 50, 50, 50))

    
    pygame.draw.rect(screen, WHITE, (100, 200, 50, 50)) # - minute
    if (100 < mouse_x < 150) and (200 < mouse_y < 250): # - minute
        pygame.draw.rect(screen, WHITE1, (100, 200, 50, 50))

    pygame.draw.rect(screen, WHITE, (200, 200, 50, 50)) # - second
    if (200 < mouse_x < 250) and (200 < mouse_y < 250): # - second
        pygame.draw.rect(screen, WHITE1, (200, 200, 50, 50))

    pygame.draw.rect(screen, WHITE, (300, 50, 150, 50)) # Start
    if (300 < mouse_x < 450) and (50 < mouse_y < 100): # Start 
        pygame.draw.rect(screen, WHITE1, (300, 50, 150, 50))

    pygame.draw.rect(screen, WHITE, (300, 200, 150, 50)) # Reset
    if (300 < mouse_x < 450) and (200 < mouse_y < 250): # Reset
        pygame.draw.rect(screen, WHITE1, (300, 200, 150, 50))

    pygame.draw.rect(screen, WHITE, (10, 5, 120, 40)) # 25 minute
    if (10 < mouse_x < 130) and (5 < mouse_y < 45):
        pygame.draw.rect(screen, WHITE1, (10, 5, 120, 40))

    pygame.draw.rect(screen, WHITE, (140, 5, 120, 40)) # 50 minute
    if (140 < mouse_x < 260) and (5 < mouse_y < 45):
        pygame.draw.rect(screen, WHITE1, (140, 5, 120, 40))




    # Display texts
    screen.blit(text_1, (100, 50))
    screen.blit(text_2, (200, 50))
    screen.blit(text_3, (100, 200))
    screen.blit(text_4, (200, 200))
    screen.blit(text_5, (300, 50))
    screen.blit(text_6, (300, 200))

    screen.blit(text_70, (15, 5))
    screen.blit(text_71, (150, 5))
    #Draw cirle
    pygame.draw.circle(screen, BLACK, (250, 400), 100)
    pygame.draw.circle(screen, WHITE, (250, 400), 95)
    pygame.draw.circle(screen, BLACK, (250, 400), 5)

    #Draw line
    # pygame.draw.line(screen, BLACK, (250, 400),(250, 310))


    #Long Rectangle
    pygame.draw.rect(screen, BLACK, (50, 520, 400, 50))
    pygame.draw.rect(screen, WHITE, (60, 530, 380, 30))



    # Press to Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        #Press mounse on the area
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if (10 < mouse_x < 130) and (5 < mouse_y < 45): # mouse move to 25 minutes
                    print("press + 25minute")
                    total_secs = 25 * 60
                    total = total_secs
                    select_time25 = 1
                    select_time50 = 0
                    text_8 = font.render('BREAK TIME 5 MINUTES', True, GREEN)

                if (140 < mouse_x < 260) and (5 < mouse_y < 45): # mouse move to 50 minutes
                    print("press + 50minute")
                    total_secs = 50 * 60
                    total = total_secs
                    select_time25 = 0
                    select_time50 = 1
                    text_8 = font.render('BREAK TIME 10 MINUTES', True, GREEN)

                if (100 < mouse_x < 150) and (50 < mouse_y < 100): # mouse move to + minute
                    print("press +minute")
                    total_secs += 60
                    total = total_secs

                if (200 < mouse_x < 250) and (50 < mouse_y < 100): # mouse move to - second
                    print("press +second")
                    total_secs += 1
                    total = total_secs

            
                if (100 < mouse_x < 150) and (200 < mouse_y < 250): # mouse move to - minute
                    print("press -minutes")
                    total_secs -= 60
                    total = total_secs
                
                
                if (200 < mouse_x < 250) and (200 < mouse_y < 250): # mouse move to - second
                    print("press -second")
                    total_secs -= 1
                    total = total_secs

            
                if (300 < mouse_x < 450) and (50 < mouse_y < 100): # mouse move to Start
                    print("press Start")
                    start = True
                    total = total_secs

                
                if (300 < mouse_x < 450) and (200 < mouse_y < 250): # mouse move to Reset
                    print("press Reset")
                    total_secs = 0
                    total = total_secs
                    start = False
                    count_pomodoro25_day = 0
                    count_pomodoro50_day = 0
                





    if start:
        total_secs -= 1
        pygame.mixer.Sound.play(sound_tick_tock)

        #Version 1.0.0.1
        time.sleep(1)
        if total_secs == 0 and break_time == 0:
            pygame.mixer.Sound.play(sound)
            break_time = 1

            if select_time25 == 1:
                total_secs = 300
            if select_time50 == 1:
                total_secs = 600

            total = total_secs
         
            

        if total_secs == 0 and break_time == 1:
            pygame.mixer.Sound.play(sound)
            break_time = 0
            total_secs = 0
            start = False
            if select_time25 == 1:
                count_pomodoro25_day += 1
            if select_time50 == 1:
                count_pomodoro50_day += 1

            # count_pomodoro_day += 1

        if total_secs != 0 and break_time == 1:
            screen.blit(text_8, (50, 395))
            

        if total_secs < 0:
            total_secs = 0
            
    
       
    if total != 0:
        pygame.draw.rect(screen, RED, (60, 530, int(380 * (total_secs/total)), 30))

        


    mins = int(total_secs/60)
    secs = total_secs - mins*60

    time_now = str(mins) + " : " + str(secs)
    time_now_text = font.render(time_now, True, BLACK)
    screen.blit(time_now_text, (120,120))
    # total_second_text = font.render(str(total_secs), True, BLACK)
    # screen.blit(total_second_text, (120,120))



    # Line secs
    x_sec = 250 + 90 * math.cos(6 * secs * math.pi/180)
    y_sec = 400 - 90 * math.sin(6 * secs * math.pi/180)
    pygame.draw.line(screen, BLACK, (250, 400), (x_sec, y_sec))


    # Line mins
    x_min = 250 + 60 * math.cos(6 * mins * math.pi/180)
    y_min = 400 - 60 * math.sin(6 * mins * math.pi/180)
    pygame.draw.line(screen, RED, (250, 400), (x_min, y_min))

    # RED RECTANGLE
   


    


    font10 = pygame.font.SysFont(str(count_pomodoro_day), 50)
    text_90 = font10.render('P25: ' + str(count_pomodoro25_day), True, GREEN)
    screen.blit(text_90, (200, 350))

    font11 = pygame.font.SysFont(str(count_pomodoro_day), 50)
    text_91 = font11.render('P50: ' + str(count_pomodoro50_day), True, GREEN)
    screen.blit(text_91, (200, 430))



        #display all things that you write
    pygame.display.flip()


pygame.quit()


    #Build file exe
    # pyinstaller count_down_clock.py --onefile --noconsole

