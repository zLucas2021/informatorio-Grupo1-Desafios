#Importante que la lista este afuera
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

class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar)
        self.es_colaborador = True
    def registrar(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar):
        nuevo_usuario = Colaborador(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar)
        usuarios_registrados.append(nuevo_usuario)
        print("Se ha registrado exitosamente.")    
    