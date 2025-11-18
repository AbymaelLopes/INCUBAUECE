import pandas as pd
from docxtpl import DocxTemplate
import dicionario
import sys
sys.path.append("bases_de_dados")
import dados

documento = DocxTemplate('Relatório semestral - CERNE 1.docx')

documento.render(dicionario.variaveis)

texto_paragrafos = "\n".join([p.text for p in documento.docx.paragraphs])
print(texto_paragrafos)

# documento.save('Relatório semestral - CERNE 1 - atualizado.docx')


