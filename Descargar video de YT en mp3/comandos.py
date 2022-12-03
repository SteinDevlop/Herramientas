from pytube import YouTube
import os, shutil,time
class commands:
    path_list = "lista amplia.txt"
    path_dowload = "\Download"
    def __init__(self) -> None:
        pass
    @classmethod
    def add_link(cls,url):
        with open(cls.path_list,"a",encoding="utf8") as lista:
            lista.write(url)
    @classmethod
    def one_link(cls,url):
        video = YouTube(url,use_oauth=False,allow_oauth_cache=True)
        video_title = video.title
        video_length = video.length
        video_author = video.author
        print("Proceso de descarga".center(50,"-"))
        print(f"""
        Informacion del video:
        Titulo: {video.title}.
        Duracion: {video.length} Seg.
        Canal: {video.author}.
        """)
        print("Audios disponibles".center(50,"-"))
        filter_video_audio = video.streams.filter(only_audio=True,mime_type="audio/mp4")
        for st in filter_video_audio:
            print(st)
        print("".center(50,"-"))
        #Seleccion de descarga
        try:
            download_choose = int(input("""(si no quere descargarlo, digite cualquier letra)
            numero itag: """))
        except ValueError as e:
            exit()
        except Exception as esxc:
            print(f"Error: {esxc}")
        try:
            stream = video.streams.get_by_itag(download_choose)
        except AttributeError:
            print("Itag seleccionado no es valido.")
        except Exception as e:
            print(f"Error: {type(e)}")
        try:
            stream.download(cls.path_dowload)
        except Exception as e:
            print(f"Error: {type(e)}")
        print("""¡Descarga Finalizada!""")
        time.sleep(10)
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