from PIL import Image

img = Image.open('source.png')
area = (0,0,100,100)
cropped_img = img.crop(area)

img.show()
cropped_img.show()