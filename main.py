import pygame as pg
import sys


def parceline(f):
    return list(map(int, f.readline()[:-1].split()))


if __name__ == "__main__":
    scale = 20.0

    filename = sys.argv[1]
    f = open(filename)
    m, n = parceline(f)

    screen = pg.display.set_mode((1280, 720))

    flat = list()
    for i in range(m):
        flat.append(parceline(f))
    print(*flat)
    y, x = parceline(f)

    view_flat = vx, vy = int(screen.get_width() * 2/3), int(screen.get_height() * 2/3)
    sf = pg.Surface((vx, vy))
    sf.fill((110, 110, 110))
    while True:
        screen.fill((140, 140, 140))
        sf.fill((110, 110, 110))
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
              if event.key == pg.K_w:
                  y -= 1
              if event.key == pg.K_s:
                  y += 1
              if event.key == pg.K_a:
                  x -= 1
              if event.key == pg.K_d:
                  x += 1
              if event.key == pg.K_SPACE:
                  flat[x][y] = 0

        if keys[pg.K_p]:
            scale += 0.1
        if keys[pg.K_o]:
            scale -= 0.1

        for i, line in enumerate(flat):
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

        pg.draw.circle(sf, (220, 0, 0), [(x + 0.5) * scale * 5, (y + 0.5) * scale * 5], scale * 2.5)

        pg.draw.polygon(screen, (80, 80, 80), [[0, 0], [vx, 0], [vx, vy], [0, vy]], 1)

        screen.blit(sf, (0, 0))

        pg.display.flip()
