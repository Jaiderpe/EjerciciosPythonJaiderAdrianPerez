class Dependencia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.consumo_electricidad = 0

    def registrar_consumo(self, consumo):
        self.consumo_electricidad += consumo


def registrar_dependencia(dependencias):
    nombre_dependencia =input("Ingrese el nombre de la dependencia: ")
    MIdependencia = Dependencia (nombre_dependencia)
    dependencias.append(MIdependencia)
    print("Dependencia registrada con exito.")


def registrar_consumo_por_dependencia(dependencias):
    if not dependencias:
        print("Primero debe registrar al menos una dependencia.")
        return

    nombre_dependencia = input("Ingrese el nombre de la dependencia: ")
    for dependencia in dependencias:
        if dependencia.nombre.lower() == nombre_dependencia.lower():
            consumo = float(input(f"Ingrese el consumo de electricidad para {dependencia.nombre.lower()}: "))
            dependencia.registrar_consumo(consumo)
            print("Consumo registrado con éxito.")
            return
    print("Dependencia no encontrada.")


def ver_co2_producido(dependencias):
    total_co2 = sum(dependencia.consumo_electricidad * 0.537 for dependencia in dependencias)
    print(f"La cantidad total de CO2 producida es: {total_co2:.2f} kg")


def dependencia_mayor_co2(dependencias):
    if not dependencias:
        print("No hay dependencias registradas.")
        return

    mayor_co2 = max(dependencias, key=lambda dependencia: dependencia.consumo_electricidad * 0.537)
    print(f"La dependencia que produce mayor CO2 es: {mayor_co2.nombre}")


def menu():
    dependencias = []

    while True:
        print("\nMenú:")
        print("1. Registrar Dependencia")
        print("2. Registrar consumo por dependencia")
        print("3. Ver CO2 producido")
        print("4. Dependencia que produce mayor CO2")
        print("5. Salir")

        opcion = input("Ingrese el número de la opción que desea: ")

        if opcion == "1":
            registrar_dependencia(dependencias)
        elif opcion == "2":
            registrar_consumo_por_dependencia(dependencias)
        elif opcion == "3":
            ver_co2_producido(dependencias)
        elif opcion == "4":
            dependencia_mayor_co2(dependencias)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 5.")


if __name__== "__main__":
 menu()