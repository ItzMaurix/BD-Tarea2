import requests
import json
def get_usuario():
    correo = input("Ingrese correo: ")
    consulta = requests.get('http://localhost:3000/api/get_usuario/'+correo)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if len(dict_data) == 1:
        return [True, dict_data[0]]
    return [False]
def get_informacion():
    correo = input("Ingrese correo: ")
    consulta = requests.get('http://localhost:3000/api/informacion/'+correo)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if len(dict_data) == 1:
        return [True, dict_data[0]]
    return [False]
def register_user(correo, clave):
    datos = {'_correo':correo,'_clave':clave}
    consulta = requests.post('http://localhost:3000/api/registrar/', json=datos)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if len(dict_data) == 1:
        return [True, dict_data[0]]
    return [False]
def block_user(correo, clave, correo_bloquear):
    datos = {'_correo':correo,'_clave':clave, '_correo_bloquear':correo_bloquear}
    consulta = requests.post('http://localhost:3000/api/bloquear/', json=datos)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if len(dict_data) == 1:
        return [True, dict_data[0]]
    return [False]
def set_favorite(correo, clave,  id_correo_favorito):
    datos = {'_correo':correo,'_clave':clave, '_id_correo_favorito': id_correo_favorito}
    consulta = requests.post('http://localhost:3000/api/marcarcorreo/', json=datos)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if len(dict_data) == 1:
        return [True, dict_data[0]]
    return [False]
def delete_favorite(correo, clave, id_correo_favorito):
    datos = {'_correo':correo,'_clave':clave, '_id_correo_favorito': id_correo_favorito}
    consulta = requests.post('http://localhost:3000/api/desmarcarcorreo/', json=datos)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if len(dict_data) == 1:
        return [True, dict_data[0]]
    return [False]
def get_favorite(correo, clave):
    datos = {'_correo':correo,'_clave':clave}
    consulta = requests.post('http://localhost:3000/api/vercorreo/', json=datos)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if len(dict_data) > 0:
        return [True, dict_data[0]]
    return [False]
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
    print("1. Ver información de una dirección de correo electrónico")
    print("2. Ver correos favoritos")
    print("3. Marcar correo como favorito")
    print("4. Desmarcar correo como favorito")
    print("5. Crear Usuario")
    print("6. Bloquear Usuario")
    print("7. Eliminar usuario")
    print("8. Terminar con la ejecución del cliente")
    opcion = int(input("Ingrese opción (1-8): "))
    if opcion == 1:
        respuesta = get_informacion()
        if not respuesta[0]:
            break
        print("Nombre: "+respuesta[1]['nombre'])
        print("Correo: "+respuesta[1]['direccion_correo'])
        print("Descripción: "+respuesta[1]['descripcion'])
    elif opcion == 2:
        print("Aquí está la lista de correos marcados como favorito")
        print(get_favorite(correo, clave))
    elif opcion == 3:
        solicitud_marcar = int(input("Ingrese id_correo_favorito: "))
        respuesta = set_favorite(correo, clave,  solicitud_marcar)
        if not respuesta[0]:
            break
        print("Marcado como favorito exitosamente")
    elif opcion == 4:
        solicitud_desmarcar = 
        
    elif opcion == 5:

    elif opcion == 6:

    elif opcion == 7:

    elif opcion == 8:
        break
print("Se ha finalizado el programa.")
exit()