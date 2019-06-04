# This is a latex compiler that compiles .latex file to image file


from latex import build_pdf
# TODO:
# 1. encapsulate into Compiler class

pdf = build_pdf(open('data/city.latex'))

pdf.save_to('data/city.pdf')