import sqlite3, bcrypt,os,sys
from PySide6.QtWidgets import *

class Conn():

    # def __init__(self):
    #     self.conexion = sqlite3.connect(database="Modulos\\PRINCIPAL\\BBDD\\BBDD_SGE_PFINAL.db")

    def __init__(self):
        
        self.conexion = sqlite3.connect(database="Modulos\\PRINCIPAL\\BBDD\\BBDD_SGE_PFINAL.db")


    #//////////////////////////////////////////////////////////////////////////////////////////////
    # metodos clientes
    # #

    def mostrarTodosClientes(self):
        try:
            #IMPORTANTE EL WITH PORQUE SI DIERA ERROR LA QUERY PODRIA PETAR TODO
            with self.conexion:
                cursor = self.conexion.cursor()

                query = 'SELECT * from clientes;'
                cursor.execute(query)
                resultados = cursor.fetchall() 
                
                clientes = []
                for columna in resultados:
                    cliente = {
                        "id": columna[0],
                        "nombre": columna[1],
                        "email": columna[2],
                        "telefono": columna[3],
                        "pais": columna[4],
                        "registro": columna[5]
                    }
                    clientes.append(cliente)
                return clientes
                  
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []
    
    def registrarCliente(self,cliente):
        try:
            with self.conexion:
                cursor = self.conexion.cursor()
                query = "INSERT INTO clientes(id_cliente,nombre_cliente,email_cliente,telefono_cliente,pais_cliente,registro_cliente)VALUES(?,?,?,?,?,?)"
                
                cursor.execute(query,cliente)
                self.conexion.commit() 
                
        except sqlite3.Error as e:
            print("Error en la base de datos"f": {e}")
            return None       
    
    def editarCliente(self,cliente_editado,cliente_id):
        try:
            with self.conexion:
                cursor = self.conexion.cursor()
                
                query = f"""
                    UPDATE clientes SET nombre_cliente = ?,email_cliente = ?, telefono_cliente = ?, pais_cliente = ? WHERE id_cliente = '{cliente_id}'
                """
                
                cursor.execute(query, cliente_editado)
                self.conexion.commit()
        
        except sqlite3.Error as e:    
            confirmacion = QMessageBox.question(
            self, 
            "Confirmar", 
            f"{e}",  
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No  
            )
        
            if confirmacion == QMessageBox.Yes:
                return None
    
    def eliminarCliente(self,cliente_id):
        print(cliente_id)
        try:
            with self.conexion:
                cursor = self.conexion.cursor()
                
                query = f"""
                    DELETE from clientes WHERE id_cliente = '{cliente_id}'
                """
                cursor.execute(query)
                self.conexion.commit()
                print("cliente eliminado correctamente")
        
        except sqlite3.Error as e:    
            print(f"Error de base de datos: {e}")
            return None
    
    #//////////////////////////////////////////////////////////////////////////////////////////////
    # metodos proveedores
    # #
    def mostrarTodosProveedores(self):
        try:
            #IMPORTANTE EL WITH PORQUE SI DIERA ERROR LA QUERY PODRIA PETAR TODO
            with self.conexion:
                cursor = self.conexion.cursor()

                query = 'SELECT * from proveedores;'
                cursor.execute(query)
                resultados = cursor.fetchall() 
                
                proveedores = []
                for columna in resultados:
                    proveedor = {
                        "id": columna[0],
                        "nombre": columna[1],
                        "cif": columna[2],
                        "email": columna[3],
                        "telefono": columna[4],
                        "direccion": columna[5],
                        "descripcion": columna[6],
                        "comentario": columna[7]
                    }
                    proveedores.append(proveedor)
                return proveedores
                  
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []

    def registrarProveedor(self,proveedor):
        try:
            with self.conexion:
                cursor = self.conexion.cursor()
                query = "INSERT INTO proveedores(nombre_proveedor,cif_proveedor,email_proveedor,telefono_proveedor,direccion_proveedor,descripcion_proveedor,comentario_proveedor)VALUES(?,?,?,?,?,?,?)"
                
                cursor.execute(query,proveedor)
                self.conexion.commit() 
                
                return True
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return None

    def editarProveedor(self,proveedor_editado,proveedor_id):
        try:
            with self.conexion:
                cursor = self.conexion.cursor()
                query = f"""
                    UPDATE proveedores SET nombre_proveedor = ?, cif_proveedor = ? ,email_proveedor = ?, telefono_proveedor = ?, direccion_proveedor = ?, descripcion_proveedor = ?, comentario_proveedor = ? WHERE id_proveedor = '{proveedor_id}'
                """
                
                cursor.execute(query, proveedor_editado)
                self.conexion.commit()
        
        except sqlite3.Error as e:    
            print(f"Error de base de datos: {e}")
            return None
    
    def eliminarProveedor(self,proveedor_id):
        print(proveedor_id)
        try:
            with self.conexion:
                cursor = self.conexion.cursor()
                
                query = f"""
                    DELETE from proveedores WHERE id_proveedor = '{proveedor_id}'
                """
                cursor.execute(query)
                self.conexion.commit()
                print("Proveedor eliminado correctamente")
        
        except sqlite3.Error as e:    
            print(f"Error de base de datos: {e}")
            return None

    #//////////////////////////////////////////////////////////////////////////////////////////////
    # metodos compras
    # #

    def mostrarTodasCompras(self):
        try:
            #IMPORTANTE EL WITH PORQUE SI DIERA ERROR LA QUERY PODRIA PETAR TODO
            with self.conexion:
                cursor = self.conexion.cursor()

                query = 'SELECT * from compras;'
                cursor.execute(query)
                resultados = cursor.fetchall() 
                
                compras = []
                for columna in resultados:
                    producto = {
                        "id": columna[0],
                        "importe": columna[1],
                        "proveedor": columna[2],
                        "fecha": columna[3],
                        "productos": columna[4],
                        "modoPago":columna[5],
                        "estado":columna[6]
                    }
                    compras.append(producto)
                return compras
                  
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []
        
    def cambiarEstadoCompra(self,id_compra,estado):
        try:
            with self.conexion:
                cursor = self.conexion.cursor()
                
                query = f"""
                    UPDATE compras SET estado_compra = ?
                    WHERE id_compra = '{id_compra}'
                """
                datos = [
                    estado
                ]
                cursor.execute(query, datos)
                self.conexion.commit()
        except:
            print("Estado de la compra no actualizado")

    def registrarCompra(self,compra):
        try:
            with self.conexion:
                cursor = self.conexion.cursor()
                query = "INSERT INTO compras(id_compra,importe_compra,proveedor_compra,fecha_compra,productos_compra,modoPago_compra,estado_compra)VALUES(?,?,?,?,?,?,?)"
                cursor.execute(query,compra)
                self.conexion.commit() 
                
                return True
        except sqlite3.Error as e:
            print(f"Error de base de datos al añadir: {e}")
            return None

    def eliminarCompra(self,cid):
        print(cid)
        try:
            with self.conexion:
                cursor = self.conexion.cursor()
                
                query = f"""
                    DELETE from compras WHERE id_compra = '{cid}'
                """
                cursor.execute(query)
                self.conexion.commit()
                print("Compra eliminada correctamente")
        except:
            print("Hubo problemas al eliminar la compra")

    #//////////////////////////////////////////////////////////////////////////////////////////////
    # metodos productos
    # #
    
    def mostrarTodosProductos(self):
        try:
            #IMPORTANTE EL WITH PORQUE SI DIERA ERROR LA QUERY PODRIA PETAR TODO
            with self.conexion:
                cursor = self.conexion.cursor()

                query = 'SELECT * from productos;'
                cursor.execute(query)
                resultados = cursor.fetchall() 
                
                productos = []
                for columna in resultados:
                    producto = {
                        "id": columna[0],
                        "nombre": columna[1],
                        "stock": columna[2],
                        "precio": columna[3],
                        "iva": columna[4],
                        "coste":columna[5]
                    }
                    productos.append(producto)
                return productos
                  
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []
    
    def registrarProducto(self,producto):
        try:
            with self.conexion:
                cursor = self.conexion.cursor()
                query = "INSERT INTO productos(id_producto,nombre_producto,stock_producto,precio_producto,iva_producto,coste_producto)VALUES(?,?,?,?,?,?)"
                
                cursor.execute(query,producto)
                self.conexion.commit() 
                
                return True
        except sqlite3.Error as e:
            print(f"Error de base de datos al añadir: {e}")
            return None       
    
    def editarProducto(self,producto_editado,producto_id):

        try:
            with self.conexion:
                cursor = self.conexion.cursor()
                
                query = f"""
                    UPDATE productos SET nombre_producto = ?,stock_producto = ?, precio_producto = ?, iva_producto = ?,coste_producto = ? WHERE id_producto = '{producto_id}'
                """
                
                cursor.execute(query, producto_editado)
                self.conexion.commit()
        
        except sqlite3.Error as e:    
            print(f"Error de base de datos: {e}")
            return None
    
    def actualizarStock(self,producto_id,producto_stock):
        try:
            with self.conexion:
                cursor = self.conexion.cursor()
                
                query = f"""
                    UPDATE productos SET stock_producto = {producto_stock} WHERE id_producto = '{producto_id}'
                """
                
                cursor.execute(query)
                self.conexion.commit()
        
        except sqlite3.Error as e:    
            print(f"Error de base de datos: {e}")
            return None

    def eliminarProducto(self,id_producto):
        print(id_producto)
        try:
            with self.conexion:
                cursor = self.conexion.cursor()
                
                query = f"""
                    DELETE from productos WHERE id_producto = '{id_producto}'
                """
                cursor.execute(query)
                self.conexion.commit()
                print("Producto eliminado correctamente")
        
        except sqlite3.Error as e:    
            print(f"Error de base de datos: {e}")
            return None
    
    #//////////////////////////////////////////////////////////////////////////////////////////////
    # metodos empleados
    # #
    
    def mostrarTodosEmpleados(self):
        try:
            #IMPORTANTE EL WITH PORQUE SI DIERA ERROR LA QUERY PODRIA PETAR TODO
            with self.conexion:
                cursor = self.conexion.cursor()

                query = 'SELECT * from empleados;'
                cursor.execute(query)
                resultados = cursor.fetchall() 
                
                empleados = []
                for columna in resultados:
                    empleado = {
                        "id": columna[0],
                        "nombre": columna[1],
                        "departamento": columna[2],
                        "telefono": columna[3],
                        "email": columna[4],
                        "rol":columna[5],
                        "contrasena":columna[6]
                    }
                    empleados.append(empleado)
                return empleados
                  
        except sqlite3.Error as e:
            print(f"Error de base de datos: {e}")
            return []
    
    def registrarEmpleado(self,empleado):
        try:
            with self.conexion:
                cursor = self.conexion.cursor()
                query = "INSERT INTO empleados(id_empleado,nombre_empleado,departamento_empleado,telefono_empleado,email_empleado,rol_empleado,password_empleado)VALUES(?,?,?,?,?,?,?)"
                
                cursor.execute(query,empleado)
                self.conexion.commit() 
                
                return True
        except sqlite3.Error as e:
            print(f"Error de base de datos al añadir: {e}")
            return None
    
    def eliminarEmpleado(self,id_empleado):
        print(id_empleado)
        try:
            with self.conexion:
                cursor = self.conexion.cursor()
                
                query = f"""
                    DELETE from empleados WHERE id_empleado = '{id_empleado}'
                """
                cursor.execute(query)
                self.conexion.commit()
                print("Empleado eliminado correctamente")
        
        except sqlite3.Error as e:    
            print(f"Error de base de datos: {e}")
            return None
        
    def editarEmpleado(self,empleado_editado,id_empleado):
        try:
            
                cursor = self.conexion.cursor()
                
                query = f"""
                    UPDATE empleados SET nombre_empleado = ?,departamento_empleado = ?, telefono_empleado = ?, email_empleado = ?, rol_empleado = ?, password_empleado = ? WHERE id_empleado = '{id_empleado}'
                """
                cursor.execute(query, empleado_editado)
                self.conexion.commit()
        
        except sqlite3.Error as e:    
            print(f"Error de base de datos: {e}")
            return None
    
    #//////////////////////////////////////////////////////////////////////////////////////////////
    # metodos pedido
    # #
    
    def registrarPedido(self,pedido):
        try:
            with self.conexion:
                cursor = self.conexion.cursor()
                query = "INSERT INTO pedidos(id_pedido,importe_pedido,fecha_pedido,cliente_pedido,productos_pedido,modoPago_pedido,descripcion_pedido)VALUES(?,?,?,?,?,?,?)"
                cursor.execute(query,pedido)
                self.conexion.commit() 
                
                return True
        except sqlite3.Error as e:
            print(f"Error de base de datos al añadir: {e}")
            return None
    
    def mostrarTodosPedidos(self):
        try:
            #IMPORTANTE EL WITH PORQUE SI DIERA ERROR LA QUERY PODRIA PETAR TODO
            with self.conexion:
                cursor = self.conexion.cursor()

                query = 'SELECT * from pedidos;'
                cursor.execute(query)
                resultados = cursor.fetchall() 
                
                pedidos = []
                for columna in resultados:
                    pedido = {
                        "id": columna[0],
                        "importe": columna[1],
                        "fecha": columna[2],
                        "cliente": columna[3],
                        "productos": columna[4],
                        "modopago":columna[5]
                    }
                    pedidos.append(pedido)
                return pedidos
        except:
            pass
    
    def eliminarPedido(self,id_pedido):
        
        print(id_pedido)
        try:
            with self.conexion:
                cursor = self.conexion.cursor()
                
                query = f"""
                    DELETE from pedidos WHERE id_pedido = '{id_pedido}'
                """
                cursor.execute(query)
                self.conexion.commit()
                print("Pedido eliminado correctamente")
        
        except sqlite3.Error as e:    
            print(f"Error de base de datos: {e}")
            return None
        #DELETE from "main"."pedidos" WHERE _rowid_ IN ('3');
    
    #//////////////////////////////////////////////////////////////////////////////////////////////
    # metodos proyectos
    # #
    
    def registrarProyecto(self,proyecto):
        try:
            with self.conexion:
                cursor = self.conexion.cursor()
                query = "INSERT INTO proyectos(id_proyecto,nombre_proyecto,empleado_proyecto,descripcion_proyecto,inicio_proyecto,fin_proyecto,estado_proyecto)VALUES(?,?,?,?,?,?,?)"
                cursor.execute(query,proyecto)
                self.conexion.commit() 
                
                return True
        except sqlite3.Error as e:
            print(f"Error de base de datos al añadir: {e}")
            return None
    
    def mostrarTodosProyectos(self):
        try:
            #IMPORTANTE EL WITH PORQUE SI DIERA ERROR LA QUERY PODRIA PETAR TODO
            with self.conexion:
                cursor = self.conexion.cursor()

                query = 'SELECT * from proyectos;'
                cursor.execute(query)
                resultados = cursor.fetchall() 
                
                proyectos = []
                for columna in resultados:
                    pedido = {
                        "id": columna[0],
                        "nombre": columna[1],
                        "empleado": columna[2],
                        "descripcion": columna[3],
                        "inicio": columna[4],
                        "fin":columna[5],
                        "estado":columna[6]
                    }
                    proyectos.append(pedido)
                return proyectos
        except:
            pass
    
    def eliminarProyecto(self,id_proyecto):
        print(id_proyecto)
        try:
            with self.conexion:
                cursor = self.conexion.cursor()
                
                query = f"""
                    DELETE from proyectos WHERE id_proyecto = '{id_proyecto}'
                """
                cursor.execute(query)
                self.conexion.commit()
                print("Pedido eliminado correctamente")
        
        except sqlite3.Error as e:    
            print(f"Error de base de datos: {e}")
            return None
    
    def cambiarEstado(self,id_proyecto,fin_proyecto,estado):
        print(estado,id_proyecto)
        try:
            with self.conexion:
                cursor = self.conexion.cursor()
                
                query = f"""
                    UPDATE proyectos SET fin_proyecto = ?, estado_proyecto = ?
                    WHERE id_proyecto = '{id_proyecto}'
                """
                datos = [
                    estado,
                    fin_proyecto
                ]
                
                #si estado no es tupla se
                cursor.execute(query, datos)
                self.conexion.commit()
        
        except sqlite3.Error as e:    
            print(f"Error de base de datos: {e}")
            return None
            
        
    #//////////////////////////////////////////////////////////////////////////////////////////////
    # metodos de clase
    # #
    
    def cerrarConexion(self):
        if self.conexion:
            self.conexion.close()
    
    def crearBD(self):
        crear_tablas = """
        CREATE TABLE IF NOT EXISTS "clientes" (
        "id_cliente"        TEXT NOT NULL UNIQUE,
            "nombre_cliente"    TEXT NOT NULL,
            "email_cliente"     TEXT UNIQUE,
            "telefono_cliente"  TEXT,
            "pais_cliente"      TEXT,
            "registro_cliente"  TEXT NOT NULL,
            PRIMARY KEY("id_cliente")
        );

        CREATE TABLE IF NOT EXISTS "empleados" (
            "id_empleado"	INTEGER NOT NULL UNIQUE,
            "nombre_empleado"	TEXT NOT NULL,
            "departamento_empleado"	TEXT NOT NULL,
            "telefono_empleado"	TEXT,
            "email_empleado"	TEXT,
            "rol_empleado"	TEXT NOT NULL,
            "password_empleado"	TEXT,
            PRIMARY KEY("id_empleado" AUTOINCREMENT)
        );

        CREATE TABLE IF NOT EXISTS "productos" (
            "id_producto"       TEXT NOT NULL UNIQUE,
            "nombre_producto"   TEXT NOT NULL,
            "stock_producto"    INTEGER NOT NULL CHECK(stock_producto >= 0),
            "precio_producto"   REAL NOT NULL CHECK(precio_producto > 0),
            "iva_producto"      REAL NOT NULL CHECK(iva_producto BETWEEN 0 AND 100),
            "coste_producto"    REAL NOT NULL CHECK(coste_producto > 0),
            PRIMARY KEY("id_producto")
        );
        
        CREATE TABLE IF NOT EXISTS "pedidos" (
            "id_pedido"	TEXT NOT NULL UNIQUE,
            "importe_pedido"	REAL NOT NULL,
            "fecha_pedido"	TEXT NOT NULL,
            "cliente_pedido"	TEXT NOT NULL,
            "productos_pedido"	TEXT NOT NULL,
            "modoPago_pedido"	TEXT NOT NULL,
            "descripcion_pedido" TEXT NOT NULL,
            PRIMARY KEY("id_pedido"),
            CONSTRAINT "ID CLIENTE PEDIDO" FOREIGN KEY("cliente_pedido") REFERENCES "clientes"("id_cliente"),
            CONSTRAINT "PRODUCTOS PEDIDO" FOREIGN KEY("productos_pedido") REFERENCES "productos"("id_producto")
        );
        
        CREATE TABLE IF NOT EXISTS "proyectos" (
            "id_proyecto"	TEXT NOT NULL UNIQUE,
            "nombre_proyecto"	TEXT NOT NULL UNIQUE,
            "empleado_proyecto"	TEXT,
            "descripcion_proyecto"	TEXT,
            "inicio_proyecto"	TEXT NOT NULL,
            "fin_proyecto"	TEXT,
            "estado_proyecto"	TEXT NOT NULL DEFAULT 'En proceso',
            FOREIGN KEY("empleado_proyecto") REFERENCES "empleados"("id_empleado"),
            PRIMARY KEY("id_proyecto") 
        );

        CREATE TABLE IF NOT EXISTS "proveedores" (
            "id_proveedor"	INTEGER NOT NULL UNIQUE,
            "nombre_proveedor"	TEXT NOT NULL,
            "cif_proveedor"	TEXT NOT NULL,
            "email_proveedor"	TEXT NOT NULL,
            "telefono_proveedor"	TEXT,
            "direccion_proveedor"	TEXT,
            "descripcion_proveedor"	TEXT,
            "comentario_proveedor"	TEXT,
            PRIMARY KEY("id_proveedor" AUTOINCREMENT)
        );

        CREATE TABLE "compras" (
            "id_compra"	TEXT NOT NULL UNIQUE,
            "importe_compra"	REAL NOT NULL,
            "proveedor_compra"	TEXT NOT NULL,
            "fecha_compra"	TEXT NOT NULL,
            "productos_compra"	TEXT NOT NULL,
            "modoPago_compra"	TEXT NOT NULL,
            "entregado_compra"	TEXT NOT NULL DEFAULT 'Comprado',
            FOREIGN KEY("productos_compra") REFERENCES "productos"("id_producto"),
            FOREIGN KEY("proveedor_compra") REFERENCES "proveedores"("id_proveedor")
            PRIMARY KEY("id_compra")
        );
        """



        #hash password admin
        hashed = bcrypt.hashpw(b"admin", bcrypt.gensalt()).decode("utf-8") 
        
        # Datos de ejemplo
        datos_ejemplo = {
            "clientes": (
                "CLI-001",
                "Cliente Anónimo",
                "Cliente@email.com",
                "+55 612345678",
                "Brasil",
                "00/00/2025"
            ),
            "empleados": (
                "Admin",
                "Informática",
                "655123456",
                "admin@admin",
                "Admin",
                f"{hashed}"
            ),
            "productos": (
                "PROD-1001",
                "Producto Ficticio",
                200,
                89.99,
                21.0,
                45.50
            ),
            "proveedores": (None,
                "Logística Rápida S.A.",
                "W54321678",
                "logistica@rapidtransporte.es",
                "+34 611 222 333",
                "Polígono Industrial Norte, Valencia",
                "Servicios de transporte de Rodamientos Rodados",
                "Horario de carga: L-V de 8:00 a 18:00"
            )
        }
        #INTRODUCCION DE LOS DATOS
        try:
            cursor = self.conexion.cursor()
                
                #Irear tablas
            cursor.executescript(crear_tablas)
                
                #Insertar datos
            cursor.execute(
                    """INSERT INTO clientes 
                    VALUES (?, ?, ?, ?, ?, ?)""",
                    datos_ejemplo["clientes"]
                )
                
            cursor.execute(
                    """INSERT INTO empleados 
                    (nombre_empleado, departamento_empleado, 
                    telefono_empleado, email_empleado, rol_empleado,password_empleado)
                    VALUES (?, ?, ?, ?, ?, ?)""",
                    datos_ejemplo["empleados"]
                )
                
            cursor.execute(
                    """INSERT INTO productos 
                    VALUES (?, ?, ?, ?, ?, ?)""",
                    datos_ejemplo["productos"]
                )
            
            cursor.execute(
                    """INSERT INTO proveedores
                    VALUES (?,?,?,?,?,?,?,?)""",
                    datos_ejemplo["proveedores"]
            )
            
            self.conexion.commit()    
            print("Base de datos creada con registros de ejemplo!")

        except sqlite3.Error as e:
            print(f"Error al introducir datos: {str(e)} \n Base de datos creada con errores.")
            if self.conexion:
                self.conexion.rollback()
        finally:
            pass