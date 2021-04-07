from os import getcwd, listdir
from os.path import isfile, join
from PIL import Image
import re
import sys

if len(sys.argv) < 2:
  print('pass in a date')
  sys.exit(1)

date = sys.argv[1]
root = getcwd()
path = f'{root}/{date}'

files = [ f'{path}/{f}' for f in listdir(path) if isfile(join(path, f)) and re.match('^[0-9][0-9].png$', f)]

# Make thumbnail
print(f'Thumbnailing {path}/01.png...')
first_image = Image.open(f'{path}/01.png')
width, height = first_image.size
thumbnail_min_width = 300
thumbnail_min_height = 400

thumbnail_scale = max(thumbnail_min_width/width, thumbnail_min_height/height)
thumbnail_final_size = (width * thumbnail_scale, height * thumbnail_scale)

first_image.thumbnail(thumbnail_final_size)
first_image.save(f'{path}/thumbnail.png')

# Reduce each image
max_width = 2000
max_height = 2000
for f in files:
  print(f'Reducing {f}...')
  image = Image.open(f)
  width, height = image.size

  scale = min(max_width/width, max_height/height)
  final_size = (width * scale, height * scale)
  image.thumbnail(final_size)

  image.save(f)





