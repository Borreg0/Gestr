import os, sys

from imports.core import *
#pages import funciona como embudo del que importar todas las paginas, que a su vez importa este archivo
from imports.pages_import import *

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
        self.page_inventario = Productos_page()
        application_pages.addWidget(self.page_inventario)

        #PAGE CONTABILIDAD
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_contabilidad = Contabilidad_Page()
        application_pages.addWidget(self.page_contabilidad)
        
        #PAGE CONTABILIDAD
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_empleados = Empleados_page()
        application_pages.addWidget(self.page_empleados)

        #PAGE TPV
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_tpv = Tpv_page()
        application_pages.addWidget(self.page_tpv)
        
        #PAGE PROYECTOS
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_proyectos = Proyectos_Page()
        application_pages.addWidget(self.page_proyectos)
        
        self.page_mantenimiento = QWidget()
        self.page_mantenimiento.setObjectName(u"page_mantenimiento")
        self.verticalLayout_7 = QVBoxLayout(self.page_mantenimiento)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.page_mantenimiento)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_7.addWidget(self.label_6)

        application_pages.addWidget(self.page_mantenimiento)
       
        
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
        self.page_ajustes.setObjectName(u"page_ajustes")
        self.verticalLayout_11 = QVBoxLayout(self.page_ajustes)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_10 = QLabel(self.page_ajustes)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_10)

        application_pages.addWidget(self.page_ajustes)
        self.page_fabricacion = QWidget()
        self.page_fabricacion.setObjectName(u"page_fabricacion")
        self.verticalLayout_5 = QVBoxLayout(self.page_fabricacion)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.page_fabricacion)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        application_pages.addWidget(self.page_fabricacion)

        application_pages.setCurrentIndex(9)


        QMetaObject.connectSlotsByName(application_pages)
    # setupUi
    
    
        
        
            
                
            
