from PIL import Image

def rev(a):
    return 255 - a

im = Image.open("david.jpg")

rgb_im = im.convert("RGB")

size = rgb_im.size

for y in range(size[1]):
    for x in range(size[0]):

        r,g,b = rgb_im.getpixel((x, y))

        ave = (r + g + b) // 3

        # white
        if ave > 125:
            print("+", end="")
        #black
        else:
            print(" ", end="")

    print("")

