from menu import Menu
from persistencia import crear_tablas
from gestor_usuario import Gestor_usuario
from validador import Validador

def mostrar_bienvenida():
    print("=" * 60)
    print("👗 BIENVENIDOS A MERCED 👗".center(60))
    print("Tienda de moda accesible y global".center(60))
    print("=" * 60)

def main():
    crear_tablas()
    mostrar_bienvenida()

    # Instanciar gestor y validador sin listas
    gestor = Gestor_usuario()
    validador = Validador()
    menu = Menu(None, gestor, validador)

    menu.menu_principal()

if __name__ == "__main__":
    main()


















































if __name__ == "__main__":
    main()