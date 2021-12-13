# Yifeng Xiong
# 14648645
# This is the main class for columes game
# Include create new game, handle input, draw the surface of the game


from faller import Faller
from jewel import Jewel
from gamestate import GameState
import pygame
import graphic
import random


SURFACE_WIDTH = 500
SURFACE_HEIGHT = 640
SURFACE_COLOR = pygame.Color(31, 133, 222)
GAME_BACKGROUND_COLOR = pygame.Color(255, 255, 255)
GAME_BACKGROUND_TOPLEFT_FRAC_X = 0.26
GAME_BACKGROUND_TOPLEFT_FRAC_Y = 0.09375
GAME_BACKGROUND_WIDTH_FRAC_X = 0.48
GAME_BACKGROUND_HEIGHT_FRAC_Y = 0.8125
RED = pygame.Color(255, 0, 0)
ORANGE = pygame.Color(255, 150 ,0)
YELLOW = pygame.Color(255, 255, 0)
GREEN = pygame.Color(0, 255, 0)
CYAN = pygame.Color(0, 255, 255)
BLUE = pygame.Color(0, 0, 255)
PURPLE = pygame.Color(255, 0, 255)
DESCEND = pygame.USEREVENT + 1


class ColumesGame:

    def __init__(self):
        self._running = True
        self._gamestate = GameState(13, 6)
        self._gamestate.new_game()

    def run(self):
        '''
        main function of the class
        create new game
        create a clock
        draw the surface
        handle events
        handle keys input
        '''
        pygame.init()
        clock = pygame.time.Clock()
        surface = pygame.display.set_mode((SURFACE_WIDTH,SURFACE_HEIGHT), pygame.RESIZABLE)
        graphic.draw_surface(surface)
        graphic.draw_table(surface)
        pygame.display.flip()
        pygame.time.set_timer(DESCEND, 1000)
        while self._running:
            clock.tick(30)
            self._handle_events()
            if self._gamestate.faller() == None:
                faller = self._create_faller()
                self._gamestate.add_faller(faller)
            elif self._gamestate.game_status() == 'landing':
                self._freezing()
                if self._gamestate.game_over() == True:
                    self._running = False
                self._gamestate.reset_faller()
            else:
                if self._gamestate.check('landing'):
                    self._gamestate.landing()
                if self._handle_keys():
                    self._handle_events()
            self._redraw()
            pygame.display.flip()
        pygame.quit()
        
    def _handle_events(self):
        '''
        quit game 
        change size
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._end_game()
            elif event.type == pygame.VIDEORESIZE:
                self._resize_surface(event.size)
            elif event.type == DESCEND:
                self._descend()
                

    def _handle_keys(self) -> bool:
        '''
        press left: move faller left
        press right: move faller right
        press space: rotate faller
        '''
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self._left()
            self._freezing()
            return True
        if keys[pygame.K_RIGHT]:
            self._right()
            self._freezing
            return True
        if keys[pygame.K_SPACE]:
            self._rotate()
            return True
        return False


    def _end_game(self):
        self._running = False

    def _resize_surface(self, size: (int, int)):
        pygame.display.set_mode(size, pygame.RESIZABLE)

    def _redraw(self):
        '''
        redraw surface
        draw jewels
        draw black lines to make a table
        '''
        surface = pygame.display.get_surface()
        graphic.draw_surface(surface)
        self._draw_jewels()
        graphic.draw_table(surface)

        pygame.display.flip()

    def _right(self):
        '''
        check whether can move right or not
        move the faller right
        '''
        if self._gamestate.check('right') == True:
            self._gamestate.right_and_landing()
            if self._gamestate.check('descend') == True:
                self._gamestate.change_status('falling')

    def _left(self):
        '''
        check whether can move left or not
        move the faller left
        '''
        if self._gamestate.check('left') == True:
            self._gamestate.left_and_landing()
            if self._gamestate.check('descend') == True:
                self._gamestate.change_status('falling')

    def _descend(self):
        '''
        check whether can descend or not
        faller descennd
        '''
        if self._gamestate.check('descend') == True:
            self._gamestate.descend_and_landing()
            
    def _freezing(self):
        '''
        if the faller is landing and nothing do on the faller
        faller freeze
        '''
        if self._gamestate.game_status() == 'landing':
            self._gamestate.freezing()
            

    def _rotate(self):
        self._gamestate.rotate()
        

    def _draw_jewels(self):
        '''
        for all jewels in the gamestate
        draw them
        '''
        surface = pygame.display.get_surface()
        graphic.draw_rectangle(surface, self._gamestate)

    def _create_faller(self) -> Faller:
        '''
        find out three different color
        find out a random colume
        create a faller
        '''
        color_1 = self._random_color()
        while True:
            color_2 = self._random_color()
            if color_2 != color_1:
                break
        while True:
            color_3 = self._random_color()
            if color_3 != color_2 and color_3 != color_1:
                break
        return Faller(random.choice([0, 1, 2, 3, 4, 5]),
                                      color_1,
                                      color_2,
                                      color_3)
        
    def _random_color(self) -> str:
        '''
        return a random color
        '''
        return random.choice([RED,
                       ORANGE,
                       YELLOW,
                       GREEN,
                       CYAN,
                       BLUE,
                       PURPLE])

if __name__ == '__main__':
    ColumesGame().run()
