from Modulos.PRINCIPAL.LOGIN.loginWindow import *

#importar widgets y pages
from Modulos.PRINCIPAL.gui.pages.ui_pages import *
from Modulos.PRINCIPAL.gui.widgets.py_push_button import PyPushButton

class UI_MainWindow(object):
    
    def setup_ui(self,parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
        
        #instancia login para recuperar su atributo usuario que sera quien tiene la sesion iniciada    
        self.login = LoginWindow()
        
        self.usuario = usuario 
        
        #PARAMETROS INICIALES VENTANA  
        parent.resize(1200,720)
        parent.setMinimumSize(960,540)

        #crear cuadro central (donde aparecera el contenido)
        self.cuadro_central = QFrame()
        
        #layout principal
        self.main_layout = QHBoxLayout(self.cuadro_central)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)
        
        #menu izquierdo (botonera)
        #///////////////////////////////////////////////////////////////////////////////////////
        self.menu_izquierdo = QFrame()
        self.menu_izquierdo.setStyleSheet("background-color: rgb(53, 107, 107);")
        self.menu_izquierdo.setMaximumWidth(50)
        self.menu_izquierdo.setMinimumWidth(50)
        
        #menu izquierdo layout
        self.menu_izquierdo_layout = QVBoxLayout(self.menu_izquierdo)
        self.menu_izquierdo_layout.setContentsMargins(0,0,0,0)
        self.menu_izquierdo_layout.setSpacing(0)
        
        #menu izquierdo botonera superior Marco
        self.menu_izquierdo_marco_superior = QFrame()
        self.menu_izquierdo_marco_superior.setMinimumHeight(40)
        self.menu_izquierdo_marco_superior.setObjectName("menu_izquierdo_marco_superior")
        
        #menu izquierdo botonera superior layout (para el marco superior)
        self.menu_izquierdo_marco_superior_layout = QVBoxLayout(self.menu_izquierdo_marco_superior)
        self.menu_izquierdo_marco_superior_layout.setContentsMargins(0,0,0,0)
        self.menu_izquierdo_marco_superior_layout.setSpacing(0)        
        
        #Menu izquierdo botonera superior botones
        self.toggle_button = PyPushButton(
            text = "Ocultar menú",
            icon_path="menu_toggle.svg"
        )
        self.btn1 = PyPushButton(
            text = "CRM",
            is_active = True,            
            icon_path="crm_icon.svg"
        )
        self.btn2 = PyPushButton(
            text = "Contabilidad",
            icon_path="abacus-icon.svg"
        )
        self.btn3 = PyPushButton(
            text = "Compras",
            icon_path="shopping-cart-icon.svg"
        )
        self.btn4 = PyPushButton(
            text = "Web",
            icon_path="globe.svg"
        )
        self.btn5 = PyPushButton(
            text = "Empleados",
            icon_path="business-team-icon.svg"
        )
        self.btn6 = PyPushButton(
            text = "Inventario",
            icon_path="boxes-icon.svg"
        )
        self.btn7 = PyPushButton(
            text = "Proveedores",
            icon_path="factory-worker.svg"
        )
        self.btn8 = PyPushButton(
            text = "Proyectos",
            icon_path="training-icon.svg"
        )
        self.btn9 = PyPushButton(
            text = "TPV",
            icon_path="pos-swipe-icon.svg"
        )
        self.btn10 = PyPushButton(
            text = "Fabricación",
            icon_path="factory-pollution-icon.svg"
        )
        
        #funcion que coloca los botones en funcion del rol del usuario introducido si se
        #consigue entrar a la aplicacion sin iniciar sesión no hay ningún botón disponible
        self.menu_izquierdo_marco_superior_layout.addWidget(self.toggle_button)
        self.permisos()
        
        #menu izquierdo botonera superior espaciador
        self.menu_izquierdo_espaciador = QSpacerItem(20,20,QSizePolicy.Minimum,QSizePolicy.Expanding)
        
        #menu izquierdo botones inferiores
        self.menu_izquierdo_marco_inferior = QFrame()
        self.menu_izquierdo_marco_inferior.setMinimumHeight(40)
        self.menu_izquierdo_marco_inferior.setObjectName("menu_izquierdo_marco_inferior")
        
        #menu izquierdo botonera inferior layout (para el marco superior)
        self.menu_izquierdo_marco_inferior_layout = QVBoxLayout(self.menu_izquierdo_marco_inferior)
        self.menu_izquierdo_marco_inferior_layout.setContentsMargins(0,0,0,0)
        self.menu_izquierdo_marco_inferior_layout.setSpacing(0)        
        
        #Menu izquierdo botonera inferior botones
        self.opciones_btn = PyPushButton(
            text = "Ajustes",
            icon_path="gear-fill.svg"
        )
        
        #Añadir botonera inferior boton
        self.menu_izquierdo_marco_inferior_layout.addWidget(self.btn4)#Web
        self.menu_izquierdo_marco_inferior_layout.addWidget(self.opciones_btn)
        
        
        #ETIQUETA DE VERSION
        self.menu_izquierdo_version = QLabel("v2.8.1")
        self.menu_izquierdo_version.setAlignment(Qt.AlignCenter)
        self.menu_izquierdo_version.setStyleSheet("font-size: 10pt; color: white")
        self.menu_izquierdo_version.setMinimumHeight(30)
        self.menu_izquierdo_version.setMaximumHeight(30)
        
        #AÑADIR AL LAYOUT MENU IZQUIERDO
        self.menu_izquierdo_layout.addWidget(self.menu_izquierdo_marco_superior)
        self.menu_izquierdo_layout.addItem(self.menu_izquierdo_espaciador)
        self.menu_izquierdo_layout.addWidget(self.menu_izquierdo_marco_inferior)
        self.menu_izquierdo_layout.addWidget(self.menu_izquierdo_version)

        #Contenido CENTRAL (Qframe donde aparecera el contenido
        #///////////////////////////////////////////////////////////////////////////////////////
        self.contenido = QFrame()
        self.cuadro_central.setStyleSheet("background-color: rgb(164, 173, 178);")
        
        #contenido SUPERIOR
        #///////////////////////////////////////////////////////////////////////////////////////
        self.layoutContenido = QVBoxLayout(self.contenido)
        self.layoutContenido.setContentsMargins(0,0,0,0)
        self.layoutContenido.setSpacing(0)
        
        #menu superior (Navbar)
        self.barra_superior = QFrame()
        self.barra_superior.setStyleSheet("background-color: #1C323F; color: white") #A4ADB2 #1C323F
        self.barra_superior.setMinimumHeight(40)
        self.barra_superior.setMaximumHeight(40)
        self.barra_superior_layout = QHBoxLayout(self.barra_superior)
        self.barra_superior_layout.setContentsMargins(10,0,10,0)
        
        #Labels
        #
        #
        #Label izquierda
        self.superior_izq = QLabel("GESTR")
        self.superior_izq.setStyleSheet("font: 700 12pt; color: white")
        #logo
        #
        #espaciador superior
        self.espaciador_barra_superior = QSpacerItem(20,20,QSizePolicy.Expanding, QSizePolicy.Minimum)
        #
        #
        #Labels
        #
        #
        #Label derecha
        #
        self.lblsuperior_der_nombre_pagina = QLabel("| TFG")
        self.lblsuperior_der_nombre_pagina.setStyleSheet("font: 700 12pt 'Segoe UI'")
        
        #AÑADIR AL LAYOUT
        self.barra_superior_layout.addWidget(self.superior_izq)
        self.barra_superior_layout.addItem(self.espaciador_barra_superior)
        self.barra_superior_layout.addWidget(self.lblsuperior_der_nombre_pagina)
        
        #MENU INFERIOR (EL OTRO NAVBAR)
        #///////////////////////////////////////////////////////////////////////////////////////
        
        #menu inferior
        self.barra_inferior = QFrame()
        self.barra_inferior.setStyleSheet("background-color: #1C323F; color: white") #A4ADB2 #1C323F
        self.barra_inferior.setMinimumHeight(31)
        self.barra_inferior.setMaximumHeight(31)
        
        self.barra_inferior_layout = QHBoxLayout(self.barra_inferior)
        self.barra_inferior_layout.setContentsMargins(10,0,10,0)
        
        #Labels
        #
        #
        #Label izquierda
        self.inferior_izq = QLabel()    
        self.inferior_izq.setStyleSheet("font-size: 12pt; color: white") 
        #
        #espaciador inferior
        self.espaciador_barra_inferior = QSpacerItem(20,20,QSizePolicy.Expanding, QSizePolicy.Minimum)
        #
        #
        #Labels
        #
        #
        #Label derecha
        #
        #datetime
        
        self.inferior_der = QLabel(datetime.now().strftime("%d/%m/%Y")) #, %H:%M:%S"))
        self.inferior_der.setStyleSheet("font: 700 12pt 'Segoe UI'")
        
        #AÑADIR AL LAYOUT
        self.barra_inferior_layout.addWidget(self.inferior_izq)
        self.barra_inferior_layout.addItem(self.espaciador_barra_inferior)
        self.barra_inferior_layout.addWidget(self.inferior_der)
 
        #PAGINAS
        #///////////////////////////////////////////////////////////////////////////////////////
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: black")
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)
        
        #CAMBIAR PARA QUE INICIE DESDE LA PAGINA QUE QUERAMOS
        #self.pages.setCurrentWidget(self.ui_pages.page_contabilidad)

        #Añadir a layoutContenido
        #///////////////////////////////////////////////////////////////////////////////////////
        self.layoutContenido.addWidget(self.barra_superior)
        self.layoutContenido.addWidget(self.pages)
        self.layoutContenido.addWidget(self.barra_inferior)

        #añadir widgets a la app
        #///////////////////////////////////////////////////////////////////////////////////////
        self.main_layout.addWidget(self.menu_izquierdo)
        self.main_layout.addWidget(self.contenido)
        
        #mostrar central widget
        #///////////////////////////////////////////////////////////////////////////////////////
        parent.setCentralWidget(self.cuadro_central)
    
    def permisos(self):
        if len(usuario)>0:
            if usuario[0]["rol"] == "Normal":
                self.menu_izquierdo_marco_superior_layout.addWidget(self.btn9)#tpv
                #hacer que inicie desde esta page
                self.pages.setCurrentWidget(self.ui_pages.page_tpv)
                
            if usuario[0]["rol"] == "Superior":
                self.menu_izquierdo_marco_superior_layout.addWidget(self.btn1)#crm
                
                self.pages.setCurrentWidget(self.ui_pages.page_crm)
            if usuario[0]["rol"] == "Ejecutivo":
                self.menu_izquierdo_marco_superior_layout.addWidget(self.btn1)#crm
                self.menu_izquierdo_marco_superior_layout.addWidget(self.btn2)#contabilidad
                self.menu_izquierdo_marco_superior_layout.addWidget(self.btn3)#compras
                self.menu_izquierdo_marco_superior_layout.addWidget(self.btn8)#proyectos
                self.menu_izquierdo_marco_superior_layout.addWidget(self.btn5)#empleados
                self.menu_izquierdo_marco_superior_layout.addWidget(self.btn6)#inventario
                self.menu_izquierdo_marco_superior_layout.addWidget(self.btn7)#proveedores
                
                self.pages.setCurrentWidget(self.ui_pages.page_crm)
            if usuario[0]["rol"] == "Admin":
                
                self.menu_izquierdo_marco_superior_layout.addWidget(self.btn1)#crm
                self.menu_izquierdo_marco_superior_layout.addWidget(self.btn2)#contabilidad
                self.menu_izquierdo_marco_superior_layout.addWidget(self.btn8)#proyectos
                self.menu_izquierdo_marco_superior_layout.addWidget(self.btn3)#compras
                #Por reorganizaciones del enunciado btn4 es la web y se añade al layout inferior con el boton ajustes
                self.menu_izquierdo_marco_superior_layout.addWidget(self.btn5)#empleados
                self.menu_izquierdo_marco_superior_layout.addWidget(self.btn6)#inventario
                self.menu_izquierdo_marco_superior_layout.addWidget(self.btn7)#proveedores
                self.menu_izquierdo_marco_superior_layout.addWidget(self.btn9)#tpv
 
                self.pages.setCurrentWidget(self.ui_pages.page_crm)
            else:
                #el usuario no tenia ninguno de los permisos listados
                pass
        else:
            #usuario es una lista vacía
            pass
            
            
            
            

        
        
        
        
        
        
    
        