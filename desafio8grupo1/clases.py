

class Usuario:
    usuarios_registrados = {}
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
        if username in self.usuarios_registrados:
            usuario = self.usuarios_registrados[username]
            if usuario.contraseña == contraseña:
                self.id = usuario.id
                self.nombre = usuario.nombre
                self.apellido = usuario.apellido
                self.telefono = usuario.telefono
                self.email = usuario.email
                self.fecha_registro = usuario.fecha_registro
                self.avatar = usuario.avatar
                self.estado = usuario.estado
                self.online = usuario.online
                print("Inicio de sesión exitoso.")
                return
        print("Credenciales incorrectas. Inténtalo nuevamente.")
        return False

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