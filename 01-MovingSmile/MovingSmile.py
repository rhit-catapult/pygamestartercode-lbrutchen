import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption("Moving Smile")
    screen = pygame.display.set_mode((640, 480))
    x=0
    y=0
    clock=pygame.time.Clock()
    while True:
        # TODO 4: Set the clock speed to 60 fps
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO 3: Make the eye pupils move with Up, Down, Left, and Right keys

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            y = y - 1
        if pressed_keys[pygame.K_DOWN]:
            y=y+1
        if pressed_keys[pygame.K_RIGHT]:
            x=x+1
        if pressed_keys[pygame.K_LEFT]:
            x=x-1
            #hi
            #a
        screen.fill((225, 225, 225))

        # API --> pygame.draw.circle(screen, color, (x, y), radius, thickness)
        # API --> pygame.draw.rect(screen, color, (x,y), radius, thickness)
        pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)  # yellow circle
        pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)  # black outline

        pygame.draw.circle(screen, (225, 225, 225), (240, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (242+x, 162+y), 7)  # black pupil

        pygame.draw.circle(screen, (225, 225, 225), (400, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (398+x, 162+y), 7)  # black pupil
        pygame.draw.circle(screen,(80,0,0),(320,245), 10 )#nose
        pygame.draw.rect(screen, (0,0,0),(230,320,180,30))#mouth
        # TODO 1: Draw a nose
        # Suggestion: color (80,0,0) location (320,245), radius 10
        # API --> pygame.draw.circle(screen, (r,g,b), (x, y), radius, thickness)

        # TODO 2: Draw a mouth
        # Suggestion: color (0,0,0), x 230, y 320, width 180, height 30
        # API --> pygame.draw.rect(screen, (r,g,b), (x, y, width, height), thickness)

        pygame.display.update()


main()
