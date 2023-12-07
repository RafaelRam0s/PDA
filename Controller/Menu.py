

def redirecionar_Menu_Inicial():
    with open("./View/menu_inicial.py") as f:
        exec(f.read())