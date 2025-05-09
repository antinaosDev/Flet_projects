class Empresa():
    def __init__(self, num_cot,fecha_cot,nom_v,tel_v,mail_v,dias_cot):
        self.num_cot = num_cot
        self.fecha_cot = fecha_cot
        self.nom_v = nom_v
        self.tel_v = tel_v
        self.mail_v = mail_v
        self.dias_c = dias_cot

        self.empresa = {}

    def ingrear_empresa(self):
            self.empresa = {
                'NUM_C': self.num_cot,
                'FECHA_COT': self.fecha_cot,
                'NOMBRE_V': self.nom_v,
                'TEL': f'+56{self.tel_v}',
                'MAIL_V': self.mail_v,
                'DIAS_COT':self.dias_c,
            }

            return self.empresa


class Cliente():
    def __init__(self,nom_c,dir_c,tel_c,mail_c):
        self.nom_c = nom_c
        self.dir_c = dir_c
        self.tel_c = tel_c
        self.mail_c = mail_c
        
        self.cliente = {}

    def ingresar_cliente(self):
            self.cliente = {
                'NOMBRE': self.nom_c,
                'DIRECCION': self.dir_c,
                'TELC':f'+56{self.tel_c}',
                'MAIL_C': self.mail_c,
            }

            return self.cliente

class Items():
    def __init__(self, lista_item, lista_cant, lista_precio):
        self.item = lista_item
        self.cant = lista_cant
        self.precio = lista_precio
        self.items = {}

    def ingreso_producto(self):
        for i, item in enumerate(self.item, 1):
            self.items[f'ITEM{i}'] = item
        for i, cant in enumerate(self.cant, 1):
            self.items[f'CANT{i}'] = cant
        for i, precio in enumerate(self.precio, 1):
            self.items[f'PRECIO{i}'] = precio
        
        for i in range(1, 8):
            clave_cant = f'CANT{i}'
            clave_prec = f'PRECIO{i}'
            clave_total = f'TOT{i}'

            if clave_cant in self.items and clave_prec in self.items:
                self.items[clave_total] = int(self.items[clave_cant]) * int(self.items[clave_prec])
                    
        return self.items

def formatear_miles(valor):
    return f"{valor:,}".replace(",", ".")


class Consolidado:
    def __init__(self, empresa, cliente, items):
        self.empresa = empresa
        self.cliente = cliente
        self.items = items
        self.consolidado = {}

    def balance(self):
        self.consolidado = {}
        self.consolidado.update(self.empresa.empresa)
        self.consolidado.update(self.cliente.cliente)
        self.consolidado.update(self.items.items)

        self.consolidado['SUBT'] = 0
        for i in range(1, 8):
            clave_sub_t = f'TOT{i}'
            if clave_sub_t in self.consolidado:
                self.consolidado['SUBT'] += int(self.consolidado[clave_sub_t])

        self.consolidado['IVA'] = round(self.consolidado['SUBT'] * 0.19)
        self.consolidado['TG'] = self.consolidado['SUBT'] + self.consolidado['IVA']

        # Formatear valores numéricos
        for i in range(1, 8):
            for key in [f'PRECIO{i}', f'TOT{i}']:
                if key in self.consolidado:
                    self.consolidado[key] = formatear_miles(int(self.consolidado[key]))

        self.consolidado['SUBT'] = formatear_miles(self.consolidado['SUBT'])
        self.consolidado['IVA'] = formatear_miles(self.consolidado['IVA'])
        self.consolidado['TG'] = formatear_miles(self.consolidado['TG'])

        # Convertir todos a string (por si acaso)
        self.consolidado = {k: str(v) for k, v in self.consolidado.items()}

        return self.consolidado
    
    def to_dict(self):
        return self.consolidado
