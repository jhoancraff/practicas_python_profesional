def decoradores(func):
    def envoltura():
        print(('Esto añade a la funcion principal'))
        func()
    return envoltura

def saludos():
    print('hola')

#saludos()
saludos = decoradores(saludos)
saludos()            