# qr_code_app/file_converter.py

import subprocess
import os
from pdf2docx import Converter
from fpdf import FPDF


# Función para convertir Word a PDF usando LibreOffice
def word_to_pdf(input_path, output_path):
    try:
        # Ejecutar LibreOffice en modo headless para convertir el archivo de Word a PDF
        subprocess.run(['libreoffice', '--headless', '--convert-to', 'pdf', '--outdir', os.path.dirname(output_path), input_path], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error al convertir el archivo Word a PDF: {e}")
        return False


# Función para convertir PDF a Word
def pdf_to_word(input_path, output_path):
    cv = Converter(input_path)
    cv.convert(output_path, start=0, end=None)
    cv.close()


# Función para verificar extensiones de archivo
def validate_file_extension(file_path, valid_extensions):
    return file_path.lower().endswith(valid_extensions)
