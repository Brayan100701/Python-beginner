def factorial(num):
    num *= factorial(num-1) if num>1 else num 
    return num


def main():
    num = int(input('Ingresa un número: '))
    facto = factorial(num)
    print(f'El factorial de {num} es {facto}')


if __name__ == '__main__':
    main()
