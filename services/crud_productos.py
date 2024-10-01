from database.db_manager import DBManager
from models.producto import ProductoAlimenticio, ProductoElectronico

class CRUDProductos:
    def __init__(self):
        self.db_manager = DBManager()
        self.db_manager.create_tables()

    def crear_producto(self, producto):
        conn = self.db_manager.connect()
        cursor = conn.cursor()
        producto_dict = producto.to_dict()
        
        cursor.execute('''
        INSERT INTO productos (idp, nombre, precio, stock, tipo, fecha_caducidad, potencia_consumida)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            producto_dict['idp'],
            producto_dict['nombre'],
            producto_dict['precio'],
            producto_dict['stock'],
            producto_dict['tipo'],
            producto_dict.get('fecha_caducidad'),
            producto_dict.get('potencia_consumida')
        ))
        
        conn.commit()
        conn.close()
        print(f"Producto guardado exitosamente")

    def leer_producto(self, idp):
        conn = self.db_manager.connect()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM productos WHERE idp = ?', (idp,))
        producto_data = cursor.fetchone()
        
        conn.close()
        
        if producto_data:
            if producto_data[4] == 'alimenticio':
                return ProductoAlimenticio(producto_data[0], producto_data[1], producto_data[2], producto_data[3], producto_data[5])
            else:
                return ProductoElectronico(producto_data[0], producto_data[1], producto_data[2], producto_data[3], producto_data[6])
        else:
            print(f"Producto no encontrado")
            return None

    def actualizar_producto(self, idp, nuevo_precio):
        conn = self.db_manager.connect()
        cursor = conn.cursor()
        
        cursor.execute('UPDATE productos SET precio = ? WHERE idp = ?', (nuevo_precio, idp))
        
        if cursor.rowcount > 0:
            print(f"Precio actualizado correctamente para el producto cuyo ID es: {idp}")
        else:
            print(f"No se encontró ID de producto")
        
        conn.commit()
        conn.close()

    def eliminar_producto(self, idp):
        conn = self.db_manager.connect()
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM productos WHERE idp = ?', (idp,))
        
        if cursor.rowcount > 0:
            print(f"Producto con idp: {idp} eliminado exitosamente")
        else:
            print(f"El producto con idp: {idp} no se encuentra en la BD")
        
        conn.commit()
        conn.close()

    def listar_productos(self):
        conn = self.db_manager.connect()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM productos')
        productos = cursor.fetchall()
        
        conn.close()
        
        print("###############Listado completo de productos#################### ")
        for producto in productos:
            if producto[4] == 'alimenticio':
                print(f"{producto[1]} - Fecha Vencimiento {producto[5]}")
            else:
                print(f"{producto[1]} - Potencia de consumo {producto[6]}")
        print("########################################################## ")