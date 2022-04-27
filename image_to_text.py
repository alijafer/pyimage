from PIL import Image
import pytesseract
import arabic_reshaper
from bidi.algorithm import get_display
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
image = 'C:/Users/ali29/pyimage/Screenshot 2022-04-27 041211.png'
text = pytesseract.image_to_string(Image.open(image), lang="ara")

with open('quotes.txt', 'w', encoding='utf-8') as f:
    f.write(text)