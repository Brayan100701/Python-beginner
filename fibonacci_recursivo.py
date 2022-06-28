def fibonacci(num):
    num = fibonacci(num-1) + fibonacci(num-2) if num>1 else num
    return num


def main():
    num = int(input('Ingresa un número: '))
    fibo = fibonacci(num)
    print(f'Fibonacci de {num}: {fibo}')


if __name__ == '__main__':
    main()