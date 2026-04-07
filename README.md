## Instalación del proyecto
Creamos y activamos el entorno virtual:
```
python3 -m venv venv
source venv/bin/activate
```
Instalamos Django
```
pip install django
```
Iniciamos el proyecto de Django
```
django-admin startproject comisionA .
```
Corremos el servidor de django
```
python3 manage.py runserver
```
## Sincronizar y poblar base de datos
(opcional) Si se modificó models.py, generar nuevas migraciones
```bash
python manage.py makemigrations
```
Sincronizar con la base de datos
```bash
python manage.py migrate
```
Crear un usuario para acceder al panel de administración:
```bash
python manage.py createsuperuser
```
