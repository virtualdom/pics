import os
from PIL import Image
import sys

if len(sys.argv) < 2:
  print('pass in a date')
  sys.exit(1)

date = sys.argv[1]
root = os.getcwd()

image = Image.open(f'{root}/{date}/01.png')
width, height = image.size
cropped_width = 300
cropped_height = 400

scale = max(cropped_width/width, cropped_height/height)
final_size = (width * scale, height * scale)

image.thumbnail(final_size)

image.save(f'{root}/{date}/thumbnail.png')
