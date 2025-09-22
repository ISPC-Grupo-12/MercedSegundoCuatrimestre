class Menu:
    def __init__(self, usuario_actual=None, gestor=None, validador=None):
        self.usuario_actual = usuario_actual
        self.gestor = gestor
        self.validador = validador

    def mostrar_menu(self, opciones):
        opciones.append("Salir")
        print("\n" + "═" * 60)
        print("📋 SELECCIONE UNA OPCIÓN".center(60))
        print("═" * 60)
        for i in range(len(opciones)):
            print(f"{i+1}. {opciones[i]}")
        return self.validador.validar_opcion(1, len(opciones))

    def menu_principal(self):
        opciones = ["Iniciar Sesión", "Registrarse"]
        while True:
            opcion = self.mostrar_menu(opciones[:])
            if opcion == 1:
                print("\n🔐 INICIO DE SESIÓN\n".center(50, "-"))
                mail = input("\nIngresar mail: ")
                while not self.validador.validar_mail_patron(mail):
                    mail = input("\nIngresar un mail correcto: ")
                contrasena = input("Ingresar contrasena: ")
                while not self.validador.validar_contrasena(contrasena):
                    contrasena = input("Ingresar una contrasena correcta: ")
                self.usuario_actual = self.gestor.login_usuario(mail, contrasena)
                while self.usuario_actual is not None:
                    if self.usuario_actual.es_admin():
                        self.menu_admin()
                    else:
                        self.menu_estandar()
            elif opcion == 2:
                print("\n📝 REGISTRO DE USUARIO\n".center(50, "-"))
                nombre = input("\nIngrese su nombre: ")
                while not self.validador.validar_str(nombre):
                    nombre = input("\nIngrese un nombre válido: ")
                apellido = input("Ingrese su apellido: ")
                while not self.validador.validar_str(apellido):
                    apellido = input("\nIngrese un apellido válido: ")
                dni = input("Ingresar número de documento: ")
                while not self.validador.validar_dni(dni):
                    dni = input("\nIngresar un número de documento válido: ")
                mail = input("Ingrese su mail: ")
                while not self.validador.validar_mail_patron(mail) or not self.validador.validar_mail_repetido(mail):
                    mail = input("\nIngresar un mail correcto: ")
                contrasena = input("Ingresar una contrasena que incluya letras y números: ")
                while not self.validador.validar_contrasena(contrasena):
                    contrasena = input("Ingresar una contrasena correcta: ")
                self.gestor.registrar_usuario(nombre, apellido, mail, contrasena, dni)
                print("✅ Registro exitoso")
            else:
                print("👋 Hasta luego!")
                break

    def menu_admin(self):
        opciones = ["Ver lista de usuarios", "Buscar usuario por Id", "Cambiar rol a un usuario", "Eliminar usuario"]
        roles = ["Estandar", "Admin"]
        while True:
            opcion = self.mostrar_menu(opciones[:])
            if opcion == 1:
                self.gestor.listar_usuarios()
            elif opcion == 2:
                try:
                    id = int(input("\nIngresar número de id del usuario: "))
                except ValueError:
                    print("❌ ID inválido.")
                    continue
                usuario = self.gestor.buscar_usuario(id)
                if usuario:
                    print(f"Usuario con el ID {id}: {usuario}")
                else:
                    print(f"❌ No se encontró ningún usuario con el ID: {id}")
            elif opcion == 3:
                try:
                    id = int(input("\nIngresar número de id: "))
                except ValueError:
                    print("❌ ID inválido.")
                    continue
                rol_opcion = self.mostrar_menu(roles[:])
                if rol_opcion <= len(roles):
                    if self.gestor.modificar_rol(id, rol_opcion - 1):
                        print(f"✅ Se modificó el rol a {roles[rol_opcion - 1]} con éxito.")
                        if self.usuario_actual.id == id:
                            self.usuario_actual = None
                            break
                    else:
                        print(f"❌ No se encontró ningún usuario con el ID: {id}")
            elif opcion == 4:
                try:
                    id = int(input("\nIngrese número de id del usuario que desea eliminar: "))
                except ValueError:
                    print("❌ ID inválido.")
                    continue
                if self.usuario_actual.id != id:
                    if self.mostrar_menu(["Confirmar"]) == 1:
                        if self.gestor.eliminar_usuario(id):
                            print(f"✅ Se eliminó el usuario con ID: {id} con éxito.")
                        else:
                            print(f"❌ No se encontró ningún usuario con el ID: {id}")
                    input("Presione ENTER para continuar...")
                else:
                    print(100 * "=", "\nNo se puede realizar esta acción.")
            else:
                self.usuario_actual = None
                break

    def menu_estandar(self):
        opciones = ["Ver datos personales", "Modificar datos personales"]
        opciones_datos = [
            "Modificar el nombre",
            "Modificar el apellido",
            "Modificar el DNI",
            "Modificar el mail",
            "Modificar la contrasena"
        ]
        while True:
            opcion = self.mostrar_menu(opciones[:])
            if opcion == 1:
                print(100 * "=", "\nTus datos personales:")
                print(self.gestor.buscar_usuario(self.usuario_actual.id))
            elif opcion == 2:
                dato = self.mostrar_menu(opciones_datos[:])
                if dato > len(opciones_datos):
                    continue
                nuevo_valor = input(f"Ingrese nuevo valor para «{opciones_datos[dato - 1]}»: ")
                if dato == 4:
                    while not self.validador.validar_mail_patron(nuevo_valor) or not self.validador.validar_mail_repetido(nuevo_valor):
                        nuevo_valor = input("mail inválido o en uso, intente nuevamente: ")
                elif dato == 3:
                    while not self.validador.validar_dni(nuevo_valor):
                        nuevo_valor = input("DNI inválido o en uso, intente nuevamente: ")
                elif dato == 5:
                    while not self.validador.validar_contrasena(nuevo_valor):
                        nuevo_valor = input("Contrasena inválida, intente nuevamente: ")
                success = self.gestor.modificar_datos(self.usuario_actual.id, dato, nuevo_valor)
                print("✅ Cambiado correctamente." if success else "❌ No se pudo modificar.")
            else:
                self.usuario_actual = None
                break