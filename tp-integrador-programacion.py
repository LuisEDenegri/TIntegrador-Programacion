# Algoritmos de Busqueda y Ordenamiento en Python
# Nombre: Luis Enrique Denegri

import time

# Funcion de busqueda binaria
def busqueda_binaria(lista, valor):
    """
    Busqueda binaria en una lista ordenada.
    
    Parametros:
    lista: lista de elementos
    valor: elemento a buscar
    
    Retorna:
    La posicion i del elemento si se encuentra, sino -1.
    """
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == valor:
            return medio
        elif lista[medio] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# Bubble Sort
def bubble_sort(lista):
    # Ordena la lista
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
#Se van a estar comparando de a dos elementos y si el primero es mayor que el segundo, se intercambian.
#se cambian de lugar, y se repite el proceso hasta que la lista este ordenada.

# Merge Sort
def merge_sort(lista):
    # Ordena la lista
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1


# Ejemplo de uso
if __name__ == "__main__":
    datos = [34, 7, 23, 32, 5, 62]

    print("Lista original:", datos)

    # Ordenamiento con Bubble Sort
    datos_bubble = datos.copy()
    inicio_bubble = time.time()
    bubble_sort(datos_bubble)
    fin_bubble = time.time()
    print("Ordenado con Bubble Sort:", datos_bubble)
    print("Tiempo Bubble Sort:", round((fin_bubble - inicio_bubble) * 1000, 4), "ms")

    # Ordenamiento con Merge Sort
    datos_merge = datos.copy()
    inicio_merge = time.time()
    merge_sort(datos_merge)
    fin_merge = time.time()
    print("Ordenado con Merge Sort:", datos_merge)
    print("Tiempo Merge Sort:", round((fin_merge - inicio_merge) * 1000, 4), "ms")

    # Busqueda Binaria
    valor_buscar = 23
    posicion = busqueda_binaria(datos_merge, valor_buscar)
    if posicion != -1:
        print(f"El valor {valor_buscar} se encuentra en la posicion {posicion}.")
    else:
        print(f"El valor {valor_buscar} no se encuentra en la lista.")
