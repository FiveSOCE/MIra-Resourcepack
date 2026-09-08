#!/usr/bin/env python3
"""Generate the permanent Mira Pyro Axe pixel texture without external dependencies."""
from pathlib import Path
import struct
import zlib

SIZE = 64
OUT = Path("assets/mira/textures/item/pyro_axe.png")

pixels = [(0, 0, 0, 0)] * (SIZE * SIZE)

def put(x, y, rgba):
    if 0 <= x < SIZE and 0 <= y < SIZE:
        pixels[y * SIZE + x] = rgba

def line(x0, y0, x1, y1, rgba, width=1):
    dx = abs(x1 - x0)
    sx = 1 if x0 < x1 else -1
    dy = -abs(y1 - y0)
    sy = 1 if y0 < y1 else -1
    err = dx + dy
    while True:
        for ox in range(-(width // 2), width // 2 + 1):
            for oy in range(-(width // 2), width // 2 + 1):
                put(x0 + ox, y0 + oy, rgba)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy

def polygon(points, rgba):
    min_y = max(0, min(y for _, y in points))
    max_y = min(SIZE - 1, max(y for _, y in points))
    for y in range(min_y, max_y + 1):
        nodes = []
        j = len(points) - 1
        for i in range(len(points)):
            xi, yi = points[i]
            xj, yj = points[j]
            if (yi < y <= yj) or (yj < y <= yi):
                if yj != yi:
                    x = int(xi + (y - yi) * (xj - xi) / (yj - yi))
                    nodes.append(x)
            j = i
        nodes.sort()
        for k in range(0, len(nodes) - 1, 2):
            for x in range(nodes[k], nodes[k + 1] + 1):
                put(x, y, rgba)

# Palette: blackened steel, hot forged edges, ember core.
STEEL_DARK = (28, 24, 27, 255)
STEEL = (55, 50, 54, 255)
STEEL_LIGHT = (93, 83, 82, 255)
EDGE_RED = (163, 38, 14, 255)
EMBER = (239, 68, 18, 255)
FIRE = (255, 145, 28, 255)
HOT = (255, 224, 102, 255)
HANDLE = (36, 26, 24, 255)
WRAP = (72, 43, 32, 255)
BRONZE = (126, 73, 33, 255)

# Long reinforced haft.
polygon([(29,24),(34,24),(35,57),(32,62),(28,57)], HANDLE)
polygon([(30,28),(33,28),(34,55),(31,59),(29,55)], WRAP)
for y in range(31, 55, 5):
    line(29, y, 34, y + 3, BRONZE, 1)
line(28, 57, 32, 62, STEEL_DARK, 2)
line(35, 57, 32, 62, STEEL_DARK, 2)
put(32, 59, EMBER)
put(32, 60, FIRE)

# Central infernal head.
polygon([(27,16),(32,10),(37,16),(36,27),(28,27)], STEEL_DARK)
polygon([(29,17),(32,13),(35,17),(34,25),(30,25)], STEEL)
polygon([(31,16),(33,16),(34,22),(32,25),(30,22)], EDGE_RED)
put(32,18,HOT); put(32,19,FIRE); put(31,20,EMBER); put(33,20,EMBER)

# Left blade silhouette.
left = [(28,17),(23,12),(16,8),(7,7),(12,12),(5,18),(13,18),(7,26),(17,23),(24,20),(28,22)]
polygon(left, STEEL_DARK)
polygon([(25,16),(21,13),(15,10),(10,9),(14,13),(8,17),(15,16),(10,22),(17,20),(23,18)], STEEL)
# Left cutting edge / flames.
line(8,7,16,8,EDGE_RED,2)
line(8,8,13,13,FIRE,1)
line(5,18,13,18,EMBER,2)
line(7,26,17,23,EDGE_RED,2)
line(9,24,15,19,FIRE,1)
put(12,10,HOT); put(9,17,FIRE); put(11,22,EMBER)

# Right blade silhouette, mirrored.
right = [(36,17),(41,12),(48,8),(57,7),(52,12),(59,18),(51,18),(57,26),(47,23),(40,20),(36,22)]
polygon(right, STEEL_DARK)
polygon([(39,16),(43,13),(49,10),(54,9),(50,13),(56,17),(49,16),(54,22),(47,20),(41,18)], STEEL)
line(56,7,48,8,EDGE_RED,2)
line(56,8,51,13,FIRE,1)
line(59,18,51,18,EMBER,2)
line(57,26,47,23,EDGE_RED,2)
line(55,24,49,19,FIRE,1)
put(52,10,HOT); put(55,17,FIRE); put(53,22,EMBER)

# Steel highlights and glowing cracks.
for x0,y0,x1,y1 in [
    (18,11,23,15),(14,16,20,17),(16,21,22,19),
    (46,11,41,15),(50,16,44,17),(48,21,42,19)
]:
    line(x0,y0,x1,y1,STEEL_LIGHT,1)
for x0,y0,x1,y1 in [
    (17,9,18,13),(18,13,16,15),(22,14,20,18),(14,19,12,22),
    (47,9,46,13),(46,13,48,15),(42,14,44,18),(50,19,52,22)
]:
    line(x0,y0,x1,y1,EMBER,1)

# Head spikes / crown.
polygon([(29,13),(27,8),(31,10),(32,3),(34,10),(38,8),(35,14)], STEEL_DARK)
line(32,4,32,11,FIRE,1)
put(32,3,HOT)

def write_png(path):
    raw = bytearray()
    for y in range(SIZE):
        raw.append(0)
        for x in range(SIZE):
            raw.extend(pixels[y * SIZE + x])
    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xffffffff)
    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", struct.pack(">IIBBBBB", SIZE, SIZE, 8, 6, 0, 0, 0))
    png += chunk(b"IDAT", zlib.compress(bytes(raw), 9))
    png += chunk(b"IEND", b"")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(png)

write_png(OUT)
print(f"Wrote {OUT}")
