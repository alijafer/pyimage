# Importing the PIL library
import arabic_reshaper
from bidi.algorithm import get_display
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import locale
locale.getpreferredencoding(False)
# Open an Image
img = Image.open('gfg-660x249.png')
 
# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)
 
# Custom font style and font size
myFont = ImageFont.truetype('c:/Windows/Fonts/trado.ttf', 65)
atext = u"علِي جعفِر"
unicode_text_reshaped = arabic_reshaper.reshape(atext )
unicode_text_reshaped_RTL = get_display(unicode_text_reshaped , base_dir='R')
I1.multiline_text((10,10), unicode_text_reshaped_RTL, font=myFont ,fill =(255, 0, 0))
# Add Text to an image
#I1.text((100, 10),unicode_text_reshaped_RTL , font=myFont ,fill =(255, 0, 0))
 
# Display edited image
img.show()
 
# Save the edited image
img.save("car2.png")