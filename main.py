# pygame and sys libraries importing
import pygame as pg
import random as rand
import math
import sys
from environment import Environment


WIDTH, HEIGHT = 1280, 720
F_WIDTH, F_HEIGHT = int(sys.argv[1]), int(sys.argv[2])
env = Environment(F_WIDTH, F_HEIGHT)


if __name__ == "__main__":
    # flat render scale
    scale = min(HEIGHT / F_HEIGHT, WIDTH / F_WIDTH)
    shift = 0
    shift_y = 0

    # creating a pygame window
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

    # creating a surface for flat render
    view_flat = vx, vy = WIDTH // 4, HEIGHT
    sf = pg.Surface((vx, vy))
    sf.set_alpha(150)

    # main cycle
    while True:
        flat = pg.surfarray.make_surface(env.flat)
        flat = pg.transform.scale(flat, (int(env.width * scale), int(env.height * scale)))
        # surfaces cleaning
        screen.fill((140, 140, 140))
        sf.fill((0, 0, 0))
        
        # checking for keyboard, window, mouse inputs or events
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
              if event.key == pg.K_w:
                 env.do("up")
              if event.key == pg.K_s:
                 env.do("down")
              if event.key == pg.K_a:
                 env.do("left")
              if event.key == pg.K_d:
                 env.do("right")
              if event.key == pg.K_SPACE:
                 env.do("clean")

        # checking for scale changes
        if keys[pg.K_p]:
            scale += 5
        if keys[pg.K_o]:
            scale -= 5
        if keys[pg.K_RIGHT]:
            shift += 5
        if keys[pg.K_LEFT]:
            shift -= 5
        if keys[pg.K_DOWN]:
            shift_y += 5
        if keys[pg.K_UP]:
            shift_y -= 5

        # drawing robot
        pg.draw.circle(flat, (220, 0, 0), [(env.x + 0.5) * scale, (env.y + 0.5) * scale], scale / 2)

        screen.blit(flat, (shift, shift_y))
        # screen.blit(sf, (WIDTH - vx, 0))

        pg.display.set_caption("$$~flat-robot " + str(round(clock.get_fps(), 2)) + " ~$$")

        pg.display.flip()
        clock.tick()
