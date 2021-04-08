

import pygame
import random
from pygame.locals import *

def main():

    def draw_rect(xpos, ypos, xsize, ysize):
        pygame.draw.rect(screen, object_color, (xpos,ypos,xsize,ysize))

    def draw_centroid():
        pygame.draw.rect(screen, object_color, (SCREEN_WIDTH/2,0, 1, SCREEN_HEIGHT))

    def draw_score(xpos, ypos, score):
        if score == 0:
            draw0(xpos, ypos)
        elif score == 1:
            draw1(xpos, ypos)
        elif score == 2:
            draw2(xpos, ypos)
        elif score == 3:
            draw3(xpos, ypos)

    def draw_p2score(score):
        pygame.draw.rect(screen, object_color, (SCREEN_WIDTH/4,0, 1, 100))

    def draw_paddle(xpos, ypos):
        pygame.draw.rect(screen, object_color, (xpos, ypos, PADDLE_SIZEX, PADDLE_SIZEY))

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
        if random_bool() == 1:
            ball_dir[0] = "right"
        else:
            ball_dir[0] = "left"
        if random_bool() == 1:
            ball_dir[1] = "down"
        else:
            ball_dir[1] = "up"
        print(ball_dir)

    def is_paddle_over_bounds(paddle_y):
        return paddle_y >= 0

    def is_paddle_under_bounds(paddle_y):
        return paddle_y <= (SCREEN_HEIGHT-PADDLE_HEIGHT)

    def is_ball_colliding_with_paddle(ball_xpos, ball_ypos, paddle_xpos, paddle_ypos):
        #return abs(paddle_xpos - ball_xpos) < 10 and abs(paddle_ypos - ball_ypos) < 100
        return abs(paddle_xpos - ball_xpos) < 10 and abs(ball_ypos- paddle_ypos) < 100 

    # init pygame
    pygame.init()

    # game constants
    (SCREEN_WIDTH, SCREEN_HEIGHT) = (1024, 768)
    (PADDLE_SIZEX, PADDLE_SIZEY) = (10, 100)
    XDIRECTIONS = ("left", "right")
    YDIRECTIONS = ("up", "down")
    BALL_DEFAULT_POSITION = [(SCREEN_WIDTH/2)-5,(SCREEN_HEIGHT/2)-5]
    BALL_SPEED = 3
    PADDLE1_SPEED = 3
    PADDLE2_SPEED = 3
    PADDLE_HEIGHT = 100

    # variables - colors
    background_colour = (0,0,0)  # black background color
    object_color = (255,255,255) # white object color
    score_color = (128,128,128)  # score color

    # variables - misc
    ball_size = (10,10)
    ball_pos = BALL_DEFAULT_POSITION
    paddle1_pos = [PADDLE_HEIGHT, (SCREEN_HEIGHT/2)-(PADDLE_HEIGHT/2)]
    paddle2_pos = [SCREEN_WIDTH-PADDLE_HEIGHT, (SCREEN_HEIGHT/2)-(PADDLE_HEIGHT/2)]

    # variables - controle
    p1_moveup = False
    p1_movedown = False
    p2_moveup = False
    p2_movedown = False

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    p2_moveup = True;
                if event.key == pygame.K_DOWN:
                    p2_movedown = True
                if event.key == ord('w'):
                    p1_moveup = True
                if event.key == ord('s'):
                    p1_movedown = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    p2_moveup = False
                if event.key == pygame.K_DOWN:
                    p2_movedown = False
                if event.key == ord('w'):
                    p1_moveup = False
                if event.key == ord('s'):
                    p1_movedown = False


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
        if p1_moveup:
            if is_paddle_over_bounds(paddle1_pos[1]):
                paddle1_pos[1] -= PADDLE1_SPEED
        if p1_movedown:
            if is_paddle_under_bounds(paddle1_pos[1]):
                paddle1_pos[1] += PADDLE1_SPEED
        if p2_moveup:
            if is_paddle_over_bounds(paddle2_pos[1]):
                paddle2_pos[1] -= PADDLE2_SPEED
        if p2_movedown:
            if is_paddle_under_bounds(paddle2_pos[1]):
                paddle2_pos[1] += PADDLE2_SPEED

        # paddle 1 collision detection
        if is_ball_colliding_with_paddle(ball_pos[0], ball_pos[1], paddle1_pos[0], paddle1_pos[1]):
            if ball_dir[0] == "right":
                ball_dir[0] = "left"
            if ball_dir[0] == "left":
                ball_dir[0] = "right"

        # paddle 2 collision detection
        if is_ball_colliding_with_paddle(ball_pos[0], ball_pos[1], paddle2_pos[0], paddle2_pos[1]):
            if ball_dir[0] == "left":
                ball_dir[0] = "right"
            if ball_dir[0] == "right":
                ball_dir[0] = "left"

        #check for goal
        if ball_pos[0] < 0:
            p2score+=1
            ball_pos = [(SCREEN_WIDTH/2)-5,(SCREEN_HEIGHT/2)-5]
            reset_ball_dir(ball_dir)

            if p2score > 2:
                print("P2 is the winner!")
                exit()

        if ball_pos[0] > SCREEN_WIDTH:
            p1score+=1
            ball_pos = [(SCREEN_WIDTH/2)-5,(SCREEN_HEIGHT/2)-5]
            reset_ball_dir(ball_dir)

            if p1score > 2:
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
        #draw paddle 1
        draw_paddle(paddle1_pos[0], paddle1_pos[1])

        #draw paddle 2
        draw_paddle(paddle2_pos[0], paddle2_pos[1])

        # redraw screen
        pygame.display.update()

main()
