# Binary Search Tree - Fase 4 UNAD

Aplicación gráfica desarrollada en Python para la implementación y visualización de un **Árbol Binario de Búsqueda (ABB)**, como parte de la actividad Fase 4: Implementación de Árboles y Estructuras Binarias de la Universidad Nacional Abierta y a Distancia (UNAD).

## Descripción del proyecto

El proyecto permite construir y administrar un árbol binario de búsqueda mediante una interfaz gráfica desarrollada con Tkinter.

La aplicación permite insertar y buscar nodos, visualizar gráficamente la estructura del árbol y consultar sus tres recorridos principales:

- Preorden (Preorder).
- Inorden (Inorder).
- Posorden (Postorder).

También incorpora validaciones para controlar la entrada de datos y limitar la profundidad del árbol a cuatro niveles.

## Funcionalidades

- Inicio de sesión mediante contraseña genérica `UNAD`.
- Inserción de nodos enteros en un árbol binario de búsqueda.
- Visualización gráfica de la estructura del árbol.
- Visualización de los recorridos Preorden, Inorden y Posorden.
- Búsqueda de nodos existentes.
- Validación de entradas no numéricas.
- Control de valores duplicados.
- Restricción de profundidad máxima de cuatro niveles.
- Opción para limpiar el árbol.
- Interfaz gráfica organizada en cuatro paneles.

## Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje de programación |
| Tkinter | Desarrollo de la interfaz gráfica |
| Matplotlib | Visualización gráfica del árbol |
| MVC | Arquitectura del proyecto |

## Arquitectura del proyecto

El proyecto utiliza el patrón arquitectónico **Modelo-Vista-Controlador (MVC)**, separando la lógica de negocio, la interfaz gráfica y el control de las operaciones.

```text
Fase4AlejandroGallo/
│
├── models/
│   ├── __init__.py
│   ├── tree_node.py
│   └── binary_search_tree.py
│
├── views/
│   ├── __init__.py
│   ├── login_view.py
│   └── tree_view.py
│
├── controllers/
│   ├── __init__.py
│   ├── login_controller.py
│   └── tree_controller.py
│
├── utils/
│   ├── __init__.py
│   └── tree_visualizer.py
│
├── main.py
├── test_models.py
├── requirements.txt
├── README.md
└── .gitignore
```

### Descripción de los componentes

- **Models:** contiene la estructura de los nodos y la lógica del árbol binario de búsqueda.
- **Views:** contiene las ventanas y los componentes gráficos de la aplicación.
- **Controllers:** administra las acciones del usuario y conecta las vistas con los modelos.
- **Utils:** contiene las herramientas auxiliares para la representación gráfica del árbol.
- **main.py:** punto de entrada de la aplicación.
- **test_models.py:** pruebas de las operaciones principales del árbol.

## Requisitos

Para ejecutar el proyecto se necesita:

- Python 3.10 o superior.
- Tkinter.
- Matplotlib.

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/Lulo7/Fase4-Arboles-Binarios-UNAD.git
```

### 2. Ingresar al directorio

```bash
cd Fase4-Arboles-Binarios-UNAD
```

### 3. Crear un entorno virtual

En Windows:

```bash
python -m venv venv
```

### 4. Activar el entorno virtual

```bash
venv\Scripts\activate
```

### 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 6. Ejecutar la aplicación

```bash
python main.py
```

## Acceso a la aplicación

La ventana de inicio de sesión solicita una contraseña para ingresar a la aplicación.

**Contraseña:** `UNAD`

## Autor

**Estudiante:** Javier Alejandro Gallo Lozano  
**Universidad:** Universidad Nacional Abierta y a Distancia (UNAD)  
**Actividad:** Fase 4 - Implementación de Árboles y Estructuras Binarias  
**Curso:** Estructura de Datos

## Licencia

Proyecto académico desarrollado con fines educativos.
