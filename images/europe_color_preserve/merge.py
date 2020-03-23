from __future__ import print_function
import os

from PIL import Image

files = [
  'europe_01_01_700.png',
  'europe_02_01_700.png',
  'europe_01_02_700.png',
  'europe_02_02_700.png']

result = Image.new("RGB", (1920, 1200))

for index, file in enumerate(files):
  path = os.path.expanduser(file)
  img = Image.open(path)
  img.thumbnail((960, 600), Image.ANTIALIAS)
  x = index // 2 * 960
  y = index % 2 * 600
  w, h = img.size
  print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
  result.paste(img, (x, y, x + w, y + h))

result.save(os.path.expanduser('image.jpg'))
