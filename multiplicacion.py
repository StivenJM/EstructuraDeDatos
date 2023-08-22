from collections import Counter
import math
import matplotlib.pyplot as plt


def transformaClave(claveString: str):
    resultado = 0
    if len(claveString) > 10:
        claveString = claveString[:10]
    for caracter in claveString:
        resultado = (resultado * 27) + ord(caracter)
    
    return resultado

def dispersion(claveNum, R, M):
    t = (claveNum * R) - math.floor(claveNum * R)
    v = int(M * t)
    return v

# Primero se obtiene una lista de strings que serviran como valores de clave
with open("texto.txt", "r", encoding="utf-8") as file_object:
    leer = file_object.read()
    lineas = leer.splitlines()

listaValores = list()
R = 0.618024
M = 1024
for linea in lineas:
    claveNum = transformaClave(linea)
    listaValores.append(dispersion(claveNum, R, M))

# Calcular la frecuencia de cada posición en la tabla hash
frecuencia = Counter(listaValores)

# Crear el gráfico de histograma
plt.figure(figsize=(10, 6))

# Generar el histograma
plt.bar(frecuencia.keys(), frecuencia.values(), color='blue', width=1)

# Configuración del eje X
plt.xlim(0, 1023)
plt.xlabel('Posiciones en la Tabla Hash')
plt.ylabel('Frecuencia')

# Título
plt.title('Distribución de Frecuencia en Tabla Hash para metodo de la multiplicación')

# Mostrar el gráfico
plt.show()



