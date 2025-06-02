
#IMPORTAR MODULOS
import sys, os
import webbrowser

#CONFIGURACION DEL PATH PARA IMPORTES RELATIVOS
#ruta en el path para el directorio raiz
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)
#ruta en el path para el directorio principal
PROJECT_ROOT2 = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PROJECT_ROOT2)

#IMPORTAR CORE
from Modulos.PRINCIPAL.imports.core import *
from Modulos.PRINCIPAL.imports.bbdd_conn import *

#importar main window
from Modulos.PRINCIPAL.gui.ui_principal import *
from Modulos.PRINCIPAL.LOGIN.loginWindow import *

#main window
class MainWindow(QMainWindow,UI_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Gestr")
        self.setWindowIcon(QIcon(r'gestr.ico'))
        self.setWindowState(Qt.WindowMaximized)

        #setup mainwindow
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        
        #toggle Button
        self.ui.toggle_button.clicked.connect(self.toggle_button)
        
        #click botones
        self.ui.btn1.clicked.connect(self.show_page_crm)
        self.ui.btn2.clicked.connect(self.show_page_contabilidad)
        self.ui.btn3.clicked.connect(self.show_page_compras)
        self.ui.btn4.clicked.connect(self.show_page_web)
        self.ui.btn5.clicked.connect(self.show_page_empleados)
        self.ui.btn6.clicked.connect(self.show_page_inventario)
        self.ui.btn7.clicked.connect(self.show_page_proveedores)
        self.ui.btn8.clicked.connect(self.show_page_proyectos)
        self.ui.btn9.clicked.connect(self.show_page_tpv)
        #self.ui.btn10.clicked.connect(self.show_page_fabricacion)
        
        #click ajustes
        self.ui.opciones_btn.clicked.connect(self.show_page_settings)

        self.hide()

    #reset selection
    def reset_selection(self):
        for btn in self.ui.menu_izquierdo.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
               pass 
    
    #FUNCIONES MOSTRAR PAGINAS     
    def show_page_crm(self):
        
        if hasattr(self.ui.ui_pages,"page_crm"):
            crm = self.ui.ui_pages.page_crm
            self.ui.pages.removeWidget(crm)
            crm.deleteLater()
            del self.ui.ui_pages.page_crm

        self.ui.ui_pages.page_crm = Crm_Page()
        self.ui.pages.addWidget(self.ui.ui_pages.page_crm)

        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_crm)
        self.ui.btn1.set_active(True)


    def show_page_contabilidad(self):

        if hasattr(self.ui.ui_pages,"page_contabilidad"):
            self.ui.pages.removeWidget(self.ui.ui_pages.page_contabilidad)
            self.ui.ui_pages.page_contabilidad.deleteLater()

        self.ui.ui_pages.page_contabilidad = Contabilidad_Page()
        self.ui.pages.addWidget(self.ui.ui_pages.page_contabilidad)

        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_contabilidad)
        self.ui.btn2.set_active(True)

    def show_page_compras(self):
        if hasattr(self.ui.ui_pages,"page_compras"):
            self.ui.pages.removeWidget(self.ui.ui_pages.page_compras)
            self.ui.ui_pages.page_compras.deleteLater()

        self.ui.ui_pages.page_compras = Compras_Page()
        self.ui.pages.addWidget(self.ui.ui_pages.page_compras)

        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_compras)
        self.ui.btn3.set_active(True)

    def show_page_web(self):
        try:
            webbrowser.open(r"Modulos\WEB\index.html")
        except:
            pass

    def show_page_empleados(self):
        if hasattr(self.ui.ui_pages,"page_empleados"):
            self.ui.pages.removeWidget(self.ui.ui_pages.page_empleados)
            self.ui.ui_pages.page_empleados.deleteLater()
        
        self.ui.ui_pages.page_empleados = Empleados_Page()
        self.ui.pages.addWidget(self.ui.ui_pages.page_empleados)

        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_empleados)
        self.ui.btn5.set_active(True)

    def show_page_inventario(self):
        if hasattr(self.ui.ui_pages,"page_inventario"):
            self.ui.pages.removeWidget(self.ui.ui_pages.page_inventario)
            self.ui.ui_pages.page_inventario.deleteLater()
        
        self.ui.ui_pages.page_inventario = Productos_Page()
        self.ui.pages.addWidget(self.ui.ui_pages.page_inventario)

        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_inventario)
        self.ui.btn6.set_active(True)

    def show_page_proveedores(self):

        if hasattr(self.ui.ui_pages,"page_proveedores"):
            self.ui.pages.removeWidget(self.ui.ui_pages.page_proveedores)
            self.ui.ui_pages.page_proveedores.deleteLater()
        
        self.ui.ui_pages.page_proveedores = Proveedores_Page()
        self.ui.pages.addWidget(self.ui.ui_pages.page_proveedores)


        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_proveedores)
        self.ui.btn7.set_active(True)
    def show_page_proyectos(self):

        if hasattr(self.ui.ui_pages,"page_proyectos"):
            self.ui.pages.removeWidget(self.ui.ui_pages.page_proyectos)
            self.ui.ui_pages.page_proyectos.deleteLater()
        
        self.ui.ui_pages.page_proyectos = Proyectos_Page()
        self.ui.pages.addWidget(self.ui.ui_pages.page_proyectos)

        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_proyectos)
        self.ui.btn8.set_active(True)
        
    def show_page_tpv(self):

        if hasattr(self.ui.ui_pages,"page_tpv"):
            self.ui.pages.removeWidget(self.ui.ui_pages.page_tpv)
            self.ui.ui_pages.page_tpv.deleteLater()
        
        self.ui.ui_pages.page_tpv = Tpv_Page()
        self.ui.pages.addWidget(self.ui.ui_pages.page_tpv)

        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_tpv)
        self.ui.btn9.set_active(True)     
    
    def show_page_settings(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_ajustes)
        self.ui.opciones_btn.set_active(True)
        
    def toggle_button(self):
        #anchura del menu lateral izquierdo
        menu_width = self.ui.menu_izquierdo.width()
        
        #comprobar anchura
        width = 50
        if menu_width == 50:
            width = 240
        
        #empezar animacion
        self.animation = QPropertyAnimation(self.ui.menu_izquierdo, b"minimumWidth")    
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.OutCirc)
        self.animation.start()

    def VentanaLogin(self):
        self.login = LoginWindow()
        self.login.login_exitoso.connect(self.aplicacion) 
        self.login.login_exitoso.connect(self.parametrosSesion)      
        self.login.show()
        
    def parametrosSesion(self, usuario: dict): 
        self.ui.inferior_izq.setText(f"Usuario: {usuario[0]['nombre']} Rol: {usuario[0]['rol']}")
        self.ui.permisos()
          
    def aplicacion(self):
        self.show()

def ejecutar():
    
    #crear bd si no está creada
    if os.path.isfile(r"Modulos\\PRINCIPAL\\BBDD\\BBDD_SGE_PFINAL.db") == False:
    #if os.path.isfile(r"Modulos\PRINCIPAL\BBDD\BBDD.db") == False:
        db = Conn()
        db.crearBD()
    else:
        pass
    
    app = QApplication(sys.argv)
    window = MainWindow()
    #descomentar para cuando haya que entrar con login
    window.VentanaLogin()
    sys.exit(app.exec())
    
    
    