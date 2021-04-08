

import pygame
import random
from pygame.locals import *

def main():

    # xpos - x position of the upper left corner
    # ypos - y position of the upper left corner
    # xsize - pixels in width
    # ysize - pixels in height
    def draw_rect(xpos, ypos, xsize, ysize):
        pygame.draw.rect(screen, object_color, (xpos,ypos,xsize,ysize))

    def draw_centroid():
        pygame.draw.rect(screen, object_color, (SCREEN_WIDTH/2,0, 1, SCREEN_HEIGHT))

    def draw_score(xpos, ypos, score):
        if(score == 0):
            draw0(xpos, ypos)
        elif(score == 1):
            draw1(xpos, ypos)
        elif(score == 2):
            draw2(xpos, ypos)
        elif(score == 3):
            draw3(xpos, ypos)
        #pygame.draw.rect(screen, object_color, (SCREEN_WIDTH-(SCREEN_WIDTH/4),0, 1, 100))

    def draw_p2score(score):
        pygame.draw.rect(screen, object_color, (SCREEN_WIDTH/4,0, 1, 100))

    def draw_paddle1():
        pygame.draw.rect(screen, object_color, (paddle1_pos[0], paddle1_pos[1], PADDLE_SIZEX, PADDLE_SIZEY))

    def draw_paddle2():
        pygame.draw.rect(screen, object_color, (paddle2_pos[0], paddle2_pos[1], PADDLE_SIZEX, PADDLE_SIZEY))

    def random_bool():
        return random.randint(0, 1)

    def draw0(xpos, ypos):
        pygame.draw.rect(screen, object_color, (xpos, ypos, 50, 10))
        pygame.draw.rect(screen, object_color, (xpos, ypos, 10, 50))
        pygame.draw.rect(screen, object_color, (xpos, ypos+40, 50, 10))
        pygame.draw.rect(screen, object_color, (xpos+40, ypos, 10, 50))
    def draw1(xpos, ypos):
        pygame.draw.rect(screen, object_color, (xpos, ypos, 30, 10))
        pygame.draw.rect(screen, object_color, (xpos+20, ypos, 10, 50))
    def draw2(xpos, ypos):
        pygame.draw.rect(screen, object_color, (xpos, ypos, 50, 10))
        pygame.draw.rect(screen, object_color, (xpos+40, ypos, 10, 30))
        pygame.draw.rect(screen, object_color, (xpos, ypos+20, 50, 10))
        pygame.draw.rect(screen, object_color, (xpos, ypos+20, 10, 30))
        pygame.draw.rect(screen, object_color, (xpos, ypos+40, 50, 10))
    def draw3(xpos, ypos):
        pygame.draw.rect(screen, object_color, (xpos, ypos, 50, 10))
        pygame.draw.rect(screen, object_color, (xpos+40, ypos, 10, 50))
        pygame.draw.rect(screen, object_color, (xpos, ypos+20, 50, 10))
        pygame.draw.rect(screen, object_color, (xpos, ypos+40, 50, 10))

    def reset_ball_dir(ball_dir):
        if(random_bool() == 1):
            ball_dir[0] = "right"
        else:
            ball_dir[0] = "left"
        
        if(random_bool() == 1):
            ball_dir[1] = "down"
        else:
            ball_dir[1] = "up"
        print(ball_dir)


    # init pygame
    pygame.init()

    # game constants
    (SCREEN_WIDTH, SCREEN_HEIGHT) = (1024, 768)
    (PADDLE_SIZEX, PADDLE_SIZEY) = (10, 100)
    XDIRECTIONS = ("left", "right")
    YDIRECTIONS = ("up", "down")
    BALL_DEFAULT_POSITION = [(SCREEN_WIDTH/2)-5,(SCREEN_HEIGHT/2)-5]
    BALL_SPEED = 3

    # variables - colors
    background_colour = (0,0,0)  # black background color
    object_color = (255,255,255) # white object color
    score_color = (128,128,128)  # score color

    # variables - misc
    ball_size = (10,10)
    ball_pos = BALL_DEFAULT_POSITION
    paddle1_pos = (100, (SCREEN_HEIGHT/2)-50)
    paddle2_pos = (SCREEN_WIDTH-100, (SCREEN_HEIGHT/2)-50)

    # variables - ball direction
    ball_dir =  ["", ""]

    # init ball starting movement direction
    reset_ball_dir(ball_dir)

    # variables - player score (3 to win)
    p1score = 0
    p2score = 0

    #create game window
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    surface = pygame.Surface(size)
    pygame.display.set_caption('PyPong')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    screen.fill(background_colour)
    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # refresh background color
        screen.fill(background_colour)

        # top and bottom bounds detection
        if(ball_pos[1] >= (SCREEN_HEIGHT-ball_size[1])):
            if(ball_dir[1] == "down"):
                ball_dir[1] = "up"

        if(ball_pos[1] <= 0):
            if(ball_dir[1] == "up"):
                ball_dir[1] = "down"


        # update ball position
        if(ball_dir[0] == "right"):
            ball_pos[0]+=BALL_SPEED
        else:
            ball_pos[0]-=BALL_SPEED

        if(ball_dir[1] == "down"):
            ball_pos[1]+=BALL_SPEED
        else:
            ball_pos[1]-=BALL_SPEED

        # update paddle positions


        #check for goal
        if(ball_pos[0] < 0):
            p2score+=1
            ball_pos = [(SCREEN_WIDTH/2)-5,(SCREEN_HEIGHT/2)-5]
            reset_ball_dir(ball_dir)

            if(p2score > 2):
                print("P2 is the winner!")
                exit()

        if(ball_pos[0] > SCREEN_WIDTH):
            p1score+=1
            ball_pos = [(SCREEN_WIDTH/2)-5,(SCREEN_HEIGHT/2)-5]
            reset_ball_dir(ball_dir)

            if(p1score > 2):
                print("P1 is the winner!")
                exit()


        # # draw center line
        draw_centroid()

        # draw scores
        # draw p1 score
        draw_score((SCREEN_WIDTH/4)-25, 20, p1score)

        # draw p2 score
        draw_score((SCREEN_WIDTH-(SCREEN_WIDTH/4))-25, 20, p2score)


        # draw ball
        draw_rect(ball_pos[0], ball_pos[1], ball_size[0], ball_size[1])

        # draw paddles
        draw_paddle1()
        draw_paddle2()

        pygame.display.update()

main()
