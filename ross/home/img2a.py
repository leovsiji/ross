from PIL import Image


def imgtoa(image_file, mode="normal"):

    if mode == "normal":
        ASCII = "@0%#*+=-:."
    else:
        ASCII = ".:-=+*#%0@"

    img = Image.open(image_file)
    img = img.convert("L")
    img = img.resize((100, 50))

    pixels = img.getdata()

    ascii_img = ""

    for i, pixel in enumerate(pixels):
        ascii_img += ASCII[pixel * len(ASCII) // 256]

        if (i + 1) % img.width == 0:
            ascii_img += "\n"

    return ascii_img