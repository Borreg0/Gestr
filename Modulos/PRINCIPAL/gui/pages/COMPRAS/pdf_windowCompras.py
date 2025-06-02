from Modulos.PRINCIPAL.imports.core import *
from Modulos.PRINCIPAL.imports.widgets_import import *
from Modulos.PRINCIPAL.imports.bbdd_conn import *

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT

from PIL import Image

class PdfWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Generar PDF")
        self.setWindowIcon(QIcon(r'Modulos\WEB\imagenes\gestr.ico'))
        
    def generarPdf(self,pid):
        
        conexion = Conn()
        compras = conexion.mostrarTodasCompras()
        # [{'id': '06052025ZZbcOBZ', 'importe': 6.0, 'proveedor': '3', 'fecha': '06/05/2025, 12:04:34', 'productos': 'CRO-c250d: 6 unidades', 'modoPago': 'Efectivo', 'estado': 'Comprado'}, {'id': '06052025QqTCPib', 'importe': 371.8, 'proveedor': '2', 'fecha': '06/05/2025, 14:42:43', 'productos': 'PLA-cb6b5: 20 unidades\nPEL-59807: 4 unidades', 'modoPago': 'Efectivo', 'estado': 'Recibido'}]
        for c in compras:
            if c["id"] == pid:
                compra = c
                break
        
        #datos del proveedor asociado a la compra
        proveedor_id = compra.get('proveedor', '')
        proveedores = conexion.mostrarTodosProveedores()
        proveedor = next((p for p in proveedores if str(p['id']) == str(proveedor_id)), {})

        #estilos del documento
        doc = SimpleDocTemplate(fr"ComprasGeneradas\Compra_{pid}.pdf", pagesize=A4)
        styles = getSampleStyleSheet()
        story = []
        
        #crear estilos
        estilos = {
            'titulo': ParagraphStyle(
                'TituloPrincipal',
                parent=styles['Heading1'],
                fontSize=20,
                alignment=TA_LEFT,
                textColor=colors.HexColor('#2c3e50')),
            'seccion': ParagraphStyle(
                'Seccion',
                parent=styles['Heading2'],
                fontSize=14,
                spaceAfter=12,
                textColor=colors.HexColor('#2980b9')),
            'campo': ParagraphStyle(
                'Campo',
                parent=styles['BodyText'],
                fontSize=12,
                leading=14,
                textColor=colors.HexColor('#2c3e50'))
            
        }

        #campos compra
        campos_compra = [
        ('id', 'ID Compra'), 
        ('proveedor', 'ID Proveedor'),
        ('fecha', 'Fecha'),
        ('importe', 'Importe'+" (€)"),
        ('modoPago', 'Método de Pago'),
        ('productos', 'Productos'),
        ('estado','Estado')
        ]

        #configuracion de los parrafos
        story.append(Paragraph("Información Comercial", estilos['titulo']))
        story.append(Spacer(1, 30))

        story.append(Paragraph("Datos de la Compra", estilos['seccion']))
        for clave, etiqueta in campos_compra:
            if clave in compra:
                valor = str(compra[clave])
                texto = f"<b>{etiqueta}:</b> {valor}"
                story.append(Paragraph(texto, estilos['campo']))
                story.append(Spacer(1, 8))
        story.append(Spacer(1, 25))
        
        #Sección de datos del proveedor
        story.append(Paragraph("Datos del Proveedor", estilos['seccion']))
        campos_proveedor = [
            ('nombre', 'Nombre'),
            ('cif', 'CIF'),
            ('direccion', 'Dirección'),
            ('telefono', 'Teléfono'),
            ('email', 'Email')
        ]
        
        for clave, etiqueta in campos_proveedor:
            valor = proveedor.get(clave, 'No disponible')
            texto = f"<b>{etiqueta}:</b> {valor}"
            story.append(Paragraph(texto, estilos['campo']))
            story.append(Spacer(1, 8))

        story.append(Spacer(1, 25))

        #construir el documento
        doc.build(story)