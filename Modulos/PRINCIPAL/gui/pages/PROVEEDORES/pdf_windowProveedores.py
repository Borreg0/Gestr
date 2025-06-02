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
        proveedores = conexion.mostrarTodosProveedores()
        
        for p in proveedores:
            if p["id"] == pid:
                proveedor = p
                break

        #estilos del documento
        doc = SimpleDocTemplate(fr"InformacionProveedores\Proveedor_{pid}.pdf", pagesize=A4)
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

        #campos del proveedor
        campos_proveedor = [
            ('id', 'ID'), 
            ('nombre', 'Nombre'),
            ('cif', 'CIF'),
            ('direccion', 'Dirección'),
            ('telefono', 'Teléfono'),
            ('email', 'Email'),
            ('descripcion', 'Descripción'),
            ('comentario', 'Comentarios')
        ]

        #configuracion de los parrafos
        story.append(Paragraph("Información Comercial", estilos['titulo']))
        story.append(Spacer(1, 30))

        story.append(Paragraph("Datos del Proveedor", estilos['seccion']))
        for clave, etiqueta in campos_proveedor:
            if clave in proveedor:
                valor = str(proveedor[clave])
                texto = f"<b>{etiqueta}:</b> {valor}"
                story.append(Paragraph(texto, estilos['campo']))
                story.append(Spacer(1, 8))
        
        story.append(Spacer(1, 25))
        
        #construir el documento
        doc.build(story)