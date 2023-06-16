from clases import *

def inicio():    
	'''
	Funcion inicio() que se ejecuta al ingresar a la aplicacion
	se devuelve a si misma , aplicando recursividad si no es correcto el input
	SI opcion = 1 se va a la funcion loginMain() para ejecutar el login
	SI opcion = 2 se va a la funcion registrarMain() para ejecutar el registro
	'''
	opcion = input("Ingrese Opcion: ")
	if opcion =="1":
		loginMain()
	elif opcion =="2":
		registrarMain()
	else:
		print("Lo siento no ingreso la opcion correcta, vallamos de nuevo")  
		return inicio()

def loginMain():
	'''
		Funcion loginMain() pide los datos :username = string y password = string
		se instancia un usuario con datos vacios, para ejecutar la consulta de login
		esos datos se evaluan con una instancia de usuario.login()
		dependiendo que valor fue devuelto por usuario.login()
		se evalua si es un objeto de tipo Publico o de tipo Colaborador y se invoca la funcion Menu(isPublico,usuario),
		si no es ninguno de esos , se vuelve a llamar aplicando el principio
		de recursividad
	'''
	username = input("Ingrese su Usuario: ")
	password = input("Ingrese su Contraseña:")
	usuario = CrearUsuarioConDatosVacios(True)
	UsuarioVerificado=usuario.login(username,password)
	if isinstance(UsuarioVerificado,Publico) :
		print(f"Bienvenido {UsuarioVerificado.nombre}\nCOMENCEMOS!!!")
		Menu(True,UsuarioVerificado)
	elif isinstance(UsuarioVerificado,Colaborador):
		print(f"Bienvenido {UsuarioVerificado.nombre}\nCOMENCEMOS!!!")
		Menu(False,UsuarioVerificado)
	else:
		print("Los datos estan mal Ingresado, Intentelo de nuevo")    
		return loginMain()

def registrarMain():
	'''
	registrarMain()
	Pide que tipo de opcion desea registrar e invoca a la funcion CrearUsuario()
	sino es correcto se vuelve a llamar con el principio de recursividad
	'''
	opcion = input('Como desea Registrarse: \n1-Como Usuario Publico\n2-Como Usuario Colaborador\nIngrese:')
	if opcion =="1":
		crearUsuario(True)
	elif opcion =="2":
		crearUsuario(False)
	else:
		print("Lo siento no ingreso la opcion correcta, vallamos de nuevo")  
		return registrarMain()
	
def crearUsuario(isPublico):
	'''
	Funcion crearUsuario(isPublico = boolean)
	Pide todo los atributos necesarios para poder crear un usuario
	dependiendo el parametro pasado lo registra como usuario Publico (True) o 
	Usuario Colaborador(False)
	y se retorna al loginMain()
	'''
	id = 0
	nombre = input('Ingrese Su nombre: ')
	apellido = input('Ingrese su apellido: ')
	telefono = input('Ingrese su telefono: ')
	nombredeUsuario = input('Ingrese su nombre de usuario: ')
	contra= input('Ingrese su contraseña: ')
	correo = input('Ingrese su correo: ')
	fecha = ''
	avatar = ''
	if isPublico:
		usuario = CrearUsuarioConDatosVacios(True)
		usuario.registrar(id,nombre,apellido,telefono,nombredeUsuario,correo,contra,fecha,avatar)
		
	else:
		usuario = CrearUsuarioConDatosVacios(False)
		usuario.registrar(id,nombre,apellido,telefono,nombredeUsuario,correo,contra,fecha,avatar)
		
	return loginMain()

def CrearUsuarioConDatosVacios(valor):
	'''
	Funcion CrearUsuarioConDatosVacios(valor = boolean)
	Crea dependiento del tipo de parametro que recibe a un Usuario Publico con datos vacios o un Usuario Colaborador
	devuelve a ese usuario'''
	if valor:
		usuario = Publico(0,'','','','','','','','')
	else:
		usuario = Colaborador(0,'','','','','','','','')
	return usuario

def Menu(isPublico,usuario):
	'''
	Funcion Menu(isPublico,usuario) recibe un parametro booleano(isPublico) y un objeto usuario para poder contar con el tipo de dato y tomar que tipo de opciones usar
	Dependiendo si el usuario es publico o colaborador se le brindara las opciones
	'''
	print("A continuacion eliga que Operacion desea realizar :\n0-Salir\n1-Comentar")
	if isPublico:
		opcion = input('Ingrese su Opcion:')
		if opcion == '1':
			print(f'{usuario.username}-Comentar')
		elif opcion == '0':
			print(f'Hasta Pronto {usuario.nombre}!!')
		else:
			print('Por favor ingrese el valor Correcto')
			return Menu(isPublico,usuario)
	else:
		print("2-Publicar Articulo")
		opcion = input('Ingrese su Opcion:')
		if opcion == '1':
			print(f'{usuario.username}-Comentar')
		elif opcion == '2':
			print(f'{usuario.username}-Escribir Aritculo')
		elif opcion == '0':
			print(f'Hasta Pronto {usuario.nombre}!!')
		else:
			print('Por favor ingrese el valor Correcto')
			return Menu(isPublico,usuario)

print('Bienvenido a el Ejercicio 8 - Somos el Grupo 1\nEn que forma desea Ingresar\n1-Si ya tiene usuario y contraseña\n2-Si desea registrarse')
usuarioPrueba = Colaborador(1,'Pedro','Luque',36445545,'pedrito','pedro@gmail.com','1234','HOY','False')
usuarios_registrados.append(usuarioPrueba)
inicio()