import time

def gen(max=int):
    n1 = 1
    n2 = 2
    contador = 0
    yield contador

    while True:
        if contador == 0:
            contador += 1
            yield n1
        elif contador == 1:
            contador += 1
            yield n2
    
        else:
            resultado = n1 + n2
            n1, n2 = n2, resultado
            contador += 1
            yield resultado     

if __name__ == '__main__':
    fibo = gen(max=5)
    for elemento in fibo:
        print(elemento)
        time.sleep(1)            