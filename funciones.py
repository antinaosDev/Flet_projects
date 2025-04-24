import base64
import requests
import tempfile
import os
from docxtpl import DocxTemplate
from plantilla_base_64 import plantilla
"""
def convertir_plantilla_b64():

    with open(r'D:\PROYECTOS PROGRAMACIÓN\facturas\cotizaciones\cotiz.docx','rb') as bin:
        base64_docx = base64.b64encode(bin.read()).decode('utf-8')

    with open('Plantilla_cotiz_base64.txt','w') as bin:
        bin.write(base64_docx)
        print('plantilla creada!')
"""


def crear_plantilla_temp(plantilla_b64):
    """
    Decodifica una plantilla en base64 y la guarda como archivo temporal.
    Retorna la ruta al archivo temporal creado.
    """
    ruta_temp = os.path.join(tempfile.gettempdir(), 'Plantilla_temp.docx')
    with open(ruta_temp, 'wb') as bin_file:
        bin_file.write(base64.b64decode(plantilla_b64))
    return ruta_temp


def generar_cot(ruta_plantilla, datos, ruta_output):
    doc = DocxTemplate(ruta_plantilla)
    doc.render(datos)
    doc.save(ruta_output)

    print(f"Documento generado en: {ruta_output}")
