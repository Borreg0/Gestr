from Modulos.PRINCIPAL.imports.core import *
from Modulos.PRINCIPAL.imports.widgets_import import *
from Modulos.PRINCIPAL.imports.bbdd_conn import *
from .pdf_windowProveedores import *

class Proveedores_Page(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent = parent)

        self.IDproveedorSeleccionado = ""
        
        self.setObjectName(u"page_proveedores")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.proveedores_layout_superior = QHBoxLayout()
        self.proveedores_layout_superior.setObjectName(u"proveedores_layout_superior")
        
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
        self.columnasTableWidget = ["ID", "Nombre", "CIF", "Email", "Teléfono","Dirección","Descripción","Comentarios"]
        self.buscarPor.addItems(self.columnasTableWidget)
        self.columnasTable = self.columnasTableWidget
        self.columnasTable.insert(0,"Acciones")
        self.buscarPor.setStyleSheet(f"border: none; font:500 13pt; height: {self.btnLupa.height()-4}")
        
        self.labelCurrentPage = QLabel("Gestión de Proveedores")
        self.labelCurrentPage.setStyleSheet(f"padding-left:10 ;border: none; font:500 13pt; font-weight: bold;")
        
        self.layoutBarraBusqueda.addWidget(self.labelCurrentPage)
        self.layoutBarraBusqueda.addSpacerItem(self.espaciadorBusqueda)
        self.layoutBarraBusqueda.addWidget(self.labelBusqueda)
        self.layoutBarraBusqueda.addWidget(self.buscarPor)
        self.layoutBarraBusqueda.addWidget(self.barraBusqueda)
        self.layoutBarraBusqueda.addWidget(self.btnLupa)
        
        self.proveedores_layout_superior.addWidget(self.frame)

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
        
        self.btn_anadirProveedor = PyPushButton(icon_path="user-plus.svg", text_padding=0)
        self.btn_anadirProveedor.setFixedWidth(50)
        self.btn_anadirProveedor.setStyleSheet("border-radius: 4; background-color: #356b6b")
        self.btn_anadirProveedor.setMaximumSize(QSize(150, 16777215))
        self.btn_anadirProveedor.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout.addWidget(self.btn_anadirProveedor)
        self.proveedores_layout_superior.addWidget(self.frame_2)
        self.verticalLayout.addLayout(self.proveedores_layout_superior)

        self.proveedores_layout_inferior = QHBoxLayout()
        
        #//////////////////////////////////////////////////////////////////////////////
        #CODIGO TABLA
        #tablewidget 
        self.tableWidget = PyTableWidget(self)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.llenarTabla()
        
        
        #añadir tabla al layout
        self.proveedores_layout_inferior.addWidget(self.tableWidget)

        #este panel debe ocultarse al principio y aparecer cuando se pulse añadir cliente
        self.datosProveedor = QFrame(self)
        self.datosProveedor.setFixedWidth(0)
        self.datosProveedor.setStyleSheet(
            '''
            background-color: beige;
            border-radius: 7px;
            border: 4px solid #444;
            '''
            )
        self.datosProveedor.setFrameShape(QFrame.Shape.StyledPanel)
        self.datosProveedor.setFrameShadow(QFrame.Shadow.Plain)
        
        #campos de informacion de Proveedor
        self.lblnuevo_proveedor = QLabel("prueba")
        self.lblnuevo_proveedor.setStyleSheet("font:600 14pt; color: Black; border:none;")
        self.lblnuevo_proveedor.setFixedSize(160,60)
        
        self.nombreProveedorlbl = QLabel("Nombre")
        self.nombreProveedorlbl.setStyleSheet("border:none; font: 12pt black")
        self.nombreProveedorlbl.setVisible(False)
        self.nombreProveedor = PyLineEdit()
        self.nombreProveedor.setPlaceholderText("Nombre")
        self.nombreProveedor.setStyleSheet("border: 2px solid #444; font:500 13pt")
        
        self.cifProveedorlbl = QLabel("CIF")
        self.cifProveedorlbl.setStyleSheet("border:none; font: 12pt black")
        self.cifProveedorlbl.setVisible(False)
        self.cifProveedor = PyLineEdit()
        self.cifProveedor.setPlaceholderText("CIF")
        self.cifProveedor.setStyleSheet("border: 2px solid #444; font:500 13pt") 
        
        self.emailProveedorlbl = QLabel("Email")
        self.emailProveedorlbl.setStyleSheet("border:none; font: 12pt black")
        self.emailProveedorlbl.setVisible(False)
        self.emailProveedor = PyLineEdit()
        self.emailProveedor.setPlaceholderText("Email")
        self.emailProveedor.setStyleSheet("border: 2px solid #444; font:500 13pt")

        self.telefonoProveedorlbl = QLabel("Teléfono")
        self.telefonoProveedorlbl.setStyleSheet("border:none; font: 12pt black")
        self.telefonoProveedorlbl.setVisible(False)
        self.telefonoProveedor = PyLineEdit()
        self.telefonoProveedor.setPlaceholderText("Telefono")
        self.telefonoProveedor.setStyleSheet("border: 2px solid #444; font:500 13pt") 
        
        self.direccionProveedorlbl = QLabel("Dirección")
        self.direccionProveedorlbl.setStyleSheet("border:none; font: 12pt black")
        self.direccionProveedorlbl.setVisible(False)
        self.direccionProveedor = PyLineEdit()
        self.direccionProveedor.setPlaceholderText("Dirección")
        self.direccionProveedor.setStyleSheet("border: 2px solid #444; font:500 13pt")

        self.descripcionProveedorlbl = QLabel("Descripción")
        self.descripcionProveedorlbl.setStyleSheet("border:none; font: 12pt black")
        self.descripcionProveedorlbl.setVisible(False)
        self.descripcionProveedor = QPlainTextEdit()
        self.descripcionProveedor.setPlaceholderText("Descripción")
        self.descripcionProveedor.setStyleSheet("border: 2px solid #444; font:500 13pt")
        
        self.comentariosProveedorlbl = QLabel("Comentarios")
        self.comentariosProveedorlbl.setStyleSheet("border:none; font: 12pt black")
        self.comentariosProveedorlbl.setVisible(False)
        self.comentariosProveedor = QPlainTextEdit()
        self.comentariosProveedor.setPlaceholderText("Comentarios")
        self.comentariosProveedor.setStyleSheet("border: 2px solid #444; font:500 13pt")
         
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
        self.layout_datosProveedor = QVBoxLayout(self.datosProveedor)
    
        self.scrollarea = QScrollArea()
        self.frameScrollArea = QFrame()
        self.frameScrollArea.setMaximumWidth(240)
        self.scrollarea.setStyleSheet("border:none;")
        self.frameScrollareaLayout = QVBoxLayout(self.frameScrollArea)
        self.frameScrollArea.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)

        self.layout_datosProveedor.addWidget(self.lblnuevo_proveedor)

        self.frameScrollareaLayout.addWidget(self.nombreProveedorlbl)
        self.frameScrollareaLayout.addWidget(self.nombreProveedor)
        self.frameScrollareaLayout.addWidget(self.cifProveedorlbl)
        self.frameScrollareaLayout.addWidget(self.cifProveedor)
        self.frameScrollareaLayout.addWidget(self.emailProveedorlbl)
        self.frameScrollareaLayout.addWidget(self.emailProveedor)
        self.frameScrollareaLayout.addWidget(self.telefonoProveedorlbl)
        self.frameScrollareaLayout.addWidget(self.telefonoProveedor)
        self.frameScrollareaLayout.addWidget(self.direccionProveedorlbl)
        self.frameScrollareaLayout.addWidget(self.direccionProveedor)
        self.frameScrollareaLayout.addWidget(self.descripcionProveedorlbl)
        self.frameScrollareaLayout.addWidget(self.descripcionProveedor)
        self.frameScrollareaLayout.addWidget(self.comentariosProveedorlbl)
        self.frameScrollareaLayout.addWidget(self.comentariosProveedor)

        self.scrollarea.setWidgetResizable(True)
        self.scrollarea.setWidget(self.frameScrollArea)
        self.scrollarea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        self.aceptar_cancelar_frame = QFrame()
        self.aceptar_cancelar_frame.setStyleSheet("border: none")
        self.layout_aceptar_cancelar_frame = QHBoxLayout(self.aceptar_cancelar_frame)
        self.layout_aceptar_cancelar_frame.addWidget(self.btn_cancelar)
        self.layout_aceptar_cancelar_frame.addWidget(self.btn_aceptar)
        self.layout_aceptar_cancelar_frame.addWidget(self.btn_editar)
        
        self.spacer_nuevoProveedorFrame = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.layout_datosProveedor.addWidget(self.scrollarea, stretch=1,alignment=Qt.AlignHCenter)
        self.layout_datosProveedor.addWidget(self.aceptar_cancelar_frame)
        
        self.proveedores_layout_inferior.addWidget(self.datosProveedor)
        self.verticalLayout.addLayout(self.proveedores_layout_inferior)
        
        #ACCIONES BOTONES
        #IMPLEMENTACION METODO BUSCAR CADA VEZ QUE SE MODIFIQUE EL TEXTO
        self.barraBusqueda.textChanged.connect(lambda checked: self.buscar())
        #funcion boton añadir proveedor mostrar qframe
        self.btn_anadirProveedor.clicked.connect(self.show_datosProveedor)
        self.btn_anadirProveedor.clicked.connect(self.show_aceptarBtn)
        #ACCIONES BOTONES ACEPTAR - EDITAR - CANCELAR
        self.btn_aceptar.clicked.connect(self.anadirProveedor)
        self.btn_editar.clicked.connect(self.editarProveedor)
        self.btn_cancelar.clicked.connect(self.hide_datosProveedor)
        
    #metodos
    def show_datosProveedor(self):
        #anchura del menu lateral izquierdo
        self.limpiarCampos()
        
        self.lblnuevo_proveedor.setText("Nuevo Proveedor")
        datosproveedor_width = self.datosProveedor.width()
        
        if datosproveedor_width <= 10:
            width = 300
            self.scrollarea.setFixedWidth(width)
        else:
            pass 
             
        #empezar animacion
        self.animation = QPropertyAnimation(self.datosProveedor, b"minimumWidth")    
        self.animation.setStartValue(datosproveedor_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.OutCirc)
        self.animation.start()
        
    def hide_datosProveedor(self):
        
        datosproveedor_width = self.datosProveedor.width()
        
        print(datosproveedor_width)
        if datosproveedor_width > 0:
                width = 0
                self.scrollarea.setFixedWidth(width)  
        else:
            pass
                
        #empezar animacion
        self.animation = QPropertyAnimation(self.datosProveedor, b"minimumWidth")    
        self.animation.setStartValue(datosproveedor_width)
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
        self.nombreProveedorlbl.setVisible(True)
        self.emailProveedorlbl.setVisible(True)
        self.telefonoProveedorlbl.setVisible(True)
        self.cifProveedorlbl.setVisible(True)
        self.direccionProveedorlbl.setVisible(True)
        self.descripcionProveedorlbl.setVisible(True)
        self.comentariosProveedorlbl.setVisible(True)

    def show_aceptarBtn(self):
        self.btn_editar.setVisible(False)
        self.btn_aceptar.setVisible(True)
        
        #hacer invisibles las label
        self.nombreProveedorlbl.setVisible(False)
        self.emailProveedorlbl.setVisible(False)
        self.telefonoProveedorlbl.setVisible(False)
        self.cifProveedorlbl.setVisible(False)
        self.direccionProveedorlbl.setVisible(False)
        self.descripcionProveedorlbl.setVisible(False)
        self.comentariosProveedorlbl.setVisible(False)

    def TodosLosProveedores(self):
        #recupera todos los proveedores de la tabla
        conexion = Conn()
        proveedores = conexion.mostrarTodosProveedores()
        if proveedores is None:
            print("ERROR: NO SE ENCONTRARON PROVEEDORES")
            proveedores = []
        return proveedores

    def llenarTabla(self):
        
        try:
            proveedores = self.TodosLosProveedores()
            
            #configuracion de la tabla
            self.tableWidget.setColumnCount(len(proveedores[0].keys())+1)
            self.tableWidget.setRowCount(0)
            self.tableWidget.setHorizontalHeaderLabels(self.columnasTable)
            
            self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
            for col in range(1, self.tableWidget.columnCount()):
                self.tableWidget.horizontalHeader().setSectionResizeMode(col, QHeaderView.Stretch)
 
            for row, proveedor in enumerate(proveedores):
                self.tableWidget.insertRow(row)
                self.tableWidget.setRowHeight(row,50)

                #botones eliminar editar
                eliminarbtn = PyPushButton_editPequeno(icon_path="trash.svg",height=35)
                eliminarbtn.clicked.connect(lambda _, pid = proveedor.get("id"): self.eliminarProveedor(pid))
                
                editarbtn = PyPushButton_editPequeno(icon_path="pen-fill.svg", height=35)
                editarbtn.clicked.connect(lambda _, pid=proveedor.get("id"): self.editarProveedorbtn(pid,proveedores))
                editarbtn.clicked.connect(self.show_editBtn)
                
                generarPdf = PyPushButtonPdfPequeno(icon_path="file-type-pdf.svg", height=35)
                generarPdf.clicked.connect(lambda _, pid=proveedor.get("id"): self.generarPdf(pid))
                
                self.tableWidget.setColumnWidth(0,140)
                generarPdf.setFixedWidth(35)

                frameOpciones = QFrame()
                frameOpciones.setStyleSheet("background-color: #444; margin:1px;")
                frameOpciones.setFixedHeight(50)
                layoutFrameOpciones = QHBoxLayout(frameOpciones)
                layoutFrameOpciones.addWidget(eliminarbtn)
                layoutFrameOpciones.addWidget(editarbtn)
                layoutFrameOpciones.addWidget(generarPdf)
                layoutFrameOpciones.setContentsMargins(5,5,5,5)

                self.tableWidget.setCellWidget(row, 0, frameOpciones)

                datos = ["",
                    str(proveedor.get("id","")),
                    proveedor.get("nombre",""),
                    proveedor.get("cif",""),
                    proveedor.get("email",""),
                    proveedor.get("telefono",""),
                    proveedor.get("direccion",""),
                    proveedor.get("descripcion",""),
                    proveedor.get("comentario","")
                ]

                #columnas de la tabla
                #//////////////////////////////////////////////////////////////////////////////////////////////////////
                
                for column,value in enumerate(datos):
                    item = QTableWidgetItem(str(value))
                    self.tableWidget.setItem(row,column,item)

                for row in range(self.tableWidget.rowCount()):
                    for col in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(row, col)
                        if item:
                            item.setFlags(item.flags() or Qt.TextWordWrap)
                            item.setToolTip(item.text())
                

        except Exception:
            print(" No hay proveedores que mostrar ")

    def botonEditarEliminar_pulsado(self, fila):
        print(f"Boton pulsado en fila: {fila}")
        self.tableWidget.setCurrentCell(fila, 1)  

    def eliminarProveedor(self,proveedor_id):
        
        conexion = Conn()
        proveedores = self.TodosLosProveedores()
        
        confirmacion = QMessageBox.question(
            self, 
            "Confirmar eliminación", 
            f"¿Estás seguro de que quieres eliminar este proveedor?\nEsta acción es irreversible",  
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No  
        )
        
        if confirmacion == QMessageBox.Yes:
                        
            for proveedor in proveedores:
                if proveedor_id==proveedor["id"]:
                    print(type(proveedor_id))
                    try:
                        conexion.eliminarProveedor(proveedor_id)
                        print("datos actualizados con exito")
                    except sqlite3.Error as e:
                        QMessageBox(self, "Error en la base de datos"f": {e}")
                    break   
                                
        else:
            print("Eliminación cancelada.")

        self.llenarTabla()
        if self.datosProveedor.width()>10: 
            self.hide_datosProveedor()
        else: pass
        
    def editarProveedorbtn(self,proveedor_id,proveedores):
        
        self.limpiarCampos()
        
        for proveedor in proveedores:
            if proveedor_id == proveedor["id"]:
                self.IDproveedorSeleccionado = proveedor_id
                #mostrar nuevoCliente
                if self.datosProveedor.width() <= 10:
                    
                    self.show_datosProveedor()
                    #cargar datos en Nuevocliente
                    self.lblnuevo_proveedor.setText("Editar proveedor")
                    
                    self.nombreProveedor.setText(proveedor["nombre"])
                    self.emailProveedor.setText(proveedor["email"])
                    self.telefonoProveedor.setText(proveedor["telefono"])
                    self.direccionProveedor.setText(proveedor["direccion"])
                    self.cifProveedor.setText(proveedor["cif"])
                    self.descripcionProveedor.setPlainText(proveedor["descripcion"])
                    self.comentariosProveedor.setPlainText(proveedor["comentario"])
                else:
                    self.lblnuevo_proveedor.setText("Editar proveedor")
                    
                    self.nombreProveedor.setText(proveedor["nombre"])
                    self.emailProveedor.setText(proveedor["email"])
                    self.telefonoProveedor.setText(proveedor["telefono"])
                    self.direccionProveedor.setText(proveedor["direccion"])
                    self.cifProveedor.setText(proveedor["cif"])
                    self.descripcionProveedor.setPlainText(proveedor["descripcion"])
                    self.comentariosProveedor.setPlainText(proveedor["comentario"])
        return proveedor_id           
        
    def editarProveedor(self):
        conexion = Conn()
        proveedores = self.TodosLosProveedores()
        proveedor_id = self.IDproveedorSeleccionado
        
        #por algun motivo si no se inicializan el mundo estalla
        proveedor_editado = None
        
        confirmacion = QMessageBox.question(
            self, 
            "Confirmar", 
            f"¿Confirmar los cambios?",  
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No  
        )

        if confirmacion == QMessageBox.Yes:

            for proveedor in proveedores:
                if proveedor_id == proveedor["id"]:
                    #datos del proveedor editado
                    proveedor_editado = [
                        self.nombreProveedor.text(),
                        self.cifProveedor.text(),
                        self.emailProveedor.text(),
                        self.telefonoProveedor.text(),
                        self.direccionProveedor.text(),
                        self.descripcionProveedor.toPlainText(),
                        self.comentariosProveedor.toPlainText()
                    ]
                    proveedor_id = proveedor["id"]
                    try:
                        conexion.editarProveedor(proveedor_editado,proveedor_id)
                        print("datos actualizados con exito")
                    except sqlite3.Error as e:
                        QMessageBox(self, "Error en la base de datos"f": {e}")
                    break   

        self.hide_datosProveedor()       
        self.llenarTabla()
        
    def generarID(self):
        from faker import Faker
        faker = Faker()
        id = str(faker.uuid4())
        id = id[::6]+self.nombreProveedor.text().replace(" ","")[::3]+self.emailProveedor.text()
        return id[:10]

    def generarPdf(self,pid):
            confirmacion = QMessageBox.question(
                self, 
                "Confirmar eliminación", 
                f"¿Generar informe de este Proveedor?\n",  
                QMessageBox.Yes | QMessageBox.No, 
                QMessageBox.No  
            )
            
            if confirmacion == QMessageBox.Yes:
                
                QMessageBox.information(
                            self,
                            "Documento generado con éxito",
                            f"Documento ubicado en el la carpeta Información proveedores\n",
                            QMessageBox.Ok
                        )
                
                self.windowPdf = PdfWindow()
                self.windowPdf.generarPdf(pid)
            
            else:
                pass

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

            #registrar datos en Nuevo proveedor
            proveedor = [
                #""+self.generarID(),
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
            
            self.hide_datosProveedor()        
            self.llenarTabla()

    def limpiarCampos(self):
        #limpiar campos
        for lineEdit in self.datosProveedor.findChildren(QLineEdit):
            try:
                lineEdit.setText("")
            except:
                print("error al limpiar lineEdits")
        for plaintext in self.datosProveedor.findChildren(QPlainTextEdit):
            try:
                plaintext.setPlainText("")
            except:
                print("error al limpiar plaintexts")

    def buscar(self):
        texto_busqueda = self.barraBusqueda.text().strip().lower()
        
        for fila in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(fila,self.buscarPor.currentIndex()+1)
            if item.text() != texto_busqueda:
                self.tableWidget.setRowHidden(fila, texto_busqueda not in item.text().lower())
            else:
                pass
    
