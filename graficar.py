import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pymongo import MongoClient

def graf_datos():
    documento = atmosfera.find_one()  
    resultados = documento["results"]  # Acceder a la parte "results" del documento

    datos = {"probabilityofprecip": [], "relativehumidity": [], "tempc": [], "windspeedkm": []}
    ciudades = []

    for resultado in resultados[:15]: 
        ciudad = resultado.get("name", "Desconocido")
        ciudades.append(ciudad)
        for clave, valor in datos.items():
            if clave in resultado:
                valor.append(float(resultado[clave]))  
            else:
                valor.append(0.0) 
        print(resultado)

    # Crear gráfico
    fig, ax = plt.subplots(figsize=(10, 6))

    num_documentos = len(datos["probabilityofprecip"])

    posiciones = list(range(num_documentos))

    ancho_barra = 0.2

    # Graficar cada conjunto de datos
    for i, (label, valores) in enumerate(datos.items()):
        ax.bar([pos + i * ancho_barra for pos in posiciones], valores, width=ancho_barra, label=label)   
        
    ax.set_xlabel('CIUDAD')
    ax.set_ylabel('DATOS')
    ax.set_title('Comparación de Datos Atmosféricos')
    ax.set_xticks([pos + (num_documentos * ancho_barra) / 2 for pos in posiciones])
    ax.set_xticklabels(ciudades)

    ax.legend()
    ax.grid(True)

    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

    plt.tight_layout()

    plt.show()

# Conexión con la base de datos MongoDB
client = MongoClient("localhost", 27017)
db = client.Pipeline
atmosfera = db.atmosfera

graf_datos()
