from PIL import Image
from pytesseract import *
# pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
filename = "source3.png"
img = Image.open(filename)

result = pytesseract.image_to_string(img,lang="kor").split()

print(result)


# tesseract --list-langs

# kor.traineddata