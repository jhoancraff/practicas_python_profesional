def is_primo(n:int) -> bool:
    if n % 2 != 0:
        return True
    else:
        return False    

def run():
    print(is_primo(4))

if __name__ == '__main__':
    run()