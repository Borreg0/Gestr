#IMPORTAR MODULOS
import sys, os, bcrypt 

from Modulos.PRINCIPAL.imports.core import *
from Modulos.PRINCIPAL.imports.widgets_import import *
from Modulos.PRINCIPAL.BBDD.ConnBBDD import *


class LoginWindow(QMainWindow):
    
    login_exitoso = Signal(list)
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Gestr - Login")
        self.setWindowIcon(QIcon(r'gestr.ico'))
        
        self.resize(541, 385)

        self.setFixedSize(self.size())
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.MSWindowsFixedSizeDialogHint)

        self.setStyleSheet(u"background-color: rgb(193, 230, 234);")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.loginCampos = QFrame(self.centralwidget)
        self.loginCampos.setObjectName(u"loginCampos")
        self.loginCampos.setGeometry(QRect(250, 30, 281, 291))
        self.loginCampos.setFrameShape(QFrame.Shape.StyledPanel)
        self.loginCampos.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout = QVBoxLayout(self.loginCampos)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.labelLogin = QLabel(self.loginCampos)
        self.labelLogin.setObjectName(u"labelLogin")
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(24)
        self.labelLogin.setFont(font)
        self.labelLogin.setScaledContents(False)
        self.labelLogin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelLogin.setText("Login empleados")

        self.verticalLayout.addWidget(self.labelLogin)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.labelEmail = QLabel(self.loginCampos)
        self.labelEmail.setObjectName(u"labelEmail")
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(16)
        self.labelEmail.setFont(font1)
        self.labelEmail.setText("Email")

        self.verticalLayout.addWidget(self.labelEmail)

        self.emailEmpleado = QLineEdit(self.loginCampos)
        self.emailEmpleado.setObjectName(u"emailEmpleado")
        self.emailEmpleado.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.emailEmpleado)

        self.labelContrasena = QLabel(self.loginCampos)
        self.labelContrasena.setObjectName(u"labelContrasena")
        self.labelContrasena.setFont(font1)
        self.labelContrasena.setText("Contraseña")

        self.verticalLayout.addWidget(self.labelContrasena)

        self.contrasenaEmpleado = QLineEdit(self.loginCampos)
        self.contrasenaEmpleado.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.contrasenaEmpleado)

        self.line = QFrame(self.loginCampos)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.frame = QFrame(self.loginCampos)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnAceptar = QPushButton(self.frame)
        self.btnAceptar.setObjectName(u"btnAceptar")
        self.btnAceptar.setStyleSheet(u"background-color: rgb(28, 50, 63);color: rgb(255, 255, 255);")
        self.btnAceptar.setText("Aceptar")

        self.horizontalLayout.addWidget(self.btnAceptar)

        self.Ayuda = QToolButton(self.frame)
        self.Ayuda.setObjectName(u"Ayuda")
        self.Ayuda.setMinimumSize(QSize(30, 0))
        self.Ayuda.setStyleSheet(u"background-color: rgb(164, 173, 178);")
        self.Ayuda.setText("?")

        self.horizontalLayout.addWidget(self.Ayuda)


        self.verticalLayout.addWidget(self.frame)

        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(10, 120, 221, 231))
        self.logo.setPixmap(QPixmap(u"gestr.ico"))
        self.logo.setScaledContents(True)
        self.gestrNombre = QLabel(self.centralwidget)
        self.gestrNombre.setObjectName(u"gestrNombre")
        self.gestrNombre.setGeometry(QRect(60, 30, 131, 71))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(36)
        self.gestrNombre.setFont(font2)
        self.gestrNombre.setText(u"Gestr")
        self.gestrNombre.setScaledContents(True)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        QMetaObject.connectSlotsByName(self)
        
        self.btnAceptar.clicked.connect(self.login)
        self.Ayuda.clicked.connect(self.info)

    def info(self):
        QMessageBox.information(self,"Información","Entra como admin@admin : admin",QMessageBox.Ok)
    
    def login(self):
        
        conex = Conn()
        empleados = conex.mostrarTodosEmpleados()
        email = self.emailEmpleado.text()
        contrasena = self.contrasenaEmpleado.text()
        
        for empleado in empleados:
            #print(empleado["nombre"],empleado["contrasena"],type(empleado["contrasena"]))
            if empleado["email"] == email:
                
                #hashear la contraseña de la bbdd
                hash_bbdd = empleado["contrasena"].encode('utf-8')
                if bcrypt.checkpw(contrasena.encode('utf-8'), hash_bbdd):
                    usuario.append(empleado)
                    self.login_exitoso.emit(usuario)
                    self.close()
                else:
                    QMessageBox.information(self,"Credenciales incorrectas","Email o contraseña incorrecto",QMessageBox.Ok)
        
        
            
    
                    

                    
                
                    
            
            
            


    