from PIL import Image


im = Image.open("david.jpg")
rgb_im = im.convert("RGB")

size = rgb_im.size
im2 = Image.new("RGB", size)

for y in range(size[1]):
    for x in range(size[0]):

        r,g,b = rgb_im.getpixel((x, y))

        ave = (r + g + b) // 3

        if ave > 125:
            im2.putpixel((x, y), (255, 255, 255, 0))
        else:
            im2.putpixel((x, y), (0, 0, 0, 0))


im2.show()
im2.save('david_binary.jpg', quality=95)

