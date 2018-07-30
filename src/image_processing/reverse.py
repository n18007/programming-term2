from PIL import Image

def rev(a):
    return 255 - a

im = Image.open("david.jpg")
rgb_im = im.convert("RGB")

size = rgb_im.size
im2 = Image.new("RGB", size)

for y in range(size[1]):
    for x in range(size[0]):

        r,g,b = rgb_im.getpixel((x, y))
        #r = 255 - r
        #g = 255 - g
        #b = 255 - b

        im2.putpixel((x, y), (rev(r), rev(g), rev(b), 0))

im2.show()
im2.save('david_reverse.jpg', quality=95)

