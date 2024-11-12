
# MultiToolsApp

Esta es una aplicación de escritorio diseñada para proporcionar una serie de herramientas útiles para los usuarios. En esta primera versión, la aplicación permite generar códigos QR a partir de una URL o de una imagen seleccionada.

## Requisitos

- Python 3.6 o superior
- Dependencias:
  - `pillow`
  - `qrcode`

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/chui24/MultiToolsApp.git
   cd MultiToolsApp
   ```

2. Crea un entorno virtual:

   ```bash
   python3 -m venv env
   source env/bin/activate  # En Linux o macOS
   # En Windows: .\env\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

   Si el archivo `requirements.txt` no está disponible, puedes crearlo ejecutando:

   ```bash
   pip freeze > requirements.txt
   ```

## Instalación de Tkinter


- En Ubuntu/Debian:
  
  ```bash
  sudo apt-get install python3-tk


4. Ejecuta la aplicación:

   ```bash
   python run.py    # Para ejecutar en Windows
   python3 run.py   # Para ejecutar en Linux o macOS
   ```

