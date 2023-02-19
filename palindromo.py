import string


def is_palindromo(palabra:str) -> bool:
    palabra = palabra.replace(' ', ' ').lower()
    return palabra == palabra[::-1]


def run():
    palabra = input('palabra: ')
    print(is_palindromo(palabra))
    


if __name__ == '__main__':
    run()