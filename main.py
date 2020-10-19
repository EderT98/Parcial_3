__author__ = "Eder Tassin"

import service


"""
Barco - patente - empresa - tipo de carga 0 14 - dias en el puerto
Se desea almacenar la información referida a los n
barcos  en un arreglo de registros de tipo Barco (definir el tipo Barco  y cargar
n por teclado).
"""
def menu():
    print("="*10,"Bienvenido al muelle", "="*10)
    print("1 -  Cargar embarcaciones:")
    print("2 - Mostrar embarcaciones ordenadas: ")
    print("3 - Cantidad de barcos por tipo: ")
    print("4 - Buscar barco por empresa y carga: ")
    print("5 - Mostrar el menor cantidad carga 0, 1 o 2")


def validar(crg):
    n = crg
    while n <= crg:
        n = int(input('Valor: '))
        if n <= crg:
            print('Tiene que ingresar un valor mayor a 0.\n')
            print('Cargue de nuevo!')
    return n


def validar_carga(cero=0, catorce=14):
    tipo = int(input('Carga numero: '))
    while tipo < cero or tipo > 14:
        tipo = int(input('Ingrese de nuevo el tipo de carga: '))
    return tipo


def carga():
    print('Ingrese la cantidad de emmbarcaciones: ')
    n = validar(0)
    v = [None] * n

    for i in range(n):
        print("\n Barco ", str(i+1))
        print('Patente del barco: ')
        patente = validar(0)

        empresa = input('Empresa: ')

        print('Ingrese el tipo de carga: ')
        print('*el tipo de carga va de 0 a 14.')
        tipo_carga = validar_carga(0, 14)

        print('Ingrese la cantidad de dias: ')
        cant_dias = validar(0)

        v[i] = service.Embarcaciones(patente, empresa, tipo_carga, cant_dias)
    return v


def mostrar_orden(vec):
    n = len(vec)
    for i in range(n-1):
        for j in range(i+1, n):
            if vec[i].patente < vec[j].patente:
                vec[i], vec[j] = vec[j], vec[i]

    for i in range(n):
        service.write(vec[i])


def conteo_tipo(vec):
    c = [0] * 15

    n = len(vec)
    for i in range(n):
        c[vec[i].tipo_carga] += 1

    print('Cantidad barcos tipo:')
    for j in range(15):
        if c[j] != 0:
            print('Tipo: ', j, 'Cantidad:', c[j])


def busqueda(vec, emp, car):
    n = len(vec)
    for i in range(n):
        if vec[i].empresa == emp and vec[i].tipo_carga == car:
            print('Se encontro la embarcacion!')
            service.write(vec[i])
            return
    print('No existe esa embarcacion: ')


def menor_dia(vec):
    menor = None
    for bar in vec:
        if menor is None or bar.cant_dias < menor and bar.tipo_carga > 3:
            menor = bar.cant_dias
    menores = []
    for bar in vec:
        if bar.cant_dias == menor:
            menores.append(bar)
    return menores


def mostrar(menor_barco):
    for i in menor_barco:
        service.write(i)


def test():

    vec = []
    datos = False
    op = -1

    while op != 0:
        menu()
        op = int(input("Ingrese una opcion: "))

        if op == 1:
            vec = carga()
            datos = True

        elif op == 2:
            if datos:
                mostrar_orden(vec)
            else:
                print('Tiene que cargar los datos de las embarcaciones')
        elif op == 3:
            if datos:
                conteo_tipo(vec)
            else:
                print('Tiene que cargar los datos de las embarcaciones')
        elif op == 4:
            if datos:
                emp = input('Ingrese la empesa que busca: ')
                print('Ingrese el tipo de carga: ')
                car = validar_carga(0)
                busqueda(vec, emp, car)
            else:
                print('Tiene que cargar los datos de las embarcaciones')
        elif op == 5:
            if datos:
                menor_barco = menor_dia(vec)
                mostrar(menor_barco)
            else:
                print('Tiene que cargar los datos de las embarcaciones')


if __name__ == "__main__":
    test()



