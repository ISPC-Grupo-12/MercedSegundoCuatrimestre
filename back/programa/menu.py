class Menu:
    def __init__(self, gestor_usuarios, gestor_productos, validador, usuario_actual=None):
        self.gestor_usuarios = gestor_usuarios
        self.gestor_productos = gestor_productos
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
            "Filtrar productos por categoria",
            "Crear nuevo producto",
            "Agregar variante de producto",
            "Eliminar producto",
            "Modificar producto",
        ]
        roles = ["Estandar", "Admin"]
        categorias={1:"Remera", 2:"Pantalon", 3:"Zapatillas", 4:"Joyeria", 5:"Campera", 6:"Vestido" } 
        talles={1:"S", 2:"M", 3:"L", 4:"XL", 5:"XXL"} 
        colores={1:"negro", 2:"rojo", 3:"verde", 4:"blanco", 5:"azul", 6:"rosa", 7:"morado", 8:"gris"} 
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
                for clave, valor in categorias.items():
                    print(f"{clave}: {valor}")
    
                categoria_opcion=int(input("📑 Selecciona la categoria: "))
                if(categoria_opcion > len(categorias)+1):
                        print("❌ Numero invalido")
                else:
                    try:
                        categoria=categorias[categoria_opcion]
                        self.gestor_productos.filtrar_por_categoria(categoria)
                    except ValueError:
                        print("❌ Ingresá valores numéricos válidos.")
                        
            elif opcion == 9:
                nombre = input("📦 Nombre del producto: ")
                descripcion = input("📝 Descripción: ")
                for clave, valor in categorias.items():
                    print(f"{clave}: {valor}")
    
                categoria_opcion=int(input("📑 Selecciona la categoria: "))
                if(categoria_opcion > len(categorias)+1):
                    print("❌ Numero invalido")
                else:
                    try:
                        categoria=categorias[categoria_opcion]
                        precio = float(input("💲 Precio: "))
                        self.gestor_productos.crear_producto(nombre, descripcion, categoria, precio)
                        print("✅ Producto creado correctamente.")
                    
                    except ValueError:
                        print("❌ Datos inválidos.")
            
            elif opcion == 10:
                id_producto = input("🆔 Id del producto: ")   
                try:
                    producto=self.gestor_productos.buscar_producto(id_producto)
                    if not producto:
                        print("❌ No se encontro un producto con ese id.")
                        return
                    else:
                            for clave, valor in talles.items():
                                print(f"{clave}: {valor}")  
                            talle_opcion= int(input("👗 Selecciona el Talle: "))
                            
                            if talle_opcion not in talles:
                                print("❌ Talle inválido.")
                                return
                            talle=talles[talle_opcion]
                            
                            for clave, valor in colores.items():
                                print(f"{clave}: {valor}")  
                            color_opcion=int(input("🎨 Selecciona el Color: "))
                            
                            if color_opcion not in colores:
                                print("❌ Color inválido.")
                                return
                            color=colores[color_opcion]
                            
                            stock = int(input("📦 Stock: "))
                            self.gestor_productos.agregar_variante(id_producto=id_producto,talle=talle,color=color,stock=stock)
                            print("✅ Producto creado correctamente.")
                except ValueError:
                    print("❌ Debe ingresar un numero.")
       
            elif opcion == 11:
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
            elif opcion == 12:
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
            elif opcion == 13:
                self.usuario_actual = None
                break                


    def menu_estandar(self):
        opciones = [
            "Ver datos personales",
            "Modificar datos personales",
            "Ver todos los productos",
            "Buscar producto por nombre",
            "Filtrar productos por precio",
            "Filtrar productos por categoria"
        ]
        opciones_datos = [
            "Modificar el nombre",
            "Modificar el apellido",
            "Modificar el mail",
            "Modificar el DNI",
            "Modificar la contrasena",
        ]
    
        categorias={1:"Remera", 2:"Pantalon", 3:"Zapatillas", 4:"Joyeria", 5:"Campera", 6:"Vestido" } 
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
                for clave, valor in categorias.items():
                    print(f"{clave}: {valor}")
    
                categoria_opcion=int(input("📑 Selecciona la categoria: "))
                if(categoria_opcion > len(categorias)+1):
                        print("❌ Numero invalido")
                else:
                    try:
                        categoria=categorias[categoria_opcion]
                        self.gestor_productos.filtrar_por_categoria(categoria)
                    except ValueError:
                        print("❌ Ingresá valores numéricos válidos.")   
                    
            else:
                self.usuario_actual = None
                break