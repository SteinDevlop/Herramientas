import pytube
import os, shutil
class commands:
    path_list = "lista amplia.txt"
    path_dowload = "Download"
    def __init__(self) -> None:
        pass
    @classmethod
    def add_link(cls,url):
        with open(cls.path_list,"a",encoding="utf8") as lista:
            lista.write(url)
    def one_link(url):
        pass #aca deberia descargar en formato .mp3 el link y guardarlo en download


    def multiple_links(url):
        pass
        #Descarga varios videos en .mp3 y lo guarda en una carpeta en download


    def playlist(url):
        pass
    
    @classmethod
    def delete_data(cls):
        #Borrar el contenido de la carpeta download
        for filename in os.listdir(cls.path_dowload):
            file_path = os.path.join(cls.path_dowload, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
        #limpiar el contenido del archivo .txt
        with open(cls.path_list,"w",encoding="utf8"):
            pass