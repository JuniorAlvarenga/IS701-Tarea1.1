class Libro:
    def __init__(self,titulo, autor, anio_publicacion, numero_paginas):
        self.titulo = str(titulo)
        self.autor = str(autor)
        self.anio_publicacion = int(anio_publicacion)
        self.numero_paginas = int(numero_paginas)
    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de Publicación: {self.anio_publicacion}")
        print(f"Número de Páginas: {self.numero_paginas}")

libro = Libro("Cuando las tarántulas atacan", "Longino Becerra", 1980, 220)

libro.mostrar_informacion()


