# Algoritmos de Busqueda y Ordenamiento en Python
# Nombre: Luis Enrique Denegri

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

#Bubble Sort
def bubble_sort(lista):

    #Ordena la lista
    
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambio de elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

'''# Se van a estar comparando de a dos elementos y si el primero es mayor que el segundo, se intercambian.'''

#Merge Sort
def merge_sort(lista):
    
    #Ordena una lista 
    
    if len(lista) > 1:
        # se verifica que la lista tenga al menos dos elementos.
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        #se divide la lista en dos mitades (izquierda y derecha).

        merge_sort(izquierda)
        merge_sort(derecha)
        # se llama recursivamente a la función para ordenar cada mitad.
        i = 0
        j = 0
        k = 0
        # se inicializan los indices en 0
        
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
        #Fusiona las listas ordenadas comparando elementos de izquierda y derecha y colocándolos en orden en la lista principal

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        #Agrega los elementos restantes de izquierda o derecha (si quedaron sin comparar)


# Ejemplo de uso
if __name__ == "__main__":
    datos = [34, 7, 23, 32, 5, 62]
    
    print("Lista original:", datos)
    
    # Ordenamiento con Bubble Sort
    datos_bubble = datos.copy()
    bubble_sort(datos_bubble)
    print("Ordenado con Bubble Sort:", datos_bubble)
    
    # Ordenamiento con Merge Sort
    datos_merge = datos.copy()
    merge_sort(datos_merge)
    print("Ordenado con Merge Sort:", datos_merge)
    
    
    # Búsqueda Binaria
    valor_buscar = 23
    posicion = busqueda_binaria(datos_merge, valor_buscar)
    if posicion != -1:
        print(f"El valor {valor_buscar} se encuentra en la posición {posicion}.")
    else:
        print(f"El valor {valor_buscar} no se encuentra en la lista.")
