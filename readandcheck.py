import re
import pdfplumber

with pdfplumber.open(r"C:\Users\liasa\Downloads\caderno2-Judiciario.pdf") as pdf:
    texto = ''
    c = 0
    for page in pdf.pages:
        c += 1
        print(c)
        extracted_text = page.extract_text()
        print(f"Processando página {page.page_number}")
        texto += extracted_text

lista = re.findall(r'[0-9]{7}-[0-9]{2}\.[0-9]{4}\.[0-9]\.[0-9]{2}\.[0-9]{4}', texto)
print(lista)