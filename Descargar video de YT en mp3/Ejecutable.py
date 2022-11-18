import pytube
import os
def eleccion_tipo_1(url_singular):
    pass
path = os.getcwd()
path_Dowload = path + "/Descargas"
print("Descargar 1 link o varios?")
print("""1 link: 1
varios links (lectura del .txt): 2
Playlist: 3""")
eleccion_tipo = input("(1/2/3): ")
if eleccion_tipo == 1:
    url_singular = str(input("Url Singular: "))

elif eleccion_tipo == 2:
    pass
elif eleccion_tipo == 3:
    pass
else:
    print("Error de ingreso: Seleccione unicamente 1 o 2 o 3.")