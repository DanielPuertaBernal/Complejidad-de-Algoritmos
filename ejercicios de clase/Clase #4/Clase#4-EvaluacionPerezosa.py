def getfibonacci():
    yield 0
    #yield guarda la funcion para no la ejecuata solo se ejecuta cuando se llama  
    a, b = 0, 1
    while True:
        yield b
        b=a+b
        a=b-a

fibonacci = getfibonacci()
print(type(fibonacci))

print("Primer Número de Fibonacci: ", next(fibonacci))

for num in fibonacci:
    if num > 30:
        break
    print("Siguiente número de Fibonacci: ", num)


