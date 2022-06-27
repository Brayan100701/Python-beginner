def main():
    facto = 1
    num = int(input('Ingresa un numero: '))
    for i in range(1,num+1):
        facto *= i
    print(f'El factorial de {num} es {facto}')


if __name__ == '__main__':
    main()
