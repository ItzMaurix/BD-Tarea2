import requests
import json
# implementación de las funciones
def get_usuario():
    correo = input("Ingrese correo: ")
    consulta = requests.get('http://localhost:3000/api/get_usuario/'+correo)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if consulta.status_code == 200:
        return [True, dict_data[0]]
    return [False]

def get_informacion():
    correo = input("Ingrese correo: ")
    consulta = requests.get('http://localhost:3000/api/informacion/'+correo)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if consulta.status_code == 200:
        return [True, dict_data[0]]
    return [False]

def register_user(nombre, correo, clave, descripcion):
    datos = {'_nombre':nombre, '_correo':correo,'_clave':clave, '_descripcion':descripcion}
    consulta = requests.post('http://localhost:3000/api/registrar/', json=datos)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if consulta.status_code == 200:
        return [True, dict_data[0]]
    return [False]

def block_user(correo, clave, correo_bloquear):
    datos = {'_correo':correo,'_clave':clave, '_correo_bloquear':correo_bloquear}
    consulta = requests.post('http://localhost:3000/api/bloquear/', json=datos)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if consulta.status_code == 200:
        return [True, dict_data[0]]
    return [False]

def set_favorite(correo, clave,  id_correo_favorito):
    datos = {'_correo':correo,'_clave':clave, '_id': id_correo_favorito}
    consulta = requests.post('http://localhost:3000/api/marcarcorreo/', json=datos)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if consulta.status_code == 200:
        return [True, dict_data]
    return [False]

def delete_favorite(correo, clave, id_correo_favorito):
    datos = {'_correo':correo,'_clave':clave, '_id': id_correo_favorito}
    consulta = requests.delete('http://localhost:3000/api/desmarcarcorreo/', json=datos)
    print(consulta.status_code)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if consulta.status_code == 200:
        return [True, dict_data[0]]
    return [False]

def get_favorite(correo, clave):
    datos = {'_correo':correo,'_clave':clave}
    consulta = requests.post('http://localhost:3000/api/vercorreo/', json=datos)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if consulta.status_code == 200:
        return [True, dict_data[0]]
    return [False]

def enviar_correo(correo, clave, asunto, cuerpo, receptor):
    datos = {'_correo':correo,'_clave':clave, '_asunto': asunto, '_cuerpo':cuerpo, '_correo_recibe': receptor}
    consulta = requests.post('http://localhost:3000/api/enviarcorreo/', json=datos)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if consulta.status_code == 200:
        return [True, dict_data[0]]
    return [False]
    
#mensaje según el número de error
def msg_error(numero):
    return 1

# ver información del correo y la clave
busqueda = get_usuario()
if not busqueda[0]:
    print("Se ha finalizado el programa.")
    exit()
correo = busqueda[1]['direccion_correo']
clave = busqueda[1]['clave']
clave = input("Ingrese clave: ")
if clave != busqueda[1]['clave']:
    print("Se ha finalizado el programa.")
    exit()


# menú de opciones
while True:
    print("\n1. Ver información de una dirección de correo electrónico")
    print("2. Ver correos favoritos")
    print("3. Marcar correo como favorito")
    print("4. Desmarcar correo como favorito")
    print("5. Registrar Usuario")
    print("6. Bloquear Usuario")
    print("7. Terminar con la ejecución del cliente")
    print("8. Enviar correo\n")
    opcion = int(input("Ingrese opción (1-7): "))
    if opcion == 1:
        respuesta = get_informacion()
        if not respuesta[0]:
            break
        print("Nombre: "+respuesta[1]['nombre'])
        print("Correo: "+respuesta[1]['direccion_correo'])
        print("Descripción: "+respuesta[1]['descripcion'])
    elif opcion == 2:
        print("Aquí está la lista de correos marcados como favorito")
        respuesta=get_favorite(correo, clave)
        print(respuesta[1])
    elif opcion == 3:
        solicitud_marcar = int(input("Ingrese id_correo_favorito: "))
        respuesta = set_favorite(correo, clave,  solicitud_marcar)
        if not respuesta[0]:
            break
        print("Marcado como favorito exitosamente")
    elif opcion == 4:
        solicitud_desmarcar = int(input("Ingrese id_correo_favorito: "))
        respuesta = delete_favorite(correo, clave, solicitud_desmarcar)
        if not respuesta[0]:
            break
    elif opcion == 5:
        nombre_registrar = input("Ingrese nombre del Usuario: ")
        correo_registrar = input("Ingrese correo del Usuario: ")
        clave_regitrar = input("Ingrese la clave del Usuario: ")
        descripcion = input("Ingrese la descripción del usuario: ")
        respuesta = register_user(nombre_registrar, correo_registrar, clave_regitrar, descripcion)
    elif opcion == 6:
        correo_bloquear = input("Ingrese correo a bloquear: ")
        respuesta = block_user(correo, clave, correo_bloquear)
    elif opcion == 7:
        break
    elif opcion == 8:
        receptor_enviar = input("Ingrese correo del usuario destinatario: ")
        asunto_enviar = input("Ingrese asunto del correo: ")
        cuerpo_enviar = input("Ingrese cuerpo del correo: ")
        respuesta = enviar_correo(correo, clave, asunto_enviar, cuerpo_enviar, receptor_enviar)
print("Se ha finalizado el programa.")
exit()




'''
para manejo de errores utilizar status_code
'''