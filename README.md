# 🚀 Trabajo Integrador - Programacion - Ordenamiento y Busqueda en Python

📌 **Descripcion**

Este proyecto presenta una implementacion practica de **algoritmos de busqueda y ordenamiento** en Python. El objetivo es aplicar conceptos teoricos y analizar la eficiencia de diferentes algoritmos.

---

## 📚 Desarrollo del tema

### 🔍 Algoritmos de Busqueda

Los algoritmos de busqueda son procedimientos para localizar un elemento en una estructura de datos. Los principales son:

- **Busqueda Secuencial (Lineal)**: recorre la lista elemento por elemento. Su eficiencia es O(n).
- **Busqueda Binaria**: funciona sobre listas ordenadas y utiliza el metodo de divide y venceras. Divide la lista en dos mitades en cada iteracion. Su eficiencia es O(log n).

### 🔄 Algoritmos de Ordenamiento

Los algoritmos de ordenamiento organizan elementos en una lista segun un criterio determinado. Los principales son:

- **Bubble Sort**: compara elementos adyacentes y los intercambia si estan desordenados. Su eficiencia es O(n²).
- **Insertion Sort**: inserta cada elemento en la posicion correcta de la sublista ordenada. Eficiencia O(n²).
- **Selection Sort**: busca el minimo y lo coloca en la posicion correcta. Eficiencia O(n²).
- **Merge Sort**: divide la lista en mitades y las fusiona ordenadas. Eficiencia O(n log n).
- **Quick Sort**: selecciona un pivote y divide la lista en menores y mayores, aplicando recursividad. Eficiencia promedio O(n log n).

### ⚖️ Comparacion de Algoritmos

| Algoritmo       | Mejor Caso | Peor Caso | Eficiencia Promedio | Estabilidad |
|-----------------|------------|-----------|----------------------|-------------|
| Bubble Sort     | O(n)       | O(n²)     | O(n²)                | Si          |
| Insertion Sort  | O(n)       | O(n²)     | O(n²)                | Si          |
| Selection Sort  | O(n²)      | O(n²)     | O(n²)                | No          |
| Merge Sort      | O(n log n) | O(n log n)| O(n log n)           | Si          |
| Quick Sort      | O(n log n) | O(n²)     | O(n log n)           | No          |

---

## 📂 Estructura del proyecto

- 📝 **trabajo-integrador-programacion.py**  
  Contiene la implementacion de:
  - 🔍 Busqueda Binaria
  - 🔄 Bubble Sort
  - 🔗 Merge Sort
  - ⚡ Quick Sort

- 📄 **README.md**  
  Documentacion del proyecto, desarrollo del tema, instrucciones de uso y reflexion.

---

## 🛠️ Instrucciones de uso

1. Ejecutar el archivo **trabajo-integrador-programacion.py** en un entorno de Python 3.
2. El script mostrara:
   - 📊 La lista original de datos.
   - 📈 Los resultados de ordenamiento con cada algoritmo.
   - ⏱️ El tiempo de ejecucion (en milisegundos) para cada metodo de ordenamiento.
   - 🔎 El resultado de la busqueda binaria.

---

## 💡 Reflexion

Durante el desarrollo del proyecto, implementamos y analizamos algoritmos de ordenamiento y busqueda para comprender su funcionamiento y eficiencia. Medimos los tiempos de ejecucion para comparar el rendimiento y evidenciar las diferencias entre algoritmos de complejidad **O(n²)** y **O(n log n)**. Este analisis nos permitio seleccionar el algoritmo mas adecuado segun el tamaño y caracteristicas de la lista a ordenar.

---

## 👥 Integrante

- Luis Enrique Denegri
