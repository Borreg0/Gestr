import os

from Modulos.PRINCIPAL.imports.core import *

class PyPushButtonPdf(QPushButton):
    def __init__(
        self,
        text = "",
        height = 40,
        minimum_width = 50,
        text_padding = 55,
        text_color = "#FFFFFF",
        icon_path = "",        
        icon_color = "#FFFFFF",
        btn_color = "#ff0000",
        btn_hover = "#8f2f2f",
        btn_pressed = "#A4ADB2",
        is_active = False):
        super().__init__()
        
        #parametros predeterminados
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)
        
        #parametros custom
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active
        
        #set style
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color= self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = self.is_active
        )
    def set_active(self, is_active_menu):
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color= self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = is_active_menu
        )
        
    def set_style(
        self,
        text_padding = 55,
        text_color = "#1C323F",
        btn_color = "#356b6b",
        btn_hover = "#354b4b",
        btn_pressed = "#A4ADB2",
        is_active = False):
        
        style = f"""
        QPushButton{{
            color:{text_color};
            background-color:{btn_color};
            padding-left: {text_padding}px;
            text-align: left;
            border-radius: 4;
            border: none;
        }}
        QPushButton:hover{{
            background-color:{btn_hover}; 
        }}
        QPushButton:pressed{{
            background-color:{btn_pressed}; 
        }}
        """

        active_style = f"""
        QPushButton{{
           background-color:{btn_hover};
           border-right: 3px solid #A4ADB2;
           border-radius: 0;                           
        }}
        """
        
        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)
            
    def paintEvent(self, event):
        #return default style
        QPushButton.paintEvent(self,event)
        #painter
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)
        
        rect = QRect(0,0, self.minimum_width,self.height())
        
        self.draw_icon(qp,self.icon_path,rect,self.icon_color)
        
        qp.end()
        
    def draw_icon(self, qp, image, rect, color):
          #Format path
          app_path = os.path.abspath(os.getcwd())
          folder = "Modulos/PRINCIPAL/gui/images/icons/"
          path = os.path.join(app_path,folder)
          icon_path = os.path.normpath(os.path.join(path,image))
          
          #draw icon
          icon = QPixmap(icon_path)
          
          painter = QPainter(icon)
          painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
          painter.fillRect(icon.rect(),color)
          qp.drawPixmap(
            (rect.width() - icon.width()) / 2 ,
            (rect.height() - icon.height()) / 2,
            icon)
          painter.end()