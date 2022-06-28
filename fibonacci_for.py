def main():
    num = int(input('Ingresa un número: '))
    if num < 1:
        print('A partir de 1 por favor')
    else:
        fibo = None
        if num == 1:
            fibo = 1
        else:
            aux1 = 1
            aux2 = 0
            for i in range(1,num):
                fibo = aux1 + aux2
                aux2 = aux1
                aux1 = fibo
        print(f'Fibonacci de {num}: {fibo}')


if __name__ == '__main__':
    main()