from imports.core import *
from imports.widgets_import import *
from imports.bbdd_conn import *

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm, inch
from reportlab.lib.pagesizes import A4

from reportlab.lib.utils import ImageReader
from PIL import Image

class PdfWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Generar PDF")
        self.setWindowIcon(QIcon(r'Modulos\WEB\imagenes\gestr.ico'))
        
    def generarPdf(self,pid):
        
        conexion = Conn()
        lista_pedidos = conexion.mostrarTodosPedidos()
        lista_clientes = conexion.mostrarTodosClientes()
        
        for p in lista_pedidos:
            if p["id"] == pid:
                pedido = p
                break
        for c in lista_clientes:
            if c["id"]==pedido["cliente"]:
                cliente = c
                break
        
        productos = [f"- {producto}" for producto in pedido["productos"].split("\n")]
        
        #introducir los datos de la empresa
        
        datos_empresa = ["Empresa 1",
                         "CIF: 289389213",
                         "ERP: Borreg0",
                         "AV. DIRECTA SN"
                         ]
        
        
        cuerpoTexto = [f"Información del pedido ID {pedido["id"]}",
                       "",
                       f"\t Fecha: {pedido["fecha"]}",
                       f"\t Cliente: {cliente["nombre"]}", f"    con código de cliente: {cliente["id"]}", f"    y email: {cliente["email"]}",
                       f"\t Productos: ",
                       *productos,
                       f"\t Con importe total de: {pedido["importe"]}€.",
                       f"\t Modo de pago: {pedido["modopago"]}."
                       ]
        
        #construir PDF        
        print(pid)
        pdf = Canvas(fr"PedidosGenerados\Pedido_{pid}.pdf", pagesize=A4)
        
        pdf.setFont("Times-Roman", 18)
        titulo = f"Pedido {pid}"
        subtitulo = "Gestr"
        
        pdf.drawCentredString(A4[0]/2, A4[1] - 50, titulo)
        pdf.drawCentredString(A4[0]/2, A4[1] - 80, subtitulo)
        
        pdf.line(50, A4[1] - 100, A4[0] - 50, A4[1] - 100)
        
        text1 = pdf.beginText(50, A4[1] - 130)
        text = pdf.beginText(100, A4[1] - 260)
        
        text.setFont("Times-Roman", 18)
   
        for linea in datos_empresa:
            text1.textLine(linea)
        pdf.drawText(text1)

        for linea in cuerpoTexto: 
            text.textLine(linea) 
        pdf.drawText(text)
         

        img = r"Modulos\WEB\imagenes\gestr.jpg"
        pdf.drawInlineImage(img, 50, A4[1] - 800, width=100, height=100)
        
        pdf.save()
        

        
