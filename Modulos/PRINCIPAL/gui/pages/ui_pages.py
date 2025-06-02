import os, sys

#from Modulos.PRINCIPAL.imports.core import *
#pages import funciona como embudo del que importar todas las paginas, que a su vez importa este archivo
from Modulos.PRINCIPAL.imports.pages_import import *

class Ui_application_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(1187, 675)
        
        #PAGE CRM
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_crm = Crm_Page()
        application_pages.addWidget(self.page_crm)
        
        #PAGE PRODUCTOS
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_inventario = Productos_Page()
        application_pages.addWidget(self.page_inventario)

        #PAGE CONTABILIDAD
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_contabilidad = Contabilidad_Page()
        application_pages.addWidget(self.page_contabilidad)
        
        #PAGE CONTABILIDAD
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_empleados = Empleados_Page()
        application_pages.addWidget(self.page_empleados)

        #PAGE TPV
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_tpv = Tpv_Page()
        application_pages.addWidget(self.page_tpv)
        
        #PAGE PROYECTOS
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_proyectos = Proyectos_Page()
        application_pages.addWidget(self.page_proyectos)

        #PAGE COMPRAS
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_compras = Compras_Page()
        application_pages.addWidget(self.page_compras)

        #PAGE PROVEEDORES
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_proveedores = Proveedores_Page()
        application_pages.addWidget(self.page_proveedores)
       
        
        self.page_web = QWidget()
        self.page_web.setObjectName(u"page_web")
        self.verticalLayout_10 = QVBoxLayout(self.page_web)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_9 = QLabel(self.page_web)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFrameShadow(QFrame.Shadow.Plain)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_9)

        application_pages.addWidget(self.page_web)
        self.page_ajustes = QWidget()
        self.verticalLayout_11 = QVBoxLayout(self.page_ajustes)
        self.label_10 = QLabel(self.page_ajustes)
        self.label_10.setText("Próximamente")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_10)

        application_pages.addWidget(self.page_ajustes)

        application_pages.setCurrentIndex(9)


        QMetaObject.connectSlotsByName(application_pages)
    # setupUi
    
    
        
        
            
                
            
