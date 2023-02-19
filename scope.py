#def mi_funcion():
    #y = 5
    #print(y)

#y = 5

#def mi_funcion2():
    #print(y)
#z = 5
#def funcion():
    #z = 3
    #print(z)    

z = 9

def ultima():
    z = 7

    def otra():
        z = 4
        print(z)

    otra()
    print(z)

def run():
    ultima()
    print(z)
    


if __name__ == '__main__':
    run()