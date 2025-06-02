from Modulos.PRINCIPAL.imports.core import *
from Modulos.PRINCIPAL.imports.widgets_import import *
from Modulos.PRINCIPAL.imports.bbdd_conn import *

import bcrypt

class Empleados_Page(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent = parent)
        
        self.setObjectName(u"page_empleados")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.empleados_layout_superior = QHBoxLayout()
        self.empleados_layout_superior.setObjectName(u"empleados_layout_superior")
        
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
        self.columnasTableWidget = ["ID","Nombre", "Departamento", "Email", "Teléfono", "Rol"]
        self.buscarPor.addItems(self.columnasTableWidget)
        self.columnasTable = self.columnasTableWidget
        self.columnasTable.insert(0,"Acciones")
        self.buscarPor.setStyleSheet(f"border: none; font:500 13pt; height: {self.btnLupa.height()-4};width: 120px")
        
        self.labelCurrentPage = QLabel("Empleados")
        self.labelCurrentPage.setStyleSheet(f"padding-left:10 ;border: none; font:500 13pt; font-weight: bold;")
        
        self.layoutBarraBusqueda.addWidget(self.labelCurrentPage)
        self.layoutBarraBusqueda.addSpacerItem(self.espaciadorBusqueda)
        self.layoutBarraBusqueda.addWidget(self.labelBusqueda)
        self.layoutBarraBusqueda.addWidget(self.buscarPor)
        self.layoutBarraBusqueda.addWidget(self.barraBusqueda)
        self.layoutBarraBusqueda.addWidget(self.btnLupa)
        
        self.empleados_layout_superior.addWidget(self.frame)

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
        
        self.btn_anadirEmpleado = PyPushButton(icon_path="user-plus.svg", text_padding=0)
        self.btn_anadirEmpleado.setFixedWidth(50)
        self.btn_anadirEmpleado.setObjectName(u"btn_anadirEmpleado")
        self.btn_anadirEmpleado.setStyleSheet("border-radius: 4; background-color: #356b6b")
        self.btn_anadirEmpleado.setMaximumSize(QSize(150, 16777215))
        self.btn_anadirEmpleado.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout.addWidget(self.btn_anadirEmpleado)
        self.empleados_layout_superior.addWidget(self.frame_2)
        self.verticalLayout.addLayout(self.empleados_layout_superior)

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

        #este panel debe ocultarse al principio y aparecer cuando se pulse añadir Empleado
        self.datosEmpleado = QFrame(self)
        self.datosEmpleado.setObjectName(u"datosEmpleado")
        self.datosEmpleado.setFixedWidth(0)
        
        self.datosEmpleado.setStyleSheet(
            '''
            background-color: beige;
            border-radius: 7px;
            border: 4px solid #444;
            '''
            )
        self.datosEmpleado.setFrameShape(QFrame.Shape.StyledPanel)
        self.datosEmpleado.setFrameShadow(QFrame.Shadow.Plain)
        
        #campos de informacion de Empleado
        self.lblnuevo_Empleado = QLabel("")
        self.lblnuevo_Empleado.setStyleSheet("font:600 14pt; color: Black; border:none;")
        self.lblnuevo_Empleado.setFixedSize(150,60)
        
        self.nombreEmpleadolbl = QLabel("Nombre")
        self.nombreEmpleadolbl.setStyleSheet("border:none; font: 12pt black")
        self.nombreEmpleadolbl.setVisible(False)
        self.nombreEmpleado = PyLineEdit()
        self.nombreEmpleado.setPlaceholderText("Nombre")
        self.nombreEmpleado.setStyleSheet("border: 2px solid #444; font:500 13pt") 
        
        self.departamentoEmpleadolbl = QLabel("Departamento")
        self.departamentoEmpleadolbl.setStyleSheet("border:none; font: 12pt black")
        self.departamentoEmpleadolbl.setVisible(False)
        self.departamentoEmpleado = QComboBox()
        self.departamentoEmpleado.addItems(departamentos)
        self.departamentoEmpleado.setStyleSheet(f"border: 2px solid #444; font:500 13pt; height: {self.nombreEmpleado.height()-4}") 
        
        self.emailEmpleadolbl = QLabel("Email")
        self.emailEmpleadolbl.setStyleSheet("border:none; font: 12pt black")
        self.emailEmpleadolbl.setVisible(False)
        self.emailEmpleado = PyLineEdit()
        self.emailEmpleado.setPlaceholderText("Email")
        self.emailEmpleado.setStyleSheet("border: 2px solid #444; font:500 13pt") 
        
        self.telefonoEmpleadolbl = QLabel("Teléfono")
        self.telefonoEmpleadolbl.setStyleSheet("border:none; font: 12pt black")
        self.telefonoEmpleadolbl.setVisible(False)
        self.telefonoEmpleado = PyLineEdit()
        self.telefonoEmpleado.setPlaceholderText("Teléfono")
        self.telefonoEmpleado.setStyleSheet("border: 2px solid #444; font:500 13pt") 
        
        #combo box roles
        self.rolEmpleadolbl = QLabel("Rol")
        self.rolEmpleadolbl.setStyleSheet("border:none; font: 12pt black")
        self.rolEmpleadolbl.setVisible(False)
        self.rolEmpleado = QComboBox()
        self.rolEmpleado.addItems(roles_usuario)
        self.rolEmpleado.setStyleSheet(f"border: 2px solid #444; font:500 13pt; height: {self.telefonoEmpleado.height()-4}")
        
        #contrasena empleado
        self.contrasenaEmpleadolbl = QLabel("Contraseña")
        self.contrasenaEmpleadolbl.setStyleSheet("border:none; font: 12pt black")
        self.contrasenaEmpleadolbl.setVisible(False)
        self.contrasenaEmpleado = PyLineEdit()
        self.contrasenaEmpleado.setPlaceholderText("Contraseña")
        self.contrasenaEmpleado.setStyleSheet("border: 2px solid #444; font:500 13pt") 
         
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
        
        #añadir a layout_datosEmpleado
        self.layout_datosEmpleado = QVBoxLayout(self.datosEmpleado)
        
        self.layout_datosEmpleado.addWidget(self.lblnuevo_Empleado)
        self.layout_datosEmpleado.addWidget(self.nombreEmpleadolbl)
        self.layout_datosEmpleado.addWidget(self.nombreEmpleado)
        self.layout_datosEmpleado.addWidget(self.emailEmpleadolbl)
        self.layout_datosEmpleado.addWidget(self.emailEmpleado)
        self.layout_datosEmpleado.addWidget(self.departamentoEmpleadolbl)
        self.layout_datosEmpleado.addWidget(self.departamentoEmpleado)
        self.layout_datosEmpleado.addWidget(self.telefonoEmpleadolbl)
        self.layout_datosEmpleado.addWidget(self.telefonoEmpleado)
        self.layout_datosEmpleado.addWidget(self.rolEmpleadolbl)
        self.layout_datosEmpleado.addWidget(self.rolEmpleado)
        self.layout_datosEmpleado.addWidget(self.contrasenaEmpleadolbl)
        self.layout_datosEmpleado.addWidget(self.contrasenaEmpleado)
        
        self.aceptar_cancelar_frame = QFrame()
        self.aceptar_cancelar_frame.setStyleSheet("border: none")
        self.layout_aceptar_cancelar_frame = QHBoxLayout(self.aceptar_cancelar_frame)
        self.layout_aceptar_cancelar_frame.addWidget(self.btn_cancelar)
        self.layout_aceptar_cancelar_frame.addWidget(self.btn_aceptar)
        self.layout_aceptar_cancelar_frame.addWidget(self.btn_editar)
        
        self.spacer_nuevoEmpleadoFrame = QSpacerItem(20,20,QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.layout_datosEmpleado.addItem(self.spacer_nuevoEmpleadoFrame)
        self.layout_datosEmpleado.addWidget(self.aceptar_cancelar_frame)
        
        self.crm_layout_inferior.addWidget(self.datosEmpleado)
        self.verticalLayout.addLayout(self.crm_layout_inferior)
        
        #ACCIONES BOTONES
        #IMPLEMENTACION METODO BUSCAR CADA VEZ QUE SE MODIFIQUE EL TEXTO
        self.barraBusqueda.textChanged.connect(lambda checked: self.buscar())
        #funcion boton añadir Empleado mostrar qframe
        self.btn_anadirEmpleado.clicked.connect(self.show_datosEmpleado)
        self.btn_anadirEmpleado.clicked.connect(self.show_aceptarBtn)
        #ACCIONES BOTONES ACEPTAR - EDITAR - CANCELAR
        self.btn_aceptar.clicked.connect(self.anadirEmpleado)
        self.btn_editar.clicked.connect(self.editarEmpleado)
        self.btn_cancelar.clicked.connect(self.hide_datosEmpleado)
        #GENERAR EMAIL EMPLEADO A MEDIDA QUE SE INTRODUCE EL NOMBRE
        self.nombreEmpleado.textChanged.connect(self.generarEmailEmpleado)
        
    #metodos
    def show_datosEmpleado(self):
        #anchura del menu lateral izquierdo
        self.limpiarCampos()
        
        self.lblnuevo_Empleado.setText("Nuevo empleado")
        datosEmpleado_width = self.datosEmpleado.width()
        
        if datosEmpleado_width <= 10:
            width = 300
        else:
            pass 
             
        try:     
        #empezar animacion (Si se pulsa dos veces el boton empieza una animacion sin final. No pasa nada, solo salta un aviso)
            self.animation = QPropertyAnimation(self.datosEmpleado, b"minimumWidth")    
            self.animation.setStartValue(datosEmpleado_width)
            self.animation.setEndValue(width)
            self.animation.setDuration(300)
            self.animation.setEasingCurve(QEasingCurve.OutCirc)
            self.animation.start()
        except:
            pass
              
    def hide_datosEmpleado(self):
        
        datosEmpleado_width = self.datosEmpleado.width()
        
        print(datosEmpleado_width)
        if datosEmpleado_width > 0:
                width = 0
        else:
            pass
                
        #empezar animacion
        self.animation = QPropertyAnimation(self.datosEmpleado, b"minimumWidth")    
        self.animation.setStartValue(datosEmpleado_width)
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
        self.nombreEmpleadolbl.setVisible(True)
        self.emailEmpleadolbl.setVisible(True)
        self.telefonoEmpleadolbl.setVisible(True)
        self.departamentoEmpleadolbl.setVisible(True)
        self.rolEmpleadolbl.setVisible(True)
        self.contrasenaEmpleadolbl.setVisible(True)
    
    def show_aceptarBtn(self):
        self.btn_editar.setVisible(False)
        self.btn_aceptar.setVisible(True)
        
        #hacer invisibles las label
        self.nombreEmpleadolbl.setVisible(False)
        self.emailEmpleadolbl.setVisible(False)
        self.telefonoEmpleadolbl.setVisible(False)
        self.departamentoEmpleadolbl.setVisible(False)
        self.departamentoEmpleado.setPlaceholderText("Departamento")
        self.departamentoEmpleado.setCurrentIndex(-1)
        self.rolEmpleadolbl.setVisible(False)
        self.rolEmpleado.setPlaceholderText("Nivel de permisos")
        self.rolEmpleado.setCurrentIndex(-1)
        self.contrasenaEmpleadolbl.setVisible(False)
    
#
    def TodosLosEmpleados(self):
        #recupera todos los Empleados de la tabla
        conexion = Conn()
        Empleados = conexion.mostrarTodosEmpleados()
        if Empleados is None:
            print("ERROR: NO SE ENCONTRARON EmpleadoS")
            Empleados = []
        conexion.cerrarConexion()
        return Empleados
        
    def llenarTabla(self):
        try:
            empleados = self.TodosLosEmpleados()
            
            #configuracion de la tabla
            self.tableWidget.setColumnCount(len(empleados[0].keys()))
            self.tableWidget.setRowCount(0)
            self.tableWidget.setHorizontalHeaderLabels(self.columnasTable)
            
            self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
            for col in range(1, self.tableWidget.columnCount()):
                self.tableWidget.horizontalHeader().setSectionResizeMode(col, QHeaderView.Stretch)


            for row, empleado in enumerate(empleados):
                self.tableWidget.insertRow(row)
                self.tableWidget.setRowHeight(row,50)

                #botones eliminar editar
                self.tableWidget.setCellWidget(row,0,self.botonesEditarEliminar(empleado.get("id",""),empleado,row))
                self.tableWidget.setColumnWidth(0,85)
                
                datos = [
                    str(empleado.get('id', "")),
                    empleado.get("nombre",""),
                    empleado.get("departamento",""),
                    empleado.get("email",""),
                    empleado.get("telefono",""), 
                    empleado.get("rol","") 
                ]
                #columnas de la tabla
                #//////////////////////////////////////////////////////////////////////////////////////////////////////

                for column,value in enumerate(datos, start=1):
                    item = QTableWidgetItem(str(value))
                    self.tableWidget.setItem(row,column,item)
            
        except Exception:
            print("No hay empleados que mostrar")

    #Empleado_id viene desde llenar tabla
    def botonesEditarEliminar(self,Empleado_id,Empleados,fila):
        frame = QFrame()
        frame.setFixedHeight = self.tableWidget.rowHeight
        
        layoutbotones = QHBoxLayout(frame)
        layoutbotones.setAlignment(Qt.AlignCenter)
        
        self.btn_editarEmpleado = PyPushButton_edit(icon_path="pen-fill.svg",posicion=fila)
        self.btn_editarEmpleado.clicked.connect(lambda checked, r=fila: self.botonEditarEliminar_pulsado(r))
        
        self.btn_eliminarEmpleado = PyPushButton_edit(icon_path="trash.svg",posicion=fila)
        self.btn_eliminarEmpleado.clicked.connect(lambda checked, r=fila: self.botonEditarEliminar_pulsado(r))
        
        #botones modificar atributos
        self.btn_editarEmpleado.setFixedHeight(30)
        self.btn_editarEmpleado.setFixedWidth(30)
        self.btn_eliminarEmpleado.setFixedHeight(30)
        self.btn_eliminarEmpleado.setFixedWidth(30)
        
        layoutbotones.addWidget(self.btn_eliminarEmpleado)
        layoutbotones.addWidget(self.btn_editarEmpleado)
        
        #añadir funciones al boton
        #btn_editar.clicked.connect(lambda checked, Empleado_id = Empleado_id , Empleados = self: self.editarEmpleadobtn(Empleado_id,Empleados))
        self.btn_editarEmpleado.clicked.connect(lambda checked, Empleado_id=Empleado_id, Empleados=[Empleados]: self.editarEmpleadobtn(Empleado_id, Empleados))
        self.btn_editarEmpleado.clicked.connect(self.show_editBtn)
        self.btn_eliminarEmpleado.clicked.connect(lambda checked, Empleado_id = Empleado_id , Empleados = [Empleados]: self.eliminarEmpleado(Empleado_id,Empleados))
        
        return frame

    def botonEditarEliminar_pulsado(self, fila):
        print(f"Boton pulsado en fila: {fila+1}")
        self.tableWidget.setCurrentCell(fila, 4)  

    def comprobarRol(self,empleado):
        if empleado["rol"] in roles_usuario:
            self.rolEmpleado.setCurrentIndex(self.rolEmpleado.findText(empleado["rol"]))
        else:
            self.rolEmpleado.setItemText(roles_usuario[0])
            
    def comprobarDepartamento(self,empleado):
        if empleado["departamento"] in departamentos:
            self.departamentoEmpleado.setCurrentIndex(self.departamentoEmpleado.findText(empleado["departamento"]))
        else:
            self.departamentoEmpleado.setItemText(departamentos[0])

    def eliminarEmpleado(self,empleado_id,Empleados):
        
        conexion = Conn()
        Empleados = self.TodosLosEmpleados()
        empleado_email = self.tableWidget.currentItem().text()
        
        confirmacion = QMessageBox.question(
            self, 
            "Confirmar eliminación", 
            f"¿Estás seguro de que quieres eliminar este empleado?\nEsta acción es irreversible",  
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No  
        )
        
        if confirmacion == QMessageBox.Yes:
                        
            for empleado in Empleados:
                if empleado_email==empleado["email"]:
                    empleado_id = empleado["id"]
                    
                    try:
                        print("entra")
                        conexion.eliminarEmpleado(empleado_id)
                        print("datos actualizados con exito")
                    except sqlite3.Error as e:
                        QMessageBox(self, "Error en la base de datos"f": {e}")
                    break   
                                
        else:
            print("Eliminación cancelada.")

        self.llenarTabla()
        if self.datosEmpleado.width()>10: 
            self.hide_datosEmpleado()
        else: pass
        conexion.cerrarConexion()
        
    def editarEmpleadobtn(self,Empleado_id,Empleados):
        
        self.limpiarCampos()
        
        for empleado in Empleados:
            if Empleado_id == empleado["id"]:
                
                #mostrar nuevoEmpleado
                if self.datosEmpleado.width() <= 10:
                    
                    self.show_datosEmpleado()
                    #cargar datos en NuevoEmpleado
                    self.lblnuevo_Empleado.setText("Editar Empleado")
                    
                    self.nombreEmpleado.setText(empleado["nombre"])
                    self.emailEmpleado.setText(empleado["email"])
                    self.telefonoEmpleado.setText(empleado["telefono"])
                    self.contrasenaEmpleado.setText(str(empleado["contrasena"]))
                    
                    #comprobacion rol
                    self.comprobarRol(empleado)
                    self.comprobarDepartamento(empleado)
                            
                else:
                    self.lblnuevo_Empleado.setText("Editar Empleado")
                    
                    self.nombreEmpleado.setText(empleado["nombre"])
                    self.emailEmpleado.setText(empleado["email"])
                    self.telefonoEmpleado.setText(empleado["telefono"])
                    self.contrasenaEmpleado.setText(empleado["contrasena"])
                    
                    #comprobacion rol
                    self.comprobarRol(empleado)
                    self.comprobarDepartamento(empleado)           
        
    def editarEmpleado(self):
        conexion = Conn()
        empleados = self.TodosLosEmpleados()
        empleado_email = self.tableWidget.currentItem().text()
        
        #por algun motivo si no se inicializan el mundo estalla
        empleado_editado = None
        empleado_id = None
        
        confirmacion = QMessageBox.question(
            self, 
            "Confirmar", 
            f"¿Confirmar los cambios?",  
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No  
        )

        if confirmacion == QMessageBox.Yes:
            if self.rolEmpleado.currentIndex()<0:
                QMessageBox.warning(self,"Error","Introduce el rol de empleado",QMessageBox.Ok)
            elif self.departamentoEmpleado.currentIndex()<0:
                QMessageBox.warning(self,"Error","Introduce el departamento del empleado",QMessageBox.Ok)
            else: 
                for empleado in empleados:
                    if empleado_email == empleado["email"]:
                        
                        #comprobar si se modifico la contraseña
                        salt = bcrypt.gensalt()
                        hashed = bcrypt.hashpw(str.encode(self.contrasenaEmpleado.text()),salt)
                        if bcrypt.checkpw(str.encode(empleado["contrasena"]),hashed):
                            print("No se modifico la contraseña")
                            contrasena = empleado["contrasena"]
                        else:
                            print("Se modifico la contraseña")
                            contrasena = bytes.decode(hashed)
                        
                        
                        
                        #datos del empleado editado
                        empleado_editado = [
                            ""+self.nombreEmpleado.text(),
                            ""+self.departamentoEmpleado.currentText(),
                            ""+self.telefonoEmpleado.text(),
                            ""+self.emailEmpleado.text(),
                            ""+self.rolEmpleado.currentText(),
                            ""+contrasena
                        ]
                        empleado_id = empleado["id"]
                        try:
                            conexion.editarEmpleado(empleado_editado,empleado_id)
                            print("datos actualizados con exito")
                            conexion.cerrarConexion()
                        except sqlite3.Error as e:
                            QMessageBox(self, "Error en la base de datos"f": {e}")
                        break                    
        self.hide_datosEmpleado()       
        self.llenarTabla()
        
    def generarID(self):
        from faker import Faker
        faker = Faker()
        id = id[::6]+self.nombreEmpleado.text().replace(" ","")[::3]+self.emailEmpleado.text()
        return id[:10]
    
    def generarEmailEmpleado(self):
        self.emailEmpleado.setText(self.nombreEmpleado.text()[:5].lower().strip(" ")+self.nombreEmpleado.text()[5:10].lower().replace(" ","")+"@empresa.com")
    
    def anadirEmpleado(self):
        confirmacion = QMessageBox.question(
            self, 
            "Confirmar", 
            f"¿Añadir nuevo Empleado?",  
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No  
        )
        
        if confirmacion == QMessageBox.Yes:
            if self.rolEmpleado.currentIndex()<0:
                QMessageBox.warning(self,"Error","Introduce el rol de empleado",QMessageBox.Ok)
            elif self.departamentoEmpleado.currentIndex()<0:
                QMessageBox.warning(self,"Error","Introduce el departamento del empleado",QMessageBox.Ok)
            elif self.contrasenaEmpleado.text() == "":
                QMessageBox.warning(self,"Error","Debes introducir una contraseña",QMessageBox.Ok)
            else:    
                #registrar datos en Nuevo Empleado
                #hash contraseña
                salt = bcrypt.gensalt()
                contrasena = self.contrasenaEmpleado.text().encode('utf-8')
                hashed = bcrypt.hashpw(contrasena,salt)

                Empleado = [
                    None,
                    ""+self.nombreEmpleado.text(),
                    ""+self.departamentoEmpleado.currentText(),
                    ""+self.telefonoEmpleado.text(),
                    ""+self.emailEmpleado.text(),
                    ""+self.rolEmpleado.currentText(),
                    #si no se decodifica a str queda corrupta en la base de datos
                    #y no se puede iniciar sesion
                    hashed.decode('utf-8')                   
                ]
                conexion = Conn()
                if conexion.registrarEmpleado(Empleado):
                    print("Exito en el registro")
                else:
                    print("Error en el registro")
                conexion.cerrarConexion()
                self.hide_datosEmpleado()        
                self.llenarTabla()

    def limpiarCampos(self):
        #limpiar campos
        for lineEdit in self.datosEmpleado.findChildren(QLineEdit):
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
            