import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinterdnd2 import TkinterDnD, DND_FILES  # Importar módulo de arrastrar y soltar
from PIL import Image, ImageTk
from .qr_functions import generar_qr_url, generar_qr_imagen  # Importar funciones de QR
from .styles import apply_styles  # Importar estilos
from app.file_converter import word_to_pdf, pdf_to_word, validate_file_extension  # Importar funciones de conversión


class QRCodeApp(TkinterDnD.Tk):  # Heredamos de TkinterDnD para drag and drop
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.title("MultiToolsApp")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f4f8")

        # Aplicar estilos
        apply_styles(self.root)

        # Inicializar la UI
        self.setup_ui()

        # Definición de las fuentes
        self.font_secondary = ("Lexend", 20)
        self.primary_color = "#000000"

    def setup_ui(self):
        self.main_frame = tk.Frame(self.root, bg="#f0f4f8")
        self.main_frame.pack(expand=True, pady=20)

        self.left_frame = tk.Frame(self.main_frame, bg="#f0f4f8")
        self.left_frame.pack(side="left", padx=20)

        self.right_frame = tk.Frame(self.main_frame, bg="#f0f4f8")
        self.right_frame.pack(side="right", padx=20)

        # Menú para seleccionar herramientas de QR o conversión de archivos
        self.label_bienvenida = tk.Label(self.left_frame, text="Seleccione una herramienta", bg="#f0f4f8", font=("Helvetica", 16, "bold"))
        self.label_bienvenida.pack(pady=20)

        self.opcion_seleccionada = tk.StringVar()
        self.opcion_menu = ttk.Combobox(self.left_frame, textvariable=self.opcion_seleccionada, state="readonly", font=("Helvetica", 12), width=25)
        self.opcion_menu['values'] = ("Seleccionar opción", "Generar QR", "Convertir archivos (Word/PDF)")
        self.opcion_menu.current(0)
        self.opcion_menu.pack(pady=10)

        self.btn_confirmar_opcion = ttk.Button(self.left_frame, text="Confirmar opción", command=self.mostrar_opciones_seleccionadas)
        self.btn_confirmar_opcion.pack(pady=10)

    def mostrar_opciones_seleccionadas(self):
        seleccion = self.opcion_seleccionada.get()

        if seleccion == "Generar QR":
            # Lógica para mostrar opciones de QR
            self.mostrar_opciones_qr()
        elif seleccion == "Convertir archivos (Word/PDF)":
            # Lógica para mostrar opciones de conversión de archivos
            self.mostrar_opciones_conversion()

    def mostrar_opciones_qr(self):
        # Aquí iría la lógica para mostrar las opciones de QR (ya existente)
        pass

    def mostrar_opciones_conversion(self):
        # Limpiar opciones previas
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # Menú para seleccionar el tipo de conversión
        self.tipo_conversion = tk.StringVar()
        self.tipo_conversion_menu = ttk.Combobox(self.right_frame, textvariable=self.tipo_conversion, state="readonly", font=("Helvetica", 12), width=25)
        self.tipo_conversion_menu['values'] = ("Seleccionar tipo", "Word a PDF", "PDF a Word")
        self.tipo_conversion_menu.current(0)
        self.tipo_conversion_menu.pack(pady=10)

        # Botón para seleccionar archivo
        self.btn_seleccionar_archivo = ttk.Button(self.right_frame, text="Seleccionar archivo", command=self.seleccionar_archivo)
        self.btn_seleccionar_archivo.pack(pady=10)

        # Área para arrastrar y soltar archivos
        self.drop_area = tk.Label(self.right_frame, text="Arrastra un archivo aquí", bg="lightgray", width=40, height=5)
        self.drop_area.pack(pady=10)

        # Configurar el área de drop para aceptar archivos
        self.drop_area.drop_target_register(DND_FILES)
        self.drop_area.dnd_bind('<<Drop>>', self.arrastrar_archivo)

        # Etiqueta de archivo seleccionado
        self.archivo_seleccionado_label = tk.Label(self.right_frame, text="", bg="#f0f4f8", font=("Helvetica", 12))
        self.archivo_seleccionado_label.pack(pady=10)

        # Botón para convertir archivo
        self.btn_convertir = ttk.Button(self.right_frame, text="Convertir archivo", command=self.convertir_archivo)
        self.btn_convertir.pack(pady=10)

    def seleccionar_archivo(self):
        # Seleccionar archivo del sistema
        self.archivo_seleccionado = filedialog.askopenfilename()
        self.archivo_seleccionado_label.config(text=f"Archivo seleccionado: {self.archivo_seleccionado}")

    def arrastrar_archivo(self, event):
        # Obtener archivo arrastrado
        self.archivo_seleccionado = event.data
        self.archivo_seleccionado_label.config(text=f"Archivo arrastrado: {self.archivo_seleccionado}")

    def convertir_archivo(self):
        tipo = self.tipo_conversion.get()
        archivo = self.archivo_seleccionado

        if tipo == "Word a PDF" and validate_file_extension(archivo, ".docx"):
            output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            word_to_pdf(archivo, output_path)
            messagebox.showinfo("Conversión completada", "El archivo ha sido convertido a PDF correctamente.")
        elif tipo == "PDF a Word" and validate_file_extension(archivo, ".pdf"):
            output_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word files", "*.docx")])
            pdf_to_word(archivo, output_path)
            messagebox.showinfo("Conversión completada", "El archivo ha sido convertido a Word correctamente.")
        else:
            messagebox.showerror("Error", "Tipo de archivo no compatible o no seleccionado correctamente.")


def apply_styles(root):
    # Aplicar estilos a la aplicación
    style = ttk.Style(root)
    style.configure('TButton', font=('Helvetica', 12), padding=10)




    def volver_menu(self):
        # Volver a la vista inicial
        self.label_url.pack_forget() if hasattr(self, 'label_url') else None
        self.entry_url.pack_forget() if hasattr(self, 'entry_url') else None
        self.btn_generar_qr.pack_forget() if hasattr(self, 'btn_generar_qr') else None

        self.label_imagen.pack_forget() if hasattr(self, 'label_imagen') else None
        self.btn_seleccionar_imagen.pack_forget() if hasattr(self, 'btn_seleccionar_imagen') else None
        self.label_imagen_seleccionada.pack_forget() if hasattr(self, 'label_imagen_seleccionada') else None
        self.btn_generar_qr_imagen.pack_forget() if hasattr(self, 'btn_generar_qr_imagen') else None

        self.opcion_menu.pack(pady=10)
        self.btn_confirmar_opcion.pack(pady=10)
        self.btn_regresar_menu.pack_forget()

        # Ocultar el frame de QR si estaba mostrado
        if self.frame_qr_preview:
            self.frame_qr_preview.pack_forget()

    def mostrar_generar_qr_url(self):
        # Ocultar el menú desplegable y el botón de confirmación
        self.opcion_menu.pack_forget()
        self.btn_confirmar_opcion.pack_forget()

        # Mostrar el campo para ingresar URL
        self.label_url = tk.Label(self.left_frame, text="Ingrese la URL:", bg="#f0f4f8", font=self.font_secondary, fg=self.primary_color)
        self.label_url.pack(pady=5)
        self.entry_url = tk.Entry(self.left_frame, font=self.font_secondary, width=40, bd=2, relief="solid")
        self.entry_url.pack(pady=5)

        # Botón para generar el QR
        self.btn_generar_qr = ttk.Button(self.left_frame, text="Generar QR", command=self.generar_qr_url)
        self.btn_generar_qr.pack(pady=10)

        # Mostrar el botón de volver al menú
        self.btn_regresar_menu.pack(pady=10)

    def mostrar_generar_qr_imagen(self):
        # Ocultar el menú desplegable y el botón de confirmación
        self.opcion_menu.pack_forget()
        self.btn_confirmar_opcion.pack_forget()

        # Mostrar el campo para seleccionar imagen
        self.label_imagen = tk.Label(self.left_frame, text="Seleccione una imagen (PNG/JPG):", bg="#f0f4f8", font=self.font_secondary, fg=self.primary_color)
        self.label_imagen.pack(pady=5)

        # Botón para seleccionar imagen
        self.btn_seleccionar_imagen = ttk.Button(self.left_frame, text="Seleccionar Imagen", command=self.seleccionar_imagen)
        self.btn_seleccionar_imagen.pack(pady=5)

        # Mostrar el botón de volver al menú
        self.btn_regresar_menu.pack(pady=10)

    def seleccionar_imagen(self):
        # Abrir explorador de archivos nativo
        self.imagen_path = filedialog.askopenfilename(title="Seleccionar imagen", filetypes=[("PNG Files", "*.png"), ("JPG Files", "*.jpg")], parent=self.root)

        if self.imagen_path:
            self.label_imagen_seleccionada = tk.Label(self.left_frame, text=f"Imagen seleccionada: {self.imagen_path}", bg="#f0f4f8", font=("Helvetica", 10), fg=self.primary_color)
            self.label_imagen_seleccionada.pack(pady=5)

            # Botón para generar el QR
            self.btn_generar_qr_imagen = ttk.Button(self.left_frame, text="Generar QR", command=self.generar_qr_imagen)
            self.btn_generar_qr_imagen.pack(pady=10)

    def generar_qr_url(self):
        url = self.entry_url.get()
        if not url.strip():  # Verifica si está vacío
            messagebox.showwarning("Advertencia", "Por favor, ingrese una URL válida.")
            return  # No genera el QR si el campo está vacío
        # Crear código QR si la URL no está vacía
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')

        # Mostrar vista previa
        self.mostrar_vista_previa(img)


    def generar_qr_imagen(self):
        if not hasattr(self, 'imagen_path') or not self.imagen_path:  # Verifica si no se ha seleccionado imagen
            messagebox.showwarning("Advertencia", "Por favor, seleccione una imagen primero.")
            return  # No genera el QR si no se selecciona una imagen
    
        # Llamar a la función generada en qr_functions.py para crear el código QR
        img = generar_qr_imagen(self.imagen_path)
    
        # Mostrar vista previa
        self.mostrar_vista_previa(img)


    def mostrar_vista_previa(self, qr_image):
        # Convertir la imagen de código QR a un formato que pueda ser mostrado en tkinter
        qr_image = qr_image.resize((250, 250))  # Hacemos la imagen más grande
        qr_tk = ImageTk.PhotoImage(qr_image)

        # Si ya existe un frame de vista previa, lo eliminamos para actualizar
        if self.frame_qr_preview:
            self.frame_qr_preview.pack_forget()

        # Crear un nuevo frame para la vista previa
        self.frame_qr_preview = tk.Frame(self.right_frame, bg="#f0f4f8")
        self.frame_qr_preview.pack(pady=20)

        # Etiqueta con la imagen del QR
        label_preview = tk.Label(self.frame_qr_preview, image=qr_tk, bg="#f0f4f8")
        label_preview.image = qr_tk  # Guardar la referencia para evitar que la imagen sea recolectada por el garbage collector
        label_preview.pack()

        # Botón para guardar el QR
        btn_guardar_qr = ttk.Button(self.frame_qr_preview, text="Guardar QR", command=lambda: self.guardar_qr(qr_image))
        btn_guardar_qr.pack(pady=5)

    def guardar_qr(self, qr_image):
        # Guardar el código QR como imagen
        archivo = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if archivo:
            qr_image.save(archivo)
            messagebox.showinfo("Guardado", "El código QR ha sido guardado correctamente.")

