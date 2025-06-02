from Modulos.PRINCIPAL.imports.core import *
from Modulos.PRINCIPAL.imports.widgets_import import *
from Modulos.PRINCIPAL.imports.bbdd_conn import *
from .pdf_windowCompras import *


class Compras_Page(QWidget):
    def __init__(self, productos_page = None , parent = None):
        QWidget.__init__(self, parent = parent)
        
        self.setObjectName(u"page_tpv")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tpv_layout_superior = QHBoxLayout()
        self.tpv_layout_superior.setObjectName(u"tpv_layout_superior") 
        
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
        self.columnasTableCompras = ["ID Compra","Importe","Fecha","Proveedor","Productos","Modo Pago","Estado"]
        self.buscarPor.addItems(self.columnasTableCompras)
        self.columnasTable = self.columnasTableCompras
        self.columnasTable.insert(len(self.columnasTableCompras),"")
        self.buscarPor.setStyleSheet(f"border: none; font:500 13pt; height: {self.btnLupa.height()-4};width: 120px")
        
        self.labelCurrentPage = QLabel("Compras a proveedores")
        self.labelCurrentPage.setStyleSheet(f"padding-left:10 ;border: none; font:500 13pt; font-weight: bold;")
        
        self.layoutBarraBusqueda.addWidget(self.labelCurrentPage)
        self.layoutBarraBusqueda.addSpacerItem(self.espaciadorBusqueda)
        self.layoutBarraBusqueda.addWidget(self.labelBusqueda)
        self.layoutBarraBusqueda.addWidget(self.buscarPor)
        self.layoutBarraBusqueda.addWidget(self.barraBusqueda)
        self.layoutBarraBusqueda.addWidget(self.btnLupa)
        
        self.tpv_layout_superior.addWidget(self.frame)
        
        #frame del boton de nueva Compra
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
        
        self.btn_anadirCompra = PyPushButton(icon_path="clipboard2-plus.svg", text_padding=0)
        self.btn_anadirCompra.setFixedWidth(50)
        self.btn_anadirCompra.setStyleSheet("border-radius: 4; background-color: #356b6b")
        self.btn_anadirCompra.setMaximumSize(QSize(150, 16777215))
        self.btn_anadirCompra.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_anadirCompra.clicked.connect(self.show_datosCompra)
        

        self.horizontalLayout.addWidget(self.btn_anadirCompra)
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
        #TABLA IZQUIERDA, MOSTRAR TODAS LAS COMPRAS 
        
        
        #tabla configuracion
        self.tableCompras = PyTableWidget()
        self.tableCompras.resizeRowsToContents()
            
        self.tableCompras.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.compraslbl = QLabel("Compras realizadas")
        self.compraslbl.setStyleSheet(f"padding-left:2;padding-bottom:2; font:550 13pt;color:black; border-bottom: 2px solid #444;")
        self.mostrarTablaCompras()
        
        #FRAME CENTRO
        
        #FRAME proveedor EXISTENTE
        #////////////////////////////////////////////////////////////////////////////////
        #FRAME y layout proveedor EXISTENTE (DEFAULT)
        self.proveedorExistenteFrame = QFrame()
        self.proveedorExistenteFrameLayout = QVBoxLayout()
        #mete el frame en el layout de FrameCentro
        self.proveedorExistenteFrameLayout.addWidget(self.proveedorExistenteFrame)
        
        #combo box Proveedors bajo radio buttons
        self.elegirProveedor = QComboBox()
        self.elegirProveedor.setStyleSheet(f"border: 2px solid #444; font:500 13pt; height: 30")
        self.elegirProveedor.setPlaceholderText(" Proveedores")
        self.elegirProveedor.setCurrentIndex(-1)
        self.elegirProveedor.addItems(self.cargarProveedores())
        
        #Combo box productos bajo combo box proveedores
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
        
        #FRAME PROVEEDOR NUEVO
        #/////////////////////////////////////////////////////////////////////////////////

        self.nombreProveedor = PyLineEdit()
        self.nombreProveedor.setPlaceholderText("Nombre")
        self.nombreProveedor.setStyleSheet("border: 2px solid #444; font:500 13pt") 
        
        self.cifProveedor = PyLineEdit()
        self.cifProveedor.setPlaceholderText("CIF")
        self.cifProveedor.setStyleSheet("border: 2px solid #444; font:500 13pt") 

        self.emailProveedor = PyLineEdit()
        self.emailProveedor.setPlaceholderText("Email")
        self.emailProveedor.setStyleSheet("border: 2px solid #444; font:500 13pt")

        self.telefonoProveedor = PyLineEdit()
        self.telefonoProveedor.setPlaceholderText("Teléfono")
        self.telefonoProveedor.setStyleSheet("border: 2px solid #444; font:500 13pt") 

        self.direccionProveedor = PyLineEdit()
        self.direccionProveedor.setPlaceholderText("Dirección")
        self.direccionProveedor.setStyleSheet("border: 2px solid #444; font:500 13pt")

        self.descripcionProveedor = QPlainTextEdit()
        self.descripcionProveedor.setPlaceholderText("Descripción")
        self.descripcionProveedor.setStyleSheet("border: 2px solid #444; font:500 13pt")

        self.comentariosProveedor = QPlainTextEdit()
        self.comentariosProveedor.setPlaceholderText("Comentarios")
        self.comentariosProveedor.setStyleSheet("border: 2px solid #444; font:500 13pt")
         
        self.btn_cancelarNuevoProveedor = PyPushButton(
            text="Cancelar",
            height=35,
            icon_path="x-lg.svg",
        )
        self.btn_aceptar = PyPushButton(
            text="Añadir",
            height=35,
            icon_path="check2.svg"
        )
        
        self.aceptar_cancelar_frameNuevoProveedor = QFrame()
        self.aceptar_cancelar_frameNuevoProveedor.setStyleSheet("border: none;")
        self.layout_aceptar_cancelar_frameNuevoProveedor = QHBoxLayout(self.aceptar_cancelar_frameNuevoProveedor)
        self.layout_aceptar_cancelar_frameNuevoProveedor.addWidget(self.btn_cancelarNuevoProveedor)
        self.layout_aceptar_cancelar_frameNuevoProveedor.addWidget(self.btn_aceptar)
        self.layout_aceptar_cancelar_frameNuevoProveedor.setAlignment(Qt.AlignTop)

        self.btn_cancelarNuevoProveedor.clicked.connect(self.cancelarCompra)
        self.btn_aceptar.clicked.connect(self.anadirProveedor)

        #FRAME Y LAYOUT PROVEEDOR NUEVO
        self.proveedorNuevoFrame = QFrame()
        self.proveedorNuevoFrameLayout = QVBoxLayout(self.proveedorNuevoFrame)
        self.proveedorNuevoFrameLayout.setContentsMargins(0, 0, 0, 0)  # Eliminar márgenes
        self.proveedorNuevoFrameLayout.setSpacing(15)  # Espaciado entre elementos

        #CONFIGURAR SCROLL AREA
        self.scrollarea = QScrollArea()
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea.setStyleSheet("border: none; background: transparent;")
        self.scrollarea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)  # Mostrar scroll cuando sea necesario
        self.scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        #CONTENEDOR DE LOS CAMPOS
        self.scrollContent = QFrame()
        self.scrollContent.setStyleSheet("background: transparent;")
        self.scrollLayout = QVBoxLayout(self.scrollContent)
        self.scrollLayout.setContentsMargins(5, 5, 15, 5)  # Margen derecho para el scroll
        self.scrollLayout.setSpacing(10)

        #AÑADIR CAMPOS AL LAYOUT DE SCROLLBARFRAME
        campos = [
            self.nombreProveedor,
            self.cifProveedor,
            self.emailProveedor,
            self.telefonoProveedor,
            self.direccionProveedor,
            self.descripcionProveedor,
            self.comentariosProveedor
        ]

        for campo in campos:
            if isinstance(campo, QPlainTextEdit):
                campo.setMinimumHeight(100)
            self.scrollLayout.addWidget(campo)
        self.scrollLayout.addStretch()

        #METEMOS EL CONTENIDO EN LA SCROLL AREA
        self.scrollarea.setWidget(self.scrollContent)

        #AÑADIR AL FRAME PRINCIAPL LA SCROLL AREA Y LOS BOTONES
        self.proveedorNuevoFrameLayout.addWidget(self.scrollarea)
        self.proveedorNuevoFrameLayout.addWidget(self.aceptar_cancelar_frameNuevoProveedor)

        self.proveedorNuevoFrame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.scrollContent.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


        #STACKED WIDGET FRAME CENTRO
        #/////////////////////////////////////////////////////////////////////////////////////
        self.frameRadioButtons = QFrame()
        
        #frame radio buttons
        self.rbuttonSeleccionarProveedor = QRadioButton("Proveedor existente ",self.frameRadioButtons)
        self.rbuttonSeleccionarProveedor.setChecked(True)
        self.rbuttonNuevoProveedor = QRadioButton("Nuevo Proveedor",self.frameRadioButtons)
        self.rbuttonNuevoProveedor.setChecked(False)
        
        #radiobuttons al layout de frame radio buttons
        self.rbuttonsLayout = QHBoxLayout(self.frameRadioButtons)
        self.rbuttonsLayout.addWidget(self.rbuttonSeleccionarProveedor)
        self.rbuttonsLayout.addWidget(self.rbuttonNuevoProveedor)
        self.rbuttonsLayout.setAlignment(Qt.AlignTop)

        layout_frameCentro = QVBoxLayout(self.frameCentro)
        layout_frameCentro.setContentsMargins(0, 0, 0, 0)
        layout_frameCentro.addWidget(self.frameRadioButtons)
        
        self.stackedWidgetProveedor = QStackedWidget()
        self.stackedWidgetProveedor.addWidget(self.proveedorExistenteFrame)
        self.stackedWidgetProveedor.addWidget(self.proveedorNuevoFrame)
        layout_frameCentro.addWidget(self.stackedWidgetProveedor)

        
        self.proveedorNuevoFrameLayout.addWidget(self.aceptar_cancelar_frameNuevoProveedor)

        #ACCIONES RADIO BUTTON
        self.rbuttonSeleccionarProveedor.toggled.connect(self.newSupplierDisplay)
        self.rbuttonNuevoProveedor.toggled.connect(self.newSupplierDisplay)

        #FRAME DERECHO
        self.productoslbl = QLabel("Productos en el pedido actual")
        self.productoslbl.setStyleSheet(f"padding-left:2;padding-bottom:2; font:550 13pt;color:black; border-bottom: 2px solid #444;")
        self.tablaProductos = PyTableWidget(self.frameDerecha)
        self.tablaProductos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.crearTabla()
        try:
            self.anadirProductoACompra(self.elegirProducto.currentIndex()[:self.elegirProducto.currentText().index(":")])
        except:
            pass
        
        #AÑADIR ELEMENTOS A LOS CUADROS CENTRALES
        self.frameCentralLayout.addWidget(self.frameIzquierda,stretch=1)
        self.frameCentralLayout.addWidget(self.frameCentro,stretch=1)
        self.frameCentralLayout.addWidget(self.frameDerecha,stretch=1)
        
        self.frameIzquierdaLayout = QVBoxLayout(self.frameIzquierda)
        self.frameIzquierdaLayout.addWidget(self.compraslbl)
        self.frameIzquierdaLayout.addWidget(self.tableCompras)
        
        self.verticalLayoutFrameClienteExistente = QVBoxLayout(self.proveedorExistenteFrame)
        self.verticalLayoutFrameClienteExistente.setAlignment(Qt.AlignTop)
        self.verticalLayoutFrameClienteExistente.addWidget(self.elegirProveedor)
        self.verticalLayoutFrameClienteExistente.addWidget(self.elegirProducto)
        self.verticalLayoutFrameClienteExistente.addWidget(self.frameStockCantidad)
        self.verticalLayoutFrameClienteExistente.addWidget(self.modoDePago)
        self.verticalLayoutFrameClienteExistente.addWidget(self.aceptar_cancelar_frame)
        
        self.verticalLayoutFrameDerecha = QVBoxLayout(self.frameDerecha)
        self.verticalLayoutFrameDerecha.addWidget(self.productoslbl)
        self.verticalLayoutFrameDerecha.addWidget(self.tablaProductos)    
    
        #FUNCION ACTUALIZAR STOCK AL CAMBIAR PRODUCTO
        self.elegirProducto.currentIndexChanged.connect(self.setMaxCantidad)
        self.btn_anadir.clicked.connect(self.anadirProductoACompra)
        self.btn_cancelar.clicked.connect(self.cancelarCompra)
        self.btn_confirmar.clicked.connect(self.anadirCompra)
        #metodo buscar
        self.barraBusqueda.textChanged.connect(lambda checked: self.buscar())
        
    
    #MOSTRAR ESCONDER FRAMES
    #/////////////////////////////////////////////////////////////
    def show_datosCompra(self): #cuadroCentral
        #anchura del menu lateral izquierdo
        self.limpiarCampos()
        datosCompra_width = self.frameCentro.width()
        
        if datosCompra_width <= 10:
            width = 420
        else:
            pass 
             
        try:     
        #empezar animacion (Si se pulsa dos veces el boton empieza una animacion sin final. No pasa nada, solo salta un aviso)
            
            self.animation = QPropertyAnimation(self.frameCentro, b"minimumWidth")    
            self.animation.setStartValue(datosCompra_width)
            self.animation.setEndValue(width)
            self.animation.setDuration(320)
            self.animation.setEasingCurve(QEasingCurve.OutCirc)
            self.animation.start()
            
            self.productos = self.cargarProductos()
            self.elegirProducto.clear()
            self.elegirProducto.addItems(self.productos)
            
            self.proveedores = self.cargarProveedores()
            self.elegirProveedor.clear()
            self.elegirProveedor.addItems(self.proveedores)
        except:
            pass
                    
    def hide_datosCompra(self):
        
        datosCompra_width = self.frameCentro.width()
        
        print(datosCompra_width)
        if datosCompra_width >= 0:
                width = 0
        else:
            pass
                
        #empezar animacion
        
        self.animation = QPropertyAnimation(self.frameCentro, b"minimumWidth")    
        self.animation.setStartValue(datosCompra_width)
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
        for plaintext in self.proveedorNuevoFrame.findChildren(QPlainTextEdit):
            try:
                plaintext.setPlainText("")
            except:
                print("error al limpiar plaintexts")
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
    
    #METODOS LLENAR TABLA DE COMPRAS
    #/////////////////////////////////////////////////////////////
    
    def mostrarTablaCompras(self):
        self.tableCompras.setColumnCount(len(self.columnasTableCompras))
        self.tableCompras.setRowCount(0)
        
        self.tableCompras.setHorizontalHeaderLabels(self.columnasTableCompras)
        
        conexion = Conn()
        compras = conexion.mostrarTodasCompras()

        #cargar proveedores una sola vez para los tooltips
        try:
            if not proveedores:  #si existe pero esta vacia
                proveedores = conexion.mostrarTodosProveedores()
        except NameError:  #si no existe
            proveedores = conexion.mostrarTodosProveedores()
            
        #diccionario id_cliente : nombre_cliente 
        proveedor_dict = {str(proveedor['id']): proveedor['nombre'] for proveedor in proveedores}

        try:
            for row, compra in enumerate(compras):
                self.tableCompras.insertRow(row)
                self.tableCompras.setRowHeight(row, 60) 

                proveedor_id = str(compra.get('proveedor', ''))
                proveedor_nombre = proveedor_dict.get(proveedor_id, 'Desconocido')

                datos = [
                str(compra.get('id', '')),
                f"{compra.get('importe', ''):.2f}€",
                compra.get('fecha', ''),
                compra.get('proveedor', ''),
                compra.get('productos', [f"{p['Código']} ({p['cantidad']}x)" for p in compra.get('productos', [])]) if isinstance(compra.get('productos'), list) else str(compra.get('productos', '')),
                compra.get('modoPago', '')
                ]

                for column, value in enumerate(datos):
                    item = QTableWidgetItem(str(value))
                    self.tableCompras.setItem(row, column, item)
                    if column == 3:
                        item.setToolTip(proveedor_nombre)

                #anadir checkbox para estado

                #cargar valor desde bbdd
                estado_value = compra.get('estado', '')
                #comprobar estados
                texto_check = "Comprado"
                checked = False
                if estado_value == "Recibido":
                    texto_check = "Recibido"
                    checked = True
                elif estado_value == "Comprado":
                    texto_check = "Comprado"

                #crear checkbox con la configuracion
                self.estado_chbox = QCheckBox(texto_check)
                self.estado_chbox.setChecked(checked)           
                #accion de la checkbox
                self.estado_chbox.stateChanged.connect(lambda estado, pid=compra.get("id"), chk=self.estado_chbox: self.cambiarEstadoCompra(pid, estado, chk))
                
                widget_estadochk = QWidget()
                widget_estadochk.setStyleSheet("background-color: #A4ADB2")
                layout_chkbox = QHBoxLayout(widget_estadochk)
                layout_chkbox.addWidget(self.estado_chbox)
                #layout_chkbox.setAlignment(Qt.AlignCenter)
                layout_chkbox.setContentsMargins(20, 0, 0, 0)
                widget_estadochk.setLayout(layout_chkbox)
                
                self.tableCompras.setCellWidget(row, 6, widget_estadochk)                   
                        
                #añadir botón de eliminar en la última columna
                eliminarbtn = PyPushButton(icon_path="trash.svg",height=35)
                #○eliminarbtn.setStyleSheet("background-color: #A4ADB2")
                eliminarbtn.clicked.connect(lambda _, pid = compra.get("id"): self.eliminarCompra(pid))
                
                # Segundo botón pdf
                generarPdf = PyPushButtonPdf(icon_path="file-type-pdf.svg", height=35)
                generarPdf.clicked.connect(lambda _, pid=compra.get("id"): self.generarPdf(pid))
                eliminarbtn.setFixedWidth(50)
                generarPdf.setFixedWidth(50)
                
                # Añadir los botones a la tabla
                frameOpciones = QFrame()
                frameOpciones.setStyleSheet("background-color: #444")
                frameOpciones.setFixedHeight(55)
                layoutFrameOpciones = QHBoxLayout(frameOpciones)
                layoutFrameOpciones.addWidget(eliminarbtn)
                layoutFrameOpciones.addWidget(generarPdf)
                
                self.tableCompras.setCellWidget(row, self.tableCompras.columnCount() - 1, frameOpciones)
                
                #colocar tooltips
                for row in range(self.tableCompras.rowCount()):
                    itemProductos = self.tableCompras.item(row, 4)
                    if itemProductos:
                        itemProductos.setFlags(itemProductos.flags() or Qt.TextWordWrap)
                        itemProductos.setToolTip(itemProductos.text())               
                for row in range(self.tableCompras.rowCount()):
                    itemFecha = self.tableCompras.item(row, 2)  
                    if itemFecha:
                        itemFecha.setToolTip(itemFecha.text())
        
        except Exception:
            print("No hay compras que mostrar")
        conexion.cerrarConexion()
    #METODOS HACER COMPRA
    #/////////////////////////////////////////////////////////////
    
    def cargarProveedores(self):
        conexion = Conn()
        proveedoresExistentes = []
        for i in conexion.mostrarTodosProveedores():
            proveedoresExistentes.append(""+i["nombre"][:12]+": "+i["email"])
        conexion.cerrarConexion()
        return proveedoresExistentes
    
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
                    return k[1]#cantidad en stock
        else:
            pass
        return 0
    
    def crearTabla(self):
        #configuracion de la tabla
        self.tablaProductos.setColumnCount(5)
        self.tablaProductos.setRowCount(0)
        self.tablaProductos.setHorizontalHeaderLabels(["Nombre","Cantidad","Precio","Código",""])
        
    def anadirProductoACompra(self):
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
            print("oculto")
            self.hide_tablaProductos()
    
    def cancelarCompra(self):
        
        self.hide_datosCompra()
        self.hide_tablaProductos()

    def anadirCompra(self):
        if self.tablaProductos.rowCount() == 0:
            msg = QMessageBox()
            msg.setWindowIcon(QIcon(r"Modulos/WEB/imagenes/gestr.ico"))
            msg.setWindowTitle("Atención")
            msg.setText("Debes seleccionar al menos un producto")
            msg.addButton(QMessageBox.StandardButton.Ok)
            msg.exec()
        else:
            conexion = Conn()
            #OBTENER PROVEEDOR
            proveedores = conexion.mostrarTodosProveedores()
            try:
                for prvdr in proveedores:
                    if prvdr["email"] == self.elegirProveedor.currentText()[self.elegirProveedor.currentText().index(":")+1:].replace(" ",""):
                        proveedor = prvdr
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
            productos = self.comprobarProductosCompra(self.obtener_ProductosTabla(self.tablaProductos))
            print(productos)
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

            descripcionProducto = "" #"\n".join([f"Producto {i+1}: {item['Nombre']} - {item["Cantidad"]} unidades - €item['subtotal'] (con IVA) - Código: {item["Código"]} - {item["iva"]} IVA" for i, item in enumerate(productos)])
            
            
            productos_id = "\n".join([f"{item["Código"]}: {item["Cantidad"]} unidades" for item in productos])

            id_compra = self.generarIDPedido()
            estado = "Comprado"
            compra = [
                id_compra,
                # - suma todos los precios de los productos
                self.obtenerTotalPrecio(productos),
                (proveedor["id"]),
                datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
                productos_id,
                modoPago,
                estado
            ]

            if conexion.registrarCompra(compra):
                self.cancelarCompra()
                conexion.cerrarConexion()
                self.mostrarTablaCompras()
                self.lblstock.setText(f"En stock: 0\tUnidades de compra:")
                #self.actualizarStock(id_compra)
        
    def comprobarProductosCompra(self,productos):
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
    
    def obtenerTotalPrecio(self,productos:list[dict]):
        total = 0.0

        for producto in productos:
            precio = float(producto.get('Precio', 0))
            cantidad = float(producto.get('Cantidad', 1))
            subtotal = precio * cantidad
            total += subtotal
        return round(total, 2)
    
    def generarIDPedido(self):
        from faker import Faker
        faker = Faker()
        return datetime.now().strftime("%d%m%Y")+''.join(faker.random_letters(7))[:10]
    
    def eliminarCompra(self,pid):
        confirmacion = QMessageBox.question(
            self, 
            "Confirmar eliminación", 
            f"¿Estás seguro de que quieres eliminar esta compra?\nEsta acción es irreversible",  
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No  
        )
        
        if confirmacion == QMessageBox.Yes:
            conexion = Conn()
            
            compras: list[dict] = self.obtener_ProductosTabla(self.tableCompras)
        
            for compra in compras:
                if compra["ID Compra"] == pid:
                    productos_str = compra["Productos"]
                    
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
                            cantidad_comprada = productos_unidades[producto_id]
                            nuevo_stock = int(stock_actual) - int(cantidad_comprada)
                            if nuevo_stock<0:
                                nuevo_stock = 0
                            conexion.actualizarStock(producto_id, nuevo_stock)
                            conexion.eliminarCompra(pid)
                            self.mostrarTablaCompras()
                        else:
                            pass
                    
                    self.mostrarTablaCompras()    
                    break   

                self.mostrarTablaCompras()
                                            
        else:
            print("Eliminación cancelada.")
            
    def actualizarStock(self,pid,bool):
        
        compras: list[dict] = self.obtener_ProductosTabla(self.tableCompras)
        
        for compra in compras:
            
            if compra["ID Compra"] == pid:
                productos_str = compra["Productos"]
                
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
                for producto_id, stock_actual in id_y_stock:
                    if producto_id in productos_unidades:
                        cantidad_vendida = productos_unidades[producto_id]
                        if bool:
                            nuevo_stock = int(stock_actual) + int(cantidad_vendida)
                        if bool == False:
                            nuevo_stock = int(stock_actual) - int(cantidad_vendida)
                        print(stock_actual, nuevo_stock)
                        conexion.actualizarStock(producto_id, nuevo_stock)
                    else:
                        pass
                    
                break   
    
    def buscar(self):
        
        texto_busqueda = self.barraBusqueda.text().strip().lower()
        
        for fila in range(self.tableCompras.rowCount()):
            item = self.tableCompras.item(fila,self.buscarPor.currentIndex())
            if item.text() != texto_busqueda:
                self.tableCompras.setRowHidden(fila, texto_busqueda not in item.text().lower())
            else:
                pass
    
    def generarPdf(self,pid):
        confirmacion = QMessageBox.question(
            self, 
            "Generar factura", 
            f"¿Generar factura de esta compra?\n",  
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No  
        )
        
        if confirmacion == QMessageBox.Yes:
            
            QMessageBox.information(
                        self,
                        "Documento generado con éxito",
                        f"Documento ubicado en el directorio ComprasGeneradas\n",
                        QMessageBox.Ok
                    )
            
            print(pid)
            self.windowPdf = PdfWindow()
            self.windowPdf.generarPdf(pid)
        
        else:
            pass 
    
    def newSupplierDisplay(self):
        if self.rbuttonSeleccionarProveedor.isChecked():
            self.stackedWidgetProveedor.setCurrentIndex(0)
        else:
            self.stackedWidgetProveedor.setCurrentIndex(1)
    
    def anadirProveedor(self):
        conexion = Conn()
        
        confirmacion = QMessageBox.question(
            self, 
            "Confirmar", 
            f"¿Añadir nuevo proveedor?",  
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No  
        )
        
        if confirmacion == QMessageBox.Yes:

            #registrar datos nuevo proveedor
            proveedor = [
                ""+self.nombreProveedor.text(),
                ""+self.cifProveedor.text(),
                ""+self.emailProveedor.text(),
                ""+self.telefonoProveedor.text(),
                ""+self.direccionProveedor.text(),
                ""+self.descripcionProveedor.toPlainText(),
                ""+self.comentariosProveedor.toPlainText()                   
            ]
            
            if conexion.registrarProveedor(proveedor):
                print("exito en el registro")
            else:
                print("Error al registrar el nuevo proveedor")
            
            self.proveedores = self.cargarProveedores()
            self.elegirProveedor.clear()
            self.elegirProveedor.addItems(self.proveedores)

            #limpiar campos
            for linedit in self.proveedorNuevoFrame.findChildren(PyLineEdit):
                try:
                    linedit.setText("")
                except:
                    print("error al limpiar")

            #cambiar a proveedor existente
            self.rbuttonSeleccionarProveedor.setChecked(True)
            self.rbuttonNuevoProveedor.setChecked(False)
            self.newSupplierDisplay()

    def generarID(self):
        from faker import Faker
        faker = Faker()
        id = str(faker.uuid4())
        id = id[::6]+self.nombreProveedor.text().replace(" ","")[::3]+self.emailProveedor.text()
        return id[:10]
    
    def cambiarEstadoCompra(self, pid, estado,estado_chbox:QCheckBox):
        conexion = Conn()
        if estado == 0:
            nuevo_estado = "Comprado"
            estado_chbox.setText(nuevo_estado)
            conexion.cambiarEstadoCompra(pid,nuevo_estado)
            self.actualizarStock(pid,False)
            print(f"Compra {pid} marcada como {nuevo_estado}")
            conexion.cerrarConexion()
        else:
            nuevo_estado = "Recibido"
            estado_chbox.setText(nuevo_estado)
            conexion.cambiarEstadoCompra(pid,nuevo_estado)
            self.actualizarStock(pid,True)
            print(f"Compra {pid} marcada como {nuevo_estado}")
            conexion.cerrarConexion()
            
        self.mostrarTablaCompras()