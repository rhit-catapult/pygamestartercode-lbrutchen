import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

# done: Create a Ball class.



def main():
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('blue'))
    clock = pygame.time.Clock()

    # done: Create an instance of the Ball class called ball1
    ball1=Ball(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # done: Move the ball
        # done: Draw the ball
        ball1.draw()
        ball1.move()
        pygame.display.update()
class Ball:
    def __init__(self, screen):
        self.screen=screen
        self.x=random.randint(1,20)
        self.y=random.randint(1,20)
        self.x_speed = random.randint(2,3 )
        self.circle_color =(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.circle_radius = random.randint(1,10)
        self.y_speed = random.randint(2, 3)
    def draw(self):
        pygame.draw.circle(self.screen, self.circle_color, (self.x,self.y),self.circle_radius)

    def move(self):

        self.y=self.y_speed+self.y
        self.x=self.x_speed+self.x
        if self.x<2:
            self.x_speed=self.x_speed*-1
        if self.x>self.screen.get_width()+2:
            self.x_speed=self.x_speed*-1
        if self.y<2:
            self.y_speed=self.y_speed*-1
        if self.y>self.screen.get_height()+2:
            self.y_speed=self.y_speed*-1


# done: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move

main()

# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
