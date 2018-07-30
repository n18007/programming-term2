from PIL import Image

im = Image.open("david.jpg")

rgb_im = im.convert("RGB")

size = rgb_im.size
im2 = Image.new("RGB", size)

for y in range(size[1]):
    for x in range(size[0]):

        r,g,b = rgb_im.getpixel((x, y))
        l = 7 

        if x == 0 or y == 0:
            pass
        elif x % l == 0 and y % l == 0:
            for yy in range(l):
                for xx in range(l):
                    im2.putpixel((x-xx, y-yy), (r, g, b, 0))

im2.show()
im2.save('david_mosaic.jpg', quality=95)

