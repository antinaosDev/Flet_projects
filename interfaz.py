import flet as ft 
from pick_data import crear_campos, obtener_valores
from clases import Empresa, Cliente, Items, Consolidado
from funciones import  crear_plantilla_temp, generar_cot
import os
from plantilla_base_64 import plantilla
def main(page: ft.Page):
    #Configuración de la pagina
    page.scroll = 'auto'

    # FilePicker debe ser creado y agregado al overlay
    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)


    #Levantamiento de datos
    num_cot,fecha_c, nombre_v, tel_v, correo_v, dias_cot, nombre_c, tel_c,direc,correo_c, productos, cantidades, precios = crear_campos()
    

    #Filas empresa
    filas_empresa_1 = ft.Row([num_cot,fecha_c])
    filas_empresa_2 = ft.Row([nombre_v,tel_v])
    filas_empresa_3 =ft.Row([correo_v,dias_cot])
    #Filas Cliente
    filas_cliente_1 = ft.Row([nombre_c,tel_c])
    filas_cliente_2 = ft.Row([direc,correo_c])
    #Filas Items
    col_items = ft.Column([*productos])
    col_cant = ft.Column([*cantidades])
    col_prec = ft.Column([*precios])
    fila_col = ft.Row([col_items,col_cant,col_prec])
    
    #Obtener datos
    ruta_temp = crear_plantilla_temp(plantilla)
    
    def obtener_data(e):
        def on_result(e: ft.FilePickerResultEvent):
            if not e.path:
                print("No se seleccionó carpeta.")
                return

            carpeta_destino = e.path

            # Obtener los valores ingresados en ese momento
            num_cot_val, fecha_cot_val, nombre_v_val, tel_v_val, correo_v_val, dias_cot_val, \
            nombre_c_val, direc_val, tel_c_val, correo_c_val, productos_val, \
            cantidades_val, precios_val = obtener_valores(
                num_cot, fecha_c, nombre_v, tel_v, correo_v, dias_cot,
                nombre_c, tel_c, direc, correo_c, productos, cantidades, precios
            )

            # Crear objetos con los datos reales
            dict_empresa = Empresa(num_cot_val, fecha_cot_val, nombre_v_val, tel_v_val, correo_v_val, dias_cot_val)
            dict_empresa.ingrear_empresa()
            dict_cliente = Cliente(nombre_c_val, direc_val, tel_c_val, correo_c_val)
            dict_cliente.ingresar_cliente()
            dict_items = Items(productos_val, cantidades_val, precios_val)
            dict_items.ingreso_producto()  # <-- Corregido: paréntesis añadidos
            dict_consolidado = Consolidado(dict_empresa, dict_cliente, dict_items)
            dict_consolidado.balance()

            # Crear archivo de salida
            nombre_archivo = f"Cotizacion_{num_cot_val}.docx"
            ruta_output = os.path.join(carpeta_destino, nombre_archivo)

            generar_cot(ruta_temp, dict_consolidado.to_dict(), ruta_output)
            print(f"Cotización guardada en: {ruta_output}")
            page.snack_bar = ft.SnackBar(ft.Text("Cotización generada correctamente."), open=True)
            page.update()

        file_picker.on_result = on_result
        file_picker.get_directory_path()

    # Botón para generar cotización
    boton = ft.ElevatedButton("Generar cotización", on_click=obtener_data)
     
    page.add(
        filas_empresa_1,filas_empresa_2,filas_empresa_3,
        filas_cliente_1,filas_cliente_2,
        fila_col,
        boton
    )


ft.app(target=main)  