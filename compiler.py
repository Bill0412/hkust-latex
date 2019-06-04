# This is a latex compiler that compiles .latex file to a well processed image file

from latex import build_pdf
from wand.image import Image
from pdf2image import convert_from_path
import os
# TODO: 1. Fix the trim issue; 2. Fix the compiler error; 3. Multi-page pdf support

class Compiler:
    def __init__(self, base_path='data/latex/'):
        self.base_path = base_path

    def compile(self, fileslug):

        # compile to .pdf
        base_filename = '{0}/{1}/{1}'.format(self.base_path.strip('/'), fileslug)
        pdf = build_pdf(open(base_filename + '.latex'))
        pdf.save_to(base_filename + '.pdf')

        # convert to .png file
        pages = convert_from_path(base_filename + '.pdf')

        # multi-page pdf support should be implemented here
        for page in pages:
            page.save(base_filename + '_temp.png', 'PNG')

        with Image(filename=base_filename + '_temp.png') as i:
            i.trim()
            i.save(filename=base_filename + '.png')
            # for web hosting
            if not os.path.exists('static'):
                os.mkdir('static')
            i.save(filename='static/{}.png'.format(fileslug))


if __name__ == '__main__':
    compiler = Compiler()
    compiler.compile('city')

