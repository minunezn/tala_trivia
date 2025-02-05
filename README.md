# TalaTrivia API

TalaTrivia es una API desarrollada con Django y FastAPI para gestionar trivias de preguntas sobre recursos humanos. Permite la gestión de usuarios, preguntas, trivias, rankings y autenticación mediante JWT.  

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- **Docker** y **Docker Compose**  
- **Python 3.10+**  
- **PostgreSQL**  

## Instalación y ejecución

### 1 Clonar el repositorio

git clone https://github.com/minunezn/tala_trivia.git
cd talatrivia

### 2 Configurar variables de entorno
Renombra el archivo .env.example a .env y actualiza los valores según tu configuración.

cp .env.example .env
Asegúrate de configurar las credenciales de la base de datos y las claves de autenticación.

### 3 Levantar el entorno con Docker
bash
docker-compose up --build
Esto iniciará los contenedores de la API, la base de datos PostgreSQL y la documentación interactiva.

### 4 Aplicar migraciones y cargar datos iniciales
Ejecuta los siguientes comandos dentro del contenedor de la aplicación:

docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

Sigue las instrucciones para crear un usuario administrador.

## Endpoints principales

| Método  | URL                                         | Descripción                               |
|---------|--------------------------------------------|-------------------------------------------|
| `POST`  | `/api/auth/login/`                        | Iniciar sesión y obtener token JWT       |
| `POST`  | `/api/auth/register/`                     | Registrar un nuevo usuario               |
| `GET`   | `/api/trivias/`                           | Listar todas las trivias                 |
| `POST`  | `/api/trivias/`                           | Crear una nueva trivia                   |
| `GET`   | `/api/trivias/{id}/`                      | Obtener detalles de una trivia           |
| `POST`  | `/api/trivias/answer/{trivia_id}/{question_id}/` | Responder una pregunta           |
| `GET`   | `/api/rankings/`                          | Ver el ranking de usuarios               |


### Tecnologías utilizadas
- Django Rest Framework y FastAPI
- PostgreSQL
- JWT Authentication
- Docker y Docker Compose
- Pytest para testing
