from PIL import Image

im = Image.open("david.jpg")

rgb_im = im.convert("RGB")

size = rgb_im.size
im2 = Image.new("RGB", size)

for y in range(size[1]):
    for x in range(size[0]):

        r,g,b = rgb_im.getpixel((x, y))
        ave = (r + g + b) // 3
        im2.putpixel((x, y), (ave, ave, ave, 0))

im2.show()
im2.save('david_gray.jpg', quality=95)

