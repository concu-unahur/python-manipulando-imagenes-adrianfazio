import logging
from api import PixabayAPI
import sys
import threading

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

carpeta_imagenes = './imagenes'
query = sys.argv[1]
cantidad = sys.argv[2]

api = PixabayAPI('15310670-a3a8919673e389446095db66b', carpeta_imagenes)

logging.info(f'Buscando imagenes de {query}')
urls = api.buscar_imagenes(query, cantidad)

for u in urls:
  logging.info(f'Descargando {u}')
  # threading.Thread(target=(lambda: api.descargar_imagen(u))).start()
  #threading.Thread(target=api.descargar_imagen, args=[u]).start()
  api.descargar_imagen(u)

print(api.lista_imagenes)