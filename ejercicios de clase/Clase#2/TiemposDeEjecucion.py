import time
import sys

def factorial_r(n):
    if n == 0:
        return 1
    else:
        return n * factorial_r(n - 1)

def factorial(n):
    respuesta = 1
    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta

if __name__ == "__main__":
    TimeInicial = time.time()
    factorial(10)
    TimeFinal = time.time()
    print("Tiempo de ejecucion Factorial: ", TimeFinal - TimeInicial)
    TimeInicial = time.time()
    sys.setrecursionlimit(100000)
    factorial_r(10)
    TimeFinal = time.time()
    print("Tiempo de ejecucion Factorial_r: ", TimeFinal - TimeInicial)
