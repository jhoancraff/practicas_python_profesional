def multipicador(x = str):
    def nombre(string):
        assert type(string) == str, 'esto no es un nombre'
        return string * x
    return nombre

def run():
    nombre2 = multipicador(2)
    print(nombre2('jhoan'))
if __name__ == '__main__':
    run()