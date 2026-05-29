# Sistema de Votación

Profe, este es nuestro sistema de votación. Aquí adjuntamos todo lo solicitado en el entregable 7.

## Capturas

*A continuación se presentan pantallas del sistema en funcionamiento:*

- **Pantalla de Inicio de Sesión:**
  ![Login](./docs/screenshots/login.png)

- **Panel Administrativo - Gestión de Elecciones:**
  ![Elecciones](./docs/screenshots/elecciones.png)

- **Panel Administrativo - Gestión de Candidatos:**
  ![Candidatos](./docs/screenshots/candidatos.png)

- **Panel Administrativo - Gestión de Votantes:**
  ![Votantes](./docs/screenshots/votantes.png)

- **Panel Administrativo - Auditoría Electoral:**
  ![Auditoria](./docs/screenshots/auditoria.png)

## Endpoints Probados

Se adjuntan pantallazos de las pruebas realizadas en Postman, donde todas nos retornan código 200 (o 201 de éxito), por lo que podemos confirmar que los endpoints están funcionando correctamente:
- ![Prueba Login](./imagenes/Captura%20de%20pantalla%202026-05-29%20052932.png)
- ![Prueba GET Elecciones](./imagenes/Captura%20de%20pantalla%202026-05-29%20053322.png)
- ![Prueba GET Elecciones 2](./imagenes/Captura%20de%20pantalla%202026-05-29%20053626.png)
- ![Prueba POST Elecciones](./imagenes/Captura%20de%20pantalla%202026-05-29%20054505.png)
- ![Prueba Error Candidato](./imagenes/Captura%20de%20pantalla%202026-05-29%20054856.png)

## Pasos de Ejecución

Para correr este proyecto en tu entorno local, necesitas tener instalados **Python** y **Node.js**. Sigue estos pasos:

### 1. Clonar el repositorio
```bash
git clone https://github.com/Joners14/proyectoaulaTendencias20261.git
cd proyectoaulaTendencias20261
```

### 2. Levantar el Backend (Django)
Abre una terminal en la carpeta principal del proyecto:
```bash
cd sistemVotacion

# Instalar las dependencias de Python
pip install -r requirements.txt

# Aplicar las migraciones a la base de datos (crea las tablas)
python manage.py migrate

# Iniciar el servidor backend 
python manage.py runserver
```
*(El backend quedará corriendo en `http://localhost:8000`)*

### 3. Levantar el Frontend (React / Vite)
Abre una **nueva terminal** en la carpeta principal del proyecto:
```bash
cd frontend

# Instalar dependencias de Node
npm install

# Correr el servidor de desarrollo del frontend
npm run dev
```
*(El frontend quedará corriendo en la ruta que te indique la terminal, generalmente `http://localhost:5173`)*

## Credenciales de Prueba

Utiliza estas credenciales de ejemplo para ingresar al sistema y probar sus funcionalidades.

| Rol | Usuario / Email | Contraseña |
|---|---|---|
| **Administrador** | `admin` | `admin` |
