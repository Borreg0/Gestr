#  Gestr - ERP

## Índice
    1. Instrucciones para instalar y ejecutar la aplicación.
    2. Descripción de los módulos y funcionalidades.
    3. Herramientas y bibliotecas utilizadas

## **Instrucciones para instalar y ejecutar la aplicación.**

- Utilicé pyinstaller y CX Freeze sin éxito, por lo que debe ejecutarse desde la propia consola de VSCode.

- Para iniciarla hay que abrir la carpeta Gestr con VSCode y luego ejecutar el archivo Gestr.py

## **Descripción de los módulos y funcionalidades.**

### *CRM*
- Permite añadir, editar, eliminar y visualizar en una tabla todos los clientes con sus datos más relevantes.

#### *funcionalidades*
- Función de búsqueda de clientes con filtro, así podemos buscar clientes por su nombre, email, país, teléfono o fecha de registro.

### *Contabilidad*
- Muestra estadísticas y métricas sobre los datos introducidos en el resto de módulos.
- Consta de 4 botones:

    1. Balance General: Muestra dos gráficos: Uno de tarta que muestra costes y ganancias brutas, sin considerar iva; y la cantidad de unidades vendidas por producto, de tal manera podemos saber qué productos se venden mejor que otros.

    2. Pedidos por fecha: Pensado para valorar la temporalidad de nuestra demanda. Muestra dos gráficos también: En el primero se muestra el porcentaje
    de ventas en una fecha concreta respecto del total de ventas ("Las ventas del día X suponen el 40% de todas nuestras ventas"); mientras el segundo gráfico muestra la cantidad de pedidos que se hicieron cada día.

    3. Compras a proveedores: Otros dos gráficos: El primero muestra el coste total del stock actual; El segundo, el valor potencial (total y parcial) de esa mercancía, de ese stock, si se vende al precio que se estipula.

    4. Tendencias: Tres gráficos:
        
        - Distribución métodos de pago: Muestra cuantos pedidos fueron hechos con según qué metodo de pago.
        - Cantidad de productos por pedido: Enseña cuántos pedidos tienen x producto/s.
        - Relación Productos por pedido/Método de Pago: Correlaciona la cantidad de productos en un pedido con un tipo de pago concreto. No es fiable ya que los datos son inventados, pero con datos reales ofrece buenos resultados.

### *Proyectos*
- Consiste en una tabla donde se muestra la información más relevante del proyecto: El nombre, los empleados involucrados, la descripción del proyecto, fechas de inicio y fin, y una casilla para cambiar su estado de "En Proceso" a "Terminado", además de un botón para eliminar.
- Al crear un nuevo proyecto le damos nombre, seleccionamos al menos un empleado y le asignamos una tarea dentro de ese proyecto.

#### *funcionalidades*
- Búsqueda con filtros.
- Tooltips en celdas de la tabla. No tiene sentido crear enormes casillas con todo el texto visible, los tooltips permiten que podamos visualizar los datos del pedido que queramos con solo dejar el cursor encima.

### *Empleados*
- Control de empleados, otro CRUD como CRM con la diferencia que aquí asignamos departamento, contraseña y nivel de permisos (Rol de usuario).

#### *funcionalidades*
- Búsqueda con filtros.
- Contraseña segura, al introducirla en la base de datos se hashea.
- Los permisos muestran o desactivan ciertos módulos, de manera que solo los administradores pueden ver la aplicación completa.
- Generador automático de email corporativo: Tomando el nombre y otros parámetros de ajuste, se generan emails como "JohnDoe@empresa.com".

### *Inventario/Productos*
- CRUD del stock disponible con columnas para el código del producto, su nombre, el stock disponible, precio por unidad, IVA, y coste de compra/producción por unidad.

#### *funcionalidades*
- Búsqueda con filtros.

### *TPV/Ventas*
- Este módulo se encarga de generar los pedidos de los clientes. De nuevo es un CRUD pero sin la función de editar, ya que no tiene sentido editar pedidos: En cualquier caso práctico se elimina el existente y crea uno nuevo, o solo se añade uno nuevo complementando al anterior.

- Funcionamiento: se escoge un cliente al que asignar el pedido, se selecciona un producto junto con la cantidad de unidades y se añaden a la cesta, luego se elige un método de pago y se confirma el pedido.

- Control de errores:
    - Para evitar comprar más de lo que hay en stock, se hace una comprobación de la suma de todas las unidades del producto X, si excede el stock se pregunta si quiere continuar el pedido con "stock unidades" del producto X.
    - Para evitar comprar 0 unidades, hay una comprobación de que en la cesta debe haber mínimo una unidad del producto X, por lo que si tampoco hay en stock (stock = 0), no puede seleccionarse al menos una unidad, y por tanto el pedido no puede seguir.
    - El producto no se elimina de la base de datos cuando hay 0 unidades, se debe eliminar manualmente.

#### *funcionalidades*
- Búsqueda con filtros. En este módulo puede apreciarse mejor esta funcionalidad, ya que cuando generemos una decena de pedidos podremos filtrarlos por cada una de sus columnas donde no es tan fácil localizar un pedido o pedidos concretos a simple vista.
- Celdas con tooltip.
- Generación de reportes: Se genera un PDF del pedido seleccionado. Se ubican por defecto en el directorio PedidosGenerados.
- Actualización automática del stock en la base de datos.

#### *funcionalidades futuras*
- Poder crear un nuevo cliente desde esa misma ventana. El radiobutton no hace nada aún.

### *Web*
- Funciona como una versión más corta de este documento. Se muestra la mayoría de las funcionalidades y módulos que ofrece este programa.

### *Funcionalidades generales y Curiosidades*

- La base de datos se crea automáticamente, junto con sus tablas, si no hay una base de datos creada.
- Los roles de usuario determinan qué módulos se cargan y qué módulos no.

- Al iniciar sesión, el nombre del empleado y el rol aparecen en la esquina inferior izquierda.
- La version v1.6.1 significa: v1 Version 1, 6 modulos funcionales, 1 modulo opcional funcional

## **Herramientas y bibliotecas utilizadas**

- En el documento requirements.txt aparecen todas las librerías necesarias para la correcta ejecución del proyecto. Son:

    - Faker==33.3.1
    - matplotlib==3.10.1
    - pandas==2.2.3
    - Pillow==11.1.0
    - PySide6==6.8.2.1
    - PySide6_Addons==6.8.1.1
    - PySide6_Essentials==6.8.1.1
    - python_bcrypt==0.3.2
    - reportlab==4.3.1

- El archivo .txt tiene por funcion instalar todas las librerías de golpe usando: pip install -r /path/to/requirements.txt
