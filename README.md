# Proyecto API de Cafés

## Descripción del Proyecto

Este proyecto consiste en una API RESTful que permite gestionar información sobre cafés. Los usuarios pueden agregar, obtener, actualizar y eliminar cafés de una base de datos SQLite. La API está construida utilizando Flask, SQLAlchemy y Pydantic para la validación de datos.

## Características

- **Obtener una lista de cafés**: Permite acceder a todos los cafés almacenados en la base de datos.
- **Agregar un café**: Permite a los usuarios agregar nuevos cafés a la base de datos.
- **Actualizar un café**: Permite actualizar la información de un café específico.
- **Eliminar un café**: Permite eliminar un café de la base de datos.
- **Buscar cafés**: Permite buscar cafés por ubicación.
- **Café aleatorio**: Permite obtener un café aleatorio de la base de datos.
- **Manejo de errores**: Respuestas adecuadas para errores como cafés no encontrados o datos no válidos.

## Estructura del Proyecto

- **`main.py`**: Contiene la lógica principal de la aplicación, incluyendo rutas, modelos de datos y configuración de la base de datos.
- **`test_app.py`**: Contiene pruebas unitarias para la API, asegurando que las funciones estén trabajando correctamente.
- **`add.py`**: Se utiliza para añadir cafés manualmente a la base de datos, aunque este proceso podría automatizarse mediante scraping o utilizando APIs externas.

## Cómo Funciona

1. **Configuración de la Base de Datos**: Se utiliza SQLAlchemy para la interacción con una base de datos SQLite. Los datos de los cafés se almacenan en la tabla `Cafe`, que contiene campos como `name`, `location`, `phone`, `webpage`, `reviews`, `ranking`, `category`, `hours`, `cuisine_types`, `special_diets`, `meals`, `average_rating`, y `advantages`.

2. **Rutas de la API**:
   - `GET /cafes`: Devuelve una lista de todos los cafés en formato JSON.
   - `POST /add`: Permite agregar un nuevo café. Se espera que los datos sean enviados en formato JSON.
   - `GET /search`: Permite buscar cafés por ubicación.
   - `PUT /update/<id>`: Permite actualizar la información de un café específico.
   - `DELETE /delete/<id>`: Permite eliminar un café específico.
   - `GET /random`: Devuelve un café aleatorio de la base de datos.
   - `GET /`: Muestra una página de inicio básica.

3. **Pruebas**: Se utilizan pruebas unitarias en `test_app.py` para garantizar el correcto funcionamiento de la API. Se verifica la capacidad de agregar y obtener cafés, así como otras funcionalidades.

## Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/StevenMend/Api_restfull_U.git
