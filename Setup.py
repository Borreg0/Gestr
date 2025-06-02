from cx_Freeze import setup,Executable

files = [("gestr.ico",""),
        ("Modulos/PRINCIPAL/BBDD/BBDD_SGE_PFINAL.db", 
        "Modulos/PRINCIPAL/BBDD/BBDD_SGE_PFINAL.db"),
        ("Modulos/PRINCIPAL/gui/images/icons",
         "Modulos/PRINCIPAL/gui/images/icons")
        ]

target = Executable(
    script="Gestr.py",
    base="Win32GUI",
    icon= "gestr.ico"
)

setup(
    name = "Gestr | TFG",
    version = "2.8.1",
    options = {'build_exe' : {'include_files': files,'packages':["numpy"]}},
    executables = [target]
)