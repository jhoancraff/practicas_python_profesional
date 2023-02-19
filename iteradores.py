class numeros_primos:
    def __init__(self, max=None) -> None:
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if not self.num or self.num <= self.max:
            resultado = self.num
            self.num += 2
            return resultado
        else:
            raise StopIteration    
