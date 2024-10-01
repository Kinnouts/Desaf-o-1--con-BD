from abc import ABC, abstractmethod
from datetime import datetime

class Producto(ABC):
    def __init__(self, idp, nombre, precio, stock):
        self.idp = self.validar_idp(idp)
        self.nombre = self.validar_nombre(nombre)
        self.precio = self.validar_precio(precio)
        self.stock = self.validar_stock(stock)

    @staticmethod
    def validar_idp(idp):
        try:
            idp_num = int(idp)
            if idp_num <= 0:
                raise ValueError("El número ingresado de ID debe ser positivo")
            return idp_num
        except ValueError:
            raise ValueError("Debe ingresar un número entero positivo para ID de producto")

    @staticmethod
    def validar_nombre(nombre):
        if not nombre.replace(" ", "").isalpha():
            raise ValueError("El nombre del producto debe contener sólo letras")
        return nombre

    @staticmethod
    def validar_precio(precio):
        try:
            precio_num = float(precio)
            if precio_num <= 0:
                raise ValueError("El valor del precio asignado al producto debe ser positivo")
            return precio_num
        except ValueError:
            raise ValueError("El precio asignado debe ser un número positivo")

    @staticmethod
    def validar_stock(stock):
        try:
            stock_num = int(stock)
            if stock_num < 0:
                raise ValueError("El número ingresado de stock no puede ser negativo")
            return stock_num
        except ValueError:
            raise ValueError("Debe ingresar un número entero para stock")

    @abstractmethod
    def to_dict(self):
        pass

class ProductoAlimenticio(Producto):
    def __init__(self, idp, nombre, precio, stock, fecha_caducidad):
        super().__init__(idp, nombre, precio, stock)
        self.fecha_caducidad = self.validar_fecha(fecha_caducidad)

    @staticmethod
    def validar_fecha(fecha_caducidad):
        try:
            fecha = datetime.strptime(fecha_caducidad, '%Y-%m-%d')
            if fecha <= datetime.now():
                raise ValueError("La fecha de caducidad debe ser una fecha futura.")
            return fecha.strftime('%Y-%m-%d')
        except ValueError as e:
            raise ValueError("Formato de fecha inválido. Use 'YYYY-MM-DD'.") from e

    def to_dict(self):
        return {
            "idp": self.idp,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "tipo": "alimenticio",
            "fecha_caducidad": self.fecha_caducidad
        }

class ProductoElectronico(Producto):
    def __init__(self, idp, nombre, precio, stock, potencia_consumida):
        super().__init__(idp, nombre, precio, stock)
        self.potencia_consumida = self.validar_potencia(potencia_consumida)

    @staticmethod
    def validar_potencia(potencia):
        try:
            potencia_num = int(potencia)
            if potencia_num < 0:
                raise ValueError("El valor de potencia debe ser positivo")
            return potencia_num
        except ValueError:
            raise ValueError("El valor de potencia ingresado debe ser un número entero")

    def to_dict(self):
        return {
            "idp": self.idp,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "tipo": "electronico",
            "potencia_consumida": self.potencia_consumida
        }