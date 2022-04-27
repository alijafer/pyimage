from PIL import Image, ImageDraw, ImageFont
import textwrap
import arabic_reshaper
from bidi.algorithm import get_display

astr = u'''سلام عليكم ورحمة الله '''
unicode_text_reshaped = arabic_reshaper.reshape(astr )
unicode_text_reshaped_RTL = get_display(unicode_text_reshaped , base_dir='R')
#print(unicode_text_reshaped_RTL)
para = textwrap.wrap(unicode_text_reshaped_RTL, width=25)
#print(type(para))
MAX_W, MAX_H = 200, 500
im = Image.new('RGB', (MAX_W, MAX_H), (0, 0, 0, 0))
draw = ImageDraw.Draw(im)
font = ImageFont.truetype(
    'c:/Windows/Fonts/trado.ttf', 18)

current_h, pad = 60, 10
for line in reversed(para):
    w, h = draw.textsize(line, font=font)
    #print(line)
    draw.text(((MAX_W - w) / 2, current_h), line, font=font)
    current_h += h + pad

im.save('test.png')