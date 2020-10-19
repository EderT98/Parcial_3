class Embarcaciones:
    def __init__(self, patente, empresa, tipo_carga, cant_dias):
        self.patente = patente
        self.empresa = empresa
        self.tipo_carga = tipo_carga
        self.cant_dias = cant_dias


def write(vec):
    print("Patente:", vec.patente)
    print("Nombte de la empresa:", vec.empresa)
    print("Tipo de carga:", vec.tipo_carga)
    print("Cantidad de dias:", vec.cant_dias, '\n')