from Modulos.PRINCIPAL.imports.core import *
from Modulos.PRINCIPAL.imports.widgets_import import *
from Modulos.PRINCIPAL.imports.bbdd_conn import *
import traceback

import matplotlib.pyplot as plt
import pandas as pd

#PEDIDOS
#-----------------------------------------------------------------
def pedidosPorFecha(self):
    try:
        conexion = Conn()
        pedidos = conexion.mostrarTodosPedidos()
        # [{'id': '19022025jczZHzb', 'importe': 302.5, 'fecha': '19/02/2025, 12:38:08', 'cliente': '9fa3e4a5-f', 'productos': 'METAL-55ecc: 5 unidades', 'modopago': 'Tarjeta'}, {'id': '19022025LvnayXG', 'importe': 48.4, 'fecha': '19/02/2025, 12:58:44', 'cliente': '8771281237', 'productos': 'CUADRO-123554: 4 unidades', 'modopago': 'Efectivo'}]
        counter = {}
        
        for pedido in pedidos:
            #fecha sin la hora
            fecha_completa = pedido['fecha']
            fecha = fecha_completa.split(',')[0].strip()
            counter[fecha] = counter.get(fecha, 0) + 1

        graficoPedidosPorFecha(counter)   
    
    except Exception:
        print(traceback.format_exc())
    conexion.cerrarConexion()

def pedidosObtenerProductos():
    # [{'id': '19022025jczZHzb', 'importe': 302.5, 'fecha': '19/02/2025, 12:38:08', 'cliente': '9fa3e4a5-f', 'productos': 'METAL-55ecc: 5 unidades', 'modopago': 'Tarjeta'}, {'id': '19022025LvnayXG', 'importe': 48.4, 'fecha': '19/02/2025, 12:58:44', 'cliente': '8771281237', 'productos': 'CUADRO-123554: 4 unidades', 'modopago': 'Efectivo'}]
    total_productos = {}
    try:
        conexion = Conn()
        pedidos = conexion.mostrarTodosPedidos()
        for pedido in pedidos:
            productos_str = pedido.get('productos', '')
            lineas_productos = productos_str.splitlines()
            
            for linea in lineas_productos:
                if not linea.strip():
                    continue
                if ": " in linea:
                    id_producto, resto = linea.split(": ", 1) 
                    partes = resto.split()
                    if partes:
                        try:
                            cantidad = int(partes[0])
                        except (ValueError, IndexError):
                            cantidad = 0
                        
                        #acumula la cantidad por producto
                        total_productos[id_producto] = total_productos.get(id_producto, 0) + cantidad
    except Exception as e:
        print(f"Error procesando pedidos: {e}")
    finally:
        conexion.cerrarConexion()
        
    conexion.cerrarConexion()            
    return total_productos            

def graficoPedidosPorFecha(datos_ventas):
    df = pd.DataFrame(list(datos_ventas.items()), columns=['Fecha', 'Ventas'])
    df = df.sort_values('Ventas', ascending=False)
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    axs[0].pie(df['Ventas'], 
              labels=df['Fecha'], 
              autopct='%1.1f%%',
              startangle=90,
              textprops={'fontsize': 8})
    axs[0].set_title('Ventas porcentuales por fecha', fontsize=12)

    bars = axs[1].bar(df['Fecha'], df['Ventas'], color='#4C72B0')
    axs[1].set_title('Cantidad de ventas por fecha', fontsize=12)
    axs[1].set_xlabel('Fecha', fontsize=10)
    axs[1].set_ylabel('Número de ventas', fontsize=10)
    axs[1].tick_params(axis='x', rotation=45)

    for bar in bars:
        height = bar.get_height()
        axs[1].text(bar.get_x() + bar.get_width()/2., 
                   height + 0.02,
                   f'{int(height)}',
                   ha='center', 
                   va='bottom',
                   fontsize=9)

    plt.tight_layout()
    plt.show()

#BALANCE
#-----------------------------------------------------------------
def calcularGanancias():
    try:
        conexion = Conn()
        productos = conexion.mostrarTodosProductos()  # Lista de productos
        pedidos = pedidosObtenerProductos()  # Diccionario {id_producto: cantidad}

        productos_dict = {p['id']: p for p in productos}
        
        ganancia_total = 0.0
        coste_total = 0.0
        
        for producto_id, cantidad in pedidos.items():
            if producto_id in productos_dict:
                producto = productos_dict[producto_id]

                ganancia_total += producto['precio'] * cantidad
                coste_total += producto['coste'] * cantidad

        conexion.cerrarConexion()
        return [ganancia_total,coste_total]
        
    except Exception as e:
        print(f"Error: {e}")
        return None   
        
def graficoGananciasYProducto():
    try:

        ganancia_total, coste_total = calcularGanancias()
        productos = pedidosObtenerProductos()

        fig, axs = plt.subplots(1, 2, figsize=(13, 6))
        
        valores = [ganancia_total, coste_total]
        total = ganancia_total + coste_total
        
        axs[0].pie(valores,
                 labels=[f'Beneficios\n{ganancia_total:.2f}€', f'Costes\n{coste_total:.2f}€'],
                 colors=['#99d3aa', '#ff9999'],
                 autopct=lambda p: f'{p:.1f}%',
                 explode=(0.05, 0),
                 startangle=90,
                 wedgeprops={'linewidth': 1, 'edgecolor': 'white'})
        
        axs[0].set_title(f'Relación Beneficios/Costes\nTotal Ingresos: {total:.2f}€', pad=20)

        df = pd.DataFrame(list(productos.items()), columns=['Producto', 'Cantidad'])
        df = df.sort_values('Cantidad', ascending=False)
        
        markerline, stemlines, baseline = axs[1].stem(
            df.index,
            df['Cantidad'],
            linefmt='C0-',
            markerfmt='C0o',
            basefmt='k-'
        )

        axs[1].set_title('Unidades vendidas por producto', pad=15)
        axs[1].set_xticks(df.index)
        axs[1].set_xticklabels(df['Producto'], rotation=45, ha='right')
        axs[1].set_ylabel('Unidades vendidas')
        axs[1].grid(axis='y', alpha=0.3)

        for i, valor in enumerate(df['Cantidad']):
            axs[1].text(i, valor + 0.1, str(valor),
                        ha='center', 
                        va='bottom',
                        fontsize=9)
        
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"Error al generar gráficos: {e}")

#INVENTARIO        
#-----------------------------------------------------------------
def productosPorStock():
    try:
        conexion = Conn()
        productos = conexion.mostrarTodosProductos()

        nombres = []
        costes_totales = []
        valores_totales = []

        for producto in productos:
            coste_total = producto['coste'] * producto['stock']
            valor_total = producto['precio'] * producto['stock']
            
            nombres.append(producto['nombre'])
            costes_totales.append(coste_total)
            valores_totales.append(valor_total)
        
        # Calcular totales
        total_costes = sum(costes_totales)
        total_valores = sum(valores_totales)
        
        fig,(ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        ax1.pie(
            costes_totales,
            labels=nombres,
            autopct=lambda p: f'{p:.1f}%',
            startangle=90,
            shadow=True,
            wedgeprops={'linewidth': 1, 'edgecolor': 'white'},
            textprops={'fontsize': 12}
        )
        ax1.set_title(f'Coste total de la mercancía\n(Total: {total_costes:.2f}€)', pad=12)

        ax2.pie(
            valores_totales,
            labels=nombres,
            autopct=lambda p: f'{p:.1f}%',
            startangle=90,
            shadow=True,
            wedgeprops={'linewidth': 1, 'edgecolor': 'white'},
            textprops={'fontsize': 12}
        )
        ax2.set_title(f'Valor total de la mercancía\n(Total: {total_valores:.2f}€)', pad=12)
        
        plt.tight_layout()
        plt.show()
        conexion.cerrarConexion()
    except Exception as e:
        print(f"Error: {e}")

#TENDENCIAS        
#----------------------------------------------------------------- 
def contarModosPago():
    conexion = Conn()
    pedidos = conexion.mostrarTodosPedidos()
    #{'id': '02032025HSaQjaE', 'importe': 66.55, 'fecha': '02/03/2025, 19:44:55', 'cliente': 'CLI-001', 'productos': 'ROD-286ac: 10 unidades', 'modopago': 'Tarjeta'}, {'id': '02032025SYpTGtQ', 'importe': 55.0, 'fecha': '02/03/2025, 21:00:40', 'cliente': 'CLI-001', 'productos': 'PEZ-02b14: 5 unidades', 'modopago': 'Tarjeta'}, {'id': '03032025zDTwdEt', 'importe': 142.4, 'fecha': '03/03/2025, 01:06:02', 'cliente': 'CLI-001', 'productos': 'PEL-59807: 4 unidades\nPEZ-02b14: 2 unidades\nROD-286ac: 5 unidades', 'modopago': 'Tarjeta'}]
    efectivo = 0
    tarjeta = 0
    
    for pedido in pedidos:
        if pedido['modopago'] == 'Efectivo':
            efectivo += 1
        elif pedido['modopago'] == 'Tarjeta':
            tarjeta += 1
                    
    modosPago = {'Efectivo': efectivo,'Tarjeta': tarjeta}
    
    #{'Efectivo': 4, 'Tarjeta': 6}
    return modosPago

def productosPorPedido():
    conexion = Conn()
    pedidos = conexion.mostrarTodosPedidos()
    counter = {}
    for pedido in pedidos:
        
        productos = pedido['productos'].split('\n')
        cantidad = len(productos)
        
        counter[cantidad] = counter.get(cantidad, 0) + 1
    
    #{1: 10, 3: 1}
    return counter

def correlacionModosPagoProductos():
    conexion = Conn()
    pedidos = conexion.mostrarTodosPedidos()
    
    correlacion = {
        'Efectivo': {},
        'Tarjeta': {}
    }
    
    for pedido in pedidos:
        modo_pago = pedido['modopago']
        productos = pedido['productos'].split('\n')
        cantidad_productos = len(productos)

        if cantidad_productos in correlacion[modo_pago]:
            correlacion[modo_pago][cantidad_productos] += 1
        else:
            correlacion[modo_pago][cantidad_productos] = 1
    
    # {'Efectivo': {1: 4}, 4 pedidos con 1 producto pagados en efectivo
    #  'Tarjeta': {1: 6, 6 pedidos con 1 producto pagados con tarjeta
    #              3: 1}} 1 pedido con 3 productos pagados con tarjeta
    return correlacion

def graficar_estadisticas1():
    
    modos_pago = contarModosPago()
    productos_pedido = productosPorPedido()
    correlacion = correlacionModosPagoProductos()
    
    #cuadrar los 3 subplots en el cuadro
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle('Análisis de los pedidos', fontsize=16, y=1.05)
    
    #subplot 1: metodos de pago mas utilizados
    ax1.bar(modos_pago.keys(), modos_pago.values(), 
            color=['#4CAF50', '#2196F3'], edgecolor='black')
    ax1.set_title('Distribución de Métodos de Pago', pad=12)
    ax1.set_ylabel('Cantidad de Pedidos')
    ax1.grid(axis='y', linestyle='--', alpha=0.7)
    
    #subplot 2: cantidad productos por pedido
    ax2.bar(productos_pedido.keys(), productos_pedido.values(), 
            color='#FF9800', edgecolor='black')
    ax2.set_title('Cantidad de productos por Pedido', pad=12)
    ax2.set_xlabel('Cantidad de Productos')
    ax2.set_ylabel('Número de Pedidos')
    ax2.grid(axis='y', linestyle='--', alpha=0.7)
    
    #subplot 3: correlación entre daots
    #ordenar productos unicos (como un set pero ordenado)
    productos_unicos = sorted({p for modo in correlacion.values() for p in modo.keys()})
    ancho_barra = 0.35
    x = range(len(productos_unicos))
    
    #datos de cada método de pago
    efectivo = [correlacion['Efectivo'].get(p, 0) for p in productos_unicos]
    tarjeta = [correlacion['Tarjeta'].get(p, 0) for p in productos_unicos]
    
    #hacer las barras
    ax3.bar([i - ancho_barra/2 for i in x], efectivo, ancho_barra, 
            label='Efectivo', color='#4CAF50', edgecolor='black')
    ax3.bar([i + ancho_barra/2 for i in x], tarjeta, ancho_barra, 
            label='Tarjeta', color='#2196F3', edgecolor='black')
    
    ax3.set_title('Relación productos por pedido/Método de Pago', pad=12)
    ax3.set_xlabel('Cantidad de Productos')
    ax3.set_ylabel('Pedidos')
    ax3.set_xticks(x)
    ax3.set_xticklabels(productos_unicos)
    ax3.legend()
    ax3.grid(axis='y', linestyle='--', alpha=0.7)
    
    #asignar valores
    for ax in [ax1, ax2, ax3]:
        for bar in ax.patches:
            height = bar.get_height()
            if height > 0:
                ax.text(bar.get_x() + bar.get_width()/2., height,
                        f'{int(height)}',
                        ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()

def correlacion():
    modos_pago = contarModosPago()
    productos_pedido = productosPorPedido()
    correlacion = correlacionModosPagoProductos()
    
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle('Análisis de los pedidos', fontsize=16, y=1.05)
    
    #subplot 1: metodos de pago mas utilizados
    ax1.bar(modos_pago.keys(), modos_pago.values(), 
            color=['#4CAF50', '#2196F3'], edgecolor='black')
    ax1.set_title('Distribución de Métodos de Pago', pad=12)
    ax1.set_ylabel('Cantidad de Pedidos')
    ax1.grid(axis='y', linestyle='--', alpha=0.7)
    
    #subplot 2: cantidad productos por pedido
    productos = sorted(productos_pedido.keys())
    cantidades = [productos_pedido[k] for k in productos]
    
    ax2.bar(productos, cantidades, 
            color='#FF9800', edgecolor='black', width=0.8)
    ax2.set_title('Cantidad de productos por Pedido', pad=12)
    ax2.set_xlabel('Cantidad de Productos')
    ax2.set_ylabel('Número de Pedidos')
    ax2.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Configuración específica para eje X entero
    ax2.set_xticks(productos)  # Fuerza ticks en posiciones enteras
    ax2.xaxis.set_major_locator(plt.MaxNLocator(integer=True))  # Fuerza números enteros
    
    #subplot 3: correlación entre daots
    #ordenar productos unicos (como un set pero ordenado)
    productos_unicos = sorted({p for modo in correlacion.values() for p in modo.keys()})
    ancho_barra = 0.35
    x = range(len(productos_unicos))
    
    #datos de cada método de pago
    efectivo = [correlacion['Efectivo'].get(p, 0) for p in productos_unicos]
    tarjeta = [correlacion['Tarjeta'].get(p, 0) for p in productos_unicos]
    
    #hacer las barras
    ax3.bar([i - ancho_barra/2 for i in x], efectivo, ancho_barra, 
            label='Efectivo', color='#4CAF50', edgecolor='black')
    ax3.bar([i + ancho_barra/2 for i in x], tarjeta, ancho_barra, 
            label='Tarjeta', color='#2196F3', edgecolor='black')
    
    ax3.set_title('Relación Productos por pedido/Método de Pago', pad=12)
    ax3.set_xlabel('Cantidad de Productos')
    ax3.set_ylabel('Pedidos')
    ax3.set_xticks(x)
    ax3.set_xticklabels(productos_unicos)
    ax3.legend()
    ax3.grid(axis='y', linestyle='--', alpha=0.7)
    
    #asignar valores
    for ax in [ax1, ax2, ax3]:
        for bar in ax.patches:
            height = bar.get_height()
            if height > 0:
                ax.text(bar.get_x() + bar.get_width()/2., height,
                        f'{int(height)}',
                        ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()