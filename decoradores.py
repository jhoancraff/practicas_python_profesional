from datetime import datetime

def ejecutar_tiempo(func):
    def envoltura(*args, **kwargs):
        iniciar_tiempo = datetime.now()
        func(*args, **kwargs)
        fin_tiempo = datetime.now()
        time = fin_tiempo - iniciar_tiempo
        print('Pasaron ' + str( time.total_seconds()) + ' segundos')
    return envoltura

@ejecutar_tiempo
def random():
    for i in range(1, 100000000):
        pass
@ejecutar_tiempo
def suma(a:int, b:int):
    return a + b
    
@ejecutar_tiempo
def saludo(nombre):
    print('hola ', nombre)

random()
suma(4,5)
saludo('jhoan')
