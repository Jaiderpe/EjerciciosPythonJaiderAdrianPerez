pesoideal = 0
obesidad1 = 0
obesidad2 = 0
obesidad3 = 0
sobrepeso = 0


for i in range(0,20):
    nombre = input(f'\ningrese el nombre del estudiante {i+1}:')
    edad = int(input(f'ingrese la edad:'))
    peso = float(input(f'ingrese el peso:'))
    altura = float(input(f'ingrese la altura:'))
    
    imc = peso //(altura**2)

    print('imc', imc)

if imc <= 18.5:
    pesoideal +=1
elif imc <= 24.9:
    pesoideal +=1
elif imc<= 29.9:
    sobrepeso +=1
elif imc<= 34.9:
    obesidad1 +=1
elif imc<=40:
    obesidad2 +=1
else:
    obesidad3 +=1

print('\nrepote de estudiante')
print('a. peso ideal:',pesoideal)
print('b.  obesidad grado1:',obesidad1 )
print('c.  obesidad grado2:',obesidad2 )
print('d.  obesidad grado3:',obesidad3 )
print('e.  sobrepeso:',sobrepeso )



    

    