from math import ceil, floor
from PIL import Image

def loweri(x):
    if x in range(0, 8):
        return 0, 3
    if x in range(8, 16):
        return 8, 3
    if x in range(16, 32):
        return 16, 4
    if x in range(32, 64):
        return 32, 5
    if x in range(64, 128):
        return 64, 6
    if x in range(128, 256):
        return 128, 7

def pvd(x, y, message):
    d = abs(x - y)
    lower, t = loweri(d)
    secret = int(message[:t].zfill(8), 2)
    dd = lower + secret
    m = abs(dd - d)
    if (x >= y and dd > d):
        x_new = x + ceil(m / 2)
        y_new = y - floor(m / 2)
    elif (x < y and dd > d):
        x_new = x - floor(m / 2)
        y_new = y + ceil(m / 2)
    elif (x >= y and dd <= d):
        x_new = x - ceil(m / 2)
        y_new = y + floor(m / 2)
    elif (x < y and dd <= d):
        x_new = x + ceil(m / 2)
        y_new = y - floor(m / 2)
    return x_new, y_new, message[t:]

imgt = Image.open(r"nhatziet.jpg")
img = imgt.convert("RGB")
pixel = img.load()
nhatziet = Image.new(img.mode, img.size)
ziet = nhatziet.load()

cipher = "01100110011011000110000101100111011110110111010001101000011010010111001101011111011010010111001101011111011101000110100001100101010111110110011001101100011000010110011101111101"
cipher = cipher + "0"*8
for x in range(img.size[0]):
    for y in range(img.size[1]):
        r, g, b = pixel[x, y]
        if len(cipher) >= 0:
            red1, green1, cipher = pvd(r, g, cipher)
            green2, blue1, cipher = pvd(g, b, cipher)
            green = round((green1 + green2) / 2)
            red = red1 - (green1 - green)
            blue = blue1 - (green2 - green)
            ziet[x, y] = red, green, blue
        else:
            ziet[x, y] = r, g, b

nhatziet.save("hidden.png")