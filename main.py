import pygame as p
print(p.ver) #poggers

WHITE = (255, 255, 255)
GRAY = (182, 128, 128)
print("test")
width = height = 500
SIZE = (width, height)
square_size = width // 8
screen = p.display.set.mode(SIZE)
while running:
    for evnt in p.event.get():
        if evnt.type == p.QUIT:
            running = False
