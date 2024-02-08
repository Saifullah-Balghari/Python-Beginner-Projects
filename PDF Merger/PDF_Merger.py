import PyPDF2 
import os


pdf_files = ['pdf1.pdf', 'pdf2.pdf', 'pdf3.pdf', 'pdf4.pdf']
output_pdf = 'Merged.pdf'

merger = PyPDF2.PdfMerger()

for pdf_file in pdf_files:
    merger.append(pdf_file)

merger.write(output_pdf)
merger.close()

