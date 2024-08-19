import PyPDF2

import os
# assign directory
directory = 'pdfs'
 
def pdf_to_text(pdf_path, output_txt):
    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PdfReader object instead of PdfFileReader
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize an empty string to store the text
        text = ''

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    # Write the extracted text to a text file
    with open(output_txt, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)
        
        
# iterate over files in
# that directory
# for pdf in os.listdir(directory):
#     f = os.path.join(directory, pdf)

#     pdf_to_text(f, f"todo/{pdf[:-4]}.txt")
    

pdf_to_text("output.pdf", f"todo/example.txt")
    