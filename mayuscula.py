def mayuscula(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura
@mayuscula
def mensaje(nombre):
    return f'{nombre},  recibistes un mensaje'   
print(mensaje('cesar'))            