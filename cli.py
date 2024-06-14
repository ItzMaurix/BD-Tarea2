import requests
def get_usuario():
    correo = input("Ingrese correo: ")
    consulta = requests.get('http://localhost:3000/existe-usuario/'+correo)
    if int(consulta.content) == 1:
        return True
    return False
#clave = input("Ingrese clave: ")
while True:
    if get_usuario():
        break
    print("Correo no encontrado")