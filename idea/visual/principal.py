import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from obj_manim.escena import Escena
from obj_manim.enlace import Enlace
from obj_manim.tex import Tex


# -----------------------------
# Clase principal de la app
# -----------------------------
class ManisspresoApp:
    def __init__(self, base):
        self.base = base
        self.base.title("Manisspreso ☕")
        self.base.geometry("1000x700")
        self.base.configure(bg="#222")

        self._crear_menu()
        self._crear_layout()
        self.enlace=Enlace()

    def _crear_menu(self):
        menu_bar = tk.Menu(self.base)

        archivo_menu = tk.Menu(menu_bar, tearoff=0)
        archivo_menu.add_command(label="Nuevo")
        archivo_menu.add_command(label="Abrir")
        archivo_menu.add_command(label="Guardar")
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.base.quit)

        editar_menu = tk.Menu(menu_bar, tearoff=0)
        editar_menu.add_command(label="Deshacer")
        editar_menu.add_command(label="Rehacer")

        animaciones_menu = tk.Menu(menu_bar, tearoff=0)
        animaciones_menu.add_command(label="FadeIn")
        animaciones_menu.add_command(label="Write")
        animaciones_menu.add_command(label="Transform")

        exportar_menu = tk.Menu(menu_bar, tearoff=0)
        exportar_menu.add_command(label="Renderizar Video")
        exportar_menu.add_command(label="Previsualizar")

        ayuda_menu = tk.Menu(menu_bar, tearoff=0)
        ayuda_menu.add_command(label="Acerca de")

        menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
        menu_bar.add_cascade(label="Editar", menu=editar_menu)
        menu_bar.add_cascade(label="Animaciones", menu=animaciones_menu)
        menu_bar.add_cascade(label="Exportar", menu=exportar_menu)
        menu_bar.add_cascade(label="Ayuda", menu=ayuda_menu)

        self.base.config(menu=menu_bar)

    def _crear_layout(self):
        # Frame general
        frame_general = ttk.Frame(self.base)
        frame_general.pack(fill="both", expand=True)

        # Panel lateral izquierdo (paleta de objetos)
        panel_izquierdo = ttk.Frame(frame_general, width=200)
        panel_izquierdo.pack(side="left", fill="y", padx=5, pady=5)

        ttk.Label(panel_izquierdo, text="Paleta de Objetos", font=("Arial", 10, "bold")).pack(pady=10)

        ttk.Button(panel_izquierdo, text="+ Texto", command=self.agregar_texto).pack(pady=5, fill="x")
        ttk.Button(panel_izquierdo, text="+ MathTex", command=self.agregar_mathtex).pack(pady=5, fill="x")
        ttk.Button(panel_izquierdo, text="+ Imagen", command=self.agregar_imagen).pack(pady=5, fill="x")
        ttk.Button(panel_izquierdo, text="+ Rectángulo", command=self.agregar_rectangulo).pack(pady=5, fill="x")
        

        # Área de edición (canvas)
        frame_canvas = ttk.Frame(frame_general)
        frame_canvas.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        self.canvas = tk.Canvas(frame_canvas, bg="white")
        self.canvas.pack(fill="both", expand=True)

        # Línea de tiempo (placeholder por ahora)
        self.timeline = ttk.Label(self.base, text="[Línea de tiempo - versión futura]",
                                  anchor="center", relief="sunken")
        self.timeline.pack(fill="x", padx=5, pady=2)

        # Barra inferior de botones
        frame_botones = ttk.Frame(self.base)
        frame_botones.pack(fill="x", padx=5, pady=5)

        ttk.Button(frame_botones, text="Renderizar Escena", command=self.renderizar).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Previsualizar", command=self.previsualizar).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Guardar Proyecto", command=self.guardar_proyecto).pack(side="right", padx=5)
        ttk.Button(frame_botones, text="Crear Escena", command=self.crear_escena).pack(side="right", padx=5)

    # -----------------------
    # Funciones de acción
    # -----------------------

    def agregar_texto(self):
        tex_obj = Tex(contenido="Nuevo Texto", x=100, y=100, color="white")
        text_id = tex_obj.renderizar_en_canvas(self.canvas)

        # Habilitar arrastre en el canvas
        self.canvas.tag_bind(text_id, "<Button1-Motion>", lambda e, obj_id=text_id: self._arrastrar_objeto(e, obj_id))
            

    def agregar_mathtex(self):
        self.canvas.create_text(100, 150, text="\\int_0^1 x^2 dx", font=("Courier", 14), fill="blue")

    def agregar_imagen(self):
        messagebox.showinfo("Info", "Función de imagen aún no implementada.")

    def agregar_rectangulo(self):
        self.canvas.create_rectangle(50, 200, 150, 250, fill="lightgray", outline="black")

    def renderizar(self):
        messagebox.showinfo("Renderizar", "Aquí se generará el archivo .py y se llamará a manim.")

    def previsualizar(self):
        messagebox.showinfo("Previsualizar", "Aquí se mostrará el video renderizado.")

    def guardar_proyecto(self):
        messagebox.showinfo("Guardar", "Aquí se guardará el proyecto como archivo .mnjs")
    def crear_escena(self):
        escena = Escena(nombre=f"Escena{len(self.enlace.escenas)}")

        # Por ahora, agregamos algo de prueba
        escena.agregar_objeto(
            tipo="MathTex",
            contenido="\\int_0^1 x^2 dx",
            posicion=(0, 0),
            color="BLUE",
            animacion="FadeIn",
            duracion=2.0
        )

        self.enlace.agregar_escena(escena)
        self.enlace.generar_archivo("temp_scene.py")

        messagebox.showinfo("Escena creada", "Se agregó una nueva escena y se regeneró el archivo.")
           


# -----------------------------
# Main del programa
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ManisspresoApp(root)
    root.mainloop()

