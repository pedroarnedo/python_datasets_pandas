# código de ejemplo que carga un conjunto de datos y realiza algunas operaciones básicas

pip install pandas

import pandas as pd

# Leer el conjunto de datos (reemplaza 'tu_dataset.csv' con la ubicación de tu archivo CSV)
df = pd.read_csv('tu_dataset.csv')

# Mostrar las primeras filas del DataFrame
print(df.head())

# Resumen estadístico del conjunto de datos
print(df.describe())

# Seleccionar una columna específica
columna_seleccionada = df['nombre_de_la_columna']

# Filtrar filas basadas en una condición
filtro = df[df['nombre_de_la_columna'] > 50]

# Agrupar y resumir datos
agrupado = df.groupby('columna_de_agrupación')['columna_de_interés'].mean()

# Visualización básica de datos (requiere Matplotlib o Seaborn)
import matplotlib.pyplot as plt

# Histograma de una columna
plt.hist(df['nombre_de_la_columna'], bins=10)
plt.xlabel('Etiqueta X')
plt.ylabel('Etiqueta Y')
plt.title('Histograma')
plt.show()
