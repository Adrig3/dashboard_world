# dashboard_world


Un pequeño panel (dashboard) web construido con Flask que muestra datos del conjunto de datos "world" (MySQL). Incluye una interfaz HTML para explorar ciudades y una API JSON para consultar tablas (`city`, `country`, `countrylanguage`).

## Características

- Interfaz web con rutas:
	- `/` — página principal (`templates/index.html`).
	- `/dashboard` — vista principal del dashboard que carga datos de ejemplo desde la tabla `city`.
- API REST simple:
	- `/api/<table>` — devuelve todas las filas de la tabla solicitada en formato JSON. Tablas soportadas: `city`, `country`, `countrylanguage`.
- Conexión a MySQL mediante `pymysql` (configuración en `db_config.py`).
- Archivos de plantilla en `templates/` y scripts JS en `static/js/` (por ejemplo `chart.js` para visualizaciones).

## Requisitos

- Python 3.8+ (se probó con versiones recientes de Python 3.x).
- MySQL / MariaDB disponible (local o remoto) para importar `world.sql`.
- Paquetes Python listados en `requirements.txt`:

```text
Flask==3.1.2
pymysql==1.1.2
```

## Instalación rápida (Windows)

1. Clona o descarga este repositorio y abre una terminal en la carpeta del proyecto.

2. Crea y activa un entorno virtual (PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

3. Instala dependencias:

```powershell
python -m pip install --upgrade pip; pip install -r requirements.txt
```

## Configurar la base de datos

El proyecto espera una base de datos llamada `world`. En `db_config.py` hay valores por defecto:

- host: `localhost`
- user: `usuario_world`
- password: `1234`
- database: `world`

Opciones para configurar la base de datos:

1. Importar el volcado SQL incluido (`world.sql`) en tu servidor MySQL:

```powershell
mysql -u root -p
-- dentro del cliente MySQL:
CREATE DATABASE IF NOT EXISTS world CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE world;
SOURCE C:/ruta/al/proyecto/world.sql; -- ajusta la ruta si es necesario
```

2. (Opcional) Crear un usuario específico y otorgar permisos (ejemplo):

```sql
CREATE USER 'usuario_world'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON world.* TO 'usuario_world'@'localhost';
FLUSH PRIVILEGES;
```

3. Si no quieres usar las credenciales por defecto, edita `db_config.py` y ajusta `host`, `user`, `password` y `database` según tu entorno. Alternativamente, puedes modificar `db_config.py` para leer variables de entorno (recomendado para producción).

## Ejecutar la aplicación

Con el entorno virtual activado y la base de datos configurada, ejecuta:

```powershell
python app.py
```

Esto arrancará un servidor de desarrollo de Flask en `http://127.0.0.1:5000` (modo debug activado por defecto en `app.py`).

Visita `http://127.0.0.1:5000` en tu navegador.

## Endpoints útiles

- `/` — página principal.
- `/dashboard` — vista del dashboard (carga hasta 20 ciudades por defecto en la plantilla).
- `/api/city` — obtén todas las filas de `city` como JSON.
- `/api/country` — obtén todas las filas de `country` como JSON.
- `/api/countrylanguage` — obtén todas las filas de `countrylanguage` como JSON.

Ejemplo simple (usar curl o abrir en el navegador):

```powershell
curl http://127.0.0.1:5000/api/city
```

## Estructura del proyecto (resumen)

- `app.py` — punto de entrada de la aplicación Flask.
- `db_config.py` — función `get_connection()` que devuelve una conexión pymysql.
- `world.sql` — volcado de base de datos `world` (tablas y datos).
- `templates/` — plantillas HTML (`index.html`, `dashboard.html`).
- `static/js/chart.js` — script JS para visualizaciones.


## Solución de problemas comunes

- Error de conexión a la base de datos: revisa que MySQL esté funcionando, que `db_config.py` tenga las credenciales correctas y que el usuario tenga permisos sobre la DB `world`.
- `ModuleNotFoundError` al ejecutar: asegúrate de tener el entorno virtual activado y haber instalado `requirements.txt`.
- Problemas al importar `world.sql`: ajusta la ruta al archivo o importa desde el cliente MySQL con `SOURCE` o desde GUI (MySQL Workbench, phpMyAdmin).

