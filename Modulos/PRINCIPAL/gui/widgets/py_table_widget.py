import os

from Modulos.PRINCIPAL.imports.core import *

class PyTableWidget(QTableWidget):
    def __init__( 
        self,
        minimum_width = 50,
        text_color = "#000000",
        icon_path = "",        
        icon_color = "#FFFFFF",
        btn_color = "#356b6b",
        btn_hover = "#354b4b",
        btn_pressed = "#A4ADB2",
        
        radius = 8,
        color = "#FFF",
        bg_color = "#444",
        selection_color = "#FFF",
        header_horizontal_color = "#444",
        header_vertical_color = "#444",
        bottom_line_color = "#555",
        grid_line_color = "#1C323F", #"#555",
        scroll_bar_bg_color = "#FFF",
        scroll_bar_btn_color = "#333",
        context_color = "#354b4b"
        
        ):
        super().__init__()
        
        #parametros predeterminados
        #self.setText(text)
        #self.setMaximumHeight(height)
        #self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.setSelectionMode(QTableWidget.NoSelection)
        
        horizontalheader = self.horizontalHeader()
        verticalheader = self.verticalHeader()

        # ESTILOS TABLA
        horizontalheader.setStyleSheet(
            "QHeaderView::section {font:600 12pt; color: black; background-color: beige !important;}"
        )
        verticalheader.setStyleSheet(
            "QHeaderView::section {font:600 12pt; color: black; background-color: beige;}"
        )
        
        self.set_stylesheet(
            radius,
            color,
            bg_color,
            header_horizontal_color,
            header_vertical_color,
            selection_color,
            bottom_line_color,
            grid_line_color,
            scroll_bar_bg_color,
            scroll_bar_btn_color,
            context_color
        )

    # SET STYLESHEET
    def set_stylesheet(
        self,
        radius,
        color,
        bg_color,
        header_horizontal_color,
        header_vertical_color,
        selection_color,
        bottom_line_color,
        grid_line_color,
        scroll_bar_bg_color,
        scroll_bar_btn_color,
        context_color
    ):
        # APPLY STYLESHEET
        style_format = style.format(
            _radius = radius,          
            _color = color,
            _bg_color = bg_color,
            _header_horizontal_color = header_horizontal_color,
            _header_vertical_color = header_vertical_color,
            _selection_color = selection_color,
            _bottom_line_color = bottom_line_color,
            _grid_line_color = grid_line_color,
            _scroll_bar_bg_color = scroll_bar_bg_color,
            _scroll_bar_btn_color = scroll_bar_btn_color,
            _context_color = context_color
        )
        self.setStyleSheet(style_format)
    # STYLE
# ///////////////////////////////////////////////////////////////
style = '''

QTableWidget {{	
	background-color: {_bg_color};
	padding: 5px;
	border-radius: {_radius}px;
	gridline-color: {_grid_line_color};
    color: {_color};
}}
QTableWidget QTableCornerButton::section {{
    border: none;
	background-color: {_header_horizontal_color};
	padding: 3px;
    border-top-left-radius: {_radius}px;
}}

QScrollBar:horizontal {{
    border: none;
    background: {_scroll_bar_bg_color};
    height: 12px;
    margin: 0px 21px 0 21px;
	border-radius: 0px;
}}
QScrollBar::handle:horizontal {{
    background: {_context_color};
    min-width: 30px;
	border-radius: 4px
}}
QScrollBar::add-line:horizontal {{
    border: none;
    background: #333;
    width: 20px;
	border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}}
QScrollBar::sub-line:horizontal {{
    border: none;
    background: #333;
    width: 20px;
	border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}}
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
{{
    background: none;
}}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{{
    background: none;
}}
QScrollBar:vertical {{
	border: none;
    background: {_scroll_bar_bg_color};
    width: 8px;
    margin: 21px 0 21px 0;
	border-radius: 0px;
}}
QScrollBar::handle:vertical {{	
	background: {_context_color};
    min-height: 25px;
	border-radius: 4px
}}
QScrollBar::add-line:vertical {{
     border: none;
    background: #333;
     height: 20px;
	border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
     subcontrol-position: bottom;
     subcontrol-origin: margin;
}}
QScrollBar::sub-line:vertical {{
	border: none;
    background: #333;
     height: 20px;
	border-top-left-radius: 4px;
    border-top-right-radius: 4px;
     subcontrol-position: top;
     subcontrol-origin: margin;
}}
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {{
     background: none;
}}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
     background: none;
}}

QToolTip {{
    background-color: beige;
}}

''' 
