import re
import pymupdf

# 1) Extrair os números de processos judiciais do pdf

doc = pymupdf.Document(r"C:\Users\liasa\Downloads\caderno2-Judiciario.pdf") # abre o documento

texto = ""

for page in doc:
    texto += page.get_text("textpage") #extrai o texto de cada página do pdf e une em um único texto

doc.close() #fecha o documento

lista = re.findall(r'[0-9]{7}-[0-9]{2}\.[0-9]{4}\.[0-9]\.[0-9]{2}\.[0-9]{4}', texto) # encontra todos os números de processo e insere em uma lista

print(lista) #mostra o tamanho da lista

