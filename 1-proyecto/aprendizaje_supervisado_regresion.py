import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Generar datos de ejemplo
np.random.seed(0)
X = np.random.randint(1, 6, size=(100, 1))  # Números enteros del 1 al 5
y = 10000 + 1000 * X + np.random.randint(0, 1000, size=(100, 1))  # Números entre 10000 y 50000

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Imprimir los datos antes de continuar
print("Conjunto de Entrenamiento:")
print("X_train:\n", X_train)
print("y_train:\n", y_train)

print("\nConjunto de Prueba:")
print("X_test:\n", X_test)
print("y_test:\n", y_test)

# Esperar a que el usuario presione Enter
input("Presiona Enter para continuar...")

# Crear y entrenar el modelo de regresión lineal
modelo_regresion = LinearRegression()
modelo_regresion.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = modelo_regresion.predict(X_test)

# Calcular el error cuadrático medio (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f"Error Cuadrático Medio (MSE): {mse}")

# Visualizar los resultados
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.title('Regresión Lineal Simple')
plt.xlabel('Número de Habitaciones')
plt.ylabel('Precio de la Vivienda')
plt.show()
