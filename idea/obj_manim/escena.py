# obj_manim/escena.py

class Escena:
    def __init__(self, nombre="MiEscena"):
        self.nombre = nombre
        self.objetos = []

    def agregar_objeto(self, tipo, contenido, posicion=(0, 0), color="WHITE", animacion="FadeIn", duracion=2.0):
        self.objetos.append({
            "tipo": tipo,
            "contenido": contenido,
            "posicion": posicion,
            "color": color,
            "animacion": animacion,
            "duracion": duracion
        })

    def generar_codigo(self):
        """Genera solo el código de esta escena."""
        codigo = [
            f"class {self.nombre}(Scene):",
            "    def construct(self):"
        ]

        for i, obj in enumerate(self.objetos):
            nombre_obj = f"obj_{i}"
            x, y = obj["posicion"]
            codigo.append(f'        {nombre_obj} = {obj["tipo"]}("{obj["contenido"]}")'
                          f'.move_to([{x}, {y}, 0]).set_color({obj["color"]})')
            codigo.append(f'        self.play({obj["animacion"]}({nombre_obj}), run_time={obj["duracion"]})\n')

        return "\n".join(codigo)

