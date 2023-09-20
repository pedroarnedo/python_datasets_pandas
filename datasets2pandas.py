import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crear un DataFrame de ejemplo con datos ficticios
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Edad': [25, 30, 35, 40, 45],
    'Puntuación': [85, 92, 78, 88, 95],
    'Ciudad': ['Nueva York', 'Los Ángeles', 'Chicago', 'Houston', 'Miami']
}

df = pd.DataFrame(data)

# Filtrar personas mayores de 30 años
personas_mayores = df[df['Edad'] > 30]

# Calcular la media de las puntuaciones
media_puntuacion = df['Puntuación'].mean()

# Visualizar la distribución de edades
plt.hist(df['Edad'], bins=10, edgecolor='k', alpha=0.65)
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.title('Distribución de Edades')
plt.grid(True)
plt.show()

# Mostrar información básica del DataFrame
print("Información básica del DataFrame:")
print(df.info())

# Guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv('datos_modificados.csv', index=False)

print("Operaciones completadas con éxito.")
