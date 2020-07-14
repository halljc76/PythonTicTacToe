import pygame as pg
from path import resource_path

pg.init()

X = pg.image.load(resource_path('X.png'))
O = pg.image.load(resource_path('O.png'))
Board = pg.image.load(resource_path('Board.png'))
