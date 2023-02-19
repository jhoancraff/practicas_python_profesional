import time

class fibona():

    def __init__(self, max=int):
        self.max = 30

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.contador = 0
        return self

    def __next__(self):
        if self.contador == 0:
            self.contador += 1
            return self.n1
        elif self.contador == 1:
            self.contador += 1
            return self.n2
        else: 
            self.result = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self.result
            self.contador += 1
            return self.result

if __name__ == '__main__':
    fibo = fibona()
    for elemento in fibo:
        print(elemento)
        time.sleep(0.5)                        
        
        
