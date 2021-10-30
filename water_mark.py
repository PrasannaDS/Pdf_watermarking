import PyPDF2
import sys

try:
    input_pdf = sys.argv[1]
    if input_pdf:
        template = PyPDF2.PdfFileReader(open(f'{input_pdf}','rb'))
        water_mark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
        output = PyPDF2.PdfFileWriter()

        for i in range(template.getNumPages()):
            page = template.getPage(i)
            page.mergePage(water_mark.getPage(0))
            output.addPage(page)
            with open('water_marked_output.pdf','wb') as file:
                output.write(file)
    else:
        print ('Enter correct pdf name in console from the current directory')
except (IndexError,FileNotFoundError):
    print('Enter correct pdf name in console from the current directory and Make sure your file exist and naming is proper.')