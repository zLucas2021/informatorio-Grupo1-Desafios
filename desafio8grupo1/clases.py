from articulo import *
from comentario import *
from datetime import datetime
#Lista de los usuarios registrados
usuarios_registrados = []
class Usuario:
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contraseña = contraseña
        self.fecha_registro = fecha_registro
        self.avatar = avatar
        self.estado = 'NO ACTIVO'
        self.online = False

    def login(self, username, contraseña):
        for usuario in usuarios_registrados:
            if usuario.username == username and usuario.contraseña == contraseña:
                self.id = usuario.id
                self.nombre = usuario.nombre
                self.apellido = usuario.apellido
                self.telefono = usuario.telefono
                self.email = usuario.email
                self.fecha_registro = usuario.fecha_registro
                self.avatar = usuario.avatar
                self.estado = "ACTIVO"
                self.online = True
                print("Inicio de sesión exitoso.")
                return usuario
        return False

    def registrar(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar):
        nuevo_usuario = Usuario(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar)
        usuarios_registrados.append(nuevo_usuario)
        print("Se ha registrado exitosamente.")

class Publico(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar)
        self.es_publico = True
    def registrar(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar):
        nuevo_usuario = Publico(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar)
        usuarios_registrados.append(nuevo_usuario)
        print("Se ha registrado exitosamente.")
    def comentar(self, id_articulo, contenido):
        nuevo_comentario = Comentario(len(comentarios)+1, id_articulo, self.id, contenido, datetime.now(), "activo")
        comentarios.append(nuevo_comentario)
        print("Comentario publicado con éxito.")
    

class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar)
        self.es_colaborador = True
    def registrar(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar):
        nuevo_usuario = Colaborador(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar)
        usuarios_registrados.append(nuevo_usuario)
        print("Se ha registrado exitosamente.")       
        
    def comentar(self, id_articulo, contenido):
        nuevo_comentario = Comentario(len(comentarios)+1, id_articulo, self.id, contenido, datetime.now(), "activo")
        comentarios.append(nuevo_comentario)
        print("Comentario publicado con éxito.")

    def publicar_articulo(self, titulo, resumen, contenido, imagen):
        nuevo_articulo = Articulo(len(articulos)+1, self.id, titulo, resumen, contenido, datetime.now(), imagen, "activo")
        articulos.append(nuevo_articulo)
        print("Artículo publicado con éxito.")  
