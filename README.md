# Proyecto Final - Miguel Angel Rizzi

Proyecto final para el curso de Python en Coderhouse. Es una aplicación web Django que permite a los usuarios hacer reservas en un hotel y dejar reseñas. Se aplico los conceptos de herencia de plantillas, formularios, vistas basadas en clases, autenticación y autorización.

---
## Instalación y ejecución

Sigue estos pasos para instalar el proyecto en tu máquina local:

- Clone este repositorio en su máquina local usando el comando `git clone https://github.com/MiguelRizzi/proyecto_final_rizzi.git`.

- Si usa Visual Studio Code, abra el archivo `requirements.txt` y haga clic en Crear ambiente, luego elegir Venv y el intérprete Python, y finalmente pregunta por las dependencias: elegimos `requirements.txt`. Esto creara el entorno virtual e instalará todas las librerías necesarias para ejecutar el proyecto.

- Si prefiere instalarlo de manera manual, use el comando `python -m venv .venv`. Esto creará una carpeta llamada `.venv` dentro del directorio del proyecto.
Active el entorno virtual usando el comando `source .venv/bin/activate` en Linux o Mac, o `.venv\Scripts\activate` en Windows.
Instale las dependencias del proyecto usando el comando `pip install -r requirements.txt`. 

- Ejecute las migraciones de la base de datos usando los comandos `python manage.py makemigrations` y `python manage.py migrate`. Esto creará las tablas necesarias en la base de datos.

- Para ejecutar el servidor de desarrollo, muévase hasta el directorio del proyecto usando el comando `cd project` y use el comando `python manage.py runserver`. Esto iniciará el servidor en el puerto 8000 de su máquina local. Abre tu navegador y navega a `http://localhost:8000` para ver la aplicación en acción.

- Si quiere detener el servidor, simplemente presione `CTRL + C` en la consola donde está ejecutándose.

---
## Funcionalidades
- Registro y inicio de sesión de usuario
- Personalización del modelo de usuario de Django usando relación uno a uno
- Operaciones CRUD para tipos de habitaciones, habitaciones y reservas
- Permisos para controlar el acceso a las vistas
- Aplicación de blog para dejar reseñas del hotel

---
## Uso

Para utilizar la aplicación, primero crea una cuenta haciendo clic en el enlace "Registrarse" en la página de inicio. Una vez que tengas una cuenta, puedes iniciar sesión y comenzar a hacer reservas y dejar reseñas.

Los miembros del staff tienen permisos adicionales y pueden crear, modificar y eliminar tipos de habitaciones, habitaciones y reservas, así como eliminar reseñas de otros usuarios.

---
## Video demostracion

https://www.youtube.com/watch?v=LnzijIFZjUo
---
