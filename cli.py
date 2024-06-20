import requests
import json

#implementación de las funciones para realizar consultas a la api
'''
Descripción: Esta función se encarga de encontrar un usuario en la base de datos.
Parámetros:-
Retorno:
Retorna una lista, donde el primer elemento es si la operación fue existosa o no, y el JSON,
de la respuesta.
'''
def get_usuario():
    correo = input("Ingrese correo: ")
    consulta = requests.get('http://localhost:3000/api/get_usuario/'+correo)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if consulta.status_code == 200:
        return [True, dict_data]
    return [False]

'''
Descripción: Obtiene la descripción del usuario.
Parámetros:-
Retorno:
Retorna una lista, donde el primer elemento es si la operación fue existosa o no, y el JSON
de la respuesta.
'''
def get_informacion():
    correo = input("Ingrese correo: ")
    consulta = requests.get('http://localhost:3000/api/informacion/'+correo)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if consulta.status_code == 200:
        return [True, dict_data]
    return [False]

'''
Descripción: Registra un usuario en la base de datos.
Parámetros:
nombre: nombre del usuario.
correo: dirección de correo electrónico.
clave: clave del usuario.
descripcion: descripción del usuario.
Retorno:
Retorna una lista, donde el primer elemento es si la operación fue existosa o no, y el JSON
de la respuesta.
'''
def register_user(nombre, correo, clave, descripcion):
    datos = {'_nombre':nombre, '_correo':correo,'_clave':clave, '_descripcion':descripcion}
    consulta = requests.post('http://localhost:3000/api/registrar/', json=datos)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if consulta.status_code == 200:
        return [True, dict_data]
    return [False]

'''
Descripción: Esta función se encarga de bloquear un usuario en la base de datos.
Parámetros:

correo: direccion de correo electronico del usuario
clave: clave del usuario
correo_bloquear: direccion de correo electronico del usuario a bloquear

Retorno:
Retorna una lista, donde el primer elemento es si la operación fue existosa o no, y el JSON,
de la respuesta.
'''
def block_user(correo, clave, correo_bloquear):
    datos = {'_correo':correo,'_clave':clave, '_correo_bloquear':correo_bloquear}
    consulta = requests.post('http://localhost:3000/api/bloquear/', json=datos)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if consulta.status_code == 200:
        return [True, dict_data]
    return [False]

'''
Descripción: Esta función se encarga de marcar un correo como favorito en la base de datos.
Parámetros:

correo: direccion de correo electronico del usuario
clave: clave del usuario
id_correo_favorito: ID del correo que se desea marcar como favorito

Retorno:
Retorna una lista, donde el primer elemento es si la operación fue existosa o no, y el JSON,
de la respuesta.
'''
def set_favorite(correo, clave,  id_correo_favorito):
    datos = {'_correo':correo,'_clave':clave, '_id': id_correo_favorito}
    consulta = requests.post('http://localhost:3000/api/marcarcorreo/', json=datos)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if consulta.status_code == 200:
        return [True, dict_data]
    return [False]

'''
Descripción: Esta función se encarga de desmarcar (eliminar) de la base de datos un correo favorito.
Parámetros:
correo: direccion de correo electronico del usuario
clave: clave del usuario
id_correo_favorito: ID del correo que se desea desmarcar como favorito
Retorno:
Retorna una lista, donde el primer elemento es si la operación fue existosa o no, y el JSON,
de la respuesta.
'''
def delete_favorite(correo, clave, id_correo_favorito):
    datos = {'_correo':correo,'_clave':clave, '_id': id_correo_favorito}
    consulta = requests.delete('http://localhost:3000/api/desmarcarcorreo/', json=datos)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if consulta.status_code == 200:
        return [True, dict_data]
    return [False]

'''
Descripción: Esta función se encarga de obtener los correos favoritos de un usuario.
Parámetros:
correo: direccion de correo electronico del usuario
clave: clave del usuario
Retorno:
Retorna una lista, donde el primer elemento es si la operación fue existosa o no, y el JSON,
de la respuesta. 
'''
def get_favorite(correo, clave):
    datos = {'_correo':correo,'_clave':clave}
    consulta = requests.post('http://localhost:3000/api/vercorreo/', json=datos)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if consulta.status_code == 200:
        return [True, dict_data]
    return [False]



'''
Descripción: Esta función se encarga de simular el envío de correo, agregandolo en la base de datos si el
usuario lo hizo correctamente.

Parámetros:
correo: direccion de correo electronico del usuario
clave: clave del usuario
asunto : asunto del correo
cuerpo : cuerpo del correo
receptor : correo del usuario que recibe el correo enviado

Retorno:
Retorna una lista, donde el primer elemento es si la operación fue existosa o no, y el JSON,
de la respuesta.
'''
def enviar_correo(correo, clave, asunto, cuerpo, receptor):
    datos = {'_correo':correo,'_clave':clave, '_asunto': asunto, '_cuerpo':cuerpo, '_correo_recibe': receptor}
    consulta = requests.post('http://localhost:3000/api/enviarcorreo/', json=datos)
    json_str = consulta.content.decode('utf-8')
    dict_data = json.loads(json_str)
    if consulta.status_code == 200:
        return [True, dict_data]
    return [False, dict_data]

while(True):
    print("\nBienvenido a CommuniKen")
    print("1. Iniciar Sesion")
    print("2. Registrarse")
    decision = int(input("Ingrese una opción: "))
    if decision == 1:
        busqueda = get_usuario()
        if not busqueda[0]:
            print("No se ha encontrado el correo.")
            print("Se ha finalizado el programa.")
            exit()
        correo = busqueda[1]['direccion_correo']
        clave = busqueda[1]['clave']
        clave = input("Ingrese clave: ")
        if clave != busqueda[1]['clave']:
            print("La contraseña es incorrecta, intentelo de nuevo")
            print("Se ha finalizado el programa.")
            exit()
        print("Se ha iniciado sesión correctamente")
        break
    elif decision == 2:
        nombre_registrar = input("Ingrese nombre del Usuario: ")
        correo_registrar = input("Ingrese correo del Usuario: ")
        clave_regitrar = input("Ingrese la clave del Usuario: ")
        descripcion = input("Ingrese la descripción del usuario: ")
        respuesta = register_user(nombre_registrar, correo_registrar, clave_regitrar, descripcion)
        if "error" in respuesta[1]:
            print(respuesta[1]["error"])
            break
        else:
            print("Usuario creado correctamente.")
            break
    else:
        print("Error, ingrese un número válido.")

# menú de opciones
while True:
    print("\n1. Ver información de una dirección de correo electrónico")
    print("2. Enviar correo")
    print("3. Marcar correo como favorito")
    print("4. Desmarcar correo como favorito")
    print("5. Crear Usuario")
    print("6. Bloquear Usuario")
    print("7. Ver ID's de correos favoritos")
    print("8. Terminar con la ejecución del cliente\n")
    opcion = int(input("Ingrese opción (1-8): "))
    if opcion == 1:
        respuesta = get_informacion()
        if "error" in respuesta[1]:
            print(respuesta[1]["error"])
            break
        else:
            print("Nombre: "+respuesta[1]['nombre'])
            print("Correo: "+respuesta[1]['direccion_correo'])
            print("Descripción: "+respuesta[1]['descripcion'])
    elif opcion == 2:
        receptor_enviar = input("Ingrese correo del usuario destinatario: ")
        asunto_enviar = input("Ingrese asunto del correo: ")
        cuerpo_enviar = input("Ingrese cuerpo del correo: ")
        respuesta = enviar_correo(correo, clave, asunto_enviar, cuerpo_enviar, receptor_enviar)
        if "error" in respuesta[1]:
            print(respuesta[1]["error"])
            break
        else:
            print("Correo enviado correctamente.")
    elif opcion == 3:
        solicitud_marcar = int(input("Ingrese id_correo_favorito: "))
        respuesta = set_favorite(correo, clave,  solicitud_marcar)
        if "error" in respuesta[1]:
            print(respuesta[1]["error"])
            break
        else:
            print("Marcado como favorito exitosamente.")
    elif opcion == 4:
        solicitud_desmarcar = int(input("Ingrese id_correo_favorito: "))
        respuesta = delete_favorite(correo, clave, solicitud_desmarcar)
        if "error" in respuesta[1]:
            print(respuesta[1]["error"])
            break
        else:
            print("Desmarcado como favorito correctamente.")
    elif opcion == 5:
        nombre_registrar = input("Ingrese nombre del Usuario: ")
        correo_registrar = input("Ingrese correo del Usuario: ")
        clave_regitrar = input("Ingrese la clave del Usuario: ")
        descripcion = input("Ingrese la descripción del usuario: ")
        respuesta = register_user(nombre_registrar, correo_registrar, clave_regitrar, descripcion)
        if "error" in respuesta[1]:
            print(respuesta[1]["error"])
            break
        else:
            print("Usuario creado correctamente.")
    elif opcion == 6:
        correo_bloquear = input("Ingrese correo a bloquear: ")
        if correo == correo_bloquear:
            print("No te puedes bloquear a ti mismo.")
            break
        respuesta = block_user(correo, clave, correo_bloquear)
        if "error" in respuesta[1]:
            print(respuesta[1]["error"])
            break
        else:
            print("Usuario bloqueado correctamente.")
    elif opcion == 7:
        respuesta=get_favorite(correo, clave)
        if "error" in respuesta[1]:
            print(respuesta[1]["error"])
            break
        else:
            if len(respuesta[1]) == 0:
                print("No hay correos marcados aún.")
                continue
            print("Aquí está la lista de correos marcados como favorito.")
            for indice in range(len(respuesta[1])):
                print(str(indice+1)+". "+str(respuesta[1][indice]['id_correo_favorito']))
    elif opcion == 8:
        break
    else:
        print("Ingrese una operación válida")
print("Se ha finalizado el programa.")
exit()