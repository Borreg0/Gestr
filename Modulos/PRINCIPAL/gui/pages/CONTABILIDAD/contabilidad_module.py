from Modulos.PRINCIPAL.imports.core import *
from Modulos.PRINCIPAL.imports.widgets_import import *
from .funciones import *


class Contabilidad_Page(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent = parent)
        self.setObjectName(u"page_contabilidad")
        self.layoutCentral = QVBoxLayout(self)

        self.botonera = QFrame(self)
        self.layoutGrid = QGridLayout(self.botonera)
        
        self.pedidos = PyPushButton("Pedidos por fecha",icon_path="clipboard2-data.svg")
        self.balance = PyPushButton("Balance general",icon_path="cash-coin.svg")
        self.inventario = PyPushButton("Compras a proveedores", icon_path="shopping-cart-icon.svg")
        self.tendencias = PyPushButton("Tendencias", icon_path="award.svg")
        self.pedidos.setStyleSheet("background-color:#1C323F; color: white;  font: 500 15pt;")
        self.balance.setStyleSheet("background-color:#1C323F; color: white;  font: 500 15pt;")
        self.inventario.setStyleSheet("background-color:#1C323F; color: white;  font: 500 15pt;")
        self.tendencias.setStyleSheet("background-color:#1C323F; color: white;  font: 500 15pt;")
        
        self.layoutGrid.addWidget(self.pedidos, 0, 2, 1, 1)
        self.layoutGrid.addWidget(self.tendencias, 1, 2, 1, 1)
        self.layoutGrid.addWidget(self.inventario, 1, 1, 1, 1)
        self.layoutGrid.addWidget(self.balance, 0, 1, 1, 1)
        
        self.layoutCentral.addWidget(self.botonera)
        
        #acciones botones
        self.pedidos.clicked.connect(pedidosPorFecha)
        self.balance.clicked.connect(graficoGananciasYProducto)
        self.inventario.clicked.connect(productosPorStock)
        self.tendencias.clicked.connect(correlacion)

        