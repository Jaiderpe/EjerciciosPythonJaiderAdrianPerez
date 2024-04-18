tusciudades=[]

def registrarciudad():
       ciudad = input("Ingrese el nombre de la ciudad: ")
       tusciudades.append({"ciudad": ciudad, "sismos": []})
       print("Ciudad registrada exitosamente.")

def registrarsismo():
    for ciudad in tusciudades:
        registros = []
        n_registros = int(input("Ingrese la cantidad de registros para la ciudad " + ciudad['ciudad'] + ": "))
        for i in range(n_registros):
            magnitud = float(input("Ingrese la magnitud del sismo " + str(i+1) + " de la ciudad " + ciudad['ciudad'] + ": "))
            registros.append(magnitud)
        ciudad['sismos'] = registros

def buscarsismosporciudad():
    ciudad = input("Ingrese el nombre de la ciudad a buscar: ")
    for c in tusciudades:
        if c['ciudad'] == ciudad:
            print("Sismos registrados en la ciudad " + ciudad + ":")
            for i, sismo in enumerate(c['sismos']):
                print("Sismo " + str(i+1) + ": " + str(sismo))
            return
    print("Ciudad no encontrada.")

def informeriesgo():
    for ciudad in tusciudades:
        promedio = sum(ciudad['sismos']) / len(ciudad['sismos'])
        print("Informe de riesgo para la ciudad " + ciudad['ciudad'] + ":")
        if promedio <= 2.5:
            print("Riesgo: Amarillo (Sin riesgo)")
        elif 2.6 <= promedio <= 4.5:
            print("Riesgo: Naranja (Riesgo medio)")
        else:
            print("Riesgo: Rojo (Riesgo alto)")

def menu():
    while True:
        print("\n----- Centro de Prevención de Sismos en Colombia -----")
        print("1. Registrar Ciudad")
        print("2. Registrar Sismo")
        print("3. Buscar sismos por ciudad")
        print("4. Informe de riesgo")
        print("5. Salir")
        opcion = int(input("Seleccione una opción (1-5): "))

        if opcion == 1:
            registrarciudad()
        elif opcion == 2:
            registrarsismo()
        elif opcion == 3:
            buscarsismosporciudad()
        elif opcion == 4:
            informeriesgo()
        elif opcion == 5:
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()