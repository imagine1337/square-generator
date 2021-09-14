from PIL import Image, ImageDraw
import random
from randsquare import randsquare
w = 600
h = 400
im = Image.new('RGB', (w, h), (0, 0, 0))
draw = ImageDraw.Draw(im)
c0=randsquare()[0]
c1=randsquare()[1]
for x in range(w):
    for y in range(h):
        if x<c0[0] and x>c0[1] and y<c1[0] and y>c1[1]:
            draw.point([x,y],(255,255,255))
im.save('square.png')
