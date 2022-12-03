from comandos import commands as cm
from url import urls as url

def eleccion_2_mensaje():
    print("""1. Añadir un video.
2. Mirar lista de url para descargar.
3. Descargar archivos de la lista.
4. Salir.""")


eleccion_tipo = None
while eleccion_tipo != 5:
    print("".center(50,"-"))
    print("Descargar video de yt en mp3")
    print("".center(50,"-"))
    print("""
    Advertencia : **********""")
    print("".center(50,"-"))
    print("""1. solo un link.
2. Gestionar lista de links. (varios que no estan en una playlist)
3. Playlist.
4. Borrar musica descargada y resetear lista de descarga.
5. Salir.""")
    print("".center(50,"-"))
    try:
        eleccion_tipo = int(input("(1/2/3/4/5): "))
    except Exception as e:
        print(f"Error generado tipo: {type(e)}")
    if eleccion_tipo == 1:
        print("".center(50,"-"))
        link = (str(input("Url del video YT: ")))
        cm.one_link(link)
        print("".center(50,"-"))
    elif eleccion_tipo == 2:
        pass
    elif eleccion_tipo == 3:
        pass
    elif eleccion_tipo == 4:
        print("".center(50,"-"))
        cm.delete_data()
        print("Datos borrados")
        print("".center(50,"-"))
    elif eleccion_tipo == 5:
        exit()