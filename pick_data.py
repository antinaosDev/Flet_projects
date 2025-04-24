import flet as ft 

def input_text_field(titulo, hints):
    return ft.TextField(label = titulo, hint_text = hints, width = 400, text_size = 14, autofocus = True)

def input_number_field(titulo, hints, caracteres):
    return ft.TextField(
        label = titulo, 
        hint_text = hints,
        text_size = 14, 
        autofocus = True, 
        width = 200,
        input_filter = ft.NumbersOnlyInputFilter(),
        max_length = caracteres,
        )

def crear_campos():
    # Datos empresa
    num_cot = input_number_field('N° Cotización:', 'N°',3)
    fecha_c = input_text_field('Fecha cotización:', 'DD/MM/AAAA')
    nombre_v = input_text_field('Nombre vendedor:', 'Nombre completo')
    tel_v = input_number_field('Celular vendedor:', '9XXXXXXXX', 9)
    correo_v = input_text_field('Mail vendedor:', 'XXX@XXX.XXX')
    dias_cot = input_number_field('Duración cotización:', 'días', 2)

    # Datos cliente
    nombre_c = input_text_field('Nombre del cliente:', 'Nombre completo')
    tel_c = input_number_field('Celular del cliente:', '9XXXXXXXX', 9)
    correo_c = input_text_field('Mail del cliente:', 'XXX@XXX.XXX')
    direc = input_text_field('Dirección del cliente:', 'Ingrese dirección:')

    # Datos productos
    productos = [input_text_field(f'Item {i}', 'Indique el detalle') for i in range(1,8)]
    cantidades = [input_number_field(f'Cantidad item {i}', 'N°', 9) for i in range(1,8)]
    precios = [input_number_field(f'Precio item {i}', 'Monto en pesos', 9) for i in range(1,8)]

    return num_cot,fecha_c, nombre_v, tel_v, correo_v, dias_cot, nombre_c, tel_c,direc,correo_c, productos, cantidades, precios

def obtener_valores(num_cot,fecha_c, nombre_v, tel_v,correo_v,dias_cot,nombre_c,tel_c,direc,correo_c,productos,cantidades,precios):
    #datos empresa
    fecha_cot_val = fecha_c.value
    num_cot_val = int(num_cot.value or 0)
    nombre_v_val = nombre_v.value
    tel_v_val = tel_v.value
    correo_v_val = correo_v.value
    dias_cot_val = int(dias_cot.value or 0)
    #Datos cliente
    nombre_c_val = nombre_c.value
    tel_c_val = tel_c.value
    direc_val = direc.value
    correo_c_val = correo_c.value
    #Datos productos
    productos_val = [p.value for p in productos]
    cantidades_val = [int(c.value or 0) for c in cantidades]
    precios_val = [int(p.value or 0) for p in precios]

    return num_cot_val, fecha_cot_val, nombre_v_val, tel_v_val,correo_v_val,dias_cot_val,nombre_c_val,direc_val,tel_c_val,correo_c_val,productos_val,cantidades_val,precios_val


