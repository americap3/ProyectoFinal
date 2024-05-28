import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pymongo import MongoClient

def graf_datos():
    documentos = nasa.find()  # Obtener todos los documentos de la colección
    fechas = []
    titulos = []

    for documento in documentos:
        fecha = documento.get("date", "Fecha desconocida")
        titulo = documento.get("title", "Título desconocido")
        
        fechas.append(fecha)
        titulos.append(titulo)
        print(documento)  

    # Crear gráfico
    fig, ax = plt.subplots(figsize=(10, 6))

    num_documentos = len(fechas)

    posiciones = list(range(num_documentos))

    ancho_barra = 0.5

    # Graficar los datos
    ax.barh(posiciones, [1] * num_documentos, height=ancho_barra, color='skyblue')  
    

    ax.set_yticks(posiciones)
    ax.set_yticklabels([f"{titulo} ({fecha})" for titulo, fecha in zip(titulos, fechas)])
    ax.set_ylabel('Imagen')
    ax.set_title('IMAGEN ASTRÓNOMICA DEL DÍA')
    ax.set_xticks([]) 

    ax.legend().set_visible(False)

    plt.tight_layout()

    plt.show()

# Conexión con la base de datos MongoDB
client = MongoClient("localhost", 27017)
db = client.Pipeline
nasa = db.nasa  

graf_datos()

