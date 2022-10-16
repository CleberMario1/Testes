from UserInterface import UserInterface
from Menu import Menu
from MenuRepository import MenuRepository
from Order import Order



def test_get_total_price():
    menu_repository = MenuRepository()
    menu_repository.menu_itens = []
    menu = Menu(1, "Test 1", 10)
    menu1 = Menu(3, "Test 2", 10)
    menu_repository.set_menu_item(menu)
    menu_repository.set_menu_item(menu1)
    user_interface = UserInterface(menu_repository)
    precototal1 = user_interface.get_total_price(Order(1,10))
    precototal2 = user_interface.get_total_price(Order(3,5))




    assert precototal1 == 100

    assert precototal2 == 50



def test_get_user_input(monkeypatch):
    menu_repository = MenuRepository()
    menu_repository.menu_itens = []
    user_interface = UserInterface(menu_repository)
    menu1 = Menu(4, "Test", 5)
    menu_repository.set_menu_item(menu1)
    monkeypatch.setattr('builtins.input', lambda _: "4 3")
    pedido = user_interface.get_user_input()



    assert Order(4,3) == pedido

