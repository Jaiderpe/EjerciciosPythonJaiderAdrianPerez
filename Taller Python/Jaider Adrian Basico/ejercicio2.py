nombres = 0
edad = 0
imc = 0
categoria = 0


for i in range(0,1,1):
    nombre = input(f'ingrese el nombre del estudiante:')
    edad = int(input(f'ingrese la edad:'))
    peso = float(input(f'ingrese el peso:'))
    altura = float(input(f'ingrese la altura:'))
    imc = peso /(altura**2)


print(f'el estudiante:{nombre},con edad:{edad},tiene imc:{imc},su estado es:')
if imc < 24.9:
    print('normal')
elif 25< 29.9:
    print('sobrepeso')
elif 30< 34.9:
    print('obesidad 1')
elif 35< 39.9:
    print('obesidad 2')
elif 39.9< 40:
    print('obesidad 3')