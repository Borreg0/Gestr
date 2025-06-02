import os

from Modulos.PRINCIPAL.imports.core import *

class PyLineEdit(QLineEdit):
    def __init__(
        self,
        text = "",
        height = 40,
        minimum_width = 50,
        text_padding = 0,
        text_color = "#FFFFFF",
        icon_path = "",        
        icon_color = "#FFFFFF",
        placeholder_color = "black"
        #btn_color = "#356b6b",
        #btn_hover = "#354b4b", #1C323F
        #btn_pressed = "#A4ADB2",
        ):
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
        #self.btn_color = btn_color
        #self.btn_hover = btn_hover
        #self.btn_pressed = btn_pressed

        
        self.setStyleSheet(
            """
            QLineEdit{{
            color: black;
            font:500 13pt
            background-color:#A4ADB2;
            text-align: left;
            border: 1px solid #1C323F;
            border-radius: 4px
            }}
            QLineEdit::Placeholder {{
            color: red;
            }}
            QLineEdit::hover{{
            background-color:{line_hover};
            border: 3px solid #1C323F;
            border-radius: 7px
            }}
            """
        )
               
        