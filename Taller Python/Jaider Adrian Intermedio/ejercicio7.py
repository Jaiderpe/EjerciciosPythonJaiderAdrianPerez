class producto:
    def __init__(self, codigo, nombre, valordecompra, valordeventa, stockminimo, stockamaximo, proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.valordecompra = valordecompra
        self.valordeventa = valordeventa
        self.stockactual = 0
        self.stockminimo = stockminimo
        self.stockamaximo = stockamaximo
        self.proveedor = proveedor

    def actualizar_stock(self, cantidad):
        self.stockactual += cantidad

    def calcularlagananciapotencial(self):
        return (self.valordeventa - self.valordecompra) * self.stockactual

    def __str__(self):
        return f'Código: {self.codigo}\nNombre: {self.nombre}\nValor de compra: {self.valordecompra}\nValor de venta: {self.valordeventa}\nStock actual: {self.stockactual}\nStock mínimo: {self.stockminimo}\nStock máximo: {self.stockamaximo}\nProveedor: {self.proveedor}\n'


class Inventario:
    def __init__(self):
        self.productos = []

    def agregarproducto(self, producto):
        self.productos.append(producto)

    def mostrarlosproductos(self):
        for producto in self.productos:
            print(producto)

    def actualizar_stock(self, codigo, cantidad):
        for producto in self.productos:
            if producto.codigo == codigo:
                producto.actualizar_stock(cantidad)
                break

    def generarinformedelosproductoscriticos(self):
        productos_criticos = [producto for producto in self.productos if producto.stockactual < producto.stockminimo]
        if productos_criticos:
            print("Productos críticos:")
            for producto in productos_criticos:
                print(producto)
        else:
            print("No hay productos críticos.")

    def calculargananciapotencialtotal(self):
        gananciatotal = 0
        for producto in self.productos:
            gananciatotal += producto.calcularlagananciapotencial()
        return gananciatotal



def main():
    inventario = Inventario()
    producto1 =producto ("008", "Producto 1", 30, 90, 7, 90, "Proveedor 1")
    producto2 =producto ("009", "Producto 2", 55, 85, 7, 90, "Proveedor 2")
    inventario.agregarproducto(producto1)
    inventario.agregarproducto(producto2)

    print("Productos registrados:")
    inventario.mostrarlosproductos()

    inventario.actualizar_stock("008", 30)

    inventario.generarinformedelosproductoscriticos()

    ganancia_total = inventario.calculargananciapotencialtotal()
    print(f"Ganancia potencial total: ${ganancia_total}")


if __name__ == "__main__":
    main()