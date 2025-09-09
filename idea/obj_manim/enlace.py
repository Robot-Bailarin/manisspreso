# obj_manim/enlace.py

from obj_manim.escena import Escena

class Enlace:
    def __init__(self):
        self.escenas = []

    def agregar_escena(self, escena: Escena):
        self.escenas.append(escena)

    def generar_archivo(self, nombre_archivo="temp_scene.py"):
        codigo = ["from manim import *\n"]

        for escena in self.escenas:
            codigo.append(escena.generar_codigo())
            codigo.append("\n")

        with open(nombre_archivo, "w") as f:
            f.write("\n".join(codigo))

        print(f"[✓] Archivo generado: {nombre_archivo}")
        return nombre_archivo

