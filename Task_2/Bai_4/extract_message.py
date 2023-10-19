def loweri(x):
    if (x in range(0,8)):
        return 0, 3
    if  x in range(8,16):
        return 8, 3
    if (x in range(16,32)):
        return 16, 4
    if (x in range(32,64)):
        return 32, 5
    if (x in range(64,128)):
        return 64, 6
    if (x in range(128,256)):
        return 128, 7

def un_pvd(x,y,flag):
    d = abs(x - y)
    lower,t = loweri(d)
    m = d - lower
    flag = flag + bin(m)[2:].zfill(8)[-t:]
    return flag


from math import*
from PIL import Image
imgt = Image.open(r"hidden.png")
img = imgt.convert("RGB")
pixel = img.load()
nhatziet = Image.new(img.mode, img.size)
ziet = nhatziet.load()

flag = ""

for x in range(img.size[0]):
    for y in range(img.size[1]):
        r, g, b = pixel[x, y]
        if not flag.endswith('0'*8):
            flag = un_pvd(r,g,flag)
            flag = un_pvd(g,b,flag)
print(flag[:-8])