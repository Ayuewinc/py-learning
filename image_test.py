from PIL import Image
img = Image.open('./a.jpeg')
print(img.size, img.format, img.mode)
img.show()