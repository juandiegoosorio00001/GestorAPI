GestorAPI

API REST desarrollada con Django y Django REST Framework (DRF) para la gestión de inventario de productos y categorías.

Descripción

Este proyecto fue desarrollado como parte del taller de nivelación de la asignatura Tendencias de software, aplicando buenas prácticas de desarrollo backend con Django y Django REST Framework.

La API permite administrar:

-Categorías
-Productos
-Relación entre productos y categorías
-Autenticación y permisos
-Filtrado, búsqueda y paginación

Tecnologías utilizadas

-Python
-Django
-Django REST Framework
-SQLite
-Django Filter
-DRF Spectacular (Swagger/OpenAPI)

Funcionalidades

-CRUD completo de categorías
-CRUD completo de productos
-Validación personalizada del precio
-Autenticación por token
-Permisos protegidos
-Paginación
-Filtrado por categoría
-Búsqueda por nombre
-Ordenamiento
-Documentación Swagger
-Pruebas automatizadas

Instalación del proyecto

1.Clonar el repositorio

bash
git clone https://github.com/juandiegoosorio00001/GestorAPI.git


2. Ingresar al proyecto

cd GestorApi

3. Crear entorno virtual

python -m venv venv


4. Activar entorno virtual

Source venv/Scripts/activate

5. Instalar dependencias

pip install -r requirements.txt

6. Ejecutar migraciones

python manage.py migrate


7. Crear superusuario

python manage.py createsuperuser

8. Ejecutar el servidor

python manage.py runserver

Documentación Swagger

Abrir en navegador:

http://127.0.0.1:8000/api/docs/

Endpoints principales

-Productos

/api/v1/productos/

Categorías

/api/v1/categorias/

Token de autenticación

/api/token/

Ejemplos de uso

Buscar producto por nombre

/api/v1/productos/?search=laptop

Filtrar productos por categoría

/api/v1/productos/?categoria=1

Ordenar productos por precio

/api/v1/productos/?ordering=precio



Ejecutar pruebas

python manage.py test

Autor

Juan Diego Osorio Araque
