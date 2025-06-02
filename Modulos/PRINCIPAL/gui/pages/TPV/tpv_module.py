from Modulos.PRINCIPAL.imports.core import *
from Modulos.PRINCIPAL.imports.widgets_import import *
from Modulos.PRINCIPAL.imports.bbdd_conn import *
from .pdf_window import *

from reportlab.pdfgen.canvas import Canvas

class Tpv_Page(QWidget):
    def __init__(self, productos_page = None , parent = None):
        QWidget.__init__(self, parent = parent)

        self.verticalLayout = QVBoxLayout(self)
        self.tpv_layout_superior = QHBoxLayout() 
        
        #ventana pdf
        self.windowPdf = None
        
        #frame barra busqueda y añadir pedido
        #///////////////////////////////////////////////////
        self.frame = QFrame(self)
        self.frame.setStyleSheet("background-color: beige; border-radius:8px;")
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 60))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        
        self.layoutBarraBusqueda = QHBoxLayout(self.frame)
        
        self.btnLupa = PyPushButton_buscar(
            icon_path="search.svg",
        )
        self.btnLupa.setMaximumSize(QSize(40, 50))
        self.espaciadorBusqueda = QSpacerItem(40,20,QSizePolicy.Expanding)
        self.barraBusqueda = PyLineEdit()
        self.barraBusqueda.setPlaceholderText("Buscar")
        self.barraBusqueda.setFixedWidth(166)
        self.barraBusqueda.setStyleSheet(
            '''
            color: black;
            font:500 10pt;
            border-bottom: 1px solid #1C323F;
            border-radius: 4px;
            '''
        )
        
        self.labelBusqueda = QLabel("Buscar por ")
        
        self.buscarPor = QComboBox()
        self.columnasTablePedidos = ["ID Pedido","Importe","Fecha","Cliente","Productos","Modo Pago"]
        self.buscarPor.addItems(self.columnasTablePedidos)
        self.columnasTable = self.columnasTablePedidos
        self.columnasTable.insert(len(self.columnasTablePedidos),"")
        self.buscarPor.setStyleSheet(f"border: none; font:500 13pt; height: {self.btnLupa.height()-4};width: 120px")
        
        self.labelCurrentPage = QLabel("TPV")
        self.labelCurrentPage.setStyleSheet(f"padding-left:10 ;border: none; font:500 13pt; font-weight: bold;")
        
        self.layoutBarraBusqueda.addWidget(self.labelCurrentPage)
        self.layoutBarraBusqueda.addSpacerItem(self.espaciadorBusqueda)
        self.layoutBarraBusqueda.addWidget(self.labelBusqueda)
        self.layoutBarraBusqueda.addWidget(self.buscarPor)
        self.layoutBarraBusqueda.addWidget(self.barraBusqueda)
        self.layoutBarraBusqueda.addWidget(self.btnLupa)
        
        self.tpv_layout_superior.addWidget(self.frame)
        
        #frame del boton de nuevoEmpleado
        self.frame_2 = QFrame(self)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(200, 0))
        self.frame_2.setMaximumSize(QSize(300, 16777215))
        self.frame_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        
        self.btn_anadirEmpleado = PyPushButton(icon_path="clipboard2-plus.svg", text_padding=0)
        self.btn_anadirEmpleado.setFixedWidth(50)
        self.btn_anadirEmpleado.setObjectName(u"btn_anadirEmpleado")
        self.btn_anadirEmpleado.setStyleSheet("border-radius: 4; background-color: #356b6b")
        self.btn_anadirEmpleado.setMaximumSize(QSize(150, 16777215))
        self.btn_anadirEmpleado.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_anadirEmpleado.clicked.connect(self.show_datosPedido)
        

        self.horizontalLayout.addWidget(self.btn_anadirEmpleado)
        self.tpv_layout_superior.addWidget(self.frame_2)
        self.verticalLayout.addLayout(self.tpv_layout_superior)

        self.tpv_layout_inferior = QHBoxLayout()
        self.tpv_layout_inferior.setObjectName(u"tpv_layout_inferior")
        
        self.frameCentral = QFrame(self)
        self.frameCentral.setStyleSheet("background-color:#444;border-radius:4px;")
        self.verticalLayout.addWidget(self.frameCentral)
        
        self.frameCentralLayout = QHBoxLayout(self.frameCentral)
        
        self.frameDerecha = QFrame(self)
        self.frameDerecha.setStyleSheet("background-color:#A4ADB2;")
        self.frameDerecha.setFixedWidth(0)
        self.frameDerecha.setMinimumWidth(0)
        self.frameCentro = QFrame(self)
        self.frameCentro.setStyleSheet("background-color:beige;")
        self.frameCentro.setFixedWidth(0)
        self.frameCentro.setMinimumWidth(0)
        self.frameIzquierda = QFrame(self)
        self.frameIzquierda.setStyleSheet("background-color:beige;")
        
        #Rellenar frames con elementos
        #//////////////////////////////////////////////////////////////////////////
        #TABLA IZQUIERDA, MOSTRAR TODOS LOS PEDIDOS
        
        
        #tabla configuracion
        self.tablePedidos = PyTableWidget()
        self.tablePedidos.resizeRowsToContents()
            
        self.tablePedidos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.pedidoslbl = QLabel("Pedidos existentes")
        self.pedidoslbl.setStyleSheet(f"padding-left:2;padding-bottom:2; font:550 13pt;color:black; border-bottom: 2px solid #444;")
        self.mostrarTablaPedidos()
        
        #FRAME CENTRO
        
        #FRAME CLIENTE EXISTENTE
        #////////////////////////////////////////////////////////////////////////////////
        #FRAME y layout CLIENTE EXISTENTE (DEFAULT)
        self.clienteExistenteFrame = QFrame()
        self.clienteExistenteFrameLayout = QVBoxLayout()
        #mete el frame en el layout de FrameCentro
        self.clienteExistenteFrameLayout.addWidget(self.clienteExistenteFrame)
        
        #combo box clientes bajo radio buttons
        self.elegirCliente = QComboBox()
        self.elegirCliente.setStyleSheet(f"border: 2px solid #444; font:500 13pt; height: 30")
        self.elegirCliente.setPlaceholderText(" Clientes")
        self.elegirCliente.setCurrentIndex(-1)
        self.elegirCliente.addItems(self.cargarClientes())
        
        #Combo box productos bajo combo box clientes
        self.elegirProducto = QComboBox()
        self.elegirProducto.setStyleSheet(f"border: 2px solid #444; font:500 13pt; height: 30")
        self.elegirProducto.setPlaceholderText(" Producto")
        self.elegirProducto.setCurrentIndex(-1)
        self.productos = self.cargarProductos()
        self.elegirProducto.addItems(self.productos)
        
        #spinbox cantidad producto
        self.cantidadProducto = QSpinBox()
        self.cantidadProducto.setMinimum(0)
        self.cantidadProducto.setStyleSheet("font:530 16px;")
        
        #combobox modo pago
        self.modoDePago = QComboBox()
        self.modoDePago.addItems(["Tarjeta","Efectivo"])
        self.modoDePago.setStyleSheet(f"border: 2px solid #444; font:500 13pt; height: 30")
        self.modoDePago.setPlaceholderText(" Método de pago")
        self.modoDePago.setCurrentIndex(-1)
        
        #label stock disponible
        cantidadProvisional = 0
        self.lblstock = QLabel(f"En stock: {cantidadProvisional}\tUnidades de compra:")
        self.lblstock.setStyleSheet("font:530 16px;")
        
        #qframe y layout stock y cantidad
        self.frameStockCantidad = QFrame()
        self.frameStockCantidadLayout = QHBoxLayout(self.frameStockCantidad)
        self.frameStockCantidadLayout.addWidget(self.lblstock)
        self.frameStockCantidadLayout.addWidget(self.cantidadProducto)
        
        #botones añadir producto, cancelar pedido 
        self.btn_cancelar = PyPushButton(
            text="Cancelar",
            text_padding=45,
            height=35,
            icon_path="x-lg.svg",
        )
        self.btn_anadir = PyPushButton(
            text="Añadir",
            height=35,
            text_padding=45,
            icon_path="box-arrow-down.svg"
        )
        self.btn_confirmar = PyPushButton(
            text="Confirmar",
            text_padding=45,
            height=35,
            icon_path="check2.svg"
        )
        
        self.aceptar_cancelar_frame = QFrame()
        self.aceptar_cancelar_frame.setStyleSheet("border: none;")
        self.layout_aceptar_cancelar_frame = QHBoxLayout(self.aceptar_cancelar_frame)
        
        self.layout_aceptar_cancelar_frame.addWidget(self.btn_cancelar)
        self.layout_aceptar_cancelar_frame.addWidget(self.btn_anadir)
        self.layout_aceptar_cancelar_frame.addWidget(self.btn_confirmar)
        
        #FRAME CLIENTE NUEVO
        #/////////////////////////////////////////////////////////////////////////////////
        #FRAME Y LAYOUT CLIENTE NUEVO
        self.clienteNuevoFrame = QFrame()
        self.clienteNuevoFrameLayout = QVBoxLayout(self.clienteNuevoFrame)

        #mete el frame en el layout de FrameCentro
        #self.clienteNuevoFrameLayout.addWidget(self.clienteNuevoFrame)

        #campos de informacion de cliente

        self.nombreCliente = PyLineEdit()
        self.nombreCliente.setPlaceholderText("Nombre")
        self.nombreCliente.setStyleSheet("border: 2px solid #444; font:500 13pt") 
        
        self.emailCliente = PyLineEdit()
        self.emailCliente.setPlaceholderText("Email")
        self.emailCliente.setStyleSheet("border: 2px solid #444; font:500 13pt") 

        self.telefonoCliente = PyLineEdit()
        self.telefonoCliente.setPlaceholderText("Telefono")
        self.telefonoCliente.setStyleSheet("border: 2px solid #444; font:500 13pt") 

        self.paisCliente = PyLineEdit()
        self.paisCliente.setPlaceholderText("País")
        self.paisCliente.setStyleSheet("border: 2px solid #444; font:500 13pt") 
         
        self.btn_cancelarNuevoCliente = PyPushButton(
            text="Cancelar",
            height=35,
            icon_path="x-lg.svg",
        )
        self.btn_aceptar = PyPushButton(
            text="Añadir",
            height=35,
            icon_path="check2.svg"
        )
        self.aceptar_cancelar_frameNuevoCliente = QFrame()
        self.aceptar_cancelar_frameNuevoCliente.setStyleSheet("border: none;")
        self.layout_aceptar_cancelar_frameNuevoCliente = QHBoxLayout(self.aceptar_cancelar_frameNuevoCliente)
        self.layout_aceptar_cancelar_frameNuevoCliente.addWidget(self.btn_cancelarNuevoCliente)
        self.layout_aceptar_cancelar_frameNuevoCliente.addWidget(self.btn_aceptar)
        self.layout_aceptar_cancelar_frameNuevoCliente.setAlignment(Qt.AlignTop)

        self.btn_cancelarNuevoCliente.clicked.connect(self.cancelarPedido)
        self.btn_aceptar.clicked.connect(self.anadirCliente)

        #STACKED WIDGET FRAME CENTRO
        #/////////////////////////////////////////////////////////////////////////////////////
        self.frameRadioButtons = QFrame()
        
        #frame radio buttons
        self.rbuttonSeleccionarCliente = QRadioButton("Cliente existente ",self.frameRadioButtons)
        self.rbuttonSeleccionarCliente.setChecked(True)
        self.rbuttonNuevoCliente = QRadioButton("Nuevo cliente",self.frameRadioButtons)
        self.rbuttonNuevoCliente.setChecked(False)
        
        #radiobuttons al layout de frame radio buttons
        self.rbuttonsLayout = QHBoxLayout(self.frameRadioButtons)
        self.rbuttonsLayout.addWidget(self.rbuttonSeleccionarCliente)
        self.rbuttonsLayout.addWidget(self.rbuttonNuevoCliente)
        self.rbuttonsLayout.setAlignment(Qt.AlignTop)

        layout_frameCentro = QVBoxLayout(self.frameCentro)
        layout_frameCentro.setContentsMargins(0, 0, 0, 0)
        layout_frameCentro.addWidget(self.frameRadioButtons)
        
        self.stackedWidgetCliente = QStackedWidget()
        self.stackedWidgetCliente.addWidget(self.clienteExistenteFrame)
        self.stackedWidgetCliente.addWidget(self.clienteNuevoFrame)
        layout_frameCentro.addWidget(self.stackedWidgetCliente)

        self.clienteNuevoFrameLayout.addWidget(self.nombreCliente)
        self.clienteNuevoFrameLayout.addWidget(self.emailCliente)
        self.clienteNuevoFrameLayout.addWidget(self.telefonoCliente)
        self.clienteNuevoFrameLayout.addWidget(self.paisCliente)
        self.clienteNuevoFrameLayout.addWidget(self.aceptar_cancelar_frameNuevoCliente)

        #ACCIONES RADIO BUTTON
        self.rbuttonSeleccionarCliente.toggled.connect(self.newClientDisplay)
        self.rbuttonNuevoCliente.toggled.connect(self.newClientDisplay)

        #FRAME DERECHO
        self.productoslbl = QLabel("Productos en el pedido actual")
        self.productoslbl.setStyleSheet(f"padding-left:2;padding-bottom:2; font:550 13pt;color:black; border-bottom: 2px solid #444;")
        self.tablaProductos = PyTableWidget(self.frameDerecha)
        self.tablaProductos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.crearTabla()
        try:
            self.anadirProductoAPedido(self.elegirProducto.currentIndex()[:self.elegirProducto.currentText().index(":")])
        except:
            pass
        
        #AÑADIR ELEMENTOS A LOS CUADROS CENTRALES
        self.frameCentralLayout.addWidget(self.frameIzquierda,stretch=1)
        self.frameCentralLayout.addWidget(self.frameCentro,stretch=1)
        self.frameCentralLayout.addWidget(self.frameDerecha,stretch=1)
        
        self.frameIzquierdaLayout = QVBoxLayout(self.frameIzquierda)
        self.frameIzquierdaLayout.addWidget(self.pedidoslbl)
        self.frameIzquierdaLayout.addWidget(self.tablePedidos)
        
        self.verticalLayoutFrameClienteExistente = QVBoxLayout(self.clienteExistenteFrame)
        self.verticalLayoutFrameClienteExistente.setAlignment(Qt.AlignTop)
        self.verticalLayoutFrameClienteExistente.addWidget(self.elegirCliente)
        self.verticalLayoutFrameClienteExistente.addWidget(self.elegirProducto)
        self.verticalLayoutFrameClienteExistente.addWidget(self.frameStockCantidad)
        self.verticalLayoutFrameClienteExistente.addWidget(self.modoDePago)
        self.verticalLayoutFrameClienteExistente.addWidget(self.aceptar_cancelar_frame)
        
        self.verticalLayoutFrameDerecha = QVBoxLayout(self.frameDerecha)
        self.verticalLayoutFrameDerecha.addWidget(self.productoslbl)
        self.verticalLayoutFrameDerecha.addWidget(self.tablaProductos)    
    
        #FUNCION ACTUALIZAR STOCK AL CAMBIAR PRODUCTO
        self.elegirProducto.currentIndexChanged.connect(self.setMaxCantidad)
        self.btn_anadir.clicked.connect(self.anadirProductoAPedido)
        self.btn_cancelar.clicked.connect(self.cancelarPedido)
        self.btn_confirmar.clicked.connect(self.anadirPedido)
        #metodo buscar
        self.barraBusqueda.textChanged.connect(lambda checked: self.buscar())
        
    
    #MOSTRAR ESCONDER FRAMES
    #/////////////////////////////////////////////////////////////
    def show_datosPedido(self): #cuadroCentral
        #anchura del menu lateral izquierdo
        self.limpiarCampos()
        datosPedido_width = self.frameCentro.width()
        
        if datosPedido_width <= 10:
            width = 420
        else:
            pass 
             
        try:     
        #empezar animacion (Si se pulsa dos veces el boton empieza una animacion sin final. No pasa nada, solo salta un aviso)
            
            self.animation = QPropertyAnimation(self.frameCentro, b"minimumWidth")    
            self.animation.setStartValue(datosPedido_width)
            self.animation.setEndValue(width)
            self.animation.setDuration(320)
            self.animation.setEasingCurve(QEasingCurve.OutCirc)
            self.animation.start()
            
            self.productos = self.cargarProductos()
            self.elegirProducto.clear()
            self.elegirProducto.addItems(self.productos)
            
            self.clientes = self.cargarClientes()
            self.elegirCliente.clear()
            self.elegirCliente.addItems(self.clientes)
        except:
            pass
                    
    def hide_datosPedido(self):
        
        datosPedido_width = self.frameCentro.width()
        
        print(datosPedido_width)
        if datosPedido_width >= 0:
                width = 0
        else:
            pass
                
        #empezar animacion
        
        self.animation = QPropertyAnimation(self.frameCentro, b"minimumWidth")    
        self.animation.setStartValue(datosPedido_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.OutCirc)
        self.animation.start()
            
        self.limpiarCampos()
    
    def limpiarCampos(self):
        #limpiar campos
        for combobox in self.frameCentro.findChildren(QComboBox):
            try:
                combobox.setCurrentIndex(-1)
            except:
                print("error al limpiar")
        for table in self.frameDerecha.findChildren(QTableView):
            try:
                self.crearTabla()
            except:
                print("Error al borrar tabla")
    
    def show_tablaProductos(self):
        datosTablaProductos_width = self.frameDerecha.width()
        
        if datosTablaProductos_width <= 10:
            width = 520
        else:
            pass 
             
        try:     
        #empezar animacion (Si se pulsa dos veces el boton empieza una animacion sin final. No pasa nada, solo salta un aviso)
            
            self.animation = QPropertyAnimation(self.frameDerecha, b"minimumWidth")    
            self.animation.setStartValue(datosTablaProductos_width)
            self.animation.setEndValue(width)
            self.animation.setDuration(320)
            self.animation.setEasingCurve(QEasingCurve.OutCirc)
            self.animation.start()
        except:
            pass
    
    def hide_tablaProductos(self):
        
        datosPedido_width = self.frameDerecha.width()
        
        print(datosPedido_width)
        if datosPedido_width > 0:
                width = 0
        else:
            pass
                
        #empezar animacion
        try:
            self.animationTProductos = QPropertyAnimation(self.frameDerecha, b"minimumWidth")    
            self.animationTProductos.setStartValue(datosPedido_width)
            self.animationTProductos.setEndValue(width)
            self.animationTProductos.setDuration(300)
            self.animationTProductos.setEasingCurve(QEasingCurve.OutCirc)
            self.animationTProductos.start()
        except:
            pass
    
    #METODOS LLENAR TABLA DE PEDIDOS
    #/////////////////////////////////////////////////////////////
    
    def mostrarTablaPedidos(self):
        self.tablePedidos.setColumnCount(7)
        self.tablePedidos.setRowCount(0)
        
        self.tablePedidos.setHorizontalHeaderLabels(self.columnasTablePedidos)
        
        conexion = Conn()
        pedidos = conexion.mostrarTodosPedidos()
        clientes = conexion.mostrarTodosClientes()

        #diccionario id_cliente : nombre_cliente 
        cliente_dict = {str(cliente['id']): cliente['nombre'] for cliente in clientes}
        
        try:
            for row, pedido in enumerate(pedidos):
                self.tablePedidos.insertRow(row)
                self.tablePedidos.setRowHeight(row, 60) 

                cliente_id = str(pedido.get('cliente', ''))
                cliente_nombre = cliente_dict.get(cliente_id, "Cliente no encontrado")

                datos = [
                str(pedido.get('id', '')),
                f"{pedido.get('importe', 0):.2f}€",
                pedido.get('fecha', ''),
                pedido.get('cliente', ''),
                pedido.get('productos', [f"{p['Código']} ({p['cantidad']}x)" for p in pedido.get('productos', [])]) if isinstance(pedido.get('productos'), list) else str(pedido.get('productos', '')),
                pedido.get('modopago', '')]

                for column, value in enumerate(datos):
                    item = QTableWidgetItem(str(value))
                    if column == 3:
                        item.setToolTip(cliente_nombre)
                    self.tablePedidos.setItem(row, column, item) 
                        
                #añadir botón de eliminar 
                eliminarbtn = PyPushButton(icon_path="trash.svg",height=35)
                eliminarbtn.clicked.connect(lambda _, pid = pedido.get("id"): self.eliminarPedido(pid))
                
                # Segundo botón pdf
                generarPdf = PyPushButtonPdf(icon_path="file-type-pdf.svg", height=35)
                generarPdf.clicked.connect(lambda _, pid=pedido.get("id"): self.generarPdf(pid))
                eliminarbtn.setFixedWidth(50)
                generarPdf.setFixedWidth(50)
                
                # Añadir los botones a la tabla
                frameOpciones = QFrame()
                frameOpciones.setStyleSheet("background-color: #444")
                frameOpciones.setFixedHeight(55)
                layoutFrameOpciones = QHBoxLayout(frameOpciones)
                layoutFrameOpciones.addWidget(eliminarbtn)
                layoutFrameOpciones.addWidget(generarPdf)
                
                self.tablePedidos.setCellWidget(row, self.tablePedidos.columnCount() - 1, frameOpciones)
                
                #colocar tooltips
                for row in range(self.tablePedidos.rowCount()):
                    itemProductos = self.tablePedidos.item(row, 4)
                    if itemProductos:
                        itemProductos.setFlags(itemProductos.flags() or Qt.TextWordWrap)
                        itemProductos.setToolTip(itemProductos.text()) 
                
                for row in range(self.tablePedidos.rowCount()):
                    itemFecha = self.tablePedidos.item(row, 2)  
                    if itemFecha:
                        itemFecha.setToolTip(itemFecha.text())

        except Exception:
            print("No hay pedidos que mostrar")
    #METODOS HACER PEDIDO
    #/////////////////////////////////////////////////////////////
    
    def cargarClientes(self):
        conexion = Conn()
        clientesExistentes = []
        for i in conexion.mostrarTodosClientes():
            clientesExistentes.append(""+i["nombre"][:12]+": "+i["email"])
        conexion.cerrarConexion()
        return clientesExistentes
    
    def cargarProductos(self):
        conexion = Conn()
        productosExistentes = []
        for i in conexion.mostrarTodosProductos():
            productosExistentes.append(""+i["id"]+": "+i["nombre"][:12])
        
        conexion.cerrarConexion()
        return productosExistentes
    
    def cargarCantidadProducto(self):
        conexion = Conn()    
        productos = []
        for i in conexion.mostrarTodosProductos():
            productos.append((i["id"],i["stock"]))
        conexion.cerrarConexion()
        return productos
    
    def setMaxCantidad(self):
        self.cantidadProducto.setValue(0)
        #cantidad tupla(id,stock)
        cantidad = self.cargarCantidadProducto()
        if self.elegirProducto.currentIndex()!=-1:
            for k in cantidad:
                if k[0] == self.elegirProducto.currentText()[:self.elegirProducto.currentText().index(":")]:
                    self.lblstock.setText(f"En stock: {str(k[1])}\tUnidades de compra:")
                    self.cantidadProducto.setMaximum(k[1])
                    return k[1]#cantidad en stock
        else:
            pass
        return 0
    
    def crearTabla(self):
        #configuracion de la tabla
        self.tablaProductos.setColumnCount(5)
        self.tablaProductos.setRowCount(0)
        self.tablaProductos.setHorizontalHeaderLabels(["Nombre","Cantidad","Precio","Código",""])
        
    def anadirProductoAPedido(self):
        conexion = Conn()
        productos = conexion.mostrarTodosProductos()
        table = self.tablaProductos
        fila_posicion = table.rowCount()
        
        #comprueba que la tabla no tenga 0 filas        
        for producto in productos:
            try: #este try-catch evita que pete cuando el indice de la qcombobox es -1, cuando esta la opcion del placeholder
                if self.elegirProducto.currentText()[:self.elegirProducto.currentText().index(":")] == producto["id"]:
                    productoValido = [producto["nombre"],int(self.cantidadProducto.text()),producto["precio"],producto["id"]]
            except:
                pass
        #si no se dan datos no hace nada
        if productos is None:
            pass
        #comprobar que la cantidad no sea 0 
        if productoValido[1] == 0:
            msg = QMessageBox()
            msg.setWindowIcon(QIcon(r"Modulos/WEB/imagenes/gestr.ico"))
            msg.setWindowTitle("Atención")
            msg.setText("Debes seleccionar al menos una unidad")
            msg.addButton(QMessageBox.StandardButton.Ok)
            msg.exec()
        
        else:
            table.insertRow(fila_posicion)
            
            for col, valor in enumerate(productoValido):
                item = QTableWidgetItem(str(valor))
                table.setItem(fila_posicion, col, item)
                item.setToolTip(item.text())

            #añadir botón de eliminar en la última columna
            eliminarbtn = QPushButton("Eliminar")
            eliminarbtn.clicked.connect(lambda _, r=fila_posicion: table.removeRow(table.currentRow()))
            eliminarbtn.clicked.connect(self.hideCheck)
            table.setCellWidget(fila_posicion, table.columnCount() - 1, eliminarbtn)

            
            self.cantidadProducto.setValue(0)
            
        if table.rowCountChanged(0,1) or table.rowCount()>0:
            self.show_tablaProductos()
        else:
            pass  
          
    def hideCheck(self):
        if self.tablaProductos.rowCount() == 0:
            self.hide_tablaProductos()
    
    def cancelarPedido(self):
        
        self.hide_datosPedido()
        self.hide_tablaProductos()

    def anadirPedido(self):
        if self.tablaProductos.rowCount() == 0:
            msg = QMessageBox()
            msg.setWindowIcon(QIcon(r"Modulos/WEB/imagenes/gestr.ico"))
            msg.setWindowTitle("Atención")
            msg.setText("Debes seleccionar al menos un producto")
            msg.addButton(QMessageBox.StandardButton.Ok)
            msg.exec()
        else:
            conexion = Conn()
            #OBTENER CLIENTE
            clientes = conexion.mostrarTodosClientes()
            try:
                for clt in clientes:
                    if clt["email"] == self.elegirCliente.currentText()[self.elegirCliente.currentText().index(":")+1:].replace(" ",""):
                        cliente = clt
                        break
            except:
                msg = QMessageBox()
                msg.setWindowIcon(QIcon(r"Modulos/WEB/imagenes/gestr.ico"))
                msg.setWindowTitle("Atención")
                msg.setText("Debes seleccionar un cliente")
                msg.addButton(QMessageBox.StandardButton.Ok)
                msg.exec()
            
            #OBTENER PRODUCTOS
            # - obtiene los productos de la tabla,
            # - comprueba la suma de las cantidades de los productos del pedido para que no exceda el stock de cada uno
            # - genera los precios de cada producto con iva
            productos = self.obtenerPreciosIva(self.comprobarProductosPedido(self.obtener_ProductosTabla(self.tablaProductos)))
            
            #OBTENER METODO DE PAGO
            #comprobar que se introduzca el metodo de pago
            if self.modoDePago.currentIndex()==-1:
                msg = QMessageBox()
                msg.setWindowIcon(QIcon(r"Modulos/WEB/imagenes/gestr.ico"))
                msg.setWindowTitle("¡Atención!")
                msg.setText("Debes seleccionar un método de pago")
                msg.addButton(QMessageBox.StandardButton.Ok)
                msg.exec()
            else:
                modoPago = self.modoDePago.currentText()

            descripcionProducto = "\n".join([f"Producto {i+1}: {item['Nombre']} - {item["Cantidad"]} unidades - €{item['subtotal']} (con IVA) - Código: {item["Código"]} - {item["iva"]} IVA" 
            for i, item in enumerate(productos)])
            
            productos_id = "\n".join([f"{item["Código"]}: {item["Cantidad"]} unidades" for item in productos])
            id_pedido = self.generarIDPedido()
            pedido = [
                id_pedido,
                # - suma todos los precios de los productos
                self.obtenerTotalPrecio(productos),
                datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
                (cliente["id"]),
                productos_id,
                modoPago,
                descripcionProducto
            ]

            if conexion.registrarPedido(pedido):
                self.cancelarPedido()
                conexion.cerrarConexion()
                self.mostrarTablaPedidos()
                self.lblstock.setText(f"En stock: 0\tUnidades de compra:")
                print("llega")
                self.actualizarStock(id_pedido)
        
    def comprobarProductosPedido(self,productos):
        combinados = {}

        id_y_stock = self.cargarCantidadProducto()
        
        for producto in productos:
            codigo_producto = producto['Código']
            nombre_producto = producto['Nombre']
            for i in id_y_stock:
                if i[0] == codigo_producto:
                    stock = i[1]
            if codigo_producto in combinados:
                combinados[codigo_producto]['Cantidad'] = str(int(combinados[codigo_producto]['Cantidad']) + int(producto['Cantidad']))
                if int(combinados[codigo_producto]['Cantidad'] ) > stock:
                    QMessageBox.warning(
                        self,
                        "Límite excedido",
                        f"¡Atención! Has comprado más unidades de {nombre_producto} de las que hay en stock. Al pedido se añadirán {stock} unidades\n",
                        QMessageBox.Ok
                    )
                    combinados[codigo_producto]['Cantidad'] = stock
                else:
                    pass
            else:
                combinados[codigo_producto] = producto.copy()
        
        return list(combinados.values())
    
    def obtener_ProductosTabla(self,tabla:QTableWidget):
        datos = []
        cabeceras = []
        for col in range(tabla.columnCount()-1):
            item_cabecera = tabla.horizontalHeaderItem(col)
            if item_cabecera is not None:
                cabeceras.append(item_cabecera.text())
            else:
                cabeceras.append(f"Columna {col + 1}")
        for fila in range(tabla.rowCount()):
            fila_datos = {}
            for col, cabecera in enumerate(cabeceras):
                item = tabla.item(fila, col)
                fila_datos[cabecera] = item.text() if item is not None else ""
                
            datos.append(fila_datos)
        return datos
        
    def obtenerPreciosIva(self,productos:list[dict]):
        
        conexion = Conn()
        todos_productos = conexion.mostrarTodosProductos()
          
        for producto in productos:
            for item in todos_productos:
                if item["id"] == producto["Código"]:
                    producto["iva"] = item["iva"]
                    break
            precio_sinIva = float(producto["Cantidad"]) * float(producto["Precio"])
            #suma del iva al producto
            producto["subtotal"] = (float(producto["iva"]/100)*precio_sinIva)+(precio_sinIva)
        
        return productos    
    
    def obtenerTotalPrecio(self,productos:list[dict]):
        total = 0.0
        for producto in productos:
            total += float(producto.get('subtotal', 0))
        return round(total, 2)
    
    def generarIDPedido(self):
        from faker import Faker
        faker = Faker()
        return datetime.now().strftime("%d%m%Y")+''.join(faker.random_letters(7))[:10]
    
    def eliminarPedido(self,pid):
        confirmacion = QMessageBox.question(
            self, 
            "Confirmar eliminación", 
            f"¿Estás seguro de que quieres eliminar este pedido?\nEsta acción es irreversible",  
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No  
        )
        
        if confirmacion == QMessageBox.Yes:
            conexion = Conn()
            
            pedidos: list[dict] = self.obtener_ProductosTabla(self.tablePedidos)
        
            for pedido in pedidos:
                if pedido["ID Pedido"] == pid:
                    productos_str = pedido["Productos"]
                    
                    #dividir la string por \n porque esto distingue entre productos
                    lineas_productos = productos_str.split('\n')
                    
                    #sacar producto : unidad
                    productos_unidades = {} #output {'CUADRO-123554': 3, 'RODAM-123787': 2}
                    for linea in lineas_productos:
                        if ": " in linea:
                            producto, detalle = linea.split(": ")
                            cantidad_str = detalle.split(" ")[0]
                            productos_unidades[producto] = int(cantidad_str)
                    
                    print(f"Productos y unidades del pedido {pid}: {productos_unidades}")
                    
                    conexion = Conn()
                    id_y_stock = self.cargarCantidadProducto() #output [('PEZ-123812', 450), ('RODAM-123787', 500)]
                    print(id_y_stock)
                    
                    for producto_id, stock_actual in id_y_stock:
                        if producto_id in productos_unidades:
                            cantidad_vendida = productos_unidades[producto_id]
                            nuevo_stock = int(stock_actual) + int(cantidad_vendida)
                            conexion.actualizarStock(producto_id, nuevo_stock)
                            conexion.eliminarPedido(pid)
                            self.mostrarTablaPedidos()
                        else:
                            pass
                        
                    break   

                self.mostrarTablaPedidos()
                                            
        else:
            print("Eliminación cancelada.")
            
    def actualizarStock(self,pid):
        
        pedidos: list[dict] = self.obtener_ProductosTabla(self.tablePedidos)
        
        for pedido in pedidos:
            if pedido["ID Pedido"] == pid:
                productos_str = pedido["Productos"]
                
                #dividir la string por \n porque esto distingue entre productos
                lineas_productos = productos_str.split('\n')
                
                #sacar producto : unidad
                productos_unidades = {} #output {'CUADRO-123554': 3, 'RODAM-123787': 2}
                for linea in lineas_productos:
                    if ": " in linea:
                        producto, detalle = linea.split(": ")
                        cantidad_str = detalle.split(" ")[0]
                        productos_unidades[producto] = int(cantidad_str)
                
                print(f"Productos y unidades del pedido {pid}: {productos_unidades}")
                
                conexion = Conn()
                id_y_stock = self.cargarCantidadProducto() #output [('PEZ-123812', 450), ('RODAM-123787', 500)]
                print("llega actualizar stock")
                for producto_id, stock_actual in id_y_stock:
                    if producto_id in productos_unidades:
                        cantidad_vendida = productos_unidades[producto_id]
                        nuevo_stock = int(stock_actual) - int(cantidad_vendida)
                        print(stock_actual, nuevo_stock)
                        conexion.actualizarStock(producto_id, nuevo_stock)
                    else:
                        pass
                    
                break   
    
    def buscar(self):
        
        texto_busqueda = self.barraBusqueda.text().strip().lower()
        
        for fila in range(self.tablePedidos.rowCount()):
            item = self.tablePedidos.item(fila,self.buscarPor.currentIndex())
            if item.text() != texto_busqueda:
                self.tablePedidos.setRowHidden(fila, texto_busqueda not in item.text().lower())
            else:
                pass
    
    def generarPdf(self,pid):
        confirmacion = QMessageBox.question(
            self, 
            "Generar factura", 
            f"¿Generar factura de este pedido?\n",  
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No  
        )
        
        if confirmacion == QMessageBox.Yes:
            
            QMessageBox.information(
                        self,
                        "Documento generado con éxito",
                        f"Documento ubicado en el directorio PedidosGenerados\n",
                        QMessageBox.Ok
                    )
            
            print(pid)
            self.windowPdf = PdfWindow()
            self.windowPdf.generarPdf(pid)
        
        else:
            pass 
    
    def newClientDisplay(self):
        if self.rbuttonSeleccionarCliente.isChecked():
            self.stackedWidgetCliente.setCurrentIndex(0)
        else:
            self.stackedWidgetCliente.setCurrentIndex(1)
    
    def anadirCliente(self):
        conexion = Conn()
        
        confirmacion = QMessageBox.question(
            self, 
            "Confirmar", 
            f"¿Añadir nuevo cliente?",  
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No  
        )
        
        if confirmacion == QMessageBox.Yes:

            #registrar datos en Nuevo cliente
            cliente = [
                ""+self.generarID(),
                ""+self.nombreCliente.text(),
                ""+self.emailCliente.text(),
                ""+self.telefonoCliente.text(),
                ""+self.paisCliente.text(),
                ""+str(datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))                   
            ]
            
            if conexion.registrarCliente(cliente):
                print("exito en el registro")
            
            self.clientes = self.cargarClientes()
            self.elegirCliente.clear()
            self.elegirCliente.addItems(self.clientes)

            #limpiar campos
            for linedit in self.clienteNuevoFrame.findChildren(PyLineEdit):
                try:
                    linedit.setText("")
                except:
                    print("error al limpiar")

            #cambiar a cliente existente
            self.rbuttonSeleccionarCliente.setChecked(True)
            self.rbuttonNuevoCliente.setChecked(False)
            self.newClientDisplay()

    def generarID(self):
        from faker import Faker
        faker = Faker()
        id = str(faker.uuid4())
        id = id[::6]+self.nombreCliente.text().replace(" ","")[::3]+self.emailCliente.text()
        return id[:10]