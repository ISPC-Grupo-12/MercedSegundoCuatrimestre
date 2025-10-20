class Menu:
    def __init__(self, gestor_usuarios, gestor_productos, gestor_pedidos, validador, usuario_actual=None):
        self.gestor_usuarios = gestor_usuarios
        self.gestor_productos = gestor_productos
        self.gestor_pedidos = gestor_pedidos
        self.validador = validador
        self.usuario_actual = usuario_actual

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
                self.usuario_actual = self.gestor_usuarios.login_usuario(mail, contrasena)
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
                self.gestor_usuarios.registrar_usuario(nombre, apellido, mail, contrasena, dni)
                print("✅ Registro exitoso")
            else:
                print("👋 Hasta luego!")
                break

    def menu_admin(self):
        opciones = [
            "Ver lista de usuarios",
            "Buscar usuario por Id",
            "Cambiar rol a un usuario",
            "Eliminar usuario",
            "Ver todos los productos",
            "Buscar producto por nombre",
            "Filtrar productos por precio",
            "Crear nuevo producto",
            "Eliminar producto",
            "Modificar producto",
            "Ver Ordenes de compras",
        ]
        roles = ["Estandar", "Admin"]
        while True:
            opcion = self.mostrar_menu(opciones[:])
            if opcion == 1:
                self.gestor_usuarios.listar_usuarios()
            elif opcion == 2:
                try:
                    id = int(input("\nIngresar número de id del usuario: "))
                except ValueError:
                    print("❌ ID inválido.")
                    continue
                usuario = self.gestor_usuarios.buscar_usuario(id)
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
                    if self.gestor_usuarios.modificar_rol(id, rol_opcion - 1):
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
                        if self.gestor_usuarios.eliminar_usuario(id):
                            print(f"✅ Se eliminó el usuario con ID: {id} con éxito.")
                        else:
                            print(f"❌ No se encontró ningún usuario con el ID: {id}")
                    input("Presione ENTER para continuar...")
                else:
                    print(100 * "=", "\nNo se puede realizar esta acción.")
            elif opcion == 5:
                self.gestor_productos.listar_productos()
            elif opcion == 6:
                nombre = input("🔍 Ingrese nombre o palabra clave del producto: ")
                self.gestor_productos.buscar_por_nombre(nombre)
            elif opcion == 7:
                try:
                    minimo = float(input("💲 Precio mínimo: "))
                    maximo = float(input("💲 Precio máximo: "))
                    self.gestor_productos.filtrar_por_precio(minimo, maximo)
                except ValueError:
                    print("❌ Ingresá valores numéricos válidos.")
            elif opcion == 8:
                nombre = input("📦 Nombre del producto: ")
                descripcion = input("📝 Descripción: ")
                try:
                    precio = float(input("💲 Precio: "))
                    self.gestor_productos.crear_producto(nombre, precio, descripcion)
                    print("✅ Producto creado correctamente.")
                except ValueError:
                    print("❌ Precio inválido.")
            elif opcion == 9:
                try:
                    id_producto = int(input("🗑️ Ingrese el ID del producto que desea eliminar: "))
                    confirmacion = self.mostrar_menu(["Confirmar eliminación"])
                    if confirmacion == 1:
                        if self.gestor_productos.eliminar_producto(id_producto):
                            print(f"✅ Producto con ID {id_producto} eliminado correctamente.")
                        else:
                            print(f"❌ No se encontró ningún producto con el ID: {id_producto}")
                except ValueError:
                    print("❌ ID inválido. Ingresá un número.")
            elif opcion == 10:
                try:
                    id_producto = int(input("🛠️ Ingrese el ID del producto que desea modificar: "))
                    campo_opcion = self.mostrar_menu(["Modificar nombre", "Modificar precio", "Modificar descripción", "Modificar imagen"])
                    if campo_opcion <= 4:
                        nuevo_valor = input("Ingrese el nuevo valor: ")
                        if campo_opcion == 2:
                            try:
                                nuevo_valor = float(nuevo_valor)
                            except ValueError:
                                print("❌ Precio inválido.")
                                continue
                        if self.gestor_productos.modificar_producto(id_producto, campo_opcion, nuevo_valor):
                            print("✅ Producto modificado correctamente.")
                        else:
                            print(f"❌ No se encontró ningún producto con el ID: {id_producto}")
                except ValueError:
                    print("❌ ID inválido. Ingresá un número.")
                    if campo_opcion <= 4:
                        nuevo_valor = input("Ingrese el nuevo valor: ")
                        if campo_opcion == 2:
                            try:
                                nuevo_valor = float(nuevo_valor)
                            except ValueError:
                                print("❌ Precio inválido.")
                                continue
                        if self.gestor_productos.modificar_producto(id_producto, campo_opcion, nuevo_valor):
                            print("✅ Producto modificado correctamente.")
                        else:
                            print(f"❌ No se encontró ningún producto con el ID: {id_producto}")
            elif opcion == 11:
                        pedidos = self.gestor_pedidos.ver_todos_los_pedidos()
                        if pedidos:
                            print("📋 Pedidos registrados:")
                        for p in pedidos:
                            print(f"🆔 {p[0]} | 👤 {p[1]} | 📦 {p[2]} | 📅 {p[3]}")
                        else:
                            print("❌ No hay pedidos registrados.")
            elif opcion == 12:
                self.usuario_actual = None
                break                


    def menu_estandar(self):
        opciones = [
            "Ver datos personales",
            "Modificar datos personales",
            "Ver todos los productos",
            "Buscar producto por nombre",
            "Filtrar productos por precio",
            "Realizar pedido",
            "Ver mis pedidos",
        ]
        opciones_datos = [
            "Modificar el nombre",
            "Modificar el apellido",
            "Modificar el DNI",
            "Modificar el mail",
            "Modificar la contrasena",
        ]
        while True:
            opcion = self.mostrar_menu(opciones[:])
            if opcion == 1:
                print(100 * "=", "\nTus datos personales:")
                print(self.gestor_usuarios.buscar_usuario(self.usuario_actual.id))
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
                success = self.gestor_usuarios.modificar_datos(self.usuario_actual.id, dato, nuevo_valor)
                print("✅ Cambiado correctamente." if success else "❌ No se pudo modificar.")
            elif opcion == 3:
                self.gestor_productos.listar_productos()
            elif opcion == 4:
                nombre = input("🔍 Ingrese nombre o palabra clave del producto: ")
                self.gestor_productos.buscar_por_nombre(nombre)
            elif opcion == 5:
                try:
                    minimo = float(input("💲 Precio mínimo: "))
                    maximo = float(input("💲 Precio máximo: "))
                    self.gestor_productos.filtrar_por_precio(minimo, maximo)
                except ValueError:
                    print("❌ Ingresá valores numéricos válidos.")
            elif opcion == 6:
                try:
                    id_producto = int(input("🛒 Ingrese el ID del producto que desea comprar: "))
                    self.gestor_pedidos.realizar_pedido(self.usuario_actual.id, id_producto)
                    print("✅ Pedido realizado correctamente.")
                except ValueError:
                    print("❌ ID inválido. Ingresá un número.")
            elif opcion == 7:
                pedidos = self.gestor_pedidos.ver_pedidos_por_usuario(self.usuario_actual.id)
                if pedidos:
                    print("📦 Tus pedidos realizados:")
                    for p in pedidos:
                        print(f"🆔 {p[0]} | Producto: {p[1]} | Fecha: {p[2]}")
                else:
                    print("❌ No se encontraron pedidos registrados.")
            else:
                self.usuario_actual = None
                break