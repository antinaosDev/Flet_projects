import flet as ft 
from pick_data import crear_campos, obtener_valores

def main(page: ft.Page):
    num_cot, nombre_v, tel_v, correo_v, dias_cot, nombre_c, tel_c, correo_c, productos, cantidades, precios = crear_campos()

    def procesar_val(e):
        datos = obtener_valores(num_cot, nombre_v, tel_v, correo_v, dias_cot, nombre_c, tel_c, 
                                correo_c, productos, cantidades, precios)

    boton = ft.ElevatedButton("Obtener valores", on_click=procesar_val)

    page.add(
        num_cot, nombre_v, tel_v, correo_v, dias_cot,
        nombre_c, tel_c, correo_c,
        *productos, *cantidades, *precios,
        boton
    )
ft.app(target=main)  
