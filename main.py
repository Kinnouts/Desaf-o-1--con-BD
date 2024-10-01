import os
import platform
from models.producto import ProductoAlimenticio, ProductoElectronico
from services.crud_productos import CRUDProductos

def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def mostrar_menu():
    print("========== Menú de Gestión de Productos ==========")
    print('1-Agregar producto alimenticio')
    print('2-Agregar producto electrónico')
    print('3-Buscar producto por ID')
    print('4-Modificar precio de producto')
    print('5-Eliminar producto')
    print('6-Listar productos')
    print('0-Salir')

def agregar_producto(gestion, tipo_producto):
    try:
        idp = input("Ingrese ID del producto: ")
        nombre = input("Ingrese nombre del producto: ")
        stock = int(input("Ingrese stock del producto: "))
        precio = float(input("Ingrese precio de venta del producto: "))
        
        if tipo_producto == '1':  # Alimenticio
            fecha_caducidad = input("Ingrese fecha de vencimiento del producto (YYYY-MM-DD): ")
            producto = ProductoAlimenticio(idp, nombre, precio, stock, fecha_caducidad)
        elif tipo_producto == '2':  # Electrónico
            potencia_consumida = int(input("Ingrese la potencia que consume este producto: "))
            producto = ProductoElectronico(idp, nombre, precio, stock, potencia_consumida)
        else:
            print("Opción inválida")
            return
        
        gestion.crear_producto(producto)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    input("Presione enter para continuar")

def buscar_producto_por_idp(gestion):
    idp = int(input("Ingrese el ID del producto a buscar: "))
    producto = gestion.leer_producto(idp)
    if producto:
        print(f"Producto encontrado: {producto.nombre}")
    input("Presione enter para continuar...")

def actualizar_precio_producto(gestion):
    idp = int(input("Ingrese el ID del producto cuyo precio desea modificar: "))
    precio = float(input("Ingrese el nuevo valor de precio que desea asociarle: "))
    gestion.actualizar_producto(idp, precio)
    input("Presione enter para continuar")

def eliminar_producto_por_idp(gestion):
    idp = int(input("Ingrese el ID del producto que desea eliminar: "))
    gestion.eliminar_producto(idp)
    input("Presione enter para continuar")

def main():
    gestion_prod = CRUDProductos()
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1' or opcion == '2':
            agregar_producto(gestion_prod, opcion)
        elif opcion == '3':
            buscar_producto_por_idp(gestion_prod)
        elif opcion == '4':
            actualizar_precio_producto(gestion_prod)
        elif opcion == '5':
            eliminar_producto_por_idp(gestion_prod)
        elif opcion == '6':
            gestion_prod.listar_productos()
            input("Presione enter para continuar")
        elif opcion == '0':
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida")
            input("Presione enter para continuar")

if __name__ == "__main__":
    main()