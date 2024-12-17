
ANCHO = 20

dic_empresas = {}

def cargar_empresas(nombre_archivo):
    archivo = open(nombre_archivo,'r')
    str_empresas = archivo.read()
    archivo.close()

    lista_empresas = str_empresas.splitlines()
    for str_fila in lista_empresas:
        lista_fila = str_fila.split(',')
        dic_registro = {
           'razon social':lista_fila[1],
           'direccion' :lista_fila[2]
        }
        dic_nueva_empresa = {
            lista_fila[0] : dic_registro
        }
        dic_empresas.update(dic_nueva_empresa)

def grabar_empresas(nombre_archivo):
    str_empresas = ""
    for empresa_clave, empresa_valor in dic_empresas.items():
        str_empresas += empresa_clave + ","
        for registro_clave, registro_valor in empresa_valor.items():
            str_empresas += registro_valor
            if registro_clave != 'direccion':
                str_empresas += ','
            else:
                str_empresas += '\n'
    
    fsalida = open(nombre_archivo,'w')
    fsalida.write(str_empresas)
    fsalida.close()

def mostrar_mensaje(texto):
    print("*" * ANCHO + "*" * ANCHO)
    if texto != " ":
        print(" " * 10 + texto)
        print("*" * ANCHO + "*" * ANCHO)

def menu():
    mostrar_mensaje("GESTIÓN DE EMPRESAS")
    print("""
         [1] REGISTRAR EMPRESAS
         [2] MOSTRAR EMPRESAS
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    mostrar_mensaje(" ")

##

def registrar():
    mostrar_mensaje("[1] REGISTRAR EMPRESA")
    ruc = input("RUC    :")
    razon = input("RAZON SOCIAL  :")
    direccion = input("DIRECCION    :")
    dic_nueva_empresa = {
        ruc : {
                'razon social': razon,
                'direccion': direccion
                }
    }
    dic_empresas.update(dic_nueva_empresa)

def mostrar():
    mostrar_mensaje("[2] MOSTRAR EMPRESAS")
    for ruc,datos in dic_empresas.items():
        print(f"RUC : {ruc}")
        print(f"RAZON SOCIAL : {datos['razon social']}")
        print(f"DIRECCION : {datos['direccion']}")
        mostrar_mensaje(" ")

def actualizar():
    mostrar_mensaje("[3] ACTUALIZAR EMPRESA")
    ruc = input("INGRESE EL RUC DE LA EMPRESA A ACTUALIZAR")
    if ruc in dic_empresas:
        print(f"EMPRESA A ACTUALIZAR  {dic_empresas[ruc]['razon social']}")
        nuevo_razon = input('Razon Social : ')
        nuevo_direccion = input('Direccion :')
        dic_act_empresa = {
            ruc : {
                'razon social':nuevo_razon,
                'direccion':nuevo_direccion
            }
        }
        dic_empresas.update(dic_act_empresa)
        print("EMPRESA ACTUALIZADA CON EXITO")

def eliminar():
    mostrar_mensaje("[4] ELIMINAR EMPRESA")
    dni = input("INGRESE EL RUC DE LA EMPRESA A ELIMINAR : ")
    if dni in dic_empresas:
        dic_empresas.pop(dni)
        print("EMPRESA ELIMINADA")
    else:
        print("NO SE ENCONTRO LA EMPRESA")