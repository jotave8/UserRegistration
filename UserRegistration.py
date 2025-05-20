TAM_USUARIO = 100
qtd_usuario = 0
opcao: int
sair = 0

lista_usuarios = [None] * TAM_USUARIO

def menu_geral():

    print("╔═════════════════════════════════════════╗");
    print("║           Cadastro de Usuário           ║");
    print("║═════════════════════════════════════════║");
    print("║                Joao Victor              ║");
    print("╚═════════════════════════════════════════╝\n");
    print("0 - Sair")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar")
    opcao = int(input('Escolha: '))

menu_geral()