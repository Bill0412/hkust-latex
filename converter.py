# This module converts the pdf file to image and crops the blank area
from wand.image import Image
from pdf2image import convert_from_path

pages = convert_from_path('data/city.pdf')

for page in pages:
    page.save('data/city.png', 'PNG')

with Image(filename='data/city.png') as i:
    i.trim()
    i.save(filename='trimed.png')

