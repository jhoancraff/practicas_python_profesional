#def main():
    #a = 1

   # def masted():
  #      print(a)

 #   return masted

#mi_funcion = main()
#mi_funcion()

#del(main)
#mi_funcion()

def hacer_multi(x):
    def multiplicador(n):
        return x * n
    return multiplicador

time7 = hacer_multi(7)
time4 = hacer_multi(4)
print(time7(10))
print(time4(5))
print(time7(time4(2)))         