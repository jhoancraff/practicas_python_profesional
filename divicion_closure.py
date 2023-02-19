def divicion(x):
    def divisor(n):
        assert type(x) == int, 'no es un numero'
        return x / n
    return divisor

def run():
    resultado24 = divicion(23)
    print(resultado24(2) )
    resultado12 = divicion(12)
    print(resultado12(4))

if __name__ == '__main__':
    run()        
