from Modulos.PRINCIPAL.imports.core import *
from Modulos.PRINCIPAL.imports.widgets_import import *
from Modulos.PRINCIPAL.imports.bbdd_conn import *

class Proyectos_Page(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent = parent)
        
        self.setObjectName(u"page_proyectos")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.proyectos_layout_superior = QHBoxLayout()
        self.proyectos_layout_superior.setObjectName(u"proyectos_layout_superior")
        
        #atributos
        self.empleados_seleccionados = []
        
        #frame barra busqueda y añadir Proyecto
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
        self.columnasTableProyectos = ["ID Proyecto","Nombre","Empleados","Descripción","Fecha inicio","Fecha fin", "Estado"]
        self.buscarPor.addItems(self.columnasTableProyectos)
        self.columnasTable = self.columnasTableProyectos
        self.columnasTable.insert(len(self.columnasTableProyectos),"")
        self.buscarPor.setStyleSheet(f"border: none; font:500 13pt; height: {self.btnLupa.height()-4};width: 120px")
        
        self.labelCurrentPage = QLabel("Proyectos")
        self.labelCurrentPage.setStyleSheet(f"padding-left:10 ;border: none; font:500 13pt; font-weight: bold;")
        
        self.layoutBarraBusqueda.addWidget(self.labelCurrentPage)
        self.layoutBarraBusqueda.addSpacerItem(self.espaciadorBusqueda)
        self.layoutBarraBusqueda.addWidget(self.labelBusqueda)
        self.layoutBarraBusqueda.addWidget(self.buscarPor)
        self.layoutBarraBusqueda.addWidget(self.barraBusqueda)
        self.layoutBarraBusqueda.addWidget(self.btnLupa)
        
        self.proyectos_layout_superior.addWidget(self.frame)
        
        #frame del boton de nuevoProyecto
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
        
        self.btn_anadirProyecto = PyPushButton(icon_path="calendar-plus.svg", text_padding=0)
        self.btn_anadirProyecto.setFixedWidth(50)
        self.btn_anadirProyecto.setObjectName(u"btn_anadirProyecto")
        self.btn_anadirProyecto.setStyleSheet("border-radius: 4; background-color: #356b6b")
        self.btn_anadirProyecto.setMaximumSize(QSize(150, 16777215))
        self.btn_anadirProyecto.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_anadirProyecto.clicked.connect(self.show_datosProyecto)

        self.horizontalLayout.addWidget(self.btn_anadirProyecto)
        self.proyectos_layout_superior.addWidget(self.frame_2)
        self.verticalLayout.addLayout(self.proyectos_layout_superior)

        self.proyectos_layout_inferior = QHBoxLayout()
        self.proyectos_layout_inferior.setObjectName(u"proyectos_layout_inferior")
        
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
        #TABLA IZQUIERDA, MOSTRAR TODOS LOS PROYECTOS
        
        #tabla configuracion
        self.tableProyectos = PyTableWidget()
        self.tableProyectos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.Proyectoslbl = QLabel("Proyectos existentes")
        self.Proyectoslbl.setStyleSheet(f"padding-left:2;padding-bottom:2; font:550 13pt;color:black; border-bottom: 2px solid #444;")
        self.mostrarTablaProyectos()

        #FRAME CENTRO
        
        self.lblnuevoProyecto = QLabel(f"Nuevo proyecto")
        self.lblnuevoProyecto.setStyleSheet("font:570 16px;")
        
        #nombre proyecto
        self.nombreProyecto = PyLineEdit()
        self.nombreProyecto.setStyleSheet(f"border: 2px solid #444; font:500 13pt; height: 30")
        self.nombreProyecto.setPlaceholderText("Nombre proyecto")
        
        #Combo box proyectos bajo combo box clientes
        self.elegirEmpleado = QComboBox()
        self.elegirEmpleado.setStyleSheet(f"border: 2px solid #444; font:500 13pt; height: {self.nombreProyecto.height()}")
        self.elegirEmpleado.setPlaceholderText("Empleado")
        self.elegirEmpleado.setCurrentIndex(-1)
        self.empleados = self.cargarEmpleados()
        self.elegirEmpleado.addItems(self.empleados)
        
        self.tarea = PyLineEdit()
        self.tarea.setPlaceholderText("Tarea")
        self.tarea.setStyleSheet(f"border: 2px solid #444; font:500 13pt; height: 30")
        
        #botones añadir producto, cancelar Proyecto 
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
        
        
        #FRAME DERECHO
        self.proyectoslbl = QLabel("Empleados en el proyecto actual")
        self.proyectoslbl.setStyleSheet(f"padding-left:2;padding-bottom:2; font:550 13pt;color:black; border-bottom: 2px solid #444;")
        self.tablaEmpleadosEnProyecto = PyTableWidget(self.frameDerecha)
        self.tablaEmpleadosEnProyecto.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.crearTabla()
        try:
            self.anadirEmpleadoAProyecto(self.elegirEmpleado.currentIndex())
        except:
            pass
        
        #AÑADIR ELEMENTOS A LOS CUADROS CENTRALES
        self.frameCentralLayout.addWidget(self.frameIzquierda,stretch=1)
        self.frameCentralLayout.addWidget(self.frameCentro,stretch=1)
        self.frameCentralLayout.addWidget(self.frameDerecha,stretch=1)
        
        self.frameIzquierdaLayout = QVBoxLayout(self.frameIzquierda)
        self.frameIzquierdaLayout.addWidget(self.lblnuevoProyecto)
        self.frameIzquierdaLayout.addWidget(self.tableProyectos)
        
        self.verticalLayoutFrameCentro = QVBoxLayout(self.frameCentro)
        self.verticalLayoutFrameCentro.setAlignment(Qt.AlignTop)
        self.verticalLayoutFrameCentro.addWidget(self.lblnuevoProyecto)
        self.verticalLayoutFrameCentro.addWidget(self.nombreProyecto)
        self.verticalLayoutFrameCentro.addWidget(self.elegirEmpleado)
        self.verticalLayoutFrameCentro.addWidget(self.tarea)
        self.verticalLayoutFrameCentro.addWidget(self.aceptar_cancelar_frame)
        
        self.verticalLayoutFrameDerecha = QVBoxLayout(self.frameDerecha)
        self.verticalLayoutFrameDerecha.addWidget(self.proyectoslbl)
        self.verticalLayoutFrameDerecha.addWidget(self.tablaEmpleadosEnProyecto)

        #FUNCION ACTUALIZAR STOCK AL CAMBIAR PRODUCTO
        self.btn_anadir.clicked.connect(self.anadirEmpleadoAProyecto)
        self.btn_cancelar.clicked.connect(self.cancelarProyecto)
        self.btn_confirmar.clicked.connect(self.anadirProyecto)
        #metodo buscar
        self.barraBusqueda.textChanged.connect(lambda checked: self.buscar())
    
    #MOSTRAR ESCONDER FRAMES
    #/////////////////////////////////////////////////////////////
    def show_datosProyecto(self): #cuadroCentral
        #anchura del menu lateral izquierdo
        self.limpiarCampos()
        
        datosProyecto_width = self.frameCentro.width()
        
        if datosProyecto_width <= 10:
            width = 420
        else:
            pass 
             
        try:     
        #empezar animacion (Si se pulsa dos veces el boton empieza una animacion sin final. No pasa nada, solo salta un aviso)
            
            self.animation = QPropertyAnimation(self.frameCentro, b"minimumWidth")    
            self.animation.setStartValue(datosProyecto_width)
            self.animation.setEndValue(width)
            self.animation.setDuration(320)
            self.animation.setEasingCurve(QEasingCurve.OutCirc)
            self.animation.start()
            
        except:
            pass
              
    def hide_datosProyecto(self):
        
        datosProyecto_width = self.frameCentro.width()
        
        if datosProyecto_width >= 0:
                width = 0
        else:
            pass
                
        #empezar animacion
        
        self.animation = QPropertyAnimation(self.frameCentro, b"minimumWidth")    
        self.animation.setStartValue(datosProyecto_width)
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
        for linedit in self.frameCentro.findChildren(QLineEdit):
            try:
                linedit.setText("")
            except:
                print("Error al borrar linedit")
        for table in self.frameDerecha.findChildren(QTableView):
            try:
                self.crearTabla()
            except:
                print("Error al borrar tabla")
    
    def show_tablaProyectos(self):
        datosTablaProyectos_width = self.frameDerecha.width()
        
        if datosTablaProyectos_width <= 10:
            width = 520
        else:
            pass 
             
        try:     
        #empezar animacion (Si se pulsa dos veces el boton empieza una animacion sin final. No pasa nada, solo salta un aviso)
            
            self.animation = QPropertyAnimation(self.frameDerecha, b"minimumWidth")    
            self.animation.setStartValue(datosTablaProyectos_width)
            self.animation.setEndValue(width)
            self.animation.setDuration(320)
            self.animation.setEasingCurve(QEasingCurve.OutCirc)
            self.animation.start()
        except:
            pass
    
    def hide_tablaProyectos(self):
        
        datosProyecto_width = self.frameDerecha.width()
        
        if datosProyecto_width > 0:
                width = 0
        else:
            pass
                
        #empezar animacion
        try:
            self.animationTProyectos = QPropertyAnimation(self.frameDerecha, b"minimumWidth")    
            self.animationTProyectos.setStartValue(datosProyecto_width)
            self.animationTProyectos.setEndValue(width)
            self.animationTProyectos.setDuration(300)
            self.animationTProyectos.setEasingCurve(QEasingCurve.OutCirc)
            self.animationTProyectos.start()
        except:
            pass
    
    def limpiarLineEdits(self):
        for linedit in self.frameCentro.findChildren(QLineEdit):
                try:
                    linedit.setText("")
                except:
                    print("Error al borrar linedit")
    
    #METODOS LLENAR TABLA DE PROYECTOS
    #/////////////////////////////////////////////////////////////
    
    def mostrarTablaProyectos(self):
        self.tableProyectos.setColumnCount(8)
        self.tableProyectos.setRowCount(0)
        self.tableProyectos.setHorizontalHeaderLabels(self.columnasTableProyectos)
        
        conexion = Conn()
        proyectos = conexion.mostrarTodosProyectos()
        
        try:
            
            for row, proyecto in enumerate(proyectos):
                self.tableProyectos.insertRow(row)
                datos = [
                str(proyecto.get('id', '')),
                f"{proyecto.get('nombre')}",
                proyecto.get('empleado', ''),
                proyecto.get('descripcion', ''),
                proyecto.get('inicio', ''),
                proyecto.get('fin', ''),
                ]
                #self.estado_proyecto = proyecto.get('estado', '')
                
                for column, value in enumerate(datos):
                    item = QTableWidgetItem(str(value))
                    self.tableProyectos.setItem(row, column, item)
                        
                #añadir botón de eliminar en la última columna
                eliminarbtn = QPushButton("Eliminar")
                eliminarbtn.setStyleSheet("background-color: #A4ADB2")
                eliminarbtn.clicked.connect(lambda _, pid = proyecto.get("id"): self.eliminarProyecto(pid))
                self.tableProyectos.setCellWidget(row, self.tableProyectos.columnCount() - 1, eliminarbtn)
                
                #añadir checkbox
                #cargar valor desde bbdd
                estado_value = proyecto.get('estado', '')

                #comprobar estados
                texto_check = "En proceso"
                checked = False
                if estado_value == "Finalizado":
                    texto_check = "Finalizado"
                    checked = True
                elif estado_value == "En proceso":
                    texto_check = "En proceso"

                #crear checkbox con la configuracion
                estado_chbox = QCheckBox(texto_check)
                estado_chbox.setChecked(checked)           
                #accion de la checkbox
                estado_chbox.stateChanged.connect(lambda estado, pid=proyecto.get("id"), chk=estado_chbox: self.cambiarEstadoProyecto(pid, estado, chk))
                
                widget_estadochk = QWidget()
                layout_chkbox = QHBoxLayout(widget_estadochk)
                layout_chkbox.addWidget(estado_chbox)
                #layout_chkbox.setAlignment(Qt.AlignCenter)
                layout_chkbox.setContentsMargins(20, 0, 0, 0)
                widget_estadochk.setLayout(layout_chkbox)
                
                self.tableProyectos.setCellWidget(row, 6, widget_estadochk)
                
                #colocar tooltips
                #tooltip fin proyecto                                  
                for row in range(self.tableProyectos.rowCount()):
                    itemFecha = self.tableProyectos.item(row, 6)  
                    if itemFecha:
                        itemFecha.setToolTip(itemFecha.text())
                #tooltip inicio proyecto                                  
                for row in range(self.tableProyectos.rowCount()):
                    itemFecha = self.tableProyectos.item(row, 5)  
                    if itemFecha:
                        itemFecha.setToolTip(itemFecha.text())
                #tooltip inicio
                for row in range(self.tableProyectos.rowCount()):
                    itemProyectos = self.tableProyectos.item(row, 4)
                    if itemProyectos:
                        itemProyectos.setFlags(itemProyectos.flags() or Qt.TextWordWrap)
                        itemProyectos.setToolTip(itemProyectos.text()) 
                #tooltip descripcion                                  
                for row in range(self.tableProyectos.rowCount()):
                    itemFecha = self.tableProyectos.item(row, 3)  
                    if itemFecha:
                        itemFecha.setToolTip(itemFecha.text())
                #tooltip empleado                                  
                for row in range(self.tableProyectos.rowCount()):
                    itemFecha = self.tableProyectos.item(row, 2)  
                    if itemFecha:
                        itemFecha.setToolTip(itemFecha.text())
                #tooltip nombre proyecto                                  
                for row in range(self.tableProyectos.rowCount()):
                    itemFecha = self.tableProyectos.item(row, 1)  
                    if itemFecha:
                        itemFecha.setToolTip(itemFecha.text())        
        except Exception:
            print("No hay proyectos que mostrar")
                    
    def cambiarEstadoProyecto(self, pid, estado,estado_chbox:QCheckBox):
        
        conexion = Conn()
        if estado == 0:
            nuevo_estado = "En Proceso"
            estado_chbox.setText(nuevo_estado)
            fin_proyecto = ""
            conexion.cambiarEstado(pid,nuevo_estado,fin_proyecto)
            print(f"Proyecto {pid} marcado como {nuevo_estado}")
            conexion.cerrarConexion()
        else:
            nuevo_estado = "Finalizado"
            estado_chbox.setText(nuevo_estado)
            fin_proyecto = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            conexion.cambiarEstado(pid,nuevo_estado,fin_proyecto)
            print(f"Proyecto {pid} marcado como {nuevo_estado}")
            conexion.cerrarConexion()
            
        self.mostrarTablaProyectos()

    #METODOS HACER PROYECTO
    #/////////////////////////////////////////////////////////////
    
    def cargarEmpleados(self):
        conexion = Conn()
        empleados = []
        for e in conexion.mostrarTodosEmpleados():
            empleados.append(""+str(e["id"])+": "+e["nombre"][:12])
        conexion.cerrarConexion()
        return empleados
    
    def crearTabla(self):
        #configuracion de la tabla
        self.tablaEmpleadosEnProyecto.setColumnCount(4)
        self.tablaEmpleadosEnProyecto.setRowCount(0)
        self.tablaEmpleadosEnProyecto.setHorizontalHeaderLabels(["ID Empleado","Nombre","Tarea",""])
        
    def anadirEmpleadoAProyecto(self):
        
        if self.elegirEmpleado.currentIndex() == -1:
            msg = QMessageBox()
            msg.setWindowIcon(QIcon(r"Modulos/WEB/imagenes/gestr.ico"))
            msg.setWindowTitle("Atención")
            msg.setText("Debes seleccionar al menos un empleado")
            msg.addButton(QMessageBox.StandardButton.Ok)
            msg.exec()
        elif self.tarea.text() == "":
            msg = QMessageBox()
            msg.setWindowIcon(QIcon(r"Modulos/WEB/imagenes/gestr.ico"))
            msg.setWindowTitle("Atención")
            msg.setText("Debes introducir una tarea")
            msg.addButton(QMessageBox.StandardButton.Ok)
            msg.exec()
        else:
            conexion = Conn()
            empleados = conexion.mostrarTodosEmpleados()
            table = self.tablaEmpleadosEnProyecto
            fila_posicion = table.rowCount()
            tarea = self.tarea.text().strip()
                
            #comprueba que la tabla no tenga 0 filas        
            for empleado in empleados:
                try: #este try-catch evita que pete cuando el indice de la qcombobox es -1, cuando esta la opcion del placeholder
                    if str(self.elegirEmpleado.currentText()[:self.elegirEmpleado.currentText().index(":")]) == str(empleado["id"]):
                        empleadoValido = [str(empleado["id"]),str(empleado["nombre"]),tarea]
                except:
                    pass
            
            table.insertRow(fila_posicion)
            
            for col, valor in enumerate(empleadoValido):
                item = QTableWidgetItem(valor)
                table.setItem(fila_posicion, col, item)
                item.setToolTip(self.tarea.text())
            
            #añadir botón de eliminar en la última columna
            eliminarbtn = QPushButton("Eliminar")
            eliminarbtn.clicked.connect(lambda _, r=fila_posicion: self.eliminarEmpleadoProyecto(fila_posicion))
            eliminarbtn.clicked.connect(lambda _, r=fila_posicion: table.removeRow(table.currentRow()))
            eliminarbtn.clicked.connect(self.hideCheck)
            table.setCellWidget(fila_posicion, table.columnCount() - 1, eliminarbtn)
        try:    
            if table.rowCountChanged(0,1) or table.rowCount()>0:
                self.show_tablaProyectos()
            else:
               pass 
            self.tarea.setText("")
            self.sacarEmpleadoCombobox()
            self.elegirEmpleado.setCurrentIndex(-1)
                
        except:
            pass  
    
    def eliminarEmpleadoProyecto(self,fila_posicion:int):
        table = self.tablaEmpleadosEnProyecto
        try: #evita que pete si se elimina el ultimo empleado de la tabla
            celda_id = table.item(fila_posicion,0).text()
        except:
            #si se elimina la última fila coge directamente el último empleado seleccionado que queda e iguala su id a la de la celda,
            #que siempre será la misma
            celda_id = self.empleados_seleccionados[0].split(":")[0]
            
        for pos, empleado in enumerate(self.empleados_seleccionados):
            id_empleado_seleccionado = empleado.split(": ")
            if id_empleado_seleccionado[0] == celda_id:
                self.empleados.append(self.empleados_seleccionados.pop(pos))
                self.elegirEmpleado.clear()
                self.elegirEmpleado.addItems(self.empleados)
                  
    def hideCheck(self):
        if self.tablaEmpleadosEnProyecto.rowCount() == 0:
            self.hide_tablaProyectos()
    
    def sacarEmpleadoCombobox(self):
        #comprueba que la lista exista para evitar sobreescrituras
        if not hasattr(self,"empleados_seleccionados"):
            self.empleados_seleccionados = []
        self.empleados_seleccionados.append(self.empleados.pop(self.elegirEmpleado.currentIndex()))    

        #vaciamos la lista para llenarla después
        self.elegirEmpleado.clear()    
        self.elegirEmpleado.addItems(self.empleados)
 
    def cancelarProyecto(self):
        
        self.empleados = self.cargarEmpleados()
        self.elegirEmpleado.clear()    
        self.elegirEmpleado.addItems(self.empleados)
        
        self.hide_datosProyecto()
        self.hide_tablaProyectos()

    def anadirProyecto(self):
        if self.tablaEmpleadosEnProyecto.rowCount() == 0:
            msg = QMessageBox()
            msg.setWindowIcon(QIcon(r"Modulos/WEB/imagenes/gestr.ico"))
            msg.setWindowTitle("Atención")
            msg.setText("Debes seleccionar al menos un empleado")
            msg.addButton(QMessageBox.StandardButton.Ok)
            msg.exec()
        elif self.nombreProyecto.text() == "":
            msg = QMessageBox()
            msg.setWindowIcon(QIcon(r"Modulos/WEB/imagenes/gestr.ico"))
            msg.setWindowTitle("Atención")
            msg.setText("Debes dar nombre al proyecto")
            msg.addButton(QMessageBox.StandardButton.Ok)
            msg.exec()
        else:
            confirmacion = QMessageBox.question(
            self, 
            "Confirmar eliminación", 
            f"Se creará un proyecto nuevo, ¿Confirmar cambios?",  
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No  
            )
        
            if confirmacion == QMessageBox.Yes:
                conexion = Conn()
                #OBTENER empleados
                #Obtiene los empleados de la tabla
                empleados:list[dict] = self.obtener_EmpleadosProyecto(self.tablaEmpleadosEnProyecto)
                aux = ""
                for empleado in empleados:
                    aux = aux + "ID: "+ empleado["Nombre"]+"\n"
                empleados_id = "".join(aux)
                print(empleados_id)
                
                #OBTENER TAREA
                #comprobar que se introduzca una tarea
                if self.tarea == "":
                    msg = QMessageBox()
                    msg.setWindowIcon(QIcon(r"Modulos/WEB/imagenes/gestr.ico"))
                    msg.setWindowTitle("¡Atención!")
                    msg.setText("Introduce alguna tarea")
                    msg.addButton(QMessageBox.StandardButton.Ok)
                    msg.exec()
                else:
                    pass

                nombre_proyecto = self.nombreProyecto.text()
                id_proyecto = self.generarIDProyecto()
                fecha_inicio = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                fecha_fin = ""
                estado = "En proceso"
                
                #descripcion del proyecto (tareas)
                tareas = []
                for empleado in empleados:
                    tareas.append(str(empleado["Nombre"]+": "+empleado["Tarea"]))
                descripcionProyecto = "\n".join(tareas)
                    
                proyecto = [
                    id_proyecto,
                    nombre_proyecto,
                    empleados_id,                
                    descripcionProyecto,
                    str(fecha_inicio),
                    fecha_fin, 
                    estado
                ]

                if conexion.registrarProyecto(proyecto):
                    self.cancelarProyecto()
                    conexion.cerrarConexion()
                    self.mostrarTablaProyectos()
                    
                    self.empleados = self.cargarEmpleados()
                    self.elegirEmpleado.clear()
                    self.elegirEmpleado.addItems(self.empleados)    
                    self.empleados_seleccionados = []
    
    def obtener_EmpleadosProyecto(self,tabla:QTableWidget):
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
    
    def generarIDProyecto(self):
        from faker import Faker
        faker = Faker()
        return datetime.now().strftime("%d%m%Y")+''.join(faker.random_letters(7))[:10]
    
    def eliminarProyecto(self,pid):
        confirmacion = QMessageBox.question(
            self, 
            "Confirmar eliminación", 
            f"¿Estás seguro de que quieres eliminar este Proyecto?\nEsta acción es irreversible",  
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No  
        )
        
        if confirmacion == QMessageBox.Yes:
            conexion = Conn()
            
            proyectos: list[dict] = self.obtener_EmpleadosProyecto(self.tableProyectos)
            for proyecto in proyectos:
                if proyecto["ID Proyecto"] == pid:
                    conexion = Conn()
                    conexion.eliminarProyecto(pid)
                    conexion.cerrarConexion()  
                    self.mostrarTablaProyectos()                                 
        else:
            print("Eliminación cancelada.")
    
    def buscar(self):
        texto_busqueda = self.barraBusqueda.text().strip().lower()
        columna_buscar = self.buscarPor.currentIndex()

        for fila in range(self.tableProyectos.rowCount()):
            # Obtener el widget o item de la celda en la columna "estado"
            celda_widget = self.tableProyectos.cellWidget(fila, columna_buscar)
            
            #comprobar que la celda tenga widget
            if celda_widget:
                #buscar entre los hijos
                for child in celda_widget.children():
                    if isinstance(child, QCheckBox):
                        texto_celda = child.text().lower()
                        break
            else:
                item = self.tableProyectos.item(fila, columna_buscar)
                texto_celda = item.text().lower() if item else ""

            coincide = texto_busqueda in texto_celda
            self.tableProyectos.setRowHidden(fila, not coincide)
            
        