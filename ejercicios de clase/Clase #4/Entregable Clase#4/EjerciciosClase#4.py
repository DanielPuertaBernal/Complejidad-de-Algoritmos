#Ejecicios Clase #4 Complejidad de algoritmos
#Daniel Puerta Bernal

#Ejercicio#1 Palindrome Number
#Link https://leetcode.com/problems/palindrome-number/description/

def numPalindromo(n):
    #pasamos el número a texto
    numNormal = str(n) #O(1)
    #pasamos el número a texto de forma inversa
    numReverse = numNormal[::-1] #O(1)
    #comparamos los dos números y validamos
    if numNormal == numReverse: #O(1)
        return True #O(1)
    else:
        return False #O(1)
#ejecutamos
print(numPalindromo(121))

#Conclución: para este caso sea verdadero o falso tenemos un Big O constate de 4 (O(4))

#Ejercicio#2 Remove Duplicates from Sorted Array
#link https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

def EliminarDuplicados(nums):
    k = 1 #O(1)
    #Recorrer el arreglo de números
    for i in range(1, len(nums)): #O(n)
        #Se verifica si el elemento actual es diferente del anterio
        if nums[i] != nums[i - 1]: #O(1)
            #k mantiene la posición donde deben estar los valores únicos en el array
            nums[k] = nums[i] #O(1)
            k += 1 #O(1)

    return k #0(1)

nums = [0,0,1,1,1,2,2]
print(EliminarDuplicados(nums))

#Conclución: este ejecicio tiene un Big O de O(n) + 0(5) es decir que tiene un big O de O(n)

#Ejercicio#3 Remove Element
#link https://leetcode.com/problems/remove-element/description/

def removeElement(nums, val):
    k = 0  #O(1)

    # Recorremos el arreglo completo
    for i in range(len(nums)):  # O(n)
        if nums[i] != val:  # O(1)
            nums[k] = nums[i]  # O(1)
            k += 1  # O(1)

    return k  # O(1)

nums = [3,2,2,3]
print(removeElement(nums, 3))

#Conclucion: Este ejercicio tiene un Big O de O(n) + O(5) es decir tiene un Big O de 0(n)

#Ejercicio#4 Letter Combinations of a Phone Number
#Link https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

def comninacionTeclado(digitos):
    mapa_teclado = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    } #O(1)

    # Lista inicial con una cadena vacía para generar combinaciones
    resultado = [""] #O(1)

    # Recorremos cada dígito en la entrada
    for digito in digitos: #O(n)
        letras_actuales = mapa_teclado[digito] #O(1)
        nuevo_resultado = [] #(1)

        # Generamos nuevas combinaciones agregando cada letra posible
        for combinacion in resultado: #O(n)
            for letra in letras_actuales: #O(n)
                nuevo_resultado.append(combinacion + letra)  #O(1)

        # Actualizamos el resultado con las nuevas combinaciones generadas
        resultado = nuevo_resultado #O(1)

    return resultado #O(1)

print(comninacionTeclado("33"))

#Conclución: Este ejercicio tiene un Big O de O(n^2) + O(n) + 0(7) es decir tiene un Big O de 0(n^2)