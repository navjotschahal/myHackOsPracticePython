from pilkit.lib import Image
from pilkit.processors import TrimBorderColor
img = Image.open('E:\Pictures\circular array itrate.PNG')
processor = TrimBorderColor()
new_img = processor.process(img)
Image.save(new_img)