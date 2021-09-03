def main():
    #escribe tu código abajo de esta línea
    a =int(input())
    suma = 0
    for i in range(a):
        b = float(input())
        suma = suma + b
    promedio = suma / a
    print(promedio)
if __name__=='__main__':
    main()
