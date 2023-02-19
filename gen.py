def gen():
    print('hola mundo')
    n = 0
    yield 0

    print('hola a todos')
    n = 1
    yield n

    print('holaaa')
    n = 2
    yield n

a = gen()

print(next(a))
print(next(a))
print(next(a))
print(next(a))