def encontrarMin(lista):
    # paso #1 inicializar variable minimo
    minimo = lista[0]
    # paso #2 Recorrer la lista
    for i in lista:
        # paso #3 Validar si numero actual < minimo actual
        if i < minimo:
            # paso $4 Actualizar el valor para minimo
            minimo = i
    # paso #5 retornar el valor minimo en la lista
    return minimo

#Mejor caso que el numero este en la posicion 1
#Peor Caso que el nuemero este en la posicion 10
#promedio que este en los centros


lista = [1,2,3,4,5,6,7,8,9,10]

print(encontrarMin(lista))

def bigSorting(lista):
    n = len(lista)

    for i in range(n - 1):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
    return lista

print(bigSorting([1,44,3,31415926535384626433832795,5,6,7,8,9,10]))

