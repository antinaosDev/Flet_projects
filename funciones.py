import base64

def convertir_plantilla_b64():

    with open(r'D:\PROYECTOS PROGRAMACIÓN\facturas\cotizaciones\cotiz.docx','rb') as bin:
        base64_docx = base64.b64encode(bin.read()).decode('utf-8')

    with open('Plantilla_cotiz_base64.txt','w') as bin:
        bin.write(base64_docx)
        print('plantilla creada!')

convertir_plantilla_b64()