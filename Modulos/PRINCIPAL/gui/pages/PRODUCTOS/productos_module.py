from Modulos.PRINCIPAL.imports.core import *
from Modulos.PRINCIPAL.imports.widgets_import import *
from Modulos.PRINCIPAL.imports.bbdd_conn import *

class Productos_Page(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent = parent)
        
        self.setObjectName(u"page_inventario")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.productos_layout_superior = QHBoxLayout()
        self.productos_layout_superior.setObjectName(u"productos_layout_superior")
        
        #frame controles sobre la tabla
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
        self.columnasTableWidget = ["Código", "Nombre", "Stock", "Precio/u (€)", "IVA","Coste/u (€)"]
        self.buscarPor.addItems(self.columnasTableWidget)
        self.columnasTable = self.columnasTableWidget
        self.columnasTable.insert(0,"Acciones")
        self.buscarPor.setStyleSheet(f"border: none; font:500 13pt; height: {self.btnLupa.height()-4}")
        
        self.labelCurrentPage = QLabel("Inventario")
        self.labelCurrentPage.setStyleSheet(f"padding-left:10 ;border: none; font:500 13pt; font-weight: bold;")
        
        self.layoutBarraBusqueda.addWidget(self.labelCurrentPage)
        self.layoutBarraBusqueda.addSpacerItem(self.espaciadorBusqueda)
        self.layoutBarraBusqueda.addWidget(self.labelBusqueda)
        self.layoutBarraBusqueda.addWidget(self.buscarPor)
        self.layoutBarraBusqueda.addWidget(self.barraBusqueda)
        self.layoutBarraBusqueda.addWidget(self.btnLupa)
        
        self.productos_layout_superior.addWidget(self.frame)

        #frame del boton de nuevoProducto
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
        
        self.btn_anadirProductos = PyPushButton(icon_path="add_box.svg", text_padding=0)
        self.btn_anadirProductos.setFixedWidth(50)
        self.btn_anadirProductos.setObjectName(u"btn_anadirProductos")
        self.btn_anadirProductos.setStyleSheet("border-radius: 4; background-color: #356b6b")
        self.btn_anadirProductos.setMaximumSize(QSize(150, 16777215))
        self.btn_anadirProductos.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout.addWidget(self.btn_anadirProductos)
        self.productos_layout_superior.addWidget(self.frame_2)
        self.verticalLayout.addLayout(self.productos_layout_superior)

        self.productos_layout_inferior = QHBoxLayout()
        self.productos_layout_inferior.setObjectName(u"productos_layout_inferior")
        
        #//////////////////////////////////////////////////////////////////////////////
        #CODIGO TABLA
        #tablewidget 
        self.tableWidget = PyTableWidget(self)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.llenarTabla()
        
        
        #añadir tabla al layout
        self.productos_layout_inferior.addWidget(self.tableWidget)

        #este panel debe ocultarse al principio y aparecer cuando se pulse añadir cliente
        self.datosProducto = QFrame(self)
        self.datosProducto.setObjectName(u"datosProducto")
        self.datosProducto.setFixedWidth(0)
        
        self.datosProducto.setStyleSheet(
            '''
            background-color: beige;
            border-radius: 7px;
            border: 4px solid #444;
            '''
            )
        self.datosProducto.setFrameShape(QFrame.Shape.StyledPanel)
        self.datosProducto.setFrameShadow(QFrame.Shadow.Plain)
        
        #campos de informacion de producto
        self.lblnuevo_producto = QLabel("")
        self.lblnuevo_producto.setStyleSheet("font:600 14pt; color: Black; border:none;")
        self.lblnuevo_producto.setFixedSize(180,60)
        
        self.nombreProductolbl = QLabel("Nombre")
        self.nombreProductolbl.setStyleSheet("border:none; font: 12pt black")
        self.nombreProductolbl.setVisible(False)
        self.nombreProducto = PyLineEdit()
        self.nombreProducto.setPlaceholderText("Nombre")
        self.nombreProducto.setStyleSheet("border: 2px solid #444; font:500 13pt") 
        
        self.stockProductolbl = QLabel("Stock")
        self.stockProductolbl.setStyleSheet("border:none; font: 12pt black")
        self.stockProductolbl.setVisible(False)
        self.stockProducto = PyLineEdit()
        self.stockProducto.setPlaceholderText("Stock")
        self.stockProducto.setStyleSheet("border: 2px solid #444; font:500 13pt") 
        
        self.precioProductolbl = QLabel("Precio/u (€)")
        self.precioProductolbl.setStyleSheet("border:none; font: 12pt black")
        self.precioProductolbl.setVisible(False)
        self.precioProducto = PyLineEdit()
        self.precioProducto.setPlaceholderText("Precio")
        self.precioProducto.setStyleSheet("border: 2px solid #444; font:500 13pt") 
        
        self.ivaProductolbl = QLabel("IVA")
        self.ivaProductolbl.setStyleSheet("border:none; font: 12pt black")
        self.ivaProductolbl.setVisible(False)
        self.ivaProducto = PyLineEdit()
        self.ivaProducto.setPlaceholderText("IVA")
        self.ivaProducto.setStyleSheet("border: 2px solid #444; font:500 13pt") 
        
        self.costeProductolbl = QLabel("Coste/u (€)")
        self.costeProductolbl.setStyleSheet("border:none; font: 12pt black")
        self.costeProductolbl.setVisible(False)
        self.costeProducto = PyLineEdit()
        self.costeProducto.setPlaceholderText("Coste ")
        self.costeProducto.setStyleSheet("border: 2px solid #444; font:500 13pt")
        
         
        self.btn_cancelar = PyPushButton(
            text="Cancelar",
            height=45,
            icon_path="x-lg.svg",
        )
        self.btn_aceptar = PyPushButton(
            text="Añadir",
            height=45,
            icon_path="check2.svg"
        )
        self.btn_editar = PyPushButton(
            text="Editar",
            height=45,
            icon_path="pen-fill.svg"
        )
        
        #añadir a layout_datosProducto
        self.layout_datosProducto = QVBoxLayout(self.datosProducto)
        
        self.layout_datosProducto.addWidget(self.lblnuevo_producto)
        self.layout_datosProducto.addWidget(self.nombreProductolbl)
        self.layout_datosProducto.addWidget(self.nombreProducto)
        self.layout_datosProducto.addWidget(self.stockProductolbl)
        self.layout_datosProducto.addWidget(self.stockProducto)
        self.layout_datosProducto.addWidget(self.precioProductolbl)
        self.layout_datosProducto.addWidget(self.precioProducto)
        self.layout_datosProducto.addWidget(self.ivaProductolbl)
        self.layout_datosProducto.addWidget(self.ivaProducto)
        self.layout_datosProducto.addWidget(self.costeProductolbl)
        self.layout_datosProducto.addWidget(self.costeProducto)
        
        self.aceptar_cancelar_frame = QFrame()
        self.aceptar_cancelar_frame.setStyleSheet("border: none")
        self.layout_aceptar_cancelar_frame = QHBoxLayout(self.aceptar_cancelar_frame)
        self.layout_aceptar_cancelar_frame.addWidget(self.btn_cancelar)
        self.layout_aceptar_cancelar_frame.addWidget(self.btn_aceptar)
        self.layout_aceptar_cancelar_frame.addWidget(self.btn_editar)
        
        self.spacer_nuevoclienteFrame = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.layout_datosProducto.addItem(self.spacer_nuevoclienteFrame)
        self.layout_datosProducto.addWidget(self.aceptar_cancelar_frame)
        
        self.productos_layout_inferior.addWidget(self.datosProducto)
        self.verticalLayout.addLayout(self.productos_layout_inferior)
        
        #ACCIONES BOTONES
        #IMPLEMENTACION METODO BUSCAR CADA VEZ QUE SE MODIFIQUE EL TEXTO
        self.barraBusqueda.textChanged.connect(lambda checked: self.buscar())
        #funcion boton añadir cliente mostrar qframe
        self.btn_anadirProductos.clicked.connect(self.show_datosProducto)
        self.btn_anadirProductos.clicked.connect(self.show_aceptarBtn)
        #ACCIONES BOTONES ACEPTAR - EDITAR - CANCELAR
        self.btn_aceptar.clicked.connect(self.anadirProducto)
        self.btn_editar.clicked.connect(self.editarProducto)
        self.btn_cancelar.clicked.connect(self.hide_datosProducto)
        
    #metodos
    def show_datosProducto(self):
        #anchura del menu lateral izquierdo
        self.limpiarCampos()
        try:
            self.lblnuevo_producto.setText("Nuevo producto")
            datosProducto_width = self.datosProducto.width()
            
            if datosProducto_width <= 10:
                width = 300
            else:
                pass 
                
            #empezar animacion
            self.animation = QPropertyAnimation(self.datosProducto, b"minimumWidth")    
            self.animation.setStartValue(datosProducto_width)
            self.animation.setEndValue(width)
            self.animation.setDuration(300)
            self.animation.setEasingCurve(QEasingCurve.OutCirc)
            self.animation.start()
        except:
            pass
        
    def hide_datosProducto(self):
        
        datosProducto_width = self.datosProducto.width()
        
        print(datosProducto_width)
        if datosProducto_width > 0:
                width = 0
        else:
            pass
                
        #empezar animacion
        self.animation = QPropertyAnimation(self.datosProducto, b"minimumWidth")    
        self.animation.setStartValue(datosProducto_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.OutCirc)
        self.animation.start()
        self.limpiarCampos()
        
    def show_editBtn(self):
        #hacer visible boton
        self.btn_aceptar.setVisible(False)
        self.btn_aceptar.hide()
        self.btn_editar.setVisible(True)
        
        #hacer visibles las label
        self.nombreProductolbl.setVisible(True)
        self.stockProductolbl.setVisible(True)
        self.precioProductolbl.setVisible(True)
        self.ivaProductolbl.setVisible(True)
        self.costeProductolbl.setVisible(True)
    
    def show_aceptarBtn(self):
        self.btn_editar.setVisible(False)
        self.btn_aceptar.setVisible(True)
        
        #hacer invisibles las label
        self.nombreProductolbl.setVisible(False)
        self.stockProductolbl.setVisible(False)
        self.precioProductolbl.setVisible(False)
        self.ivaProductolbl.setVisible(False)
        self.costeProductolbl.setVisible(False)
    
#
    def TodosLosProductos(self):
        #recupera todos los productos de la tabla
        conexion = Conn()
        productos = conexion.mostrarTodosProductos()
        if productos is None:
            print("ERROR: NO SE ENCONTRARON PRODUCTOS")
            productos = []
        return productos

    def llenarTabla(self):

        try:
            productos = self.TodosLosProductos()

            #configuracion de la tabla
            self.tableWidget.setColumnCount(len(productos[0].keys())+1)
            self.tableWidget.setRowCount(0)
            self.tableWidget.setHorizontalHeaderLabels(self.columnasTable)    
            self.tableWidget.horizontalHeader().setSectionResizeMode(0,QHeaderView.Fixed)

            self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
            for col in range(1, self.tableWidget.columnCount()):
                self.tableWidget.horizontalHeader().setSectionResizeMode(col, QHeaderView.Stretch)

            for row, producto in enumerate(productos):
                self.tableWidget.insertRow(row)
                self.tableWidget.setRowHeight(row,50)

                #botones eliminar editar
                self.tableWidget.setCellWidget(row,0,self.botonesEditarEliminar(producto.get("id",""),producto,row))
                self.tableWidget.setColumnWidth(0,85)

                datos = [
                    str(producto.get("id","")),
                    producto.get("nombre",""),
                    producto.get("stock",""),
                    producto.get("precio",""),
                    producto.get("iva",""),
                    producto.get("coste","")
                ]
                #columnas de la tabla
                #//////////////////////////////////////////////////////////////////////////////////////////////////////
                for column,value in enumerate(datos,start=1):
                    item = QTableWidgetItem(str(value))
                    self.tableWidget.setItem(row,column,item)
              
        except Exception:
            print("No hay productos que mostrar")

    #cliente_id viene desde llenar tabla
    def botonesEditarEliminar(self,producto_id,productos,fila):
        frame = QFrame()
        frame.setFixedHeight = self.tableWidget.rowHeight
        
        layoutbotones = QHBoxLayout(frame)
        
        layoutbotones.setAlignment(Qt.AlignCenter)
        
        self.btn_editarProducto = PyPushButton_edit(icon_path="pen-fill.svg",posicion=fila)
        self.btn_editarProducto.clicked.connect(lambda checked, r=fila: self.botonEditarEliminar_pulsado(r))
        
        self.btn_eliminarProducto = PyPushButton_edit(icon_path="trash.svg",posicion=fila)
        self.btn_eliminarProducto.clicked.connect(lambda checked, r=fila: self.botonEditarEliminar_pulsado(r))
        
        #botones modificar atributos
        self.btn_editarProducto.setFixedHeight(30)
        self.btn_editarProducto.setFixedWidth(30)
        self.btn_eliminarProducto.setFixedHeight(30)
        self.btn_eliminarProducto.setFixedWidth(30)
        
        layoutbotones.addWidget(self.btn_eliminarProducto)
        layoutbotones.addWidget(self.btn_editarProducto)
        
        #añadir funciones al boton
        
        self.btn_editarProducto.clicked.connect(lambda checked, producto_id=producto_id, productos=[productos]: self.editarProductobtn(producto_id, productos))
        self.btn_editarProducto.clicked.connect(self.show_editBtn)
        self.btn_eliminarProducto.clicked.connect(lambda checked, producto_id=producto_id, productos=[productos]: self.eliminarProducto(producto_id,productos))
        
        return frame

    def botonEditarEliminar_pulsado(self, fila):
        print(f"Boton pulsado en fila: {fila}")
        self.tableWidget.setCurrentCell(fila, 1)  

    def eliminarProducto(self,cliente_id,clientes):
        
        conexion = Conn()
        productos = self.TodosLosProductos()
        producto_id = self.tableWidget.currentItem().text()
        
        confirmacion = QMessageBox.question(
            self, 
            "Confirmar eliminación", 
            f"¿Estás seguro de que quieres eliminar este producto?\nEsta acción es irreversible",  
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No  
        )
        
        if confirmacion == QMessageBox.Yes:
            
            for producto in productos:
                if producto_id == producto["id"]:
                    try:
                        conexion.eliminarProducto(producto_id)
                        print("datos actualizados con exito")
                    except sqlite3.Error as e:
                        QMessageBox(self, "Error en la base de datos"f": {e}")
                    break   
                                
        else:
            print("Eliminación cancelada.")

        self.llenarTabla()
        if self.datosProducto.width()>10: 
            self.hide_datosProducto()
        else: pass
        
    def editarProductobtn(self,producto_id,productos):
        
        self.limpiarCampos()
        
        for producto in productos:
            if producto_id == producto["id"]:
                
                #mostrar nuevoCliente
                if self.datosProducto.width() <= 10:
                    
                    self.show_datosProducto()
                    #cargar datos en Nuevocliente
                    self.lblnuevo_producto.setText("Editar producto")
                    
                    self.nombreProducto.setText(producto["nombre"])
                    self.stockProducto.setText(str(producto["stock"]))
                    self.precioProducto.setText(str(producto["precio"]))
                    self.ivaProducto.setText(str(producto["iva"]))
                    self.costeProducto.setText(str(producto["coste"]))
                else:
                    
                    self.lblnuevo_producto.setText("Editar producto")
                    
                    self.nombreProducto.setText(producto["nombre"])
                    self.stockProducto.setText(str(producto["stock"]))
                    self.precioProducto.setText(str(producto["precio"]))
                    self.ivaProducto.setText(str(producto["iva"]))
                    self.costeProducto.setText(str(producto["coste"]))           
        
    def editarProducto(self):
        conexion = Conn()
        productos = self.TodosLosProductos()
        producto_id = self.tableWidget.currentItem().text()
        
        confirmacion = QMessageBox.question(
            self, 
            "Confirmar", 
            f"¿Confirmar los cambios?",  
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No  
        )

        if confirmacion == QMessageBox.Yes:
            for producto in productos:
                print(producto_id,producto["id"])
                if producto_id == producto["id"]:
                    #datos del cliente editado
                    producto_editado = [
                        self.nombreProducto.text(),
                        int(self.stockProducto.text()),
                        float(self.precioProducto.text()),
                        float(self.ivaProducto.text()),
                        float(self.costeProducto.text())
                    ]
                    try:
                        conexion.editarProducto(producto_editado,producto_id)
                        print("datos actualizados con exito")
                    except sqlite3.Error as e:
                        QMessageBox(self, "Error en la base de datos"f": {e}")
                    break   

        self.hide_datosProducto()       
        self.llenarTabla()
        
    def generarID(self,nombreProducto:str):
        from faker import Faker
        faker = Faker()

        return nombreProducto.upper()[:3]+"-"+str(faker.uuid4())[:5]

    def anadirProducto(self):
        conexion = Conn()
        
        confirmacion = QMessageBox.question(
            self, 
            "Confirmar", 
            f"¿Añadir nuevo producto?",  
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No  
        )
        
        if confirmacion == QMessageBox.Yes:

            #registrar datos en Nuevo productos
            producto = [
                ""+self.generarID(self.nombreProducto.text()),
                ""+self.nombreProducto.text(),
                ""+self.stockProducto.text(),
                ""+self.precioProducto.text(),
                ""+self.ivaProducto.text(),
                ""+self.costeProducto.text()                   
            ]
            
            if conexion.registrarProducto(producto):
                print("exito en el registro")
            
            self.hide_datosProducto()        
            self.llenarTabla()

    def limpiarCampos(self):
        #limpiar campos
        for lineEdit in self.datosProducto.findChildren(QLineEdit):
            try:
                lineEdit.setText("")
            except:
                print("error al limpiar lineEdits")

    def buscar(self):
        texto_busqueda = self.barraBusqueda.text().strip().lower()
        
        for fila in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(fila,self.buscarPor.currentIndex()+1)
            if item.text() != texto_busqueda:
                self.tableWidget.setRowHidden(fila, texto_busqueda not in item.text().lower())
            else:
                pass
        