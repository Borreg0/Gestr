from Modulos.PRINCIPAL.imports.core import *
from Modulos.PRINCIPAL.imports.widgets_import import *
from Modulos.PRINCIPAL.imports.bbdd_conn import *

class Crm_Page(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent = parent)
        
        self.setObjectName(u"page_crm")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.crm_layout_superior = QHBoxLayout()
        self.crm_layout_superior.setObjectName(u"crm_layout_superior")
        
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
        self.columnasTableWidget = ["Nombre", "Email", "Teléfono", "País", "Fecha Registro"]
        self.buscarPor.addItems(self.columnasTableWidget)
        self.columnasTable = self.columnasTableWidget
        self.columnasTable.insert(0,"Acciones")
        self.buscarPor.setStyleSheet(f"border: none; font:500 13pt; height: {self.btnLupa.height()-4}")
        
        self.labelCurrentPage = QLabel("CRM")
        self.labelCurrentPage.setStyleSheet(f"padding-left:10 ;border: none; font:500 13pt; font-weight: bold;")
        
        self.layoutBarraBusqueda.addWidget(self.labelCurrentPage)
        self.layoutBarraBusqueda.addSpacerItem(self.espaciadorBusqueda)
        self.layoutBarraBusqueda.addWidget(self.labelBusqueda)
        self.layoutBarraBusqueda.addWidget(self.buscarPor)
        self.layoutBarraBusqueda.addWidget(self.barraBusqueda)
        self.layoutBarraBusqueda.addWidget(self.btnLupa)
        
        self.crm_layout_superior.addWidget(self.frame)

        #frame del boton de nuevoCliente
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
        
        self.btn_anadirCliente = PyPushButton(icon_path="user-plus.svg", text_padding=0)
        self.btn_anadirCliente.setFixedWidth(50)
        self.btn_anadirCliente.setObjectName(u"btn_anadirCliente")
        self.btn_anadirCliente.setStyleSheet("border-radius: 4; background-color: #356b6b")
        self.btn_anadirCliente.setMaximumSize(QSize(150, 16777215))
        self.btn_anadirCliente.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout.addWidget(self.btn_anadirCliente)
        self.crm_layout_superior.addWidget(self.frame_2)
        self.verticalLayout.addLayout(self.crm_layout_superior)

        self.crm_layout_inferior = QHBoxLayout()
        self.crm_layout_inferior.setObjectName(u"crm_layout_inferior")
        
        #//////////////////////////////////////////////////////////////////////////////
        #CODIGO TABLA
        #tablewidget 
        self.tableWidget = PyTableWidget(self)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.llenarTabla()
        
        
        #añadir tabla al layout
        self.crm_layout_inferior.addWidget(self.tableWidget)

        #este panel debe ocultarse al principio y aparecer cuando se pulse añadir cliente
        self.datosCliente = QFrame(self)
        self.datosCliente.setObjectName(u"datosCliente")
        self.datosCliente.setFixedWidth(0)
        
        self.datosCliente.setStyleSheet(
            '''
            background-color: beige;
            border-radius: 7px;
            border: 4px solid #444;
            '''
            )
        self.datosCliente.setFrameShape(QFrame.Shape.StyledPanel)
        self.datosCliente.setFrameShadow(QFrame.Shadow.Plain)
        
        #campos de informacion de cliente
        self.lblnuevo_cliente = QLabel("")
        self.lblnuevo_cliente.setStyleSheet("font:600 14pt; color: Black; border:none;")
        self.lblnuevo_cliente.setFixedSize(130,60)
        
        self.nombreClientelbl = QLabel("Nombre")
        self.nombreClientelbl.setStyleSheet("border:none; font: 12pt black")
        self.nombreClientelbl.setVisible(False)
        self.nombreCliente = PyLineEdit()
        self.nombreCliente.setPlaceholderText("Nombre")
        self.nombreCliente.setStyleSheet("border: 2px solid #444; font:500 13pt") 
        
        self.emailClientelbl = QLabel("Email")
        self.emailClientelbl.setStyleSheet("border:none; font: 12pt black")
        self.emailClientelbl.setVisible(False)
        self.emailCliente = PyLineEdit()
        self.emailCliente.setPlaceholderText("Email")
        self.emailCliente.setStyleSheet("border: 2px solid #444; font:500 13pt") 
        
        self.telefonoClientelbl = QLabel("Teléfono")
        self.telefonoClientelbl.setStyleSheet("border:none; font: 12pt black")
        self.telefonoClientelbl.setVisible(False)
        self.telefonoCliente = PyLineEdit()
        self.telefonoCliente.setPlaceholderText("Telefono")
        self.telefonoCliente.setStyleSheet("border: 2px solid #444; font:500 13pt") 
        
        self.paisClientelbl = QLabel("País")
        self.paisClientelbl.setStyleSheet("border:none; font: 12pt black")
        self.paisClientelbl.setVisible(False)
        self.paisCliente = PyLineEdit()
        self.paisCliente.setPlaceholderText("País")
        self.paisCliente.setStyleSheet("border: 2px solid #444; font:500 13pt") 
         
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
        
        #añadir a layout_datoscliente
        self.layout_datosCliente = QVBoxLayout(self.datosCliente)
        
        self.layout_datosCliente.addWidget(self.lblnuevo_cliente)
        self.layout_datosCliente.addWidget(self.nombreClientelbl)
        self.layout_datosCliente.addWidget(self.nombreCliente)
        self.layout_datosCliente.addWidget(self.emailClientelbl)
        self.layout_datosCliente.addWidget(self.emailCliente)
        self.layout_datosCliente.addWidget(self.telefonoClientelbl)
        self.layout_datosCliente.addWidget(self.telefonoCliente)
        self.layout_datosCliente.addWidget(self.paisClientelbl)
        self.layout_datosCliente.addWidget(self.paisCliente)
        
        self.aceptar_cancelar_frame = QFrame()
        self.aceptar_cancelar_frame.setStyleSheet("border: none")
        self.layout_aceptar_cancelar_frame = QHBoxLayout(self.aceptar_cancelar_frame)
        self.layout_aceptar_cancelar_frame.addWidget(self.btn_cancelar)
        self.layout_aceptar_cancelar_frame.addWidget(self.btn_aceptar)
        self.layout_aceptar_cancelar_frame.addWidget(self.btn_editar)
        
        self.spacer_nuevoclienteFrame = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.layout_datosCliente.addItem(self.spacer_nuevoclienteFrame)
        self.layout_datosCliente.addWidget(self.aceptar_cancelar_frame)
        
        self.crm_layout_inferior.addWidget(self.datosCliente)
        self.verticalLayout.addLayout(self.crm_layout_inferior)
        
        #ACCIONES BOTONES
        #IMPLEMENTACION METODO BUSCAR CADA VEZ QUE SE MODIFIQUE EL TEXTO
        self.barraBusqueda.textChanged.connect(lambda checked: self.buscar())
        #funcion boton añadir cliente mostrar qframe
        self.btn_anadirCliente.clicked.connect(self.show_datosCliente)
        self.btn_anadirCliente.clicked.connect(self.show_aceptarBtn)
        #ACCIONES BOTONES ACEPTAR - EDITAR - CANCELAR
        self.btn_aceptar.clicked.connect(self.anadirCliente)
        self.btn_editar.clicked.connect(self.editarCliente)
        self.btn_cancelar.clicked.connect(self.hide_datoscliente)
        
    #metodos
    def show_datosCliente(self):
        #anchura del menu lateral izquierdo
        self.limpiarCampos()
        
        self.lblnuevo_cliente.setText("Nuevo cliente")
        datoscliente_width = self.datosCliente.width()
        
        if datoscliente_width <= 10:
            width = 300
        else:
            pass 
             
        #empezar animacion
        self.animation = QPropertyAnimation(self.datosCliente, b"minimumWidth")    
        self.animation.setStartValue(datoscliente_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.OutCirc)
        self.animation.start()
        
    def hide_datoscliente(self):
        
        datoscliente_width = self.datosCliente.width()
        
        print(datoscliente_width)
        if datoscliente_width > 0:
                width = 0
        else:
            pass
                
        #empezar animacion
        self.animation = QPropertyAnimation(self.datosCliente, b"minimumWidth")    
        self.animation.setStartValue(datoscliente_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.OutCirc)
        self.animation.start()
        self.limpiarCampos()
        
    def show_editBtn(self):
        self.btn_aceptar.setVisible(False)
        self.btn_aceptar.hide()
        self.btn_editar.setVisible(True)
        
        #hacer visibles las label
        self.nombreClientelbl.setVisible(True)
        self.emailClientelbl.setVisible(True)
        self.telefonoClientelbl.setVisible(True)
        self.paisClientelbl.setVisible(True)
    
    def show_aceptarBtn(self):
        self.btn_editar.setVisible(False)
        self.btn_aceptar.setVisible(True)
        
        #hacer invisibles las label
        self.nombreClientelbl.setVisible(False)
        self.emailClientelbl.setVisible(False)
        self.telefonoClientelbl.setVisible(False)
        self.paisClientelbl.setVisible(False)
    
#
    def TodosLosClientes(self):
        #recupera todos los clientes de la tabla
        conexion = Conn()
        clientes = conexion.mostrarTodosClientes()
        if clientes is None:
            print("ERROR: NO SE ENCONTRARON CLIENTES")
            clientes = []
        return clientes

    def llenarTabla(self):
        
        try:
            clientes = self.TodosLosClientes()
            
            #configuracion de la tabla
            self.tableWidget.setColumnCount(len(clientes[0].keys()))
            self.tableWidget.setRowCount(0)
            self.tableWidget.setHorizontalHeaderLabels(self.columnasTable)
            
            self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
            for col in range(1, self.tableWidget.columnCount()):
                self.tableWidget.horizontalHeader().setSectionResizeMode(col, QHeaderView.Stretch)

            
            for row, cliente in enumerate(clientes):
                self.tableWidget.insertRow(row)
                self.tableWidget.setRowHeight(row,50)

                #botones eliminar editar
                self.tableWidget.setCellWidget(row,0,self.botonesEditarEliminar(cliente.get("id",""),cliente,row))
                self.tableWidget.setColumnWidth(0,85)

                datos = [
                    str(cliente.get("id","")),
                    cliente.get("nombre",""),
                    cliente.get("email",""),
                    cliente.get("telefono",""),
                    cliente.get("pais",""),
                    cliente.get("registro","")
                ]

                #columnas de la tabla
                #//////////////////////////////////////////////////////////////////////////////////////////////////////
                
                for column,value in enumerate(datos):
                    item = QTableWidgetItem(str(value))
                    self.tableWidget.setItem(row,column,item)

        except Exception:
            print(" No hay clientes que mostrar ")

    #cliente_id viene desde llenar tabla
    def botonesEditarEliminar(self,cliente_id,clientes,fila):
        frame = QFrame()
        frame.setFixedHeight = self.tableWidget.rowHeight
        
        layoutbotones = QHBoxLayout(frame)
        layoutbotones.setAlignment(Qt.AlignCenter)
        
        self.btn_editarCliente = PyPushButton_edit(icon_path="pen-fill.svg",posicion=fila)
        self.btn_editarCliente.clicked.connect(lambda checked, r=fila: self.botonEditarEliminar_pulsado(r))
        
        self.btn_eliminarCliente = PyPushButton_edit(icon_path="trash.svg",posicion=fila)
        self.btn_eliminarCliente.clicked.connect(lambda checked, r=fila: self.botonEditarEliminar_pulsado(r))
        
        #botones modificar atributos
        self.btn_editarCliente.setFixedHeight(30)
        self.btn_editarCliente.setFixedWidth(30)
        self.btn_eliminarCliente.setFixedHeight(30)
        self.btn_eliminarCliente.setFixedWidth(30)
        
        layoutbotones.addWidget(self.btn_eliminarCliente)
        layoutbotones.addWidget(self.btn_editarCliente)
        
        #añadir funciones al boton
        #btn_editar.clicked.connect(lambda checked, cliente_id = cliente_id , clientes = self: self.editarClientebtn(cliente_id,clientes))
        self.btn_editarCliente.clicked.connect(lambda checked, cliente_id=cliente_id, clientes=[clientes]: self.editarClientebtn(cliente_id, clientes))
        self.btn_editarCliente.clicked.connect(self.show_editBtn)
        self.btn_eliminarCliente.clicked.connect(lambda checked, cliente_id = cliente_id , clientes = [clientes]: self.eliminarCliente(cliente_id,clientes))
        
        return frame

    def botonEditarEliminar_pulsado(self, fila):
        print(f"Boton pulsado en fila: {fila}")
        self.tableWidget.setCurrentCell(fila, 2)  

    def eliminarCliente(self,cliente_id,clientes):
        
        conexion = Conn()
        clientes = self.TodosLosClientes()
        cliente_email = self.tableWidget.currentItem().text()
        
        confirmacion = QMessageBox.question(
            self, 
            "Confirmar eliminación", 
            f"¿Estás seguro de que quieres eliminar este cliente?\nEsta acción es irreversible",  
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No  
        )
        
        if confirmacion == QMessageBox.Yes:
                        
            for cliente in clientes:
                if cliente_email==cliente["email"]:
                    cliente_id = cliente["id"]
                    print(type(cliente_id))
                    try:
                        conexion.eliminarCliente(cliente_id)
                        print("datos actualizados con exito")
                    except sqlite3.Error as e:
                        QMessageBox(self, "Error en la base de datos"f": {e}")
                    break   
                                
        else:
            print("Eliminación cancelada.")

        self.llenarTabla()
        if self.datosCliente.width()>10: 
            self.hide_datoscliente()
        else: pass
        
    def editarClientebtn(self,cliente_id,clientes):
        
        self.limpiarCampos()
        
        for cliente in clientes:
            if cliente_id == cliente["id"]:
                
                #mostrar nuevoCliente
                if self.datosCliente.width() <= 10:
                    
                    self.show_datosCliente()
                    #cargar datos en Nuevocliente
                    self.lblnuevo_cliente.setText("Editar cliente")
                    
                    self.nombreCliente.setText(cliente["nombre"])
                    self.emailCliente.setText(cliente["email"])
                    self.telefonoCliente.setText(cliente["telefono"])
                    #self.registroCliente.setText(cliente["registro"])
                    self.paisCliente.setText(cliente["pais"])
                else:
                    
                    self.lblnuevo_cliente.setText("Editar cliente")
                    
                    self.nombreCliente.setText(cliente["nombre"])
                    self.emailCliente.setText(cliente["email"])
                    self.telefonoCliente.setText(cliente["telefono"])
                    #self.registroCliente.setText(cliente["registro"])
                    self.paisCliente.setText(cliente["pais"])           
        
    def editarCliente(self):
        conexion = Conn()
        clientes = self.TodosLosClientes()
        cliente_email = self.tableWidget.currentItem().text()
        
        #por algun motivo si no se inicializan el mundo estalla
        cliente_editado = None
        cliente_id = None
        
        confirmacion = QMessageBox.question(
            self, 
            "Confirmar", 
            f"¿Confirmar los cambios?",  
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No  
        )

        if confirmacion == QMessageBox.Yes:

            for cliente in clientes:
                if cliente_email == cliente["email"]:
                    #datos del cliente editado
                    cliente_editado = [
                        self.nombreCliente.text(),
                        self.emailCliente.text(),
                        self.telefonoCliente.text(),
                        self.paisCliente.text()
                    ]
                    cliente_id = cliente["id"]
                    try:
                        conexion.editarCliente(cliente_editado,cliente_id)
                        print("datos actualizados con exito")
                    except sqlite3.Error as e:
                        QMessageBox(self, "Error en la base de datos"f": {e}")
                    break   

        self.hide_datoscliente()       
        self.llenarTabla()
        
    def generarID(self):
        from faker import Faker
        faker = Faker()
        id = str(faker.uuid4())
        id = id[::6]+self.nombreCliente.text().replace(" ","")[::3]+self.emailCliente.text()
        return id[:10]

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
            
            self.hide_datoscliente()        
            self.llenarTabla()

    def limpiarCampos(self):
        #limpiar campos
        for lineEdit in self.datosCliente.findChildren(QLineEdit):
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
    
