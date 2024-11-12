# qr_code_app/file_converter.py

from docx import Document
from pdf2docx import Converter
from fpdf import FPDF
import os

# Función para convertir Word a PDF
def word_to_pdf(input_path, output_path):
    document = Document(input_path)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Agregar contenido del archivo Word al PDF
    for para in document.paragraphs:
        pdf.multi_cell(0, 10, para.text)
    
    # Guardar el PDF
    pdf.output(output_path)

# Función para convertir PDF a Word
def pdf_to_word(input_path, output_path):
    cv = Converter(input_path)
    cv.convert(output_path, start=0, end=None)
    cv.close()

# Función para verificar extensiones de archivo
def validate_file_extension(file_path, valid_extensions):
    return file_path.lower().endswith(valid_extensions)
