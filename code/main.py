import pygame, sys
from settings import *
from debug import debug
from level import Level

# Set window icon
Icon = pygame.image.load('icon.jpg')
pygame.display.set_icon(Icon)

class Game:
    def __init__(self):

        # genral setup
        pygame.init()
        # Create screen/surface
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # Set window name 
        pygame.display.set_caption(WINDOW_NAME)
        # Create clock
        self.clock = pygame.time.Clock()
        # Create level
        self.level = Level()

    def run(self):
        while True:
            # Event loop checks weather game is on or off
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            debug('Hey! this this shit is still working Well done!')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__': # Check if this is main file
    game = Game() # Create instance 
    game.run() # run this game 