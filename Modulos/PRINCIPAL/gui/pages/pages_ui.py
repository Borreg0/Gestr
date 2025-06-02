# -*- coding: utf-8 -*-

################################################################################
## Form generated from Modulos.PRINCIPAL.reading UI file 'pages.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from Modulos.PRINCIPAL.Modulos.PRINCIPAL.imports.core import *

class Ui_application_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(1187, 675)
        
        #PAGE CRM
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_crm = QWidget()
        self.page_crm.setObjectName(u"page_crm")
        self.verticalLayout = QVBoxLayout(self.page_crm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.crm_layour_superior = QHBoxLayout()
        self.crm_layour_superior.setObjectName(u"crm_layour_superior")
        self.frame = QFrame(self.page_crm)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 60))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.crm_layour_superior.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_crm)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(200, 0))
        self.frame_2.setMaximumSize(QSize(300, 16777215))
        self.frame_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.btn_anadirCliente = QPushButton(self.frame_2)
        self.btn_anadirCliente.setObjectName(u"btn_anadirCliente")
        self.btn_anadirCliente.setMaximumSize(QSize(150, 16777215))
        self.btn_anadirCliente.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout.addWidget(self.btn_anadirCliente)


        self.crm_layour_superior.addWidget(self.frame_2)


        self.verticalLayout.addLayout(self.crm_layour_superior)

        self.crm_layout_inferior = QHBoxLayout()
        self.crm_layout_inferior.setObjectName(u"crm_layout_inferior")
        self.tableWidget = QTableWidget(self.page_crm)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QtableWidget{\n"
"border-radius:5px;\n"
"}")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)

        self.crm_layout_inferior.addWidget(self.tableWidget)

        self.datosCliente = QFrame(self.page_crm)
        self.datosCliente.setObjectName(u"datosCliente")
        self.datosCliente.setMinimumSize(QSize(300, 0))
        self.datosCliente.setFrameShape(QFrame.Shape.StyledPanel)
        self.datosCliente.setFrameShadow(QFrame.Shadow.Raised)

        self.crm_layout_inferior.addWidget(self.datosCliente)


        self.verticalLayout.addLayout(self.crm_layout_inferior)

        application_pages.addWidget(self.page_crm)
        
        #PAGE CONTABILIDAD
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_contabilidad = QWidget()
        self.page_contabilidad.setObjectName(u"page_contabilidad")
        self.verticalLayout_2 = QVBoxLayout(self.page_contabilidad)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.page_contabilidad)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        application_pages.addWidget(self.page_contabilidad)
        
        #PAGE COMPRAS
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_compras = QWidget()
        self.page_compras.setObjectName(u"page_compras")
        self.verticalLayout_3 = QVBoxLayout(self.page_compras)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.page_compras)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        application_pages.addWidget(self.page_compras)
        
        #PAGE EMPLEADOS
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_empleados = QWidget()
        self.page_empleados.setObjectName(u"page_empleados")
        self.verticalLayout_4 = QVBoxLayout(self.page_empleados)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.page_empleados)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        application_pages.addWidget(self.page_empleados)
        
        #PAGE INVENTARIO
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_inventario = QWidget()
        self.page_inventario.setObjectName(u"page_inventario")
        self.verticalLayout_6 = QVBoxLayout(self.page_inventario)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.page_inventario)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)

        application_pages.addWidget(self.page_inventario)
        
        #PAGE MANTENIMIENTO
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_mantenimiento = QWidget()
        self.page_mantenimiento.setObjectName(u"page_mantenimiento")
        self.verticalLayout_7 = QVBoxLayout(self.page_mantenimiento)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.page_mantenimiento)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)

        application_pages.addWidget(self.page_mantenimiento)
        
        #PAGE PROYECTOS
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_proyectos = QWidget()
        self.page_proyectos.setObjectName(u"page_proyectos")
        self.verticalLayout_8 = QVBoxLayout(self.page_proyectos)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.page_proyectos)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        application_pages.addWidget(self.page_proyectos)
        
        #PAGE TPV
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_tpv = QWidget()
        self.page_tpv.setObjectName(u"page_tpv")
        self.verticalLayout_9 = QVBoxLayout(self.page_tpv)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_8 = QLabel(self.page_tpv)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_8)

        application_pages.addWidget(self.page_tpv)
        
        #PAGE VENTAS
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_ventas = QWidget()
        self.page_ventas.setObjectName(u"page_ventas")
        self.verticalLayout_10 = QVBoxLayout(self.page_ventas)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_9 = QLabel(self.page_ventas)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFrameShadow(QFrame.Shadow.Plain)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_9)

        application_pages.addWidget(self.page_ventas)
        
        #PAGE AJUSTES
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_ajustes = QWidget()
        self.page_ajustes.setObjectName(u"page_ajustes")
        self.verticalLayout_11 = QVBoxLayout(self.page_ajustes)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_10 = QLabel(self.page_ajustes)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_10)

        application_pages.addWidget(self.page_ajustes)
        
        #PAGE FABRICACION
        #/////////////////////////////////////////////////////////////////////////////////////
        self.page_fabricacion = QWidget()
        self.page_fabricacion.setObjectName(u"page_fabricacion")
        self.verticalLayout_5 = QVBoxLayout(self.page_fabricacion)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.page_fabricacion)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        application_pages.addWidget(self.page_fabricacion)

        self.retranslateUi(application_pages)

        application_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(application_pages)
    # setupUi

    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("application_pages", u"StackedWidget", None))
        self.btn_anadirCliente.setText(QCoreApplication.translate("application_pages", u"A\u00f1adir cliente", None))
        self.label_2.setText(QCoreApplication.translate("application_pages", u"Contabilidad", None))
        self.label_3.setText(QCoreApplication.translate("application_pages", u"Compras", None))
        self.label.setText(QCoreApplication.translate("application_pages", u"Empleados", None))
        self.label_5.setText(QCoreApplication.translate("application_pages", u"Inventario", None))
        self.label_6.setText(QCoreApplication.translate("application_pages", u"Mantenimiento", None))
        self.label_7.setText(QCoreApplication.translate("application_pages", u"Proyectos", None))
        self.label_8.setText(QCoreApplication.translate("application_pages", u"TPV", None))
        self.label_9.setText(QCoreApplication.translate("application_pages", u"Ventas", None))
        self.label_10.setText(QCoreApplication.translate("application_pages", u"Ajustes", None))
        self.label_4.setText(QCoreApplication.translate("application_pages", u"Fabricaci\u00f3n", None))
    # retranslateUi

