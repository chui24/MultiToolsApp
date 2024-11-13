import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from .qr_functions import generar_qr_url, generar_qr_imagen  # Importar funciones de QR
from .styles import apply_styles  # Importar estilos
from app.file_converter import word_to_pdf, pdf_to_word, validate_file_extension  # Importar funciones de conversión
import qrcode
from PIL import Image, ImageTk  # Pillow para cargar y mostrar imágenes
from tkinter import filedialog


class InterfaceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MultiToolsApp")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f4f8")
        apply_styles(self.root)
        
        self.font_secondary = ("Lexend", 20)
        self.primary_color = "#000000"
        self.setup_ui()
    
    def setup_ui(self):
        # Crear el layout principal
        self.main_frame = tk.Frame(self.root, bg="#f0f4f8")
        self.main_frame.pack(expand=True, pady=20)

        # Dividir en dos secciones
        self.left_frame = tk.Frame(self.main_frame, bg="#f0f4f8")
        self.left_frame.pack(side="left", padx=20)

        self.right_frame = tk.Frame(self.main_frame, bg="#f0f4f8")
        self.right_frame.pack(side="right", padx=20)

        self.label_bienvenida = tk.Label(self.left_frame, text="Seleccione una herramienta", bg="#f0f4f8", font=("Helvetica", 16, "bold"))
        self.label_bienvenida.pack(pady=20)

        # Menú de opciones
        self.opcion_seleccionada = tk.StringVar()
        self.opcion_menu = ttk.Combobox(self.left_frame, textvariable=self.opcion_seleccionada, state="readonly", font=("Helvetica", 12), width=25)
        self.opcion_menu['values'] = ("Seleccionar opción", "Generar QR", "Convertir archivos (Word/PDF)")
        self.opcion_menu.current(0)
        self.opcion_menu.pack(pady=10)

        self.btn_confirmar_opcion = ttk.Button(self.left_frame, text="Confirmar opción", command=self.on_opcion_seleccionada)
        self.btn_confirmar_opcion.pack(pady=10)
    
    def on_opcion_seleccionada(self):
        seleccion = self.opcion_seleccionada.get()
        if seleccion == "Generar QR":
            QRCodeManager(self.left_frame)
        elif seleccion == "Convertir archivos (Word/PDF)":
            FileConverter(self.right_frame)
    
class FileConverter:
    def __init__(self, parent):
        self.parent = parent
        self.archivo_seleccionado = ""
        self.setup_ui()
    
    def setup_ui(self):
        for widget in self.parent.winfo_children():
            widget.destroy()  # Limpiar los widgets previos

        self.tipo_conversion = tk.StringVar()
        self.tipo_conversion_menu = ttk.Combobox(self.parent, textvariable=self.tipo_conversion, state="readonly", font=("Helvetica", 12), width=25)
        self.tipo_conversion_menu['values'] = ("Seleccionar tipo", "Word a PDF", "PDF a Word")
        self.tipo_conversion_menu.current(0)
        self.tipo_conversion_menu.pack(pady=10)

        self.btn_seleccionar_archivo = ttk.Button(self.parent, text="Seleccionar archivo", command=self.seleccionar_archivo)
        self.btn_seleccionar_archivo.pack(pady=10)

        self.archivo_seleccionado_label = tk.Label(self.parent, text="", bg="#f0f4f8", font=("Helvetica", 12))
        self.archivo_seleccionado_label.pack(pady=10)

        self.btn_convertir = ttk.Button(self.parent, text="Convertir archivo", command=self.convertir_archivo)
        self.btn_convertir.pack(pady=10)
    
    def seleccionar_archivo(self):
        self.archivo_seleccionado = filedialog.askopenfilename()
        self.archivo_seleccionado_label.config(text=f"Archivo seleccionado: {self.archivo_seleccionado}")
    
    def convertir_archivo(self):
        tipo = self.tipo_conversion.get()
        archivo = self.archivo_seleccionado
        if tipo == "Word a PDF" and validate_file_extension(archivo, ".docx"):
            output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if word_to_pdf(archivo, output_path):
                messagebox.showinfo("Conversión completada", "El archivo ha sido convertido a PDF correctamente.")
            else:
                messagebox.showerror("Error", "Hubo un problema al convertir el archivo.")
        elif tipo == "PDF a Word" and validate_file_extension(archivo, ".pdf"):
            output_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word files", "*.docx")])
            pdf_to_word(archivo, output_path)
            messagebox.showinfo("Conversión completada", "El archivo ha sido convertido a Word correctamente.")
        else:
            messagebox.showerror("Error", "Tipo de archivo no compatible o no seleccionado correctamente.")

class QRCodeManager:
    def __init__(self, parent):
        self.parent = parent
        self.imagen_path = ""
        self.frame_qr_preview = None  # Para la vista previa del QR
        self.setup_ui()

    def setup_ui(self):
        for widget in self.parent.winfo_children():
            widget.destroy()

        self.label_bienvenida = tk.Label(self.parent, text="Seleccione el tipo de QR a generar", bg="#f0f4f8", font=("Helvetica", 16, "bold"))
        self.label_bienvenida.pack(pady=20)

        self.opcion_seleccionada = tk.StringVar()
        self.opcion_menu = ttk.Combobox(self.parent, textvariable=self.opcion_seleccionada, state="readonly", font=("Helvetica", 12), width=25)
        self.opcion_menu['values'] = ("Seleccionar opción", "Generar QR para URL", "Generar QR para Imagen")
        self.opcion_menu.current(0)
        self.opcion_menu.pack(pady=10)

        self.btn_confirmar_opcion = ttk.Button(self.parent, text="Confirmar opción", command=self.mostrar_opciones_seleccionadas)
        self.btn_confirmar_opcion.pack(pady=10)

    def mostrar_opciones_seleccionadas(self):
        seleccion = self.opcion_seleccionada.get()

        if seleccion == "Generar QR para URL":
            self.mostrar_generar_qr_url()
        elif seleccion == "Generar QR para Imagen":
            self.mostrar_generar_qr_imagen()

    def mostrar_generar_qr_url(self):
        self.limpiar_frame()

        label = tk.Label(self.parent, text="Ingrese la URL:", font=("Helvetica", 11))
        label.pack(pady=5)
        entry_url = tk.Entry(self.parent, font=("Helvetica", 12), width=40)
        entry_url.pack(pady=5)

        btn_generar_qr = ttk.Button(self.parent, text="Generar QR", command=lambda: self.generar_qr_url(entry_url.get()))
        btn_generar_qr.pack(pady=10)

    def generar_qr_url(self, url):
        if not url.strip():  # Verifica si la URL está vacía
            messagebox.showwarning("Advertencia", "Por favor, ingrese una URL válida.")
            return

        # Crear código QR para la URL
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')

        # Mostrar vista previa
        self.mostrar_vista_previa(img)

    def mostrar_generar_qr_imagen(self):
        self.limpiar_frame()

        label = tk.Label(self.parent, text="Seleccione una imagen (PNG/JPG):", font=("Helvetica", 12))
        label.pack(pady=5)

        btn_seleccionar_imagen = ttk.Button(self.parent, text="Seleccionar Imagen", command=self.seleccionar_imagen)
        btn_seleccionar_imagen.pack(pady=5)

    def seleccionar_imagen(self):
        self.imagen_path = filedialog.askopenfilename(title="Seleccionar imagen", filetypes=[("PNG Files", "*.png"), ("JPG Files", "*.jpg")])
        if self.imagen_path:
            self.mostrar_vista_previa_qr_imagen()

    def mostrar_vista_previa_qr_imagen(self):
        if not self.imagen_path:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una imagen válida.")
            return

        img_qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        img_qr.add_data(self.imagen_path)
        img_qr.make(fit=True)
        img = img_qr.make_image(fill='black', back_color='white')

        # Mostrar vista previa
        self.mostrar_vista_previa(img)

    def mostrar_vista_previa(self, qr_image):
        qr_image = qr_image.resize((250, 250))  # Hacer la imagen más grande
        qr_tk = ImageTk.PhotoImage(qr_image)

        # Si ya existe un frame de vista previa, lo eliminamos para actualizar
        if self.frame_qr_preview:
            self.frame_qr_preview.pack_forget()

        # Crear un nuevo frame para la vista previa
        self.frame_qr_preview = tk.Frame(self.parent, bg="#f0f4f8")
        self.frame_qr_preview.pack(pady=20)

        # Etiqueta con la imagen del QR
        label_preview = tk.Label(self.frame_qr_preview, image=qr_tk, bg="#f0f4f8")
        label_preview.image = qr_tk  # Guardar la referencia para evitar que la imagen sea recolectada por el garbage collector
        label_preview.pack()

        # Botón para guardar el QR
        btn_guardar_qr = ttk.Button(self.frame_qr_preview, text="Guardar QR", command=lambda: self.guardar_qr(qr_image))
        btn_guardar_qr.pack(pady=5)

    def guardar_qr(self, qr_image):
        archivo = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if archivo:
            qr_image.save(archivo)
            messagebox.showinfo("Guardado", "El código QR ha sido guardado correctamente.")

    def limpiar_frame(self):
        for widget in self.parent.winfo_children():
            widget.destroy()