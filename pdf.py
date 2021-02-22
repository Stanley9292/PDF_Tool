import PyPDF2


with open('pdf_Files\dummy.pdf', 'r') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.num)