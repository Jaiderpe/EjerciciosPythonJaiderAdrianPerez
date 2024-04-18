def main():
    numeros = []
    totalnumeros = 0
    totalpares = 0
    totalimpares= 0
    sumapares= 0
    sumaimpares= 0
    menoeres_10_= 0
    entre20y50=0
    mayores_que_100=0

    while True:
        num = int(input('ingrese un positivo(ingrese un negativo)'))

        if num < 0: 
            break

        numeros.append(num)
        totalnumeros += 1
         
        if num % 2 == 0:
            totalpares +=1
            sumapares += num
        else:
            totalimpares += 1
            sumaimpares += num
        if num < 10:
            menoeres_10_ +=1
        elif 20 <= num <= 50:
            entre20y50 +=1
        elif num > 100:
            mayores_que_100 +=1 
    if totalpares > 0:
            promediopares = sumapares / totalpares
    else:
            promediopares = 0
    if totalimpares > 0:
            promedioinpares = sumaimpares / totalimpares
    else:
            promedioinpares = 0

    print('\nreporte:')
    print('a. total de numeros ingresados:',totalnumeros)
    print('b. total de numeros pares ingresados:',totalimpares)
    print('c. promedio de los numeros pares:',promediopares)
    print('d. promedio de los numeros impares:',promedioinpares)
    print('e. cuantos numeros son menores que 10:',menoeres_10_)
    print('f. cunatos numeros estan entre  20 y 50:',entre20y50)
    print('g. cuantos numeros son menores que 100:',mayores_que_100)

if __name__ == '__main__':
        main()