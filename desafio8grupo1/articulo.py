articulos = []
class Articulo():
    def __init__(self, id, id_usuario, titulo, resumen,contenido,fecha_publicacion, imagen,estado):
        self.id=id
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.fecha_publicacion = fecha_publicacion
        self.imagen = imagen
        self.estado = estado