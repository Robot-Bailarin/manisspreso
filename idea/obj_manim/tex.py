# obj_manim/tex.py

# obj_manim/tex.py

class Tex:
    def __init__(self, contenido="Texto", x=100, y=100, color="white", escena=None):
        self.contenido = contenido
        self.x = x
        self.y = y
        self.color = color
        self.escena = escena  # ← Aquí se asocia la escena

    def renderizar_en_canvas(self, canvas):
        """Dibuja en el canvas (Tkinter) y retorna el ID del objeto canvas."""
        return canvas.create_text(self.x, self.y, text=self.contenido, font=("Arial", 16), fill=self.color)

    def exportar_a_dict(self):
        """Devuelve un diccionario con los datos de este objeto para Manim."""
        return {
            "tipo": "Tex",
            "contenido": self.contenido,
            "posicion": (self.x, self.y),
            "color": self.color,
            "animacion": "FadeIn",
            "duracion": 2.0
        }

