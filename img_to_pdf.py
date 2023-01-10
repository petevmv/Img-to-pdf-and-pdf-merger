from PIL import Image
import os

img_list = []
for file in os.listdir(os.curdir):
    if file.endswith(".png"):
        image = Image.open(file)
        im = image.convert("RGB")
        im.save(f'{file}.pdf')
