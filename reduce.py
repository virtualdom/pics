import os
from PIL import Image
import sys

if len(sys.argv) < 2:
  print('pass in a date')
  sys.exit(1)

file = sys.argv[1]
root = os.getcwd()

image = Image.open(f'{root}/{file}')
width, height = image.size
cropped_width = 2000
cropped_height = 2000

scale = min(cropped_width/width, cropped_height/height)
final_size = (width * scale, height * scale)

image.thumbnail(final_size)

image.save(f'{root}/{file}')
