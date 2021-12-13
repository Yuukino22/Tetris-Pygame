# Yifeng Xiong
# 14648645
# Include three functions
# Draw surface, lines on the surface, and jewels in the surface
from faller import Faller
from jewel import Jewel
from gamestate import GameState
import pygame
SURFACE_WIDTH = 500
SURFACE_HEIGHT = 640
SURFACE_COLOR = pygame.Color(31, 133, 222)
GAME_BACKGROUND_COLOR = pygame.Color(255, 255, 255)
GAME_BACKGROUND_TOPLEFT_FRAC_X = 0.26
GAME_BACKGROUND_TOPLEFT_FRAC_Y = 0.09375
GAME_BACKGROUND_WIDTH_FRAC_X = 0.48
GAME_BACKGROUND_HEIGHT_FRAC_Y = 0.8125

def draw_surface(surface):
    '''
    draw the basic background
    '''
    width = surface.get_width()
    height = surface.get_height()
    surface.fill(SURFACE_COLOR)
    
    pygame.draw.rect(surface,
                     GAME_BACKGROUND_COLOR,
                     [GAME_BACKGROUND_TOPLEFT_FRAC_X * width,
                      GAME_BACKGROUND_TOPLEFT_FRAC_Y * height,
                      GAME_BACKGROUND_WIDTH_FRAC_X * width,
                      GAME_BACKGROUND_HEIGHT_FRAC_Y * height])

def draw_table(surface):
    '''
    draw a 6*13 table
    '''
    width = surface.get_width()
    height = surface.get_height()
    for col in range(6):
        for row in range(13):
            rec_topleft_frac_x = GAME_BACKGROUND_TOPLEFT_FRAC_X + col * 0.08
            rec_topleft_frac_y = GAME_BACKGROUND_TOPLEFT_FRAC_Y + row * 0.0625
            rec_width_frac_x = 0.08
            rec_height_frac_y = 0.0625

            rec_topleft_pixel_x = rec_topleft_frac_x * width
            rec_topleft_pixel_y = rec_topleft_frac_y * height
            rec_width_pixel_x = rec_width_frac_x * width
            rec_height_pixel_y = rec_height_frac_y * height
            
            pygame.draw.rect(surface,
                             pygame.Color(0, 0, 0),
                             [rec_topleft_pixel_x,
                              rec_topleft_pixel_y,
                              rec_width_pixel_x,
                              rec_height_pixel_y],
                             2)

def draw_rectangle(surface, gamestate: GameState):
    '''
    fill colors of the table draw above
    white if there is no jewel at that position
    jewel's color if there is a jewel
    '''
    width = surface.get_width()
    height = surface.get_height()
    for col in range(gamestate.col()):
        for row in range(gamestate.row()):
            rec_topleft_frac_x = GAME_BACKGROUND_TOPLEFT_FRAC_X + col * 0.08
            rec_topleft_frac_y = GAME_BACKGROUND_TOPLEFT_FRAC_Y + row * 0.0625
            rec_width_frac_x = 0.08
            rec_height_frac_y = 0.0625

            rec_topleft_pixel_x = rec_topleft_frac_x * width
            rec_topleft_pixel_y = rec_topleft_frac_y * height
            rec_width_pixel_x = rec_width_frac_x * width
            rec_height_pixel_y = rec_height_frac_y * height
    
            if type(gamestate.board()[col][row]) == Jewel:
                pygame.draw.rect(surface,
                                 gamestate.board()[col][row].color(),
                                 [rec_topleft_pixel_x,
                                  rec_topleft_pixel_y,
                                  rec_width_pixel_x,
                                  rec_height_pixel_y])
            else:
                pygame.draw.rect(surface,
                                 GAME_BACKGROUND_COLOR,
                                 [rec_topleft_pixel_x,
                                  rec_topleft_pixel_y,
                                  rec_width_pixel_x,
                                  rec_height_pixel_y])
    
