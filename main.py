from langchain import OpenAI
from PyPDF2 import PdfReader


openai_api_key = "sk-proj-0g5nceIwfhEk81RL5UKcT3BlbkFJBwxVH4aVjhdmsol2bNQf"

llm = OpenAI(temperature=0,openai_api_key=openai_api_key)

# extract text from pdf
import PyPDF2
import requests
import io


# import pdftotext

# # Load your PDF
# with open("miami.pdf", "rb") as f:
#     pdf = pdftotext.PDF(f)
# # # If it's password-protected
# # with open("secure.pdf", "rb") as f:
# #     pdf = pdftotext.PDF(f, "secret")
# # How many pages?
# print(len(pdf))
# # Iterate over all the pages
# for page in pdf:
#     print(page)
# Read some individual pages
# print(pdf[0])
# print(pdf[1])
# Read all the text into one string
# print("\n\n".join(pdf))

#use pdf reader [i dont think we need this]

# url = 'https://www.mass.gov/doc/doherty-denise-v-department-of-state-police-related-superior-court-decision-62818/download'
# response = requests.get(url)
# # print(response)
# f = io.BytesIO(response.content)
# # print(f)
# reader = PyPDF2.PdfReader(f)
# # print(reader)
# pages = reader.pages
# # print(pages)
# # get all pages data
# text = "".join([page.extract_text() for page in pages])

# print(text)

# 

import requests, pdf2image
from pdf2image import convert_from_path, convert_from_bytes

pdf = requests.get('https://www.mass.gov/doc/doherty-denise-v-department-of-state-police-related-superior-court-decision-62818/download', stream=True)
pages = pdf2image.convert_from_bytes(pdf.content)

'''How to do this without saving these locally? maybe not
now we have a jpg and can extract the text! next step is bounding with cv'''
 
# for i in range(len(images)):
   
#       # Save pages as images in the pdf
#     images[i].save('page'+ str(i) +'.jpg', 'JPEG')

#You're going to have to use Tesseract OCR to extract text from image.
from PIL import Image
import pytesseract
tess_cfg = '--psm 6'
data=""
doc = 1
for i in range(len(pages)):
    direct = f"images/{i}.jpg"
    pages[i].save(direct, "JPEG")
    image = Image.open(direct)
    # data = (pytesseract.image_to_string(image, lang='eng', config = tess_cfg))
    data += (pytesseract.image_to_string(Image.open(f"images/{i}.jpg"), lang='eng', config = tess_cfg))
    
# print(data)
print(len(data))

output = open("Output.txt", "w")

output.write(data)

output.close()

# print(data.count("PROCEDURAL HISTORY"))
# li = data.split("PRODEDURAL HISTORY AND RELEVANT FINDINGS")
# # print(li[1])
# string = li[1].split("CONCLUSION AND ORDER")
# print(string[0])
# llm prompt



# prompt = f'Based on the following Civil Service Commissions document on police misconduct, give a short and concise summary: \n TEXT: {string[0]}'

# num_tokens = llm.get_num_tokens(prompt)

# output = llm(prompt)
# print (f"Our prompt has {num_tokens} tokens", "Summary: ", output)