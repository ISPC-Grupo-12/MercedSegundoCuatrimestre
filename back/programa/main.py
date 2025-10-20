from persistencia import crear_tablas
from gestor_usuario import Gestor_usuario
from gestor_producto import Gestor_producto
from gestor_pedido import Gestor_pedido
from validador import Validador
from menu import Menu

def main():
    crear_tablas()

    print("═" * 60)
    print("👗 BIENVENIDOS A MERCED 👗".center(60))
    print("Tienda de moda accesible y global".center(60))
    print("═" * 60)

    gestor_usuarios = Gestor_usuario()
    gestor_productos = Gestor_producto()
    gestor_pedidos = Gestor_pedido()
    validador = Validador()

    menu = Menu(
        gestor_usuarios=gestor_usuarios,
        gestor_productos=gestor_productos,
        gestor_pedidos=gestor_pedidos,
        validador=validador
    )

    menu.menu_principal()

if __name__ == "__main__":
    main()
















































if __name__ == "__main__":
    main()