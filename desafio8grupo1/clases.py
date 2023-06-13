

class Usuario:
    usuarios_registrados = []
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contraseña = contraseña
        self.fecha_registro = fecha_registro
        self.avatar = avatar
        self.estado = estado
        self.online = online
def login(self, username, contraseña):
        if self.username == username and self.contraseña == contraseña:
            print("Inicio de sesión exitoso.")
        else:
            print("Los datos ingresados son incorrectos. Inténtalo nuevamente.")

def registrar(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar):
        nuevo_usuario = Usuario(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, "activo", True)
        self.usuarios_registrados.append(nuevo_usuario)
        print("Se ha registrado exitosamente.")

class Publico(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online, es_publico):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
        self.es_publico = es_publico

class Colaborador(Usuario):
      def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online, es_colaborador):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
        self.es_colaborador = es_colaborador