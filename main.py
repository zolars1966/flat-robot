#  main.py
#  
#  Copyright 2021 User TGZolars
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# pygame and sys libraries importing
import pygame as pg
import random as rand
import sys
from environment import Environment


F_WIDTH, F_HEIGHT = int(sys.argv[1]), int(sys.argv[2])
env = Environment(F_WIDTH, F_HEIGHT)


if __name__ == "__main__":
    # flat render scale
    scale = 75 / (max(F_WIDTH, F_HEIGHT))

    # creating a pygame window
    screen = pg.display.set_mode((1280, 720))

    # creating a surface for flat render
    view_flat = vx, vy = int(screen.get_width() * 2/3), int(screen.get_height() * 2/3)
    sf = pg.Surface((vx, vy))
    sf.fill((110, 110, 110))

    # main cycle
    while True:
        # surfaces cleaning
        screen.fill((140, 140, 140))
        sf.fill((110, 110, 110))
        
        # checking for keyboard, window, mouse inputs or events
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
              pass
              # robot's controls
              #if event.key == pg.K_w:
              #    y -= 1
              #if event.key == pg.K_s:
              #    y += 1
              #if event.key == pg.K_a:
              #    x -= 1
              #if event.key == pg.K_d:
              #    x += 1
              #if event.key == pg.K_SPACE:
              #    flat[x][y] = 0

        # checking for scale changes
        if keys[pg.K_p]:
            scale += 0.1
        if keys[pg.K_o]:
            scale -= 0.1

        # drawing flat
        for i, line in enumerate(env.flat):
            for j, quad in enumerate(line):
                if not quad:
                    pg.draw.polygon(sf, (255, 255, 255), [[min(vx, i * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, (j + 1) * scale * 5)],
                                                          [min(vx, i * scale * 5), min(vy, (j + 1) * scale * 5)]])
                    pg.draw.polygon(sf, (127, 127, 127), [[min(vx, i * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, (j + 1) * scale * 5)],
                                                          [min(vx, i * scale * 5), min(vy, (j + 1) * scale * 5)]], 1)
                else:
                    pg.draw.polygon(sf, (160, 160, 160), [[min(vx, i * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, (j + 1) * scale * 5)],
                                                          [min(vx, i * scale * 5), min(vy, (j + 1) * scale * 5)]])
                    pg.draw.polygon(sf, (127, 127, 127), [[min(vx, i * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, j * scale * 5)],
                                                          [min(vx, (i + 1) * scale * 5), min(vy, (j + 1) * scale * 5)],
                                                          [min(vx, i * scale * 5), min(vy, (j + 1) * scale * 5)]], 1)

        # drawing robot
        pg.draw.circle(sf, (220, 0, 0), [(env.r_x + 0.5) * scale * 5, (env.r_y + 0.5) * scale * 5], scale * 2.5)

        pg.draw.polygon(screen, (80, 80, 80), [[0, 0], [vx, 0], [vx, vy], [0, vy]], 1)

        screen.blit(sf, (0, 0))

        pg.display.flip()
