from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

model    = ChatOpenAI(openai_api_key=openai_api_key, temperature=.5) # temperature = how random

# Steps

# 1. Get all the pdfs downloaded done.
#    a. Sort accordingly on excel ->
#    b. If they need OCR, take care of that
#    c. If not, just skip to downloading them as a .txt

# 2. Read/write the text file done.
temp = open('todo/earley.txt','r').read().split('\n')
# print(temp)

# 3. So now we have them all in txt files locally, go through each one and craft summary, then extract important info to copy and paste 7/10
# 4. Double check everything, move from todo to finish


summary_prompt_text = "I would like you to read this civil service commission document and summarize it from the perspective of a civil liberties and civil rights advocate, detailing the incident of police misconduct in this scenario. Please be comprehensive but concise, and if there was an injustice, please describe it.: {narrative}"
misconduct_prompt_text = "Please extract the following information from the following civil commission document. If no information available, please indicate that instead. Display output in an ordered list format: 1. Year of misconduct 2. City of Police Department the police officer belonged to 3. What, if any, consequences did the officer face?: {narrative}"
violence_prompt_text = "Please extract the following information from the following civil commission document. : 1. Name of officer 2. Date of incident 3. City of police department the police officer belonged to 4. Search the web for address of said police department and return here 5. What, if any, consequences did the officer face?  : {narrative}"
other_prompt = "Please detail the misconduct of the police officer in this document. What did the police officer do and say? {narrative}"

prompt = ChatPromptTemplate.from_template(summary_prompt_text)
chain = prompt | model | StrOutputParser()

output = chain.invoke({"narrative": temp})
print(output)