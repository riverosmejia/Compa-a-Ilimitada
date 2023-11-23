#esto no sirve de nada siga adelante :p
from user import Usuario_
import json
# Ejemplo de uso
# Crear una instancia de Usuario
usuario1 = Usuario_(nombre="Ejemplo", contraseña="1234",monto=1000000000)

# Convertir la instancia a un diccionario y guardarlo en un archivo JSON
datos_usuario = usuario1.to_dict()
with open('usuario.json', 'w') as archivo_json:
    json.dump(datos_usuario, archivo_json)

# Cargar datos desde el archivo JSON y crear una nueva instancia de Usuario
with open('usuario.json', 'r') as archivo_json:
    datos_cargados = json.load(archivo_json)
    usuario_cargado = Usuario.from_dict(datos_cargados)

# Imprimir los detalles del usuario cargado
print(f"Nombre: {usuario_cargado.nombre}, Contraseña: {usuario_cargado.contraseña}, Monto: {usuario_cargado.monto}")